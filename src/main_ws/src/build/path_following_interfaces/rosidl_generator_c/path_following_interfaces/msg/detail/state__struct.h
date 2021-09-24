// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from path_following_interfaces:msg\State.idl
// generated code does not contain a copyright notice

#ifndef PATH_FOLLOWING_INTERFACES__MSG__DETAIL__STATE__STRUCT_H_
#define PATH_FOLLOWING_INTERFACES__MSG__DETAIL__STATE__STRUCT_H_

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
#include "path_following_interfaces/msg/detail/position__struct.h"
// Member 'velocity'
#include "path_following_interfaces/msg/detail/velocity__struct.h"

// Struct defined in msg/State in the package path_following_interfaces.
typedef struct path_following_interfaces__msg__State
{
  path_following_interfaces__msg__Position position;
  path_following_interfaces__msg__Velocity velocity;
  float time;
} path_following_interfaces__msg__State;

// Struct for a sequence of path_following_interfaces__msg__State.
typedef struct path_following_interfaces__msg__State__Sequence
{
  path_following_interfaces__msg__State * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} path_following_interfaces__msg__State__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // PATH_FOLLOWING_INTERFACES__MSG__DETAIL__STATE__STRUCT_H_
