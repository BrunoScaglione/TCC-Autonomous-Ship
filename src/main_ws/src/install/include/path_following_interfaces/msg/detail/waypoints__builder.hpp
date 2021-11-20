// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from path_following_interfaces:msg\Waypoints.idl
// generated code does not contain a copyright notice

#ifndef PATH_FOLLOWING_INTERFACES__MSG__DETAIL__WAYPOINTS__BUILDER_HPP_
#define PATH_FOLLOWING_INTERFACES__MSG__DETAIL__WAYPOINTS__BUILDER_HPP_

#include "path_following_interfaces/msg/detail/waypoints__struct.hpp"
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <utility>


namespace path_following_interfaces
{

namespace msg
{

namespace builder
{

class Init_Waypoints_velocity
{
public:
  explicit Init_Waypoints_velocity(::path_following_interfaces::msg::Waypoints & msg)
  : msg_(msg)
  {}
  ::path_following_interfaces::msg::Waypoints velocity(::path_following_interfaces::msg::Waypoints::_velocity_type arg)
  {
    msg_.velocity = std::move(arg);
    return std::move(msg_);
  }

private:
  ::path_following_interfaces::msg::Waypoints msg_;
};

class Init_Waypoints_position
{
public:
  Init_Waypoints_position()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_Waypoints_velocity position(::path_following_interfaces::msg::Waypoints::_position_type arg)
  {
    msg_.position = std::move(arg);
    return Init_Waypoints_velocity(msg_);
  }

private:
  ::path_following_interfaces::msg::Waypoints msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::path_following_interfaces::msg::Waypoints>()
{
  return path_following_interfaces::msg::builder::Init_Waypoints_position();
}

}  // namespace path_following_interfaces

#endif  // PATH_FOLLOWING_INTERFACES__MSG__DETAIL__WAYPOINTS__BUILDER_HPP_
