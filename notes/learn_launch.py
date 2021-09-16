#https://design.ros2.org/articles/node_lifecycle.html
#https://github.com/ros2/launch_ros/blob/master/launch_ros/examples/lifecycle_pub_sub_launch.py
#https://github.com/ros2/launch/blob/foxy/launch/doc/source/architecture.rst#id1
#https://answers.ros.org/question/304370/ros2-launch-how-to-correctly-create-a-lifecycle-launch-file/
  
"""Launch a lifecycle talker and a lifecycle listener."""

import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))  # noqa
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'launch'))  # noqa

import launch  # noqa: E402
import launch.actions  # noqa: E402
import launch.events  # noqa: E402

import launch_ros.actions  # noqa: E402
import launch_ros.events  # noqa: E402
import launch_ros.events.lifecycle  # noqa: E402

import lifecycle_msgs.msg  # noqa: E402


def main(argv=sys.argv[1:]):
    """Run lifecycle nodes via launch."""
    ld = launch.LaunchDescription()

    # Prepare the talker node.
    talker_node = launch_ros.actions.LifecycleNode(
        name='talker', namespace='',
        package='lifecycle', executable='lifecycle_talker', output='screen')

    # When the talker reaches the 'inactive' state, make it take the 'activate' transition.
    register_event_handler_for_talker_reaches_inactive_state = launch.actions.RegisterEventHandler(
        launch_ros.event_handlers.OnStateTransition(
            target_lifecycle_node=talker_node, goal_state='inactive',
            entities=[
                launch.actions.LogInfo(
                    msg="node 'talker' reached the 'inactive' state, 'activating'."),
                launch.actions.EmitEvent(event=launch_ros.events.lifecycle.ChangeState(
                    lifecycle_node_matcher=launch.events.matches_action(talker_node),
                    transition_id=lifecycle_msgs.msg.Transition.TRANSITION_ACTIVATE,
                )),
            ],
        )
    )

    # When the talker node reaches the 'active' state, log a message and start the listener node.
    register_event_handler_for_talker_reaches_active_state = launch.actions.RegisterEventHandler(
        launch_ros.event_handlers.OnStateTransition(
            target_lifecycle_node=talker_node, goal_state='active',
            entities=[
                launch.actions.LogInfo(
                    msg="node 'talker' reached the 'active' state, launching 'listener'."),
                launch_ros.actions.LifecycleNode(
                    name='listener', namespace='',
                    package='lifecycle', executable='lifecycle_listener', output='screen'),
            ],
        )
    )

    # Make the talker node take the 'configure' transition.
    emit_event_to_request_that_talker_does_configure_transition = launch.actions.EmitEvent(
        event=launch_ros.events.lifecycle.ChangeState(
            lifecycle_node_matcher=launch.events.matches_action(talker_node),
            transition_id=lifecycle_msgs.msg.Transition.TRANSITION_CONFIGURE,
        )
    )

    # Add the actions to the launch description.
    # The order they are added reflects the order in which they will be executed.
    ld.add_action(register_event_handler_for_talker_reaches_inactive_state)
    ld.add_action(register_event_handler_for_talker_reaches_active_state)
    ld.add_action(talker_node)
    ld.add_action(emit_event_to_request_that_talker_does_configure_transition)

    print('Starting introspection of launch description...')
    print('')

    print(launch.LaunchIntrospector().format_launch_description(ld))

    print('')
    print('Starting launch of launch description...')
    print('')

    # ls = launch.LaunchService(argv=argv, debug=True)
    ls = launch.LaunchService(argv=argv)
    ls.include_launch_description(ld)
    return ls.run()


if __name__ == '__main__':
    main()