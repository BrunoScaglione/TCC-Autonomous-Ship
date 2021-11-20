// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from path_following_interfaces:msg\PositionsXY.idl
// generated code does not contain a copyright notice
#include "path_following_interfaces/msg/detail/positions_xy__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>


// Include directives for member types
// Member `x`
// Member `y`
#include "rosidl_runtime_c/primitives_sequence_functions.h"

bool
path_following_interfaces__msg__PositionsXY__init(path_following_interfaces__msg__PositionsXY * msg)
{
  if (!msg) {
    return false;
  }
  // x
  {
    bool success = rosidl_runtime_c__float__Sequence__init(&msg->x, 5);
    if (!success) {
      goto abort_init_0;
    }
  }
  msg->x.data[0] = 500.0f;
  msg->x.data[1] = 1000.0f;
  msg->x.data[2] = 1500.0f;
  msg->x.data[3] = 2000.0f;
  msg->x.data[4] = 2500.0f;
  // y
  {
    bool success = rosidl_runtime_c__float__Sequence__init(&msg->y, 5);
    if (!success) {
      goto abort_init_1;
    }
  }
  msg->y.data[0] = 500.0f;
  msg->y.data[1] = 1000.0f;
  msg->y.data[2] = 1500.0f;
  msg->y.data[3] = 2000.0f;
  msg->y.data[4] = 2500.0f;
  return true;
abort_init_1:
  rosidl_runtime_c__float__Sequence__fini(&msg->x);
abort_init_0:
  return false;
}

void
path_following_interfaces__msg__PositionsXY__fini(path_following_interfaces__msg__PositionsXY * msg)
{
  if (!msg) {
    return;
  }
  // x
  rosidl_runtime_c__float__Sequence__fini(&msg->x);
  // y
  rosidl_runtime_c__float__Sequence__fini(&msg->y);
}

path_following_interfaces__msg__PositionsXY *
path_following_interfaces__msg__PositionsXY__create()
{
  path_following_interfaces__msg__PositionsXY * msg = (path_following_interfaces__msg__PositionsXY *)malloc(sizeof(path_following_interfaces__msg__PositionsXY));
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(path_following_interfaces__msg__PositionsXY));
  bool success = path_following_interfaces__msg__PositionsXY__init(msg);
  if (!success) {
    free(msg);
    return NULL;
  }
  return msg;
}

void
path_following_interfaces__msg__PositionsXY__destroy(path_following_interfaces__msg__PositionsXY * msg)
{
  if (msg) {
    path_following_interfaces__msg__PositionsXY__fini(msg);
  }
  free(msg);
}


bool
path_following_interfaces__msg__PositionsXY__Sequence__init(path_following_interfaces__msg__PositionsXY__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  path_following_interfaces__msg__PositionsXY * data = NULL;
  if (size) {
    data = (path_following_interfaces__msg__PositionsXY *)calloc(size, sizeof(path_following_interfaces__msg__PositionsXY));
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = path_following_interfaces__msg__PositionsXY__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        path_following_interfaces__msg__PositionsXY__fini(&data[i - 1]);
      }
      free(data);
      return false;
    }
  }
  array->data = data;
  array->size = size;
  array->capacity = size;
  return true;
}

void
path_following_interfaces__msg__PositionsXY__Sequence__fini(path_following_interfaces__msg__PositionsXY__Sequence * array)
{
  if (!array) {
    return;
  }
  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      path_following_interfaces__msg__PositionsXY__fini(&array->data[i]);
    }
    free(array->data);
    array->data = NULL;
    array->size = 0;
    array->capacity = 0;
  } else {
    // ensure that data, size, and capacity values are consistent
    assert(0 == array->size);
    assert(0 == array->capacity);
  }
}

path_following_interfaces__msg__PositionsXY__Sequence *
path_following_interfaces__msg__PositionsXY__Sequence__create(size_t size)
{
  path_following_interfaces__msg__PositionsXY__Sequence * array = (path_following_interfaces__msg__PositionsXY__Sequence *)malloc(sizeof(path_following_interfaces__msg__PositionsXY__Sequence));
  if (!array) {
    return NULL;
  }
  bool success = path_following_interfaces__msg__PositionsXY__Sequence__init(array, size);
  if (!success) {
    free(array);
    return NULL;
  }
  return array;
}

void
path_following_interfaces__msg__PositionsXY__Sequence__destroy(path_following_interfaces__msg__PositionsXY__Sequence * array)
{
  if (array) {
    path_following_interfaces__msg__PositionsXY__Sequence__fini(array);
  }
  free(array);
}
