import os

from ament_index_python.packages import get_package_share_directory, get_package_prefix
from launch import LaunchDescription
from launch_ros.actions import Node

# obs: not exaclty shure where generate_launch_description is invoked
# however absolute paths should do, with get_package_share_directory

def generate_launch_description():
    pkg_share_dir = get_package_share_directory('pydyna_simple')
    pkg_install_dir = get_package_prefix('pydyna_simple')
    pkg_dir =  os.path.join(pkg_install_dir, 'lib', 'pydyna_simple')
    logs_dir = os.path.join(pkg_share_dir, 'logs')

    os.environ['ROS_LOG_DIR'] = os.path.join(logs_dir, 'roslogs')
    # Set LOG format
    os.environ['RCUTILS_CONSOLE_OUTPUT_FORMAT'] = '[{severity} {time}] [{name}]: {message} ({function_name}() at {file_name}:{line_number})'

    ld = LaunchDescription()

    cd_2_logs = launch.actions.ExecuteProcess(
            cmd=['cd', logs_dir],
            output='screen'
    ) 

    rosbag_record_all = launch.actions.ExecuteProcess(
            cmd=['ros2', 'bag', 'record', '-o', 'rosbags\subset' , '-a'],
            output='screen'
    )

    pydyna_simple_node = Node(
        package='pydyna_simple',
        executable='pydyna_simple',
        name='/pydyna_simple_node',
        output='screen',
        emulate_tty=True,
        parameters=[
                {'pkg_share_dir': pkg_share_dir},
                {'pkg_dir': pkg_dir}
        ]
    )                   

    # start pydyna_simple_node
    ld.add_action(cd_2_logs)
    ld.add_action(rosbag_record_all)
    ld.add_action(pydyna_simple_node)
    return ld