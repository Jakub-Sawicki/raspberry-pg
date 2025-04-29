# Dockerfile
FROM ros:humble

# Ustawienia podstawowe
ENV DEBIAN_FRONTEND=noninteractive

# Aktualizacja systemu
RUN apt-get update && apt-get install -y \
    git \
    python3-colcon-common-extensions \
    python3-pip \
    ros-humble-navigation2 \
    ros-humble-nav2-bringup \
    ros-humble-slam-toolbox \
    ros-humble-turtlebot3* \
    ros-humble-rviz2 \
    ros-humble-xacro \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Tworzenie workspace
RUN mkdir -p /ros2_ws/src
WORKDIR /ros2_ws

# Sourcing ROS
SHELL ["/bin/bash", "-c"]
RUN echo "source /opt/ros/humble/setup.bash" >> ~/.bashrc
RUN echo "source /ros2_ws/install/setup.bash" >> ~/.bashrc

# Domyślnie source'uj ros2_ws po uruchomieniu
CMD ["bash"]
