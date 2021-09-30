// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from path_following_interfaces:srv\StartEndSimul.idl
// generated code does not contain a copyright notice

#ifndef PATH_FOLLOWING_INTERFACES__SRV__DETAIL__START_END_SIMUL__BUILDER_HPP_
#define PATH_FOLLOWING_INTERFACES__SRV__DETAIL__START_END_SIMUL__BUILDER_HPP_

#include "path_following_interfaces/srv/detail/start_end_simul__struct.hpp"
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <utility>


namespace path_following_interfaces
{

namespace srv
{

namespace builder
{

class Init_StartEndSimul_Request_end_simul
{
public:
  explicit Init_StartEndSimul_Request_end_simul(::path_following_interfaces::srv::StartEndSimul_Request & msg)
  : msg_(msg)
  {}
  ::path_following_interfaces::srv::StartEndSimul_Request end_simul(::path_following_interfaces::srv::StartEndSimul_Request::_end_simul_type arg)
  {
    msg_.end_simul = std::move(arg);
    return std::move(msg_);
  }

private:
  ::path_following_interfaces::srv::StartEndSimul_Request msg_;
};

class Init_StartEndSimul_Request_initial_state
{
public:
  Init_StartEndSimul_Request_initial_state()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_StartEndSimul_Request_end_simul initial_state(::path_following_interfaces::srv::StartEndSimul_Request::_initial_state_type arg)
  {
    msg_.initial_state = std::move(arg);
    return Init_StartEndSimul_Request_end_simul(msg_);
  }

private:
  ::path_following_interfaces::srv::StartEndSimul_Request msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::path_following_interfaces::srv::StartEndSimul_Request>()
{
  return path_following_interfaces::srv::builder::Init_StartEndSimul_Request_initial_state();
}

}  // namespace path_following_interfaces


namespace path_following_interfaces
{

namespace srv
{

namespace builder
{

class Init_StartEndSimul_Response_reporting
{
public:
  Init_StartEndSimul_Response_reporting()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::path_following_interfaces::srv::StartEndSimul_Response reporting(::path_following_interfaces::srv::StartEndSimul_Response::_reporting_type arg)
  {
    msg_.reporting = std::move(arg);
    return std::move(msg_);
  }

private:
  ::path_following_interfaces::srv::StartEndSimul_Response msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::path_following_interfaces::srv::StartEndSimul_Response>()
{
  return path_following_interfaces::srv::builder::Init_StartEndSimul_Response_reporting();
}

}  // namespace path_following_interfaces

#endif  // PATH_FOLLOWING_INTERFACES__SRV__DETAIL__START_END_SIMUL__BUILDER_HPP_
