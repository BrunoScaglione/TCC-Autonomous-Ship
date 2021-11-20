// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from path_following_interfaces:srv\InitValues.idl
// generated code does not contain a copyright notice
#include "path_following_interfaces/srv/detail/init_values__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

// Include directives for member types
// Member `initial_state`
#include "path_following_interfaces/msg/detail/state__functions.h"
// Member `waypoints`
#include "path_following_interfaces/msg/detail/waypoints__functions.h"

bool
path_following_interfaces__srv__InitValues_Request__init(path_following_interfaces__srv__InitValues_Request * msg)
{
  if (!msg) {
    return false;
  }
  // initial_state
  if (!path_following_interfaces__msg__State__init(&msg->initial_state)) {
    path_following_interfaces__srv__InitValues_Request__fini(msg);
    return false;
  }
  // waypoints
  if (!path_following_interfaces__msg__Waypoints__init(&msg->waypoints)) {
    path_following_interfaces__srv__InitValues_Request__fini(msg);
    return false;
  }
  // surge
  msg->surge = 0.0f;
  // yaw
  msg->yaw = 0.0f;
  return true;
}

void
path_following_interfaces__srv__InitValues_Request__fini(path_following_interfaces__srv__InitValues_Request * msg)
{
  if (!msg) {
    return;
  }
  // initial_state
  path_following_interfaces__msg__State__fini(&msg->initial_state);
  // waypoints
  path_following_interfaces__msg__Waypoints__fini(&msg->waypoints);
  // surge
  // yaw
}

path_following_interfaces__srv__InitValues_Request *
path_following_interfaces__srv__InitValues_Request__create()
{
  path_following_interfaces__srv__InitValues_Request * msg = (path_following_interfaces__srv__InitValues_Request *)malloc(sizeof(path_following_interfaces__srv__InitValues_Request));
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(path_following_interfaces__srv__InitValues_Request));
  bool success = path_following_interfaces__srv__InitValues_Request__init(msg);
  if (!success) {
    free(msg);
    return NULL;
  }
  return msg;
}

void
path_following_interfaces__srv__InitValues_Request__destroy(path_following_interfaces__srv__InitValues_Request * msg)
{
  if (msg) {
    path_following_interfaces__srv__InitValues_Request__fini(msg);
  }
  free(msg);
}


bool
path_following_interfaces__srv__InitValues_Request__Sequence__init(path_following_interfaces__srv__InitValues_Request__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  path_following_interfaces__srv__InitValues_Request * data = NULL;
  if (size) {
    data = (path_following_interfaces__srv__InitValues_Request *)calloc(size, sizeof(path_following_interfaces__srv__InitValues_Request));
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = path_following_interfaces__srv__InitValues_Request__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        path_following_interfaces__srv__InitValues_Request__fini(&data[i - 1]);
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
path_following_interfaces__srv__InitValues_Request__Sequence__fini(path_following_interfaces__srv__InitValues_Request__Sequence * array)
{
  if (!array) {
    return;
  }
  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      path_following_interfaces__srv__InitValues_Request__fini(&array->data[i]);
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

path_following_interfaces__srv__InitValues_Request__Sequence *
path_following_interfaces__srv__InitValues_Request__Sequence__create(size_t size)
{
  path_following_interfaces__srv__InitValues_Request__Sequence * array = (path_following_interfaces__srv__InitValues_Request__Sequence *)malloc(sizeof(path_following_interfaces__srv__InitValues_Request__Sequence));
  if (!array) {
    return NULL;
  }
  bool success = path_following_interfaces__srv__InitValues_Request__Sequence__init(array, size);
  if (!success) {
    free(array);
    return NULL;
  }
  return array;
}

void
path_following_interfaces__srv__InitValues_Request__Sequence__destroy(path_following_interfaces__srv__InitValues_Request__Sequence * array)
{
  if (array) {
    path_following_interfaces__srv__InitValues_Request__Sequence__fini(array);
  }
  free(array);
}


bool
path_following_interfaces__srv__InitValues_Response__init(path_following_interfaces__srv__InitValues_Response * msg)
{
  if (!msg) {
    return false;
  }
  // surge
  msg->surge = 0.0f;
  // yaw
  msg->yaw = 0.0f;
  return true;
}

void
path_following_interfaces__srv__InitValues_Response__fini(path_following_interfaces__srv__InitValues_Response * msg)
{
  if (!msg) {
    return;
  }
  // surge
  // yaw
}

path_following_interfaces__srv__InitValues_Response *
path_following_interfaces__srv__InitValues_Response__create()
{
  path_following_interfaces__srv__InitValues_Response * msg = (path_following_interfaces__srv__InitValues_Response *)malloc(sizeof(path_following_interfaces__srv__InitValues_Response));
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(path_following_interfaces__srv__InitValues_Response));
  bool success = path_following_interfaces__srv__InitValues_Response__init(msg);
  if (!success) {
    free(msg);
    return NULL;
  }
  return msg;
}

void
path_following_interfaces__srv__InitValues_Response__destroy(path_following_interfaces__srv__InitValues_Response * msg)
{
  if (msg) {
    path_following_interfaces__srv__InitValues_Response__fini(msg);
  }
  free(msg);
}


bool
path_following_interfaces__srv__InitValues_Response__Sequence__init(path_following_interfaces__srv__InitValues_Response__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  path_following_interfaces__srv__InitValues_Response * data = NULL;
  if (size) {
    data = (path_following_interfaces__srv__InitValues_Response *)calloc(size, sizeof(path_following_interfaces__srv__InitValues_Response));
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = path_following_interfaces__srv__InitValues_Response__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        path_following_interfaces__srv__InitValues_Response__fini(&data[i - 1]);
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
path_following_interfaces__srv__InitValues_Response__Sequence__fini(path_following_interfaces__srv__InitValues_Response__Sequence * array)
{
  if (!array) {
    return;
  }
  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      path_following_interfaces__srv__InitValues_Response__fini(&array->data[i]);
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

path_following_interfaces__srv__InitValues_Response__Sequence *
path_following_interfaces__srv__InitValues_Response__Sequence__create(size_t size)
{
  path_following_interfaces__srv__InitValues_Response__Sequence * array = (path_following_interfaces__srv__InitValues_Response__Sequence *)malloc(sizeof(path_following_interfaces__srv__InitValues_Response__Sequence));
  if (!array) {
    return NULL;
  }
  bool success = path_following_interfaces__srv__InitValues_Response__Sequence__init(array, size);
  if (!success) {
    free(array);
    return NULL;
  }
  return array;
}

void
path_following_interfaces__srv__InitValues_Response__Sequence__destroy(path_following_interfaces__srv__InitValues_Response__Sequence * array)
{
  if (array) {
    path_following_interfaces__srv__InitValues_Response__Sequence__fini(array);
  }
  free(array);
}