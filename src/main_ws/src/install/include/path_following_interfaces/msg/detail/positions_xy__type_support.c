// generated from rosidl_typesupport_introspection_c/resource/idl__type_support.c.em
// with input from path_following_interfaces:msg\PositionsXY.idl
// generated code does not contain a copyright notice

#include <stddef.h>
#include "path_following_interfaces/msg/detail/positions_xy__rosidl_typesupport_introspection_c.h"
#include "path_following_interfaces/msg/rosidl_typesupport_introspection_c__visibility_control.h"
#include "rosidl_typesupport_introspection_c/field_types.h"
#include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/message_introspection.h"
#include "path_following_interfaces/msg/detail/positions_xy__functions.h"
#include "path_following_interfaces/msg/detail/positions_xy__struct.h"


// Include directives for member types
// Member `x`
// Member `y`
#include "rosidl_runtime_c/primitives_sequence_functions.h"

#ifdef __cplusplus
extern "C"
{
#endif

void PositionsXY__rosidl_typesupport_introspection_c__PositionsXY_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  path_following_interfaces__msg__PositionsXY__init(message_memory);
}

void PositionsXY__rosidl_typesupport_introspection_c__PositionsXY_fini_function(void * message_memory)
{
  path_following_interfaces__msg__PositionsXY__fini(message_memory);
}

static rosidl_typesupport_introspection_c__MessageMember PositionsXY__rosidl_typesupport_introspection_c__PositionsXY_message_member_array[2] = {
  {
    "x",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_FLOAT,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    true,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(path_following_interfaces__msg__PositionsXY, x),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "y",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_FLOAT,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    true,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(path_following_interfaces__msg__PositionsXY, y),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers PositionsXY__rosidl_typesupport_introspection_c__PositionsXY_message_members = {
  "path_following_interfaces__msg",  // message namespace
  "PositionsXY",  // message name
  2,  // number of fields
  sizeof(path_following_interfaces__msg__PositionsXY),
  PositionsXY__rosidl_typesupport_introspection_c__PositionsXY_message_member_array,  // message members
  PositionsXY__rosidl_typesupport_introspection_c__PositionsXY_init_function,  // function to initialize message memory (memory has to be allocated)
  PositionsXY__rosidl_typesupport_introspection_c__PositionsXY_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t PositionsXY__rosidl_typesupport_introspection_c__PositionsXY_message_type_support_handle = {
  0,
  &PositionsXY__rosidl_typesupport_introspection_c__PositionsXY_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_path_following_interfaces
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, path_following_interfaces, msg, PositionsXY)() {
  if (!PositionsXY__rosidl_typesupport_introspection_c__PositionsXY_message_type_support_handle.typesupport_identifier) {
    PositionsXY__rosidl_typesupport_introspection_c__PositionsXY_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &PositionsXY__rosidl_typesupport_introspection_c__PositionsXY_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif
