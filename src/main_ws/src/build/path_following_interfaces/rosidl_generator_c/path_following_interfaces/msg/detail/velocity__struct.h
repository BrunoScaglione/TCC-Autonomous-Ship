// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from path_following_interfaces:msg\Velocity.idl
// generated code does not contain a copyright notice

#ifndef PATH_FOLLOWING_INTERFACES__MSG__DETAIL__VELOCITY__STRUCT_H_
#define PATH_FOLLOWING_INTERFACES__MSG__DETAIL__VELOCITY__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Struct defined in msg/Velocity in the package path_following_interfaces.
typedef struct path_following_interfaces__msg__Velocity
{
  float u;
  float v;
  float r;
} path_following_interfaces__msg__Velocity;

// Struct for a sequence of path_following_interfaces__msg__Velocity.
typedef struct path_following_interfaces__msg__Velocity__Sequence
{
  path_following_interfaces__msg__Velocity * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} path_following_interfaces__msg__Velocity__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // PATH_FOLLOWING_INTERFACES__MSG__DETAIL__VELOCITY__STRUCT_H_
