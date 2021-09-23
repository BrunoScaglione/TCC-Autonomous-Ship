// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from path_following_interfaces:srv\Waypoints.idl
// generated code does not contain a copyright notice

#ifndef PATH_FOLLOWING_INTERFACES__SRV__DETAIL__WAYPOINTS__BUILDER_HPP_
#define PATH_FOLLOWING_INTERFACES__SRV__DETAIL__WAYPOINTS__BUILDER_HPP_

#include "path_following_interfaces/srv/detail/waypoints__struct.hpp"
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <utility>


namespace path_following_interfaces
{

namespace srv
{

namespace builder
{

class Init_Waypoints_Request_velocity
{
public:
  explicit Init_Waypoints_Request_velocity(::path_following_interfaces::srv::Waypoints_Request & msg)
  : msg_(msg)
  {}
  ::path_following_interfaces::srv::Waypoints_Request velocity(::path_following_interfaces::srv::Waypoints_Request::_velocity_type arg)
  {
    msg_.velocity = std::move(arg);
    return std::move(msg_);
  }

private:
  ::path_following_interfaces::srv::Waypoints_Request msg_;
};

class Init_Waypoints_Request_position
{
public:
  Init_Waypoints_Request_position()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_Waypoints_Request_velocity position(::path_following_interfaces::srv::Waypoints_Request::_position_type arg)
  {
    msg_.position = std::move(arg);
    return Init_Waypoints_Request_velocity(msg_);
  }

private:
  ::path_following_interfaces::srv::Waypoints_Request msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::path_following_interfaces::srv::Waypoints_Request>()
{
  return path_following_interfaces::srv::builder::Init_Waypoints_Request_position();
}

}  // namespace path_following_interfaces


namespace path_following_interfaces
{

namespace srv
{

namespace builder
{

class Init_Waypoints_Response_reporting
{
public:
  Init_Waypoints_Response_reporting()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::path_following_interfaces::srv::Waypoints_Response reporting(::path_following_interfaces::srv::Waypoints_Response::_reporting_type arg)
  {
    msg_.reporting = std::move(arg);
    return std::move(msg_);
  }

private:
  ::path_following_interfaces::srv::Waypoints_Response msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::path_following_interfaces::srv::Waypoints_Response>()
{
  return path_following_interfaces::srv::builder::Init_Waypoints_Response_reporting();
}

}  // namespace path_following_interfaces

#endif  // PATH_FOLLOWING_INTERFACES__SRV__DETAIL__WAYPOINTS__BUILDER_HPP_
