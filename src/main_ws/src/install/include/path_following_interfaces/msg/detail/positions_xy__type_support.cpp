// generated from rosidl_typesupport_introspection_cpp/resource/idl__type_support.cpp.em
// with input from path_following_interfaces:msg\PositionsXY.idl
// generated code does not contain a copyright notice

#include "array"
#include "cstddef"
#include "string"
#include "vector"
#include "rosidl_runtime_c/message_type_support_struct.h"
#include "rosidl_typesupport_cpp/message_type_support.hpp"
#include "rosidl_typesupport_interface/macros.h"
#include "path_following_interfaces/msg/detail/positions_xy__struct.hpp"
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

void PositionsXY_init_function(
  void * message_memory, rosidl_runtime_cpp::MessageInitialization _init)
{
  new (message_memory) path_following_interfaces::msg::PositionsXY(_init);
}

void PositionsXY_fini_function(void * message_memory)
{
  auto typed_message = static_cast<path_following_interfaces::msg::PositionsXY *>(message_memory);
  typed_message->~PositionsXY();
}

size_t size_function__PositionsXY__x(const void * untyped_member)
{
  const auto * member = reinterpret_cast<const std::vector<float> *>(untyped_member);
  return member->size();
}

const void * get_const_function__PositionsXY__x(const void * untyped_member, size_t index)
{
  const auto & member =
    *reinterpret_cast<const std::vector<float> *>(untyped_member);
  return &member[index];
}

void * get_function__PositionsXY__x(void * untyped_member, size_t index)
{
  auto & member =
    *reinterpret_cast<std::vector<float> *>(untyped_member);
  return &member[index];
}

void resize_function__PositionsXY__x(void * untyped_member, size_t size)
{
  auto * member =
    reinterpret_cast<std::vector<float> *>(untyped_member);
  member->resize(size);
}

size_t size_function__PositionsXY__y(const void * untyped_member)
{
  const auto * member = reinterpret_cast<const std::vector<float> *>(untyped_member);
  return member->size();
}

const void * get_const_function__PositionsXY__y(const void * untyped_member, size_t index)
{
  const auto & member =
    *reinterpret_cast<const std::vector<float> *>(untyped_member);
  return &member[index];
}

void * get_function__PositionsXY__y(void * untyped_member, size_t index)
{
  auto & member =
    *reinterpret_cast<std::vector<float> *>(untyped_member);
  return &member[index];
}

void resize_function__PositionsXY__y(void * untyped_member, size_t size)
{
  auto * member =
    reinterpret_cast<std::vector<float> *>(untyped_member);
  member->resize(size);
}

static const ::rosidl_typesupport_introspection_cpp::MessageMember PositionsXY_message_member_array[2] = {
  {
    "x",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_FLOAT,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    true,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(path_following_interfaces::msg::PositionsXY, x),  // bytes offset in struct
    nullptr,  // default value
    size_function__PositionsXY__x,  // size() function pointer
    get_const_function__PositionsXY__x,  // get_const(index) function pointer
    get_function__PositionsXY__x,  // get(index) function pointer
    resize_function__PositionsXY__x  // resize(index) function pointer
  },
  {
    "y",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_FLOAT,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    true,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(path_following_interfaces::msg::PositionsXY, y),  // bytes offset in struct
    nullptr,  // default value
    size_function__PositionsXY__y,  // size() function pointer
    get_const_function__PositionsXY__y,  // get_const(index) function pointer
    get_function__PositionsXY__y,  // get(index) function pointer
    resize_function__PositionsXY__y  // resize(index) function pointer
  }
};

static const ::rosidl_typesupport_introspection_cpp::MessageMembers PositionsXY_message_members = {
  "path_following_interfaces::msg",  // message namespace
  "PositionsXY",  // message name
  2,  // number of fields
  sizeof(path_following_interfaces::msg::PositionsXY),
  PositionsXY_message_member_array,  // message members
  PositionsXY_init_function,  // function to initialize message memory (memory has to be allocated)
  PositionsXY_fini_function  // function to terminate message instance (will not free memory)
};

static const rosidl_message_type_support_t PositionsXY_message_type_support_handle = {
  ::rosidl_typesupport_introspection_cpp::typesupport_identifier,
  &PositionsXY_message_members,
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
get_message_type_support_handle<path_following_interfaces::msg::PositionsXY>()
{
  return &::path_following_interfaces::msg::rosidl_typesupport_introspection_cpp::PositionsXY_message_type_support_handle;
}

}  // namespace rosidl_typesupport_introspection_cpp

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_INTROSPECTION_CPP_PUBLIC
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_cpp, path_following_interfaces, msg, PositionsXY)() {
  return &::path_following_interfaces::msg::rosidl_typesupport_introspection_cpp::PositionsXY_message_type_support_handle;
}

#ifdef __cplusplus
}
#endif
