// generated from rosidl_typesupport_introspection_c/resource/idl__type_support.c.em
// with input from path_following_interfaces:srv\InitValues.idl
// generated code does not contain a copyright notice

#include <stddef.h>
#include "path_following_interfaces/srv/detail/init_values__rosidl_typesupport_introspection_c.h"
#include "path_following_interfaces/msg/rosidl_typesupport_introspection_c__visibility_control.h"
#include "rosidl_typesupport_introspection_c/field_types.h"
#include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/message_introspection.h"
#include "path_following_interfaces/srv/detail/init_values__functions.h"
#include "path_following_interfaces/srv/detail/init_values__struct.h"


// Include directives for member types
// Member `initial_state`
#include "path_following_interfaces/msg/state.h"
// Member `initial_state`
#include "path_following_interfaces/msg/detail/state__rosidl_typesupport_introspection_c.h"
// Member `waypoints`
#include "path_following_interfaces/msg/waypoints.h"
// Member `waypoints`
#include "path_following_interfaces/msg/detail/waypoints__rosidl_typesupport_introspection_c.h"

#ifdef __cplusplus
extern "C"
{
#endif

void InitValues_Request__rosidl_typesupport_introspection_c__InitValues_Request_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  path_following_interfaces__srv__InitValues_Request__init(message_memory);
}

void InitValues_Request__rosidl_typesupport_introspection_c__InitValues_Request_fini_function(void * message_memory)
{
  path_following_interfaces__srv__InitValues_Request__fini(message_memory);
}

static rosidl_typesupport_introspection_c__MessageMember InitValues_Request__rosidl_typesupport_introspection_c__InitValues_Request_message_member_array[4] = {
  {
    "initial_state",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message (initialized later)
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(path_following_interfaces__srv__InitValues_Request, initial_state),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "waypoints",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message (initialized later)
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(path_following_interfaces__srv__InitValues_Request, waypoints),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "surge",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_FLOAT,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(path_following_interfaces__srv__InitValues_Request, surge),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "yaw",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_FLOAT,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(path_following_interfaces__srv__InitValues_Request, yaw),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers InitValues_Request__rosidl_typesupport_introspection_c__InitValues_Request_message_members = {
  "path_following_interfaces__srv",  // message namespace
  "InitValues_Request",  // message name
  4,  // number of fields
  sizeof(path_following_interfaces__srv__InitValues_Request),
  InitValues_Request__rosidl_typesupport_introspection_c__InitValues_Request_message_member_array,  // message members
  InitValues_Request__rosidl_typesupport_introspection_c__InitValues_Request_init_function,  // function to initialize message memory (memory has to be allocated)
  InitValues_Request__rosidl_typesupport_introspection_c__InitValues_Request_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t InitValues_Request__rosidl_typesupport_introspection_c__InitValues_Request_message_type_support_handle = {
  0,
  &InitValues_Request__rosidl_typesupport_introspection_c__InitValues_Request_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_path_following_interfaces
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, path_following_interfaces, srv, InitValues_Request)() {
  InitValues_Request__rosidl_typesupport_introspection_c__InitValues_Request_message_member_array[0].members_ =
    ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, path_following_interfaces, msg, State)();
  InitValues_Request__rosidl_typesupport_introspection_c__InitValues_Request_message_member_array[1].members_ =
    ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, path_following_interfaces, msg, Waypoints)();
  if (!InitValues_Request__rosidl_typesupport_introspection_c__InitValues_Request_message_type_support_handle.typesupport_identifier) {
    InitValues_Request__rosidl_typesupport_introspection_c__InitValues_Request_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &InitValues_Request__rosidl_typesupport_introspection_c__InitValues_Request_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif

// already included above
// #include <stddef.h>
// already included above
// #include "path_following_interfaces/srv/detail/init_values__rosidl_typesupport_introspection_c.h"
// already included above
// #include "path_following_interfaces/msg/rosidl_typesupport_introspection_c__visibility_control.h"
// already included above
// #include "rosidl_typesupport_introspection_c/field_types.h"
// already included above
// #include "rosidl_typesupport_introspection_c/identifier.h"
// already included above
// #include "rosidl_typesupport_introspection_c/message_introspection.h"
// already included above
// #include "path_following_interfaces/srv/detail/init_values__functions.h"
// already included above
// #include "path_following_interfaces/srv/detail/init_values__struct.h"


#ifdef __cplusplus
extern "C"
{
#endif

void InitValues_Response__rosidl_typesupport_introspection_c__InitValues_Response_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  path_following_interfaces__srv__InitValues_Response__init(message_memory);
}

void InitValues_Response__rosidl_typesupport_introspection_c__InitValues_Response_fini_function(void * message_memory)
{
  path_following_interfaces__srv__InitValues_Response__fini(message_memory);
}

static rosidl_typesupport_introspection_c__MessageMember InitValues_Response__rosidl_typesupport_introspection_c__InitValues_Response_message_member_array[2] = {
  {
    "surge",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_FLOAT,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(path_following_interfaces__srv__InitValues_Response, surge),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "yaw",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_FLOAT,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(path_following_interfaces__srv__InitValues_Response, yaw),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers InitValues_Response__rosidl_typesupport_introspection_c__InitValues_Response_message_members = {
  "path_following_interfaces__srv",  // message namespace
  "InitValues_Response",  // message name
  2,  // number of fields
  sizeof(path_following_interfaces__srv__InitValues_Response),
  InitValues_Response__rosidl_typesupport_introspection_c__InitValues_Response_message_member_array,  // message members
  InitValues_Response__rosidl_typesupport_introspection_c__InitValues_Response_init_function,  // function to initialize message memory (memory has to be allocated)
  InitValues_Response__rosidl_typesupport_introspection_c__InitValues_Response_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t InitValues_Response__rosidl_typesupport_introspection_c__InitValues_Response_message_type_support_handle = {
  0,
  &InitValues_Response__rosidl_typesupport_introspection_c__InitValues_Response_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_path_following_interfaces
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, path_following_interfaces, srv, InitValues_Response)() {
  if (!InitValues_Response__rosidl_typesupport_introspection_c__InitValues_Response_message_type_support_handle.typesupport_identifier) {
    InitValues_Response__rosidl_typesupport_introspection_c__InitValues_Response_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &InitValues_Response__rosidl_typesupport_introspection_c__InitValues_Response_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif

#include "rosidl_runtime_c/service_type_support_struct.h"
// already included above
// #include "path_following_interfaces/msg/rosidl_typesupport_introspection_c__visibility_control.h"
// already included above
// #include "path_following_interfaces/srv/detail/init_values__rosidl_typesupport_introspection_c.h"
// already included above
// #include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/service_introspection.h"

// this is intentionally not const to allow initialization later to prevent an initialization race
static rosidl_typesupport_introspection_c__ServiceMembers path_following_interfaces__srv__detail__init_values__rosidl_typesupport_introspection_c__InitValues_service_members = {
  "path_following_interfaces__srv",  // service namespace
  "InitValues",  // service name
  // these two fields are initialized below on the first access
  NULL,  // request message
  // path_following_interfaces__srv__detail__init_values__rosidl_typesupport_introspection_c__InitValues_Request_message_type_support_handle,
  NULL  // response message
  // path_following_interfaces__srv__detail__init_values__rosidl_typesupport_introspection_c__InitValues_Response_message_type_support_handle
};

static rosidl_service_type_support_t path_following_interfaces__srv__detail__init_values__rosidl_typesupport_introspection_c__InitValues_service_type_support_handle = {
  0,
  &path_following_interfaces__srv__detail__init_values__rosidl_typesupport_introspection_c__InitValues_service_members,
  get_service_typesupport_handle_function,
};

// Forward declaration of request/response type support functions
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, path_following_interfaces, srv, InitValues_Request)();

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, path_following_interfaces, srv, InitValues_Response)();

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_path_following_interfaces
const rosidl_service_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__SERVICE_SYMBOL_NAME(rosidl_typesupport_introspection_c, path_following_interfaces, srv, InitValues)() {
  if (!path_following_interfaces__srv__detail__init_values__rosidl_typesupport_introspection_c__InitValues_service_type_support_handle.typesupport_identifier) {
    path_following_interfaces__srv__detail__init_values__rosidl_typesupport_introspection_c__InitValues_service_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  rosidl_typesupport_introspection_c__ServiceMembers * service_members =
    (rosidl_typesupport_introspection_c__ServiceMembers *)path_following_interfaces__srv__detail__init_values__rosidl_typesupport_introspection_c__InitValues_service_type_support_handle.data;

  if (!service_members->request_members_) {
    service_members->request_members_ =
      (const rosidl_typesupport_introspection_c__MessageMembers *)
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, path_following_interfaces, srv, InitValues_Request)()->data;
  }
  if (!service_members->response_members_) {
    service_members->response_members_ =
      (const rosidl_typesupport_introspection_c__MessageMembers *)
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, path_following_interfaces, srv, InitValues_Response)()->data;
  }

  return &path_following_interfaces__srv__detail__init_values__rosidl_typesupport_introspection_c__InitValues_service_type_support_handle;
}
