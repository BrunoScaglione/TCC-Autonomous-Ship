// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from path_following_interfaces:msg\Control.idl
// generated code does not contain a copyright notice

#ifndef PATH_FOLLOWING_INTERFACES__MSG__DETAIL__CONTROL__BUILDER_HPP_
#define PATH_FOLLOWING_INTERFACES__MSG__DETAIL__CONTROL__BUILDER_HPP_

#include "path_following_interfaces/msg/detail/control__struct.hpp"
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <utility>


namespace path_following_interfaces
{

namespace msg
{

namespace builder
{

class Init_Control_distance_waypoints
{
public:
  explicit Init_Control_distance_waypoints(::path_following_interfaces::msg::Control & msg)
  : msg_(msg)
  {}
  ::path_following_interfaces::msg::Control distance_waypoints(::path_following_interfaces::msg::Control::_distance_waypoints_type arg)
  {
    msg_.distance_waypoints = std::move(arg);
    return std::move(msg_);
  }

private:
  ::path_following_interfaces::msg::Control msg_;
};

class Init_Control_desired_value
{
public:
  Init_Control_desired_value()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_Control_distance_waypoints desired_value(::path_following_interfaces::msg::Control::_desired_value_type arg)
  {
    msg_.desired_value = std::move(arg);
    return Init_Control_distance_waypoints(msg_);
  }

private:
  ::path_following_interfaces::msg::Control msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::path_following_interfaces::msg::Control>()
{
  return path_following_interfaces::msg::builder::Init_Control_desired_value();
}

}  // namespace path_following_interfaces

#endif  // PATH_FOLLOWING_INTERFACES__MSG__DETAIL__CONTROL__BUILDER_HPP_
