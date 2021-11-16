// generated from rosidl_generator_c/resource/idl__functions.h.em
// with input from path_following_interfaces:msg\State.idl
// generated code does not contain a copyright notice

#ifndef PATH_FOLLOWING_INTERFACES__MSG__DETAIL__STATE__FUNCTIONS_H_
#define PATH_FOLLOWING_INTERFACES__MSG__DETAIL__STATE__FUNCTIONS_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stdlib.h>

#include "rosidl_runtime_c/visibility_control.h"
#include "path_following_interfaces/msg/rosidl_generator_c__visibility_control.h"

#include "path_following_interfaces/msg/detail/state__struct.h"

/// Initialize msg/State message.
/**
 * If the init function is called twice for the same message without
 * calling fini inbetween previously allocated memory will be leaked.
 * \param[in,out] msg The previously allocated message pointer.
 * Fields without a default value will not be initialized by this function.
 * You might want to call memset(msg, 0, sizeof(
 * path_following_interfaces__msg__State
 * )) before or use
 * path_following_interfaces__msg__State__create()
 * to allocate and initialize the message.
 * \return true if initialization was successful, otherwise false
 */
ROSIDL_GENERATOR_C_PUBLIC_path_following_interfaces
bool
path_following_interfaces__msg__State__init(path_following_interfaces__msg__State * msg);

/// Finalize msg/State message.
/**
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_path_following_interfaces
void
path_following_interfaces__msg__State__fini(path_following_interfaces__msg__State * msg);

/// Create msg/State message.
/**
 * It allocates the memory for the message, sets the memory to zero, and
 * calls
 * path_following_interfaces__msg__State__init().
 * \return The pointer to the initialized message if successful,
 * otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_path_following_interfaces
path_following_interfaces__msg__State *
path_following_interfaces__msg__State__create();

/// Destroy msg/State message.
/**
 * It calls
 * path_following_interfaces__msg__State__fini()
 * and frees the memory of the message.
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_path_following_interfaces
void
path_following_interfaces__msg__State__destroy(path_following_interfaces__msg__State * msg);


/// Initialize array of msg/State messages.
/**
 * It allocates the memory for the number of elements and calls
 * path_following_interfaces__msg__State__init()
 * for each element of the array.
 * \param[in,out] array The allocated array pointer.
 * \param[in] size The size / capacity of the array.
 * \return true if initialization was successful, otherwise false
 * If the array pointer is valid and the size is zero it is guaranteed
 # to return true.
 */
ROSIDL_GENERATOR_C_PUBLIC_path_following_interfaces
bool
path_following_interfaces__msg__State__Sequence__init(path_following_interfaces__msg__State__Sequence * array, size_t size);

/// Finalize array of msg/State messages.
/**
 * It calls
 * path_following_interfaces__msg__State__fini()
 * for each element of the array and frees the memory for the number of
 * elements.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_path_following_interfaces
void
path_following_interfaces__msg__State__Sequence__fini(path_following_interfaces__msg__State__Sequence * array);

/// Create array of msg/State messages.
/**
 * It allocates the memory for the array and calls
 * path_following_interfaces__msg__State__Sequence__init().
 * \param[in] size The size / capacity of the array.
 * \return The pointer to the initialized array if successful, otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_path_following_interfaces
path_following_interfaces__msg__State__Sequence *
path_following_interfaces__msg__State__Sequence__create(size_t size);

/// Destroy array of msg/State messages.
/**
 * It calls
 * path_following_interfaces__msg__State__Sequence__fini()
 * on the array,
 * and frees the memory of the array.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_path_following_interfaces
void
path_following_interfaces__msg__State__Sequence__destroy(path_following_interfaces__msg__State__Sequence * array);

#ifdef __cplusplus
}
#endif

#endif  // PATH_FOLLOWING_INTERFACES__MSG__DETAIL__STATE__FUNCTIONS_H_
