from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration

def generate_launch_description():
    ld = LaunchDescription()
    
    ld.add_action(
        Node(
            package="tf2_ros",
            executable="static_transform_publisher",
            output="screen",
            # X, Y, Z, Roll, Pitch, Yaw
            arguments=["0", "0", "0", "0", "0", "0", "0", "map", "world"]
        ))
    return ld