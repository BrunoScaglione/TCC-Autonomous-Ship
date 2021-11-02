// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from path_following_interfaces:msg\Position.idl
// generated code does not contain a copyright notice
#include "path_following_interfaces/msg/detail/position__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>


bool
path_following_interfaces__msg__Position__init(path_following_interfaces__msg__Position * msg)
{
  if (!msg) {
    return false;
  }
  // x
  msg->x = 0.0f;
  // y
  msg->y = 0.0f;
  // psi
  msg->psi = 0.0f;
  return true;
}

void
path_following_interfaces__msg__Position__fini(path_following_interfaces__msg__Position * msg)
{
  if (!msg) {
    return;
  }
  // x
  // y
  // psi
}

path_following_interfaces__msg__Position *
path_following_interfaces__msg__Position__create()
{
  path_following_interfaces__msg__Position * msg = (path_following_interfaces__msg__Position *)malloc(sizeof(path_following_interfaces__msg__Position));
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(path_following_interfaces__msg__Position));
  bool success = path_following_interfaces__msg__Position__init(msg);
  if (!success) {
    free(msg);
    return NULL;
  }
  return msg;
}

void
path_following_interfaces__msg__Position__destroy(path_following_interfaces__msg__Position * msg)
{
  if (msg) {
    path_following_interfaces__msg__Position__fini(msg);
  }
  free(msg);
}


bool
path_following_interfaces__msg__Position__Sequence__init(path_following_interfaces__msg__Position__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  path_following_interfaces__msg__Position * data = NULL;
  if (size) {
    data = (path_following_interfaces__msg__Position *)calloc(size, sizeof(path_following_interfaces__msg__Position));
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = path_following_interfaces__msg__Position__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        path_following_interfaces__msg__Position__fini(&data[i - 1]);
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
path_following_interfaces__msg__Position__Sequence__fini(path_following_interfaces__msg__Position__Sequence * array)
{
  if (!array) {
    return;
  }
  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      path_following_interfaces__msg__Position__fini(&array->data[i]);
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

path_following_interfaces__msg__Position__Sequence *
path_following_interfaces__msg__Position__Sequence__create(size_t size)
{
  path_following_interfaces__msg__Position__Sequence * array = (path_following_interfaces__msg__Position__Sequence *)malloc(sizeof(path_following_interfaces__msg__Position__Sequence));
  if (!array) {
    return NULL;
  }
  bool success = path_following_interfaces__msg__Position__Sequence__init(array, size);
  if (!success) {
    free(array);
    return NULL;
  }
  return array;
}

void
path_following_interfaces__msg__Position__Sequence__destroy(path_following_interfaces__msg__Position__Sequence * array)
{
  if (array) {
    path_following_interfaces__msg__Position__Sequence__fini(array);
  }
  free(array);
}
