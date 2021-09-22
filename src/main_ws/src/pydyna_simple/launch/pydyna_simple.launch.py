import os

from ament_index_python.packages import get_package_share_directory, get_package_prefix
from launch import LaunchDescription  
from launch.actions import ExecuteProcess
from launch_ros.actions import Node

# obs: not exaclty shure where generate_launch_description is invoked
# however absolute paths should do, with get_package_share_directory

def generate_launch_description():
    pkg_share_dir = get_package_share_directory('path_following')
    pydyna_install_dir = get_package_prefix('pydyna_simple')
    pydyna_dir = os.path.join(pydyna_install_dir, 'lib', 'pydyna_simple')
    logs_dir = os.path.join(pkg_share_dir, 'logs')

    os.environ['ROS_LOG_DIR'] = os.path.join(logs_dir, 'roslogs')
    # Set LOG format
    os.environ['RCUTILS_CONSOLE_OUTPUT_FORMAT'] = '[{severity} {time}] [{name}]: {message} ({function_name}() at {file_name}:{line_number})'

    ld = LaunchDescription()

    rosbag_record_all = ExecuteProcess(
        cmd=['ros2', 'bag', 'record', '-a'], # '-o', 'rosbags'
        output='screen'
    )

    start_pydyna_simple_node = Node(
        package='pydyna_simple',
        executable='simul',
        name='pydyna_simple_node',
        output='screen',
        parameters=[
                {'pkg_share_dir': pkg_share_dir},
                {'pkg_dir': pydyna_dir}
        ]
    )                   

    # start pydyna_simple_node
    ld.add_action(rosbag_record_all)
    ld.add_action(start_pydyna_simple_node)
    return ld