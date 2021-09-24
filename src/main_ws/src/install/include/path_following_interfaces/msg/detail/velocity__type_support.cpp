// generated from rosidl_typesupport_introspection_cpp/resource/idl__type_support.cpp.em
// with input from path_following_interfaces:msg\Velocity.idl
// generated code does not contain a copyright notice

#include "array"
#include "cstddef"
#include "string"
#include "vector"
#include "rosidl_runtime_c/message_type_support_struct.h"
#include "rosidl_typesupport_cpp/message_type_support.hpp"
#include "rosidl_typesupport_interface/macros.h"
#include "path_following_interfaces/msg/detail/velocity__struct.hpp"
#include "rosidl_typesupport_introspection_cpp/field_types.hpp"
#include "rosidl_typesupport_introspection_cpp/identifier.hpp"
#include "rosidl_typesupport_introspection_cpp/message_introspection.hpp"
#include "rosidl_typesupport_introspection_cpp/message_type_support_decl.hpp"
#include "rosidl_typesupport_introspection_cpp/visibility_control.h"

namespace path_following_interfaces
{

namespace msg
{

namespace rosidl_typesupport_introspection_cpp
{

void Velocity_init_function(
  void * message_memory, rosidl_runtime_cpp::MessageInitialization _init)
{
  new (message_memory) path_following_interfaces::msg::Velocity(_init);
}

void Velocity_fini_function(void * message_memory)
{
  auto typed_message = static_cast<path_following_interfaces::msg::Velocity *>(message_memory);
  typed_message->~Velocity();
}

static const ::rosidl_typesupport_introspection_cpp::MessageMember Velocity_message_member_array[3] = {
  {
    "u",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_FLOAT,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(path_following_interfaces::msg::Velocity, u),  // bytes offset in struct
    nullptr,  // default value
    nullptr,  // size() function pointer
    nullptr,  // get_const(index) function pointer
    nullptr,  // get(index) function pointer
    nullptr  // resize(index) function pointer
  },
  {
    "v",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_FLOAT,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(path_following_interfaces::msg::Velocity, v),  // bytes offset in struct
    nullptr,  // default value
    nullptr,  // size() function pointer
    nullptr,  // get_const(index) function pointer
    nullptr,  // get(index) function pointer
    nullptr  // resize(index) function pointer
  },
  {
    "r",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_FLOAT,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(path_following_interfaces::msg::Velocity, r),  // bytes offset in struct
    nullptr,  // default value
    nullptr,  // size() function pointer
    nullptr,  // get_const(index) function pointer
    nullptr,  // get(index) function pointer
    nullptr  // resize(index) function pointer
  }
};

static const ::rosidl_typesupport_introspection_cpp::MessageMembers Velocity_message_members = {
  "path_following_interfaces::msg",  // message namespace
  "Velocity",  // message name
  3,  // number of fields
  sizeof(path_following_interfaces::msg::Velocity),
  Velocity_message_member_array,  // message members
  Velocity_init_function,  // function to initialize message memory (memory has to be allocated)
  Velocity_fini_function  // function to terminate message instance (will not free memory)
};

static const rosidl_message_type_support_t Velocity_message_type_support_handle = {
  ::rosidl_typesupport_introspection_cpp::typesupport_identifier,
  &Velocity_message_members,
  get_message_typesupport_handle_function,
};

}  // namespace rosidl_typesupport_introspection_cpp

}  // namespace msg

}  // namespace path_following_interfaces


namespace rosidl_typesupport_introspection_cpp
{

template<>
ROSIDL_TYPESUPPORT_INTROSPECTION_CPP_PUBLIC
const rosidl_message_type_support_t *
get_message_type_support_handle<path_following_interfaces::msg::Velocity>()
{
  return &::path_following_interfaces::msg::rosidl_typesupport_introspection_cpp::Velocity_message_type_support_handle;
}

}  // namespace rosidl_typesupport_introspection_cpp

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_INTROSPECTION_CPP_PUBLIC
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_cpp, path_following_interfaces, msg, Velocity)() {
  return &::path_following_interfaces::msg::rosidl_typesupport_introspection_cpp::Velocity_message_type_support_handle;
}

#ifdef __cplusplus
}
#endif
