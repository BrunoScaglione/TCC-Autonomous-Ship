// generated from rosidl_typesupport_fastrtps_cpp/resource/idl__type_support.cpp.em
// with input from path_following_interfaces:srv\InitValues.idl
// generated code does not contain a copyright notice
#include "path_following_interfaces/srv/detail/init_values__rosidl_typesupport_fastrtps_cpp.hpp"
#include "path_following_interfaces/srv/detail/init_values__struct.hpp"

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
bool cdr_serialize(
  const path_following_interfaces::msg::State &,
  eprosima::fastcdr::Cdr &);
bool cdr_deserialize(
  eprosima::fastcdr::Cdr &,
  path_following_interfaces::msg::State &);
size_t get_serialized_size(
  const path_following_interfaces::msg::State &,
  size_t current_alignment);
size_t
max_serialized_size_State(
  bool & full_bounded,
  size_t current_alignment);
}  // namespace typesupport_fastrtps_cpp
}  // namespace msg
}  // namespace path_following_interfaces

namespace path_following_interfaces
{
namespace msg
{
namespace typesupport_fastrtps_cpp
{
bool cdr_serialize(
  const path_following_interfaces::msg::Waypoints &,
  eprosima::fastcdr::Cdr &);
bool cdr_deserialize(
  eprosima::fastcdr::Cdr &,
  path_following_interfaces::msg::Waypoints &);
size_t get_serialized_size(
  const path_following_interfaces::msg::Waypoints &,
  size_t current_alignment);
size_t
max_serialized_size_Waypoints(
  bool & full_bounded,
  size_t current_alignment);
}  // namespace typesupport_fastrtps_cpp
}  // namespace msg
}  // namespace path_following_interfaces


namespace path_following_interfaces
{

namespace srv
{

namespace typesupport_fastrtps_cpp
{

bool
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_path_following_interfaces
cdr_serialize(
  const path_following_interfaces::srv::InitValues_Request & ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  // Member: initial_state
  path_following_interfaces::msg::typesupport_fastrtps_cpp::cdr_serialize(
    ros_message.initial_state,
    cdr);
  // Member: waypoints
  path_following_interfaces::msg::typesupport_fastrtps_cpp::cdr_serialize(
    ros_message.waypoints,
    cdr);
  // Member: surge
  cdr << ros_message.surge;
  // Member: yaw
  cdr << ros_message.yaw;
  return true;
}

bool
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_path_following_interfaces
cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  path_following_interfaces::srv::InitValues_Request & ros_message)
{
  // Member: initial_state
  path_following_interfaces::msg::typesupport_fastrtps_cpp::cdr_deserialize(
    cdr, ros_message.initial_state);

  // Member: waypoints
  path_following_interfaces::msg::typesupport_fastrtps_cpp::cdr_deserialize(
    cdr, ros_message.waypoints);

  // Member: surge
  cdr >> ros_message.surge;

  // Member: yaw
  cdr >> ros_message.yaw;

  return true;
}

size_t
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_path_following_interfaces
get_serialized_size(
  const path_following_interfaces::srv::InitValues_Request & ros_message,
  size_t current_alignment)
{
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;

  // Member: initial_state

  current_alignment +=
    path_following_interfaces::msg::typesupport_fastrtps_cpp::get_serialized_size(
    ros_message.initial_state, current_alignment);
  // Member: waypoints

  current_alignment +=
    path_following_interfaces::msg::typesupport_fastrtps_cpp::get_serialized_size(
    ros_message.waypoints, current_alignment);
  // Member: surge
  {
    size_t item_size = sizeof(ros_message.surge);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: yaw
  {
    size_t item_size = sizeof(ros_message.yaw);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }

  return current_alignment - initial_alignment;
}

size_t
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_path_following_interfaces
max_serialized_size_InitValues_Request(
  bool & full_bounded,
  size_t current_alignment)
{
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;
  (void)full_bounded;


  // Member: initial_state
  {
    size_t array_size = 1;


    for (size_t index = 0; index < array_size; ++index) {
      current_alignment +=
        path_following_interfaces::msg::typesupport_fastrtps_cpp::max_serialized_size_State(
        full_bounded, current_alignment);
    }
  }

  // Member: waypoints
  {
    size_t array_size = 1;


    for (size_t index = 0; index < array_size; ++index) {
      current_alignment +=
        path_following_interfaces::msg::typesupport_fastrtps_cpp::max_serialized_size_Waypoints(
        full_bounded, current_alignment);
    }
  }

  // Member: surge
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }

  // Member: yaw
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }

  return current_alignment - initial_alignment;
}

static bool _InitValues_Request__cdr_serialize(
  const void * untyped_ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  auto typed_message =
    static_cast<const path_following_interfaces::srv::InitValues_Request *>(
    untyped_ros_message);
  return cdr_serialize(*typed_message, cdr);
}

static bool _InitValues_Request__cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  void * untyped_ros_message)
{
  auto typed_message =
    static_cast<path_following_interfaces::srv::InitValues_Request *>(
    untyped_ros_message);
  return cdr_deserialize(cdr, *typed_message);
}

static uint32_t _InitValues_Request__get_serialized_size(
  const void * untyped_ros_message)
{
  auto typed_message =
    static_cast<const path_following_interfaces::srv::InitValues_Request *>(
    untyped_ros_message);
  return static_cast<uint32_t>(get_serialized_size(*typed_message, 0));
}

static size_t _InitValues_Request__max_serialized_size(bool & full_bounded)
{
  return max_serialized_size_InitValues_Request(full_bounded, 0);
}

static message_type_support_callbacks_t _InitValues_Request__callbacks = {
  "path_following_interfaces::srv",
  "InitValues_Request",
  _InitValues_Request__cdr_serialize,
  _InitValues_Request__cdr_deserialize,
  _InitValues_Request__get_serialized_size,
  _InitValues_Request__max_serialized_size
};

static rosidl_message_type_support_t _InitValues_Request__handle = {
  rosidl_typesupport_fastrtps_cpp::typesupport_identifier,
  &_InitValues_Request__callbacks,
  get_message_typesupport_handle_function,
};

}  // namespace typesupport_fastrtps_cpp

}  // namespace srv

}  // namespace path_following_interfaces

namespace rosidl_typesupport_fastrtps_cpp
{

template<>
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_EXPORT_path_following_interfaces
const rosidl_message_type_support_t *
get_message_type_support_handle<path_following_interfaces::srv::InitValues_Request>()
{
  return &path_following_interfaces::srv::typesupport_fastrtps_cpp::_InitValues_Request__handle;
}

}  // namespace rosidl_typesupport_fastrtps_cpp

#ifdef __cplusplus
extern "C"
{
#endif

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_cpp, path_following_interfaces, srv, InitValues_Request)() {
  return &path_following_interfaces::srv::typesupport_fastrtps_cpp::_InitValues_Request__handle;
}

#ifdef __cplusplus
}
#endif

// already included above
// #include <limits>
// already included above
// #include <stdexcept>
// already included above
// #include <string>
// already included above
// #include "rosidl_typesupport_cpp/message_type_support.hpp"
// already included above
// #include "rosidl_typesupport_fastrtps_cpp/identifier.hpp"
// already included above
// #include "rosidl_typesupport_fastrtps_cpp/message_type_support.h"
// already included above
// #include "rosidl_typesupport_fastrtps_cpp/message_type_support_decl.hpp"
// already included above
// #include "rosidl_typesupport_fastrtps_cpp/wstring_conversion.hpp"
// already included above
// #include "fastcdr/Cdr.h"


// forward declaration of message dependencies and their conversion functions

namespace path_following_interfaces
{

namespace srv
{

namespace typesupport_fastrtps_cpp
{

bool
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_path_following_interfaces
cdr_serialize(
  const path_following_interfaces::srv::InitValues_Response & ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  // Member: surge
  cdr << ros_message.surge;
  // Member: yaw
  cdr << ros_message.yaw;
  return true;
}

bool
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_path_following_interfaces
cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  path_following_interfaces::srv::InitValues_Response & ros_message)
{
  // Member: surge
  cdr >> ros_message.surge;

  // Member: yaw
  cdr >> ros_message.yaw;

  return true;
}

size_t
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_path_following_interfaces
get_serialized_size(
  const path_following_interfaces::srv::InitValues_Response & ros_message,
  size_t current_alignment)
{
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;

  // Member: surge
  {
    size_t item_size = sizeof(ros_message.surge);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: yaw
  {
    size_t item_size = sizeof(ros_message.yaw);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }

  return current_alignment - initial_alignment;
}

size_t
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_path_following_interfaces
max_serialized_size_InitValues_Response(
  bool & full_bounded,
  size_t current_alignment)
{
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;
  (void)full_bounded;


  // Member: surge
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }

  // Member: yaw
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }

  return current_alignment - initial_alignment;
}

static bool _InitValues_Response__cdr_serialize(
  const void * untyped_ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  auto typed_message =
    static_cast<const path_following_interfaces::srv::InitValues_Response *>(
    untyped_ros_message);
  return cdr_serialize(*typed_message, cdr);
}

static bool _InitValues_Response__cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  void * untyped_ros_message)
{
  auto typed_message =
    static_cast<path_following_interfaces::srv::InitValues_Response *>(
    untyped_ros_message);
  return cdr_deserialize(cdr, *typed_message);
}

static uint32_t _InitValues_Response__get_serialized_size(
  const void * untyped_ros_message)
{
  auto typed_message =
    static_cast<const path_following_interfaces::srv::InitValues_Response *>(
    untyped_ros_message);
  return static_cast<uint32_t>(get_serialized_size(*typed_message, 0));
}

static size_t _InitValues_Response__max_serialized_size(bool & full_bounded)
{
  return max_serialized_size_InitValues_Response(full_bounded, 0);
}

static message_type_support_callbacks_t _InitValues_Response__callbacks = {
  "path_following_interfaces::srv",
  "InitValues_Response",
  _InitValues_Response__cdr_serialize,
  _InitValues_Response__cdr_deserialize,
  _InitValues_Response__get_serialized_size,
  _InitValues_Response__max_serialized_size
};

static rosidl_message_type_support_t _InitValues_Response__handle = {
  rosidl_typesupport_fastrtps_cpp::typesupport_identifier,
  &_InitValues_Response__callbacks,
  get_message_typesupport_handle_function,
};

}  // namespace typesupport_fastrtps_cpp

}  // namespace srv

}  // namespace path_following_interfaces

namespace rosidl_typesupport_fastrtps_cpp
{

template<>
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_EXPORT_path_following_interfaces
const rosidl_message_type_support_t *
get_message_type_support_handle<path_following_interfaces::srv::InitValues_Response>()
{
  return &path_following_interfaces::srv::typesupport_fastrtps_cpp::_InitValues_Response__handle;
}

}  // namespace rosidl_typesupport_fastrtps_cpp

#ifdef __cplusplus
extern "C"
{
#endif

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_cpp, path_following_interfaces, srv, InitValues_Response)() {
  return &path_following_interfaces::srv::typesupport_fastrtps_cpp::_InitValues_Response__handle;
}

#ifdef __cplusplus
}
#endif

#include "rmw/error_handling.h"
// already included above
// #include "rosidl_typesupport_fastrtps_cpp/identifier.hpp"
#include "rosidl_typesupport_fastrtps_cpp/service_type_support.h"
#include "rosidl_typesupport_fastrtps_cpp/service_type_support_decl.hpp"

namespace path_following_interfaces
{

namespace srv
{

namespace typesupport_fastrtps_cpp
{

static service_type_support_callbacks_t _InitValues__callbacks = {
  "path_following_interfaces::srv",
  "InitValues",
  ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_cpp, path_following_interfaces, srv, InitValues_Request)(),
  ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_cpp, path_following_interfaces, srv, InitValues_Response)(),
};

static rosidl_service_type_support_t _InitValues__handle = {
  rosidl_typesupport_fastrtps_cpp::typesupport_identifier,
  &_InitValues__callbacks,
  get_service_typesupport_handle_function,
};

}  // namespace typesupport_fastrtps_cpp

}  // namespace srv

}  // namespace path_following_interfaces

namespace rosidl_typesupport_fastrtps_cpp
{

template<>
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_EXPORT_path_following_interfaces
const rosidl_service_type_support_t *
get_service_type_support_handle<path_following_interfaces::srv::InitValues>()
{
  return &path_following_interfaces::srv::typesupport_fastrtps_cpp::_InitValues__handle;
}

}  // namespace rosidl_typesupport_fastrtps_cpp

#ifdef __cplusplus
extern "C"
{
#endif

const rosidl_service_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__SERVICE_SYMBOL_NAME(rosidl_typesupport_fastrtps_cpp, path_following_interfaces, srv, InitValues)() {
  return &path_following_interfaces::srv::typesupport_fastrtps_cpp::_InitValues__handle;
}

#ifdef __cplusplus
}
#endif
