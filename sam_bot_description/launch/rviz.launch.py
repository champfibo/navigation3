import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
# from launch.action import DeclareLaunchArgument
from launch.actions import IncludeLaunchDescription, DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node
import xacro


def generate_launch_description():

    package_dir = get_package_share_directory('sam_bot_description')
    urdf = os.path.join(package_dir,'FINAL_MBSE.urdf')
    return LaunchDescription([
        Node(
            package='robot_state_publisher',
            name='robot_state_publisher',
            executable='robot_state_publisher',
            output ='screen',
            arguments=[urdf]),
       
        Node(
            package='rviz2',
            
            executable='rviz2',
            name='rviz2',  
            output ='screen',  ),

        
    ])