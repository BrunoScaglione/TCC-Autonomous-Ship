// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from path_following_interfaces:msg\PositionsXY.idl
// generated code does not contain a copyright notice

#ifndef PATH_FOLLOWING_INTERFACES__MSG__DETAIL__POSITIONS_XY__STRUCT_H_
#define PATH_FOLLOWING_INTERFACES__MSG__DETAIL__POSITIONS_XY__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Include directives for member types
// Member 'x'
// Member 'y'
#include "rosidl_runtime_c/primitives_sequence.h"

// Struct defined in msg/PositionsXY in the package path_following_interfaces.
typedef struct path_following_interfaces__msg__PositionsXY
{
  rosidl_runtime_c__float__Sequence x;
  rosidl_runtime_c__float__Sequence y;
} path_following_interfaces__msg__PositionsXY;

// Struct for a sequence of path_following_interfaces__msg__PositionsXY.
typedef struct path_following_interfaces__msg__PositionsXY__Sequence
{
  path_following_interfaces__msg__PositionsXY * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} path_following_interfaces__msg__PositionsXY__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // PATH_FOLLOWING_INTERFACES__MSG__DETAIL__POSITIONS_XY__STRUCT_H_
