from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():
    # Ścieżki do paczek
    lidar_pkg = get_package_share_directory('ldlidar_stl_ros2')
    slam_pkg = get_package_share_directory('slam_toolbox')
    nav2_pkg = get_package_share_directory('nav2_bringup')

    my_robot_pkg = get_package_share_directory('my_robot')

    # Pliki konfiguracyjne
    slam_config = os.path.join(my_robot_pkg, 'config', 'slam_config.yaml')
    nav2_config = os.path.join(my_robot_pkg, 'config', 'nav2_params.yaml')

    # Launch LIDAR
    lidar_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(lidar_pkg, 'launch', 'ld19.launch.py')
        )
    )

    # SLAM Toolbox (async)
    slam_toolbox = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(slam_pkg, 'launch', 'online_async_launch.py')
        ),
        launch_arguments={
            'use_sim_time': 'false',
            'slam_params_file': slam_config
        }.items()
    )

    # Statyczny TF (base_link → base_laser)
    static_tf = Node(
        package='tf2_ros',
        executable='static_transform_publisher',
        name='static_tf_base_to_laser',
        arguments=['0', '0', '0', '0', '0', '0', 'base_link', 'base_laser'],
        output='screen'
    )

    controller_server_node = Node(
        package='nav2_controller',
        executable='controller_server',
        name='controller_server',
        output='screen',
        parameters=[
            os.path.join(get_package_share_directory('my_robot'), 'config', 'controller_server.yaml')
        ]
    )

    # Nav2 bringup (headless)
    nav2 = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(nav2_pkg, 'launch', 'navigation_launch.py')
        ),
        launch_arguments={
            'use_sim_time': 'false',
            'params_file': nav2_config,
            'autostart': 'true'
        }.items()
    )

    return LaunchDescription([
        lidar_launch,
        slam_toolbox,
        static_tf,
        nav2,
        controller_server_node
    ])
