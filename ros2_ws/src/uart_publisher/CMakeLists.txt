cmake_minimum_required(VERSION 3.5)
project(uart_publisher)

find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(geometry_msgs REQUIRED)

add_executable(uart_publisher src/uart_publisher.cpp)

ament_target_dependencies(uart_publisher rclcpp geometry_msgs)

install(TARGETS
  uart_publisher
  DESTINATION lib/${PROJECT_NAME}
)

ament_package()
