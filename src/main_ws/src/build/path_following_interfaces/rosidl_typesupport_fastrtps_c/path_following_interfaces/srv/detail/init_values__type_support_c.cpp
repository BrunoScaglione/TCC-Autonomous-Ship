// generated from rosidl_typesupport_fastrtps_c/resource/idl__type_support_c.cpp.em
// with input from path_following_interfaces:srv\InitValues.idl
// generated code does not contain a copyright notice
#include "path_following_interfaces/srv/detail/init_values__rosidl_typesupport_fastrtps_c.h"


#include <cassert>
#include <limits>
#include <string>
#include "rosidl_typesupport_fastrtps_c/identifier.h"
#include "rosidl_typesupport_fastrtps_c/wstring_conversion.hpp"
#include "rosidl_typesupport_fastrtps_cpp/message_type_support.h"
#include "path_following_interfaces/msg/rosidl_typesupport_fastrtps_c__visibility_control.h"
#include "path_following_interfaces/srv/detail/init_values__struct.h"
#include "path_following_interfaces/srv/detail/init_values__functions.h"
#include "fastcdr/Cdr.h"

#ifndef _WIN32
# pragma GCC diagnostic push
# pragma GCC diagnostic ignored "-Wunused-parameter"
# ifdef __clang__
#  pragma clang diagnostic ignored "-Wdeprecated-register"
#  pragma clang diagnostic ignored "-Wreturn-type-c-linkage"
# endif
#endif
#ifndef _WIN32
# pragma GCC diagnostic pop
#endif

// includes and forward declarations of message dependencies and their conversion functions

#if defined(__cplusplus)
extern "C"
{
#endif

#include "path_following_interfaces/msg/detail/state__functions.h"  // initial_state
#include "path_following_interfaces/msg/detail/waypoints__functions.h"  // waypoints

// forward declare type support functions
size_t get_serialized_size_path_following_interfaces__msg__State(
  const void * untyped_ros_message,
  size_t current_alignment);

size_t max_serialized_size_path_following_interfaces__msg__State(
  bool & full_bounded,
  size_t current_alignment);

const rosidl_message_type_support_t *
  ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, path_following_interfaces, msg, State)();
size_t get_serialized_size_path_following_interfaces__msg__Waypoints(
  const void * untyped_ros_message,
  size_t current_alignment);

size_t max_serialized_size_path_following_interfaces__msg__Waypoints(
  bool & full_bounded,
  size_t current_alignment);

const rosidl_message_type_support_t *
  ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, path_following_interfaces, msg, Waypoints)();


using _InitValues_Request__ros_msg_type = path_following_interfaces__srv__InitValues_Request;

static bool _InitValues_Request__cdr_serialize(
  const void * untyped_ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  const _InitValues_Request__ros_msg_type * ros_message = static_cast<const _InitValues_Request__ros_msg_type *>(untyped_ros_message);
  // Field name: initial_state
  {
    const message_type_support_callbacks_t * callbacks =
      static_cast<const message_type_support_callbacks_t *>(
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(
        rosidl_typesupport_fastrtps_c, path_following_interfaces, msg, State
      )()->data);
    if (!callbacks->cdr_serialize(
        &ros_message->initial_state, cdr))
    {
      return false;
    }
  }

  // Field name: waypoints
  {
    const message_type_support_callbacks_t * callbacks =
      static_cast<const message_type_support_callbacks_t *>(
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(
        rosidl_typesupport_fastrtps_c, path_following_interfaces, msg, Waypoints
      )()->data);
    if (!callbacks->cdr_serialize(
        &ros_message->waypoints, cdr))
    {
      return false;
    }
  }

  // Field name: surge
  {
    cdr << ros_message->surge;
  }

  // Field name: yaw
  {
    cdr << ros_message->yaw;
  }

  return true;
}

static bool _InitValues_Request__cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  void * untyped_ros_message)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  _InitValues_Request__ros_msg_type * ros_message = static_cast<_InitValues_Request__ros_msg_type *>(untyped_ros_message);
  // Field name: initial_state
  {
    const message_type_support_callbacks_t * callbacks =
      static_cast<const message_type_support_callbacks_t *>(
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(
        rosidl_typesupport_fastrtps_c, path_following_interfaces, msg, State
      )()->data);
    if (!callbacks->cdr_deserialize(
        cdr, &ros_message->initial_state))
    {
      return false;
    }
  }

  // Field name: waypoints
  {
    const message_type_support_callbacks_t * callbacks =
      static_cast<const message_type_support_callbacks_t *>(
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(
        rosidl_typesupport_fastrtps_c, path_following_interfaces, msg, Waypoints
      )()->data);
    if (!callbacks->cdr_deserialize(
        cdr, &ros_message->waypoints))
    {
      return false;
    }
  }

  // Field name: surge
  {
    cdr >> ros_message->surge;
  }

  // Field name: yaw
  {
    cdr >> ros_message->yaw;
  }

  return true;
}  // NOLINT(readability/fn_size)

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_path_following_interfaces
size_t get_serialized_size_path_following_interfaces__srv__InitValues_Request(
  const void * untyped_ros_message,
  size_t current_alignment)
{
  const _InitValues_Request__ros_msg_type * ros_message = static_cast<const _InitValues_Request__ros_msg_type *>(untyped_ros_message);
  (void)ros_message;
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;

  // field.name initial_state

  current_alignment += get_serialized_size_path_following_interfaces__msg__State(
    &(ros_message->initial_state), current_alignment);
  // field.name waypoints

  current_alignment += get_serialized_size_path_following_interfaces__msg__Waypoints(
    &(ros_message->waypoints), current_alignment);
  // field.name surge
  {
    size_t item_size = sizeof(ros_message->surge);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name yaw
  {
    size_t item_size = sizeof(ros_message->yaw);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }

  return current_alignment - initial_alignment;
}

static uint32_t _InitValues_Request__get_serialized_size(const void * untyped_ros_message)
{
  return static_cast<uint32_t>(
    get_serialized_size_path_following_interfaces__srv__InitValues_Request(
      untyped_ros_message, 0));
}

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_path_following_interfaces
size_t max_serialized_size_path_following_interfaces__srv__InitValues_Request(
  bool & full_bounded,
  size_t current_alignment)
{
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;
  (void)full_bounded;

  // member: initial_state
  {
    size_t array_size = 1;


    for (size_t index = 0; index < array_size; ++index) {
      current_alignment +=
        max_serialized_size_path_following_interfaces__msg__State(
        full_bounded, current_alignment);
    }
  }
  // member: waypoints
  {
    size_t array_size = 1;


    for (size_t index = 0; index < array_size; ++index) {
      current_alignment +=
        max_serialized_size_path_following_interfaces__msg__Waypoints(
        full_bounded, current_alignment);
    }
  }
  // member: surge
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }
  // member: yaw
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }

  return current_alignment - initial_alignment;
}

static size_t _InitValues_Request__max_serialized_size(bool & full_bounded)
{
  return max_serialized_size_path_following_interfaces__srv__InitValues_Request(
    full_bounded, 0);
}


static message_type_support_callbacks_t __callbacks_InitValues_Request = {
  "path_following_interfaces::srv",
  "InitValues_Request",
  _InitValues_Request__cdr_serialize,
  _InitValues_Request__cdr_deserialize,
  _InitValues_Request__get_serialized_size,
  _InitValues_Request__max_serialized_size
};

static rosidl_message_type_support_t _InitValues_Request__type_support = {
  rosidl_typesupport_fastrtps_c__identifier,
  &__callbacks_InitValues_Request,
  get_message_typesupport_handle_function,
};

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, path_following_interfaces, srv, InitValues_Request)() {
  return &_InitValues_Request__type_support;
}

#if defined(__cplusplus)
}
#endif

// already included above
// #include <cassert>
// already included above
// #include <limits>
// already included above
// #include <string>
// already included above
// #include "rosidl_typesupport_fastrtps_c/identifier.h"
// already included above
// #include "rosidl_typesupport_fastrtps_c/wstring_conversion.hpp"
// already included above
// #include "rosidl_typesupport_fastrtps_cpp/message_type_support.h"
// already included above
// #include "path_following_interfaces/msg/rosidl_typesupport_fastrtps_c__visibility_control.h"
// already included above
// #include "path_following_interfaces/srv/detail/init_values__struct.h"
// already included above
// #include "path_following_interfaces/srv/detail/init_values__functions.h"
// already included above
// #include "fastcdr/Cdr.h"

#ifndef _WIN32
# pragma GCC diagnostic push
# pragma GCC diagnostic ignored "-Wunused-parameter"
# ifdef __clang__
#  pragma clang diagnostic ignored "-Wdeprecated-register"
#  pragma clang diagnostic ignored "-Wreturn-type-c-linkage"
# endif
#endif
#ifndef _WIN32
# pragma GCC diagnostic pop
#endif

// includes and forward declarations of message dependencies and their conversion functions

#if defined(__cplusplus)
extern "C"
{
#endif


// forward declare type support functions


using _InitValues_Response__ros_msg_type = path_following_interfaces__srv__InitValues_Response;

static bool _InitValues_Response__cdr_serialize(
  const void * untyped_ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  const _InitValues_Response__ros_msg_type * ros_message = static_cast<const _InitValues_Response__ros_msg_type *>(untyped_ros_message);
  // Field name: surge
  {
    cdr << ros_message->surge;
  }

  // Field name: yaw
  {
    cdr << ros_message->yaw;
  }

  return true;
}

static bool _InitValues_Response__cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  void * untyped_ros_message)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  _InitValues_Response__ros_msg_type * ros_message = static_cast<_InitValues_Response__ros_msg_type *>(untyped_ros_message);
  // Field name: surge
  {
    cdr >> ros_message->surge;
  }

  // Field name: yaw
  {
    cdr >> ros_message->yaw;
  }

  return true;
}  // NOLINT(readability/fn_size)

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_path_following_interfaces
size_t get_serialized_size_path_following_interfaces__srv__InitValues_Response(
  const void * untyped_ros_message,
  size_t current_alignment)
{
  const _InitValues_Response__ros_msg_type * ros_message = static_cast<const _InitValues_Response__ros_msg_type *>(untyped_ros_message);
  (void)ros_message;
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;

  // field.name surge
  {
    size_t item_size = sizeof(ros_message->surge);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name yaw
  {
    size_t item_size = sizeof(ros_message->yaw);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }

  return current_alignment - initial_alignment;
}

static uint32_t _InitValues_Response__get_serialized_size(const void * untyped_ros_message)
{
  return static_cast<uint32_t>(
    get_serialized_size_path_following_interfaces__srv__InitValues_Response(
      untyped_ros_message, 0));
}

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_path_following_interfaces
size_t max_serialized_size_path_following_interfaces__srv__InitValues_Response(
  bool & full_bounded,
  size_t current_alignment)
{
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;
  (void)full_bounded;

  // member: surge
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }
  // member: yaw
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }

  return current_alignment - initial_alignment;
}

static size_t _InitValues_Response__max_serialized_size(bool & full_bounded)
{
  return max_serialized_size_path_following_interfaces__srv__InitValues_Response(
    full_bounded, 0);
}


static message_type_support_callbacks_t __callbacks_InitValues_Response = {
  "path_following_interfaces::srv",
  "InitValues_Response",
  _InitValues_Response__cdr_serialize,
  _InitValues_Response__cdr_deserialize,
  _InitValues_Response__get_serialized_size,
  _InitValues_Response__max_serialized_size
};

static rosidl_message_type_support_t _InitValues_Response__type_support = {
  rosidl_typesupport_fastrtps_c__identifier,
  &__callbacks_InitValues_Response,
  get_message_typesupport_handle_function,
};

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, path_following_interfaces, srv, InitValues_Response)() {
  return &_InitValues_Response__type_support;
}

#if defined(__cplusplus)
}
#endif

#include "rosidl_typesupport_fastrtps_cpp/service_type_support.h"
#include "rosidl_typesupport_cpp/service_type_support.hpp"
// already included above
// #include "rosidl_typesupport_fastrtps_c/identifier.h"
// already included above
// #include "path_following_interfaces/msg/rosidl_typesupport_fastrtps_c__visibility_control.h"
#include "path_following_interfaces/srv/init_values.h"

#if defined(__cplusplus)
extern "C"
{
#endif

static service_type_support_callbacks_t InitValues__callbacks = {
  "path_following_interfaces::srv",
  "InitValues",
  ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, path_following_interfaces, srv, InitValues_Request)(),
  ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, path_following_interfaces, srv, InitValues_Response)(),
};

static rosidl_service_type_support_t InitValues__handle = {
  rosidl_typesupport_fastrtps_c__identifier,
  &InitValues__callbacks,
  get_service_typesupport_handle_function,
};

const rosidl_service_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__SERVICE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, path_following_interfaces, srv, InitValues)() {
  return &InitValues__handle;
}

#if defined(__cplusplus)
}
#endif
