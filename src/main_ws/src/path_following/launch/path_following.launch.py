import os

from ament_index_python.packages import get_package_share_directory, get_package_prefix
from launch import LaunchDescription  
from launch.actions import ExecuteProcess
from launch_ros.actions import Node

# obs: not exaclty shure where generate_launch_description is invoked
# however absolute paths should do, with get_package_share_directory

def generate_launch_description():
    pkg_share_dir = get_package_share_directory('path_following')
    pkg_install_dir = get_package_prefix('path_following')
    pkg_dir = os.path.join(pkg_install_dir, 'lib', 'pydyna_simple')
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
                {'pkg_dir': pkg_dir}
        ]
    )

    start_backend_node = Node(
        package='path_following',
        executable='backend',
        name='backend_node',
        output='screen'
    )

    start_los_guidance_node = Node(
        package='path_following',
        executable='los_guidance',
        name='los_guidance_node',
        output='screen'
    ) 

    start_surge_controller_node = Node(
        package='path_following',
        executable='surge_controller',
        name='surge_controller_node',
        output='screen'
    ) 

    start_yaw_controller_node = Node(
        package='path_following',
        executable='yaw_controller',
        name='yaw_controller_node',
        output='screen'
    )

    start_control_allocation_node = Node(
        package='path_following',
        executable='control_allocation',
        name='control_allocation_node',
        output='screen'
    )

    start_gps_imu_simul_node = Node(
        package='path_following',
        executable='gps_imu_simul',
        name='gps_imu_simul_node',
        output='screen'
    )

    start_kalman_filter_node = Node(
        package='path_following',
        executable='kalman_filter',
        name='kalman_filter_node',
        output='screen'
    ) 

    start_wave_filter_node = Node(
        package='path_following',
        executable='wave_filter',
        name='wave_filter_node',
        output='screen'
    ) 

    start_venus_node = Node(
        package='path_following',
        executable='venus',
        name='venus_node',
        output='screen'
    )          

    ld.add_action(rosbag_record_all)
    ld.add_action(start_pydyna_simple_node)
    ld.add_action(start_backend_node)
    ld.add_action(start_los_guidance_node)
    ld.add_action(start_surge_controller_node)
    ld.add_action(start_yaw_controller_node)
    ld.add_action(start_control_allocation_node)
    ld.add_action(start_gps_imu_simul_node)
    ld.add_action(start_kalman_filter_node)
    ld.add_action(start_wave_filter_node)
    ld.add_action(start_venus_node)
    
    return ld