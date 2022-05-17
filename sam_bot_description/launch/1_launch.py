import os
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, DeclareLaunchArgument
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import ThisLaunchFileDir,LaunchConfiguration,FindExecutable
from launch_ros.actions import Node
from launch.actions import ExecuteProcess
from ament_index_python.packages import get_package_share_directory
import xacro
def generate_launch_description():
    use_sim_time = LaunchConfiguration('use_sim_time', default='True')
    world_file_name = 'house.sdf'
    pkg_dir = get_package_share_directory('sam_bot_description')

    os.environ["GAZEBO_MODEL_PATH"] = os.path.join(pkg_dir, 'src/urdf')

    robot_description_path =  os.path.join(pkg_dir,"src/urdf","test.urdf",)
    robot_description = {"robot_description": xacro.process_file(robot_description_path).toxml()}
    
    robot_state_publisher_node = Node(package="robot_state_publisher", executable="robot_state_publisher",output="both",parameters=[robot_description],)

    world = os.path.join(pkg_dir, 'world', world_file_name)
   


    # node_robot_state_publisher = Node(
    #     package='robot_state_publisher',
    #     executable='robot_state_publisher',
    #     output='both',
        
    # )

   
    gazebo = ExecuteProcess(cmd=['gazebo', '--verbose', world, '-s', 'libgazebo_ros_init.so', '-s', 'libgazebo_ros_factory.so'],output='screen')
    # spawn_entity = Node(package='py_pkg', executable='spawn_carver',arguments=['robot1', 'robot1', '1', '0', '0.0'],output='screen')
    spawn_entity = Node(package='gazebo_ros', executable='spawn_entity.py',
                        arguments=['-topic', 'robot_description',
                                   '-entity', 'Panda'],
                        output='screen')

    
    return LaunchDescription([
        gazebo,
        robot_state_publisher_node ,
        spawn_entity,
        
        
    ])

    