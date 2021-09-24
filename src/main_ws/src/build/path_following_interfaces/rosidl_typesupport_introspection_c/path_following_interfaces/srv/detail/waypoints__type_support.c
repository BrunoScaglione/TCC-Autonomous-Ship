// generated from rosidl_typesupport_introspection_c/resource/idl__type_support.c.em
// with input from path_following_interfaces:srv\Waypoints.idl
// generated code does not contain a copyright notice

#include <stddef.h>
#include "path_following_interfaces/srv/detail/waypoints__rosidl_typesupport_introspection_c.h"
#include "path_following_interfaces/msg/rosidl_typesupport_introspection_c__visibility_control.h"
#include "rosidl_typesupport_introspection_c/field_types.h"
#include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/message_introspection.h"
#include "path_following_interfaces/srv/detail/waypoints__functions.h"
#include "path_following_interfaces/srv/detail/waypoints__struct.h"


// Include directives for member types
// Member `position`
#include "path_following_interfaces/msg/positions_xy.h"
// Member `position`
#include "path_following_interfaces/msg/detail/positions_xy__rosidl_typesupport_introspection_c.h"
// Member `velocity`
#include "rosidl_runtime_c/primitives_sequence_functions.h"

#ifdef __cplusplus
extern "C"
{
#endif

void Waypoints_Request__rosidl_typesupport_introspection_c__Waypoints_Request_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  path_following_interfaces__srv__Waypoints_Request__init(message_memory);
}

void Waypoints_Request__rosidl_typesupport_introspection_c__Waypoints_Request_fini_function(void * message_memory)
{
  path_following_interfaces__srv__Waypoints_Request__fini(message_memory);
}

static rosidl_typesupport_introspection_c__MessageMember Waypoints_Request__rosidl_typesupport_introspection_c__Waypoints_Request_message_member_array[2] = {
  {
    "position",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message (initialized later)
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(path_following_interfaces__srv__Waypoints_Request, position),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "velocity",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_FLOAT,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    true,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(path_following_interfaces__srv__Waypoints_Request, velocity),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers Waypoints_Request__rosidl_typesupport_introspection_c__Waypoints_Request_message_members = {
  "path_following_interfaces__srv",  // message namespace
  "Waypoints_Request",  // message name
  2,  // number of fields
  sizeof(path_following_interfaces__srv__Waypoints_Request),
  Waypoints_Request__rosidl_typesupport_introspection_c__Waypoints_Request_message_member_array,  // message members
  Waypoints_Request__rosidl_typesupport_introspection_c__Waypoints_Request_init_function,  // function to initialize message memory (memory has to be allocated)
  Waypoints_Request__rosidl_typesupport_introspection_c__Waypoints_Request_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t Waypoints_Request__rosidl_typesupport_introspection_c__Waypoints_Request_message_type_support_handle = {
  0,
  &Waypoints_Request__rosidl_typesupport_introspection_c__Waypoints_Request_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_path_following_interfaces
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, path_following_interfaces, srv, Waypoints_Request)() {
  Waypoints_Request__rosidl_typesupport_introspection_c__Waypoints_Request_message_member_array[0].members_ =
    ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, path_following_interfaces, msg, PositionsXY)();
  if (!Waypoints_Request__rosidl_typesupport_introspection_c__Waypoints_Request_message_type_support_handle.typesupport_identifier) {
    Waypoints_Request__rosidl_typesupport_introspection_c__Waypoints_Request_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &Waypoints_Request__rosidl_typesupport_introspection_c__Waypoints_Request_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif

// already included above
// #include <stddef.h>
// already included above
// #include "path_following_interfaces/srv/detail/waypoints__rosidl_typesupport_introspection_c.h"
// already included above
// #include "path_following_interfaces/msg/rosidl_typesupport_introspection_c__visibility_control.h"
// already included above
// #include "rosidl_typesupport_introspection_c/field_types.h"
// already included above
// #include "rosidl_typesupport_introspection_c/identifier.h"
// already included above
// #include "rosidl_typesupport_introspection_c/message_introspection.h"
// already included above
// #include "path_following_interfaces/srv/detail/waypoints__functions.h"
// already included above
// #include "path_following_interfaces/srv/detail/waypoints__struct.h"


// Include directives for member types
// Member `reporting`
#include "rosidl_runtime_c/string_functions.h"

#ifdef __cplusplus
extern "C"
{
#endif

void Waypoints_Response__rosidl_typesupport_introspection_c__Waypoints_Response_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  path_following_interfaces__srv__Waypoints_Response__init(message_memory);
}

void Waypoints_Response__rosidl_typesupport_introspection_c__Waypoints_Response_fini_function(void * message_memory)
{
  path_following_interfaces__srv__Waypoints_Response__fini(message_memory);
}

static rosidl_typesupport_introspection_c__MessageMember Waypoints_Response__rosidl_typesupport_introspection_c__Waypoints_Response_message_member_array[1] = {
  {
    "reporting",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_STRING,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(path_following_interfaces__srv__Waypoints_Response, reporting),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers Waypoints_Response__rosidl_typesupport_introspection_c__Waypoints_Response_message_members = {
  "path_following_interfaces__srv",  // message namespace
  "Waypoints_Response",  // message name
  1,  // number of fields
  sizeof(path_following_interfaces__srv__Waypoints_Response),
  Waypoints_Response__rosidl_typesupport_introspection_c__Waypoints_Response_message_member_array,  // message members
  Waypoints_Response__rosidl_typesupport_introspection_c__Waypoints_Response_init_function,  // function to initialize message memory (memory has to be allocated)
  Waypoints_Response__rosidl_typesupport_introspection_c__Waypoints_Response_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t Waypoints_Response__rosidl_typesupport_introspection_c__Waypoints_Response_message_type_support_handle = {
  0,
  &Waypoints_Response__rosidl_typesupport_introspection_c__Waypoints_Response_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_path_following_interfaces
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, path_following_interfaces, srv, Waypoints_Response)() {
  if (!Waypoints_Response__rosidl_typesupport_introspection_c__Waypoints_Response_message_type_support_handle.typesupport_identifier) {
    Waypoints_Response__rosidl_typesupport_introspection_c__Waypoints_Response_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &Waypoints_Response__rosidl_typesupport_introspection_c__Waypoints_Response_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif

#include "rosidl_runtime_c/service_type_support_struct.h"
// already included above
// #include "path_following_interfaces/msg/rosidl_typesupport_introspection_c__visibility_control.h"
// already included above
// #include "path_following_interfaces/srv/detail/waypoints__rosidl_typesupport_introspection_c.h"
// already included above
// #include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/service_introspection.h"

// this is intentionally not const to allow initialization later to prevent an initialization race
static rosidl_typesupport_introspection_c__ServiceMembers path_following_interfaces__srv__detail__waypoints__rosidl_typesupport_introspection_c__Waypoints_service_members = {
  "path_following_interfaces__srv",  // service namespace
  "Waypoints",  // service name
  // these two fields are initialized below on the first access
  NULL,  // request message
  // path_following_interfaces__srv__detail__waypoints__rosidl_typesupport_introspection_c__Waypoints_Request_message_type_support_handle,
  NULL  // response message
  // path_following_interfaces__srv__detail__waypoints__rosidl_typesupport_introspection_c__Waypoints_Response_message_type_support_handle
};

static rosidl_service_type_support_t path_following_interfaces__srv__detail__waypoints__rosidl_typesupport_introspection_c__Waypoints_service_type_support_handle = {
  0,
  &path_following_interfaces__srv__detail__waypoints__rosidl_typesupport_introspection_c__Waypoints_service_members,
  get_service_typesupport_handle_function,
};

// Forward declaration of request/response type support functions
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, path_following_interfaces, srv, Waypoints_Request)();

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, path_following_interfaces, srv, Waypoints_Response)();

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_path_following_interfaces
const rosidl_service_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__SERVICE_SYMBOL_NAME(rosidl_typesupport_introspection_c, path_following_interfaces, srv, Waypoints)() {
  if (!path_following_interfaces__srv__detail__waypoints__rosidl_typesupport_introspection_c__Waypoints_service_type_support_handle.typesupport_identifier) {
    path_following_interfaces__srv__detail__waypoints__rosidl_typesupport_introspection_c__Waypoints_service_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  rosidl_typesupport_introspection_c__ServiceMembers * service_members =
    (rosidl_typesupport_introspection_c__ServiceMembers *)path_following_interfaces__srv__detail__waypoints__rosidl_typesupport_introspection_c__Waypoints_service_type_support_handle.data;

  if (!service_members->request_members_) {
    service_members->request_members_ =
      (const rosidl_typesupport_introspection_c__MessageMembers *)
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, path_following_interfaces, srv, Waypoints_Request)()->data;
  }
  if (!service_members->response_members_) {
    service_members->response_members_ =
      (const rosidl_typesupport_introspection_c__MessageMembers *)
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, path_following_interfaces, srv, Waypoints_Response)()->data;
  }

  return &path_following_interfaces__srv__detail__waypoints__rosidl_typesupport_introspection_c__Waypoints_service_type_support_handle;
}
