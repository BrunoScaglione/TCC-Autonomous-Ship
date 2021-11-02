// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from path_following_interfaces:msg\Waypoints.idl
// generated code does not contain a copyright notice
#include "path_following_interfaces/msg/detail/waypoints__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>


// Include directives for member types
// Member `position`
#include "path_following_interfaces/msg/detail/positions_xy__functions.h"
// Member `velocity`
#include "rosidl_runtime_c/primitives_sequence_functions.h"

bool
path_following_interfaces__msg__Waypoints__init(path_following_interfaces__msg__Waypoints * msg)
{
  if (!msg) {
    return false;
  }
  // position
  if (!path_following_interfaces__msg__PositionsXY__init(&msg->position)) {
    path_following_interfaces__msg__Waypoints__fini(msg);
    return false;
  }
  // velocity
  {
    bool success = rosidl_runtime_c__float__Sequence__init(&msg->velocity, 5);
    if (!success) {
      goto abort_init_0;
    }
  }
  msg->velocity.data[0] = 1.0f;
  msg->velocity.data[1] = 2.0f;
  msg->velocity.data[2] = 3.0f;
  msg->velocity.data[3] = 4.0f;
  msg->velocity.data[4] = 5.0f;
  return true;
abort_init_0:
  return false;
}

void
path_following_interfaces__msg__Waypoints__fini(path_following_interfaces__msg__Waypoints * msg)
{
  if (!msg) {
    return;
  }
  // position
  path_following_interfaces__msg__PositionsXY__fini(&msg->position);
  // velocity
  rosidl_runtime_c__float__Sequence__fini(&msg->velocity);
}

path_following_interfaces__msg__Waypoints *
path_following_interfaces__msg__Waypoints__create()
{
  path_following_interfaces__msg__Waypoints * msg = (path_following_interfaces__msg__Waypoints *)malloc(sizeof(path_following_interfaces__msg__Waypoints));
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(path_following_interfaces__msg__Waypoints));
  bool success = path_following_interfaces__msg__Waypoints__init(msg);
  if (!success) {
    free(msg);
    return NULL;
  }
  return msg;
}

void
path_following_interfaces__msg__Waypoints__destroy(path_following_interfaces__msg__Waypoints * msg)
{
  if (msg) {
    path_following_interfaces__msg__Waypoints__fini(msg);
  }
  free(msg);
}


bool
path_following_interfaces__msg__Waypoints__Sequence__init(path_following_interfaces__msg__Waypoints__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  path_following_interfaces__msg__Waypoints * data = NULL;
  if (size) {
    data = (path_following_interfaces__msg__Waypoints *)calloc(size, sizeof(path_following_interfaces__msg__Waypoints));
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = path_following_interfaces__msg__Waypoints__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        path_following_interfaces__msg__Waypoints__fini(&data[i - 1]);
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
path_following_interfaces__msg__Waypoints__Sequence__fini(path_following_interfaces__msg__Waypoints__Sequence * array)
{
  if (!array) {
    return;
  }
  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      path_following_interfaces__msg__Waypoints__fini(&array->data[i]);
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

path_following_interfaces__msg__Waypoints__Sequence *
path_following_interfaces__msg__Waypoints__Sequence__create(size_t size)
{
  path_following_interfaces__msg__Waypoints__Sequence * array = (path_following_interfaces__msg__Waypoints__Sequence *)malloc(sizeof(path_following_interfaces__msg__Waypoints__Sequence));
  if (!array) {
    return NULL;
  }
  bool success = path_following_interfaces__msg__Waypoints__Sequence__init(array, size);
  if (!success) {
    free(array);
    return NULL;
  }
  return array;
}

void
path_following_interfaces__msg__Waypoints__Sequence__destroy(path_following_interfaces__msg__Waypoints__Sequence * array)
{
  if (array) {
    path_following_interfaces__msg__Waypoints__Sequence__fini(array);
  }
  free(array);
}
