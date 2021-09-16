from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    ld = LaunchDescription()
    
    pydyna_simple_node = Node(
        package='pydyna_simple',
        executable='pydyna_simple',
        name='pydyna_simple_node',
        output='screen',
        emulate_tty=True
    )                                                  

    # start pydyna_simple_node
    ld.add_action(pydyna_simple_node)
    return ld