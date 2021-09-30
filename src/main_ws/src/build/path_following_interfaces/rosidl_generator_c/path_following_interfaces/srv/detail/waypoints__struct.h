// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from path_following_interfaces:srv\Waypoints.idl
// generated code does not contain a copyright notice

#ifndef PATH_FOLLOWING_INTERFACES__SRV__DETAIL__WAYPOINTS__STRUCT_H_
#define PATH_FOLLOWING_INTERFACES__SRV__DETAIL__WAYPOINTS__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Include directives for member types
// Member 'position'
#include "path_following_interfaces/msg/detail/positions_xy__struct.h"
// Member 'velocity'
#include "rosidl_runtime_c/primitives_sequence.h"

// Struct defined in srv/Waypoints in the package path_following_interfaces.
typedef struct path_following_interfaces__srv__Waypoints_Request
{
  path_following_interfaces__msg__PositionsXY position;
  rosidl_runtime_c__float__Sequence velocity;
} path_following_interfaces__srv__Waypoints_Request;

// Struct for a sequence of path_following_interfaces__srv__Waypoints_Request.
typedef struct path_following_interfaces__srv__Waypoints_Request__Sequence
{
  path_following_interfaces__srv__Waypoints_Request * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} path_following_interfaces__srv__Waypoints_Request__Sequence;


// Constants defined in the message

// Include directives for member types
// Member 'reporting'
#include "rosidl_runtime_c/string.h"

// Struct defined in srv/Waypoints in the package path_following_interfaces.
typedef struct path_following_interfaces__srv__Waypoints_Response
{
  rosidl_runtime_c__String reporting;
} path_following_interfaces__srv__Waypoints_Response;

// Struct for a sequence of path_following_interfaces__srv__Waypoints_Response.
typedef struct path_following_interfaces__srv__Waypoints_Response__Sequence
{
  path_following_interfaces__srv__Waypoints_Response * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} path_following_interfaces__srv__Waypoints_Response__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // PATH_FOLLOWING_INTERFACES__SRV__DETAIL__WAYPOINTS__STRUCT_H_
