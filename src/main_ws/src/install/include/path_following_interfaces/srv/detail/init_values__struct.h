// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from path_following_interfaces:srv\InitValues.idl
// generated code does not contain a copyright notice

#ifndef PATH_FOLLOWING_INTERFACES__SRV__DETAIL__INIT_VALUES__STRUCT_H_
#define PATH_FOLLOWING_INTERFACES__SRV__DETAIL__INIT_VALUES__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Include directives for member types
// Member 'initial_state'
#include "path_following_interfaces/msg/detail/state__struct.h"
// Member 'waypoints'
#include "path_following_interfaces/msg/detail/waypoints__struct.h"

// Struct defined in srv/InitValues in the package path_following_interfaces.
typedef struct path_following_interfaces__srv__InitValues_Request
{
  path_following_interfaces__msg__State initial_state;
  path_following_interfaces__msg__Waypoints waypoints;
  float surge;
  float yaw;
} path_following_interfaces__srv__InitValues_Request;

// Struct for a sequence of path_following_interfaces__srv__InitValues_Request.
typedef struct path_following_interfaces__srv__InitValues_Request__Sequence
{
  path_following_interfaces__srv__InitValues_Request * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} path_following_interfaces__srv__InitValues_Request__Sequence;


// Constants defined in the message

// Struct defined in srv/InitValues in the package path_following_interfaces.
typedef struct path_following_interfaces__srv__InitValues_Response
{
  float surge;
  float yaw;
} path_following_interfaces__srv__InitValues_Response;

// Struct for a sequence of path_following_interfaces__srv__InitValues_Response.
typedef struct path_following_interfaces__srv__InitValues_Response__Sequence
{
  path_following_interfaces__srv__InitValues_Response * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} path_following_interfaces__srv__InitValues_Response__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // PATH_FOLLOWING_INTERFACES__SRV__DETAIL__INIT_VALUES__STRUCT_H_
