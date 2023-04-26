import os
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import Command, FindExecutable, LaunchConfiguration
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare
from launch_ros.parameter_descriptions import ParameterValue


def generate_launch_description():
    load_gui = LaunchConfiguration('gui')

    pkg_share = FindPackageShare('za_description').find('za_description')
    za_xacro_file = os.path.join(pkg_share, 'urdf', 'za.xacro')
    rviz_file = os.path.join(pkg_share, 'rviz', 'za_model_viewer.rviz')

    robot_description = Command([FindExecutable(name='xacro'), ' ', za_xacro_file])

    return LaunchDescription([
        DeclareLaunchArgument(
            'gui',
            default_value='true'),
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            name='robot_state_publisher',
            output='screen',
            parameters=[{'robot_description': ParameterValue(
                robot_description, value_type=str)}]
        ),
        Node(
            package='joint_state_publisher_gui',
            executable='joint_state_publisher_gui',
            name='joint_state_publisher_gui'
        ),
        Node(package='rviz2',
             executable='rviz2',
             name='rviz2',
             arguments=['--display-config', rviz_file])  
    ])