// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from path_following_interfaces:msg\State.idl
// generated code does not contain a copyright notice
#include "path_following_interfaces/msg/detail/state__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>


// Include directives for member types
// Member `position`
#include "path_following_interfaces/msg/detail/position__functions.h"
// Member `velocity`
#include "path_following_interfaces/msg/detail/velocity__functions.h"

bool
path_following_interfaces__msg__State__init(path_following_interfaces__msg__State * msg)
{
  if (!msg) {
    return false;
  }
  // position
  if (!path_following_interfaces__msg__Position__init(&msg->position)) {
    path_following_interfaces__msg__State__fini(msg);
    return false;
  }
  // velocity
  if (!path_following_interfaces__msg__Velocity__init(&msg->velocity)) {
    path_following_interfaces__msg__State__fini(msg);
    return false;
  }
  // time
  msg->time = 0.0f;
  return true;
}

void
path_following_interfaces__msg__State__fini(path_following_interfaces__msg__State * msg)
{
  if (!msg) {
    return;
  }
  // position
  path_following_interfaces__msg__Position__fini(&msg->position);
  // velocity
  path_following_interfaces__msg__Velocity__fini(&msg->velocity);
  // time
}

path_following_interfaces__msg__State *
path_following_interfaces__msg__State__create()
{
  path_following_interfaces__msg__State * msg = (path_following_interfaces__msg__State *)malloc(sizeof(path_following_interfaces__msg__State));
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(path_following_interfaces__msg__State));
  bool success = path_following_interfaces__msg__State__init(msg);
  if (!success) {
    free(msg);
    return NULL;
  }
  return msg;
}

void
path_following_interfaces__msg__State__destroy(path_following_interfaces__msg__State * msg)
{
  if (msg) {
    path_following_interfaces__msg__State__fini(msg);
  }
  free(msg);
}


bool
path_following_interfaces__msg__State__Sequence__init(path_following_interfaces__msg__State__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  path_following_interfaces__msg__State * data = NULL;
  if (size) {
    data = (path_following_interfaces__msg__State *)calloc(size, sizeof(path_following_interfaces__msg__State));
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = path_following_interfaces__msg__State__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        path_following_interfaces__msg__State__fini(&data[i - 1]);
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
path_following_interfaces__msg__State__Sequence__fini(path_following_interfaces__msg__State__Sequence * array)
{
  if (!array) {
    return;
  }
  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      path_following_interfaces__msg__State__fini(&array->data[i]);
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

path_following_interfaces__msg__State__Sequence *
path_following_interfaces__msg__State__Sequence__create(size_t size)
{
  path_following_interfaces__msg__State__Sequence * array = (path_following_interfaces__msg__State__Sequence *)malloc(sizeof(path_following_interfaces__msg__State__Sequence));
  if (!array) {
    return NULL;
  }
  bool success = path_following_interfaces__msg__State__Sequence__init(array, size);
  if (!success) {
    free(array);
    return NULL;
  }
  return array;
}

void
path_following_interfaces__msg__State__Sequence__destroy(path_following_interfaces__msg__State__Sequence * array)
{
  if (array) {
    path_following_interfaces__msg__State__Sequence__fini(array);
  }
  free(array);
}
