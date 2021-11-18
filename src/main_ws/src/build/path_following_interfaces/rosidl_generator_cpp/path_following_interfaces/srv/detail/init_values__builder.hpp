// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from path_following_interfaces:srv\InitValues.idl
// generated code does not contain a copyright notice

#ifndef PATH_FOLLOWING_INTERFACES__SRV__DETAIL__INIT_VALUES__BUILDER_HPP_
#define PATH_FOLLOWING_INTERFACES__SRV__DETAIL__INIT_VALUES__BUILDER_HPP_

#include "path_following_interfaces/srv/detail/init_values__struct.hpp"
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <utility>


namespace path_following_interfaces
{

namespace srv
{

namespace builder
{

class Init_InitValues_Request_yaw
{
public:
  explicit Init_InitValues_Request_yaw(::path_following_interfaces::srv::InitValues_Request & msg)
  : msg_(msg)
  {}
  ::path_following_interfaces::srv::InitValues_Request yaw(::path_following_interfaces::srv::InitValues_Request::_yaw_type arg)
  {
    msg_.yaw = std::move(arg);
    return std::move(msg_);
  }

private:
  ::path_following_interfaces::srv::InitValues_Request msg_;
};

class Init_InitValues_Request_surge
{
public:
  explicit Init_InitValues_Request_surge(::path_following_interfaces::srv::InitValues_Request & msg)
  : msg_(msg)
  {}
  Init_InitValues_Request_yaw surge(::path_following_interfaces::srv::InitValues_Request::_surge_type arg)
  {
    msg_.surge = std::move(arg);
    return Init_InitValues_Request_yaw(msg_);
  }

private:
  ::path_following_interfaces::srv::InitValues_Request msg_;
};

class Init_InitValues_Request_waypoints
{
public:
  explicit Init_InitValues_Request_waypoints(::path_following_interfaces::srv::InitValues_Request & msg)
  : msg_(msg)
  {}
  Init_InitValues_Request_surge waypoints(::path_following_interfaces::srv::InitValues_Request::_waypoints_type arg)
  {
    msg_.waypoints = std::move(arg);
    return Init_InitValues_Request_surge(msg_);
  }

private:
  ::path_following_interfaces::srv::InitValues_Request msg_;
};

class Init_InitValues_Request_initial_state
{
public:
  Init_InitValues_Request_initial_state()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_InitValues_Request_waypoints initial_state(::path_following_interfaces::srv::InitValues_Request::_initial_state_type arg)
  {
    msg_.initial_state = std::move(arg);
    return Init_InitValues_Request_waypoints(msg_);
  }

private:
  ::path_following_interfaces::srv::InitValues_Request msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::path_following_interfaces::srv::InitValues_Request>()
{
  return path_following_interfaces::srv::builder::Init_InitValues_Request_initial_state();
}

}  // namespace path_following_interfaces


namespace path_following_interfaces
{

namespace srv
{

namespace builder
{

class Init_InitValues_Response_yaw
{
public:
  explicit Init_InitValues_Response_yaw(::path_following_interfaces::srv::InitValues_Response & msg)
  : msg_(msg)
  {}
  ::path_following_interfaces::srv::InitValues_Response yaw(::path_following_interfaces::srv::InitValues_Response::_yaw_type arg)
  {
    msg_.yaw = std::move(arg);
    return std::move(msg_);
  }

private:
  ::path_following_interfaces::srv::InitValues_Response msg_;
};

class Init_InitValues_Response_surge
{
public:
  Init_InitValues_Response_surge()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_InitValues_Response_yaw surge(::path_following_interfaces::srv::InitValues_Response::_surge_type arg)
  {
    msg_.surge = std::move(arg);
    return Init_InitValues_Response_yaw(msg_);
  }

private:
  ::path_following_interfaces::srv::InitValues_Response msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::path_following_interfaces::srv::InitValues_Response>()
{
  return path_following_interfaces::srv::builder::Init_InitValues_Response_surge();
}

}  // namespace path_following_interfaces

#endif  // PATH_FOLLOWING_INTERFACES__SRV__DETAIL__INIT_VALUES__BUILDER_HPP_
