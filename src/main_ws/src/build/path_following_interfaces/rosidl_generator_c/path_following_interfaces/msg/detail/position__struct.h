// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from path_following_interfaces:msg\Position.idl
// generated code does not contain a copyright notice

#ifndef PATH_FOLLOWING_INTERFACES__MSG__DETAIL__POSITION__STRUCT_H_
#define PATH_FOLLOWING_INTERFACES__MSG__DETAIL__POSITION__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Struct defined in msg/Position in the package path_following_interfaces.
typedef struct path_following_interfaces__msg__Position
{
  float x;
  float y;
  float theta;
} path_following_interfaces__msg__Position;

// Struct for a sequence of path_following_interfaces__msg__Position.
typedef struct path_following_interfaces__msg__Position__Sequence
{
  path_following_interfaces__msg__Position * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} path_following_interfaces__msg__Position__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // PATH_FOLLOWING_INTERFACES__MSG__DETAIL__POSITION__STRUCT_H_
