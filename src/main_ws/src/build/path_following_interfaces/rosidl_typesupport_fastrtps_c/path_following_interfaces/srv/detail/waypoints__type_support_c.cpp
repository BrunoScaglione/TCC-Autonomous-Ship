// generated from rosidl_typesupport_fastrtps_c/resource/idl__type_support_c.cpp.em
// with input from path_following_interfaces:srv\Waypoints.idl
// generated code does not contain a copyright notice
#include "path_following_interfaces/srv/detail/waypoints__rosidl_typesupport_fastrtps_c.h"


#include <cassert>
#include <limits>
#include <string>
#include "rosidl_typesupport_fastrtps_c/identifier.h"
#include "rosidl_typesupport_fastrtps_c/wstring_conversion.hpp"
#include "rosidl_typesupport_fastrtps_cpp/message_type_support.h"
#include "path_following_interfaces/msg/rosidl_typesupport_fastrtps_c__visibility_control.h"
#include "path_following_interfaces/srv/detail/waypoints__struct.h"
#include "path_following_interfaces/srv/detail/waypoints__functions.h"
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

#include "path_following_interfaces/msg/detail/positions_xy__functions.h"  // position
#include "rosidl_runtime_c/primitives_sequence.h"  // velocity
#include "rosidl_runtime_c/primitives_sequence_functions.h"  // velocity

// forward declare type support functions
size_t get_serialized_size_path_following_interfaces__msg__PositionsXY(
  const void * untyped_ros_message,
  size_t current_alignment);

size_t max_serialized_size_path_following_interfaces__msg__PositionsXY(
  bool & full_bounded,
  size_t current_alignment);

const rosidl_message_type_support_t *
  ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, path_following_interfaces, msg, PositionsXY)();


using _Waypoints_Request__ros_msg_type = path_following_interfaces__srv__Waypoints_Request;

static bool _Waypoints_Request__cdr_serialize(
  const void * untyped_ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  const _Waypoints_Request__ros_msg_type * ros_message = static_cast<const _Waypoints_Request__ros_msg_type *>(untyped_ros_message);
  // Field name: position
  {
    const message_type_support_callbacks_t * callbacks =
      static_cast<const message_type_support_callbacks_t *>(
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(
        rosidl_typesupport_fastrtps_c, path_following_interfaces, msg, PositionsXY
      )()->data);
    if (!callbacks->cdr_serialize(
        &ros_message->position, cdr))
    {
      return false;
    }
  }

  // Field name: velocity
  {
    size_t size = ros_message->velocity.size;
    auto array_ptr = ros_message->velocity.data;
    cdr << static_cast<uint32_t>(size);
    cdr.serializeArray(array_ptr, size);
  }

  return true;
}

static bool _Waypoints_Request__cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  void * untyped_ros_message)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  _Waypoints_Request__ros_msg_type * ros_message = static_cast<_Waypoints_Request__ros_msg_type *>(untyped_ros_message);
  // Field name: position
  {
    const message_type_support_callbacks_t * callbacks =
      static_cast<const message_type_support_callbacks_t *>(
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(
        rosidl_typesupport_fastrtps_c, path_following_interfaces, msg, PositionsXY
      )()->data);
    if (!callbacks->cdr_deserialize(
        cdr, &ros_message->position))
    {
      return false;
    }
  }

  // Field name: velocity
  {
    uint32_t cdrSize;
    cdr >> cdrSize;
    size_t size = static_cast<size_t>(cdrSize);
    if (ros_message->velocity.data) {
      rosidl_runtime_c__float__Sequence__fini(&ros_message->velocity);
    }
    if (!rosidl_runtime_c__float__Sequence__init(&ros_message->velocity, size)) {
      fprintf(stderr, "failed to create array for field 'velocity'");
      return false;
    }
    auto array_ptr = ros_message->velocity.data;
    cdr.deserializeArray(array_ptr, size);
  }

  return true;
}  // NOLINT(readability/fn_size)

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_path_following_interfaces
size_t get_serialized_size_path_following_interfaces__srv__Waypoints_Request(
  const void * untyped_ros_message,
  size_t current_alignment)
{
  const _Waypoints_Request__ros_msg_type * ros_message = static_cast<const _Waypoints_Request__ros_msg_type *>(untyped_ros_message);
  (void)ros_message;
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;

  // field.name position

  current_alignment += get_serialized_size_path_following_interfaces__msg__PositionsXY(
    &(ros_message->position), current_alignment);
  // field.name velocity
  {
    size_t array_size = ros_message->velocity.size;
    auto array_ptr = ros_message->velocity.data;
    current_alignment += padding +
      eprosima::fastcdr::Cdr::alignment(current_alignment, padding);
    (void)array_ptr;
    size_t item_size = sizeof(array_ptr[0]);
    current_alignment += array_size * item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }

  return current_alignment - initial_alignment;
}

static uint32_t _Waypoints_Request__get_serialized_size(const void * untyped_ros_message)
{
  return static_cast<uint32_t>(
    get_serialized_size_path_following_interfaces__srv__Waypoints_Request(
      untyped_ros_message, 0));
}

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_path_following_interfaces
size_t max_serialized_size_path_following_interfaces__srv__Waypoints_Request(
  bool & full_bounded,
  size_t current_alignment)
{
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;
  (void)full_bounded;

  // member: position
  {
    size_t array_size = 1;


    for (size_t index = 0; index < array_size; ++index) {
      current_alignment +=
        max_serialized_size_path_following_interfaces__msg__PositionsXY(
        full_bounded, current_alignment);
    }
  }
  // member: velocity
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

static size_t _Waypoints_Request__max_serialized_size(bool & full_bounded)
{
  return max_serialized_size_path_following_interfaces__srv__Waypoints_Request(
    full_bounded, 0);
}


static message_type_support_callbacks_t __callbacks_Waypoints_Request = {
  "path_following_interfaces::srv",
  "Waypoints_Request",
  _Waypoints_Request__cdr_serialize,
  _Waypoints_Request__cdr_deserialize,
  _Waypoints_Request__get_serialized_size,
  _Waypoints_Request__max_serialized_size
};

static rosidl_message_type_support_t _Waypoints_Request__type_support = {
  rosidl_typesupport_fastrtps_c__identifier,
  &__callbacks_Waypoints_Request,
  get_message_typesupport_handle_function,
};

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, path_following_interfaces, srv, Waypoints_Request)() {
  return &_Waypoints_Request__type_support;
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
// #include "path_following_interfaces/srv/detail/waypoints__struct.h"
// already included above
// #include "path_following_interfaces/srv/detail/waypoints__functions.h"
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

#include "rosidl_runtime_c/string.h"  // reporting
#include "rosidl_runtime_c/string_functions.h"  // reporting

// forward declare type support functions


using _Waypoints_Response__ros_msg_type = path_following_interfaces__srv__Waypoints_Response;

static bool _Waypoints_Response__cdr_serialize(
  const void * untyped_ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  const _Waypoints_Response__ros_msg_type * ros_message = static_cast<const _Waypoints_Response__ros_msg_type *>(untyped_ros_message);
  // Field name: reporting
  {
    const rosidl_runtime_c__String * str = &ros_message->reporting;
    if (str->capacity == 0 || str->capacity <= str->size) {
      fprintf(stderr, "string capacity not greater than size\n");
      return false;
    }
    if (str->data[str->size] != '\0') {
      fprintf(stderr, "string not null-terminated\n");
      return false;
    }
    cdr << str->data;
  }

  return true;
}

static bool _Waypoints_Response__cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  void * untyped_ros_message)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  _Waypoints_Response__ros_msg_type * ros_message = static_cast<_Waypoints_Response__ros_msg_type *>(untyped_ros_message);
  // Field name: reporting
  {
    std::string tmp;
    cdr >> tmp;
    if (!ros_message->reporting.data) {
      rosidl_runtime_c__String__init(&ros_message->reporting);
    }
    bool succeeded = rosidl_runtime_c__String__assign(
      &ros_message->reporting,
      tmp.c_str());
    if (!succeeded) {
      fprintf(stderr, "failed to assign string into field 'reporting'\n");
      return false;
    }
  }

  return true;
}  // NOLINT(readability/fn_size)

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_path_following_interfaces
size_t get_serialized_size_path_following_interfaces__srv__Waypoints_Response(
  const void * untyped_ros_message,
  size_t current_alignment)
{
  const _Waypoints_Response__ros_msg_type * ros_message = static_cast<const _Waypoints_Response__ros_msg_type *>(untyped_ros_message);
  (void)ros_message;
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;

  // field.name reporting
  current_alignment += padding +
    eprosima::fastcdr::Cdr::alignment(current_alignment, padding) +
    (ros_message->reporting.size + 1);

  return current_alignment - initial_alignment;
}

static uint32_t _Waypoints_Response__get_serialized_size(const void * untyped_ros_message)
{
  return static_cast<uint32_t>(
    get_serialized_size_path_following_interfaces__srv__Waypoints_Response(
      untyped_ros_message, 0));
}

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_path_following_interfaces
size_t max_serialized_size_path_following_interfaces__srv__Waypoints_Response(
  bool & full_bounded,
  size_t current_alignment)
{
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;
  (void)full_bounded;

  // member: reporting
  {
    size_t array_size = 1;

    full_bounded = false;
    for (size_t index = 0; index < array_size; ++index) {
      current_alignment += padding +
        eprosima::fastcdr::Cdr::alignment(current_alignment, padding) +
        1;
    }
  }

  return current_alignment - initial_alignment;
}

static size_t _Waypoints_Response__max_serialized_size(bool & full_bounded)
{
  return max_serialized_size_path_following_interfaces__srv__Waypoints_Response(
    full_bounded, 0);
}


static message_type_support_callbacks_t __callbacks_Waypoints_Response = {
  "path_following_interfaces::srv",
  "Waypoints_Response",
  _Waypoints_Response__cdr_serialize,
  _Waypoints_Response__cdr_deserialize,
  _Waypoints_Response__get_serialized_size,
  _Waypoints_Response__max_serialized_size
};

static rosidl_message_type_support_t _Waypoints_Response__type_support = {
  rosidl_typesupport_fastrtps_c__identifier,
  &__callbacks_Waypoints_Response,
  get_message_typesupport_handle_function,
};

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, path_following_interfaces, srv, Waypoints_Response)() {
  return &_Waypoints_Response__type_support;
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
#include "path_following_interfaces/srv/waypoints.h"

#if defined(__cplusplus)
extern "C"
{
#endif

static service_type_support_callbacks_t Waypoints__callbacks = {
  "path_following_interfaces::srv",
  "Waypoints",
  ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, path_following_interfaces, srv, Waypoints_Request)(),
  ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, path_following_interfaces, srv, Waypoints_Response)(),
};

static rosidl_service_type_support_t Waypoints__handle = {
  rosidl_typesupport_fastrtps_c__identifier,
  &Waypoints__callbacks,
  get_service_typesupport_handle_function,
};

const rosidl_service_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__SERVICE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, path_following_interfaces, srv, Waypoints)() {
  return &Waypoints__handle;
}

#if defined(__cplusplus)
}
#endif
