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
    config_file = os.path.join(
        get_package_share_directory('my_robot'),
        'config',
        'slam_config.yaml'
    )

    # Launch LIDAR
    lidar_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(lidar_pkg, 'launch', 'ld19.launch.py')
        )
    )

    # Static transform
    static_tf = Node(
        package='tf2_ros',
        executable='static_transform_publisher',
        name='static_tf_odom_base_link',
        arguments=['0', '0', '0', '0', '0', '0', 'odom', 'base_link'],
    )

    # SLAM Toolbox
    slam_toolbox = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(slam_pkg, 'launch', 'online_async_launch.py')
        ),
        launch_arguments={
            'use_sim_time': 'false',
            'slam_params_file': config_file
        }.items()
    )

    return LaunchDescription([
        lidar_launch,
        static_tf,
        slam_toolbox,
    ])
