// generated from rosidl_typesupport_fastrtps_cpp/resource/idl__type_support.cpp.em
// with input from path_following_interfaces:msg\PositionsXY.idl
// generated code does not contain a copyright notice
#include "path_following_interfaces/msg/detail/positions_xy__rosidl_typesupport_fastrtps_cpp.hpp"
#include "path_following_interfaces/msg/detail/positions_xy__struct.hpp"

#include <limits>
#include <stdexcept>
#include <string>
#include "rosidl_typesupport_cpp/message_type_support.hpp"
#include "rosidl_typesupport_fastrtps_cpp/identifier.hpp"
#include "rosidl_typesupport_fastrtps_cpp/message_type_support.h"
#include "rosidl_typesupport_fastrtps_cpp/message_type_support_decl.hpp"
#include "rosidl_typesupport_fastrtps_cpp/wstring_conversion.hpp"
#include "fastcdr/Cdr.h"


// forward declaration of message dependencies and their conversion functions

namespace path_following_interfaces
{

namespace msg
{

namespace typesupport_fastrtps_cpp
{

bool
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_path_following_interfaces
cdr_serialize(
  const path_following_interfaces::msg::PositionsXY & ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  // Member: x
  {
    cdr << ros_message.x;
  }
  // Member: y
  {
    cdr << ros_message.y;
  }
  return true;
}

bool
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_path_following_interfaces
cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  path_following_interfaces::msg::PositionsXY & ros_message)
{
  // Member: x
  {
    cdr >> ros_message.x;
  }

  // Member: y
  {
    cdr >> ros_message.y;
  }

  return true;
}

size_t
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_path_following_interfaces
get_serialized_size(
  const path_following_interfaces::msg::PositionsXY & ros_message,
  size_t current_alignment)
{
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;

  // Member: x
  {
    size_t array_size = ros_message.x.size();

    current_alignment += padding +
      eprosima::fastcdr::Cdr::alignment(current_alignment, padding);
    size_t item_size = sizeof(ros_message.x[0]);
    current_alignment += array_size * item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: y
  {
    size_t array_size = ros_message.y.size();

    current_alignment += padding +
      eprosima::fastcdr::Cdr::alignment(current_alignment, padding);
    size_t item_size = sizeof(ros_message.y[0]);
    current_alignment += array_size * item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }

  return current_alignment - initial_alignment;
}

size_t
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_path_following_interfaces
max_serialized_size_PositionsXY(
  bool & full_bounded,
  size_t current_alignment)
{
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;
  (void)full_bounded;


  // Member: x
  {
    size_t array_size = 0;
    full_bounded = false;
    current_alignment += padding +
      eprosima::fastcdr::Cdr::alignment(current_alignment, padding);

    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }

  // Member: y
  {
    size_t array_size = 0;
    full_bounded = false;
    current_alignment += padding +
      eprosima::fastcdr::Cdr::alignment(current_alignment, padding);

    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }

  return current_alignment - initial_alignment;
}

static bool _PositionsXY__cdr_serialize(
  const void * untyped_ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  auto typed_message =
    static_cast<const path_following_interfaces::msg::PositionsXY *>(
    untyped_ros_message);
  return cdr_serialize(*typed_message, cdr);
}

static bool _PositionsXY__cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  void * untyped_ros_message)
{
  auto typed_message =
    static_cast<path_following_interfaces::msg::PositionsXY *>(
    untyped_ros_message);
  return cdr_deserialize(cdr, *typed_message);
}

static uint32_t _PositionsXY__get_serialized_size(
  const void * untyped_ros_message)
{
  auto typed_message =
    static_cast<const path_following_interfaces::msg::PositionsXY *>(
    untyped_ros_message);
  return static_cast<uint32_t>(get_serialized_size(*typed_message, 0));
}

static size_t _PositionsXY__max_serialized_size(bool & full_bounded)
{
  return max_serialized_size_PositionsXY(full_bounded, 0);
}

static message_type_support_callbacks_t _PositionsXY__callbacks = {
  "path_following_interfaces::msg",
  "PositionsXY",
  _PositionsXY__cdr_serialize,
  _PositionsXY__cdr_deserialize,
  _PositionsXY__get_serialized_size,
  _PositionsXY__max_serialized_size
};

static rosidl_message_type_support_t _PositionsXY__handle = {
  rosidl_typesupport_fastrtps_cpp::typesupport_identifier,
  &_PositionsXY__callbacks,
  get_message_typesupport_handle_function,
};

}  // namespace typesupport_fastrtps_cpp

}  // namespace msg

}  // namespace path_following_interfaces

namespace rosidl_typesupport_fastrtps_cpp
{

template<>
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_EXPORT_path_following_interfaces
const rosidl_message_type_support_t *
get_message_type_support_handle<path_following_interfaces::msg::PositionsXY>()
{
  return &path_following_interfaces::msg::typesupport_fastrtps_cpp::_PositionsXY__handle;
}

}  // namespace rosidl_typesupport_fastrtps_cpp

#ifdef __cplusplus
extern "C"
{
#endif

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_cpp, path_following_interfaces, msg, PositionsXY)() {
  return &path_following_interfaces::msg::typesupport_fastrtps_cpp::_PositionsXY__handle;
}

#ifdef __cplusplus
}
#endif
