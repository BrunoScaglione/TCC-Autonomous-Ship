import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    # Set LOG format
    os.environ['RCUTILS_CONSOLE_OUTPUT_FORMAT'] = '[{severity} {time}] [{name}]: {message} ({function_name}() at {file_name}:{line_number})'

    pkg_share_dir = get_package_share_directory('pydyna_simple')

    ld = LaunchDescription()

    cd_2_logs = launch.actions.ExecuteProcess(
            cmd=['cd',  pkg_share_dir + '\logs'],
            output='screen'
    ) 

    rosbag_record_all = launch.actions.ExecuteProcess(
            cmd=['ros2', 'bag', 'record', '-o', 'rosbags\subset' , '-a'],
            output='screen'
    )

    pydyna_simple_node = Node(
        package='pydyna_simple',
        executable='pydyna_simple',
        name='pydyna_simple_node',
        output='screen',
        emulate_tty=True,
        parameters=[
                {'pkg_share_dir': pkg_share_dir}
        ]
    )                   

    # start pydyna_simple_node
    ld.add_action(cd_2_logs)
    ld.add_action(rosbag_record_all)
    ld.add_action(pydyna_simple_node)
    return ld