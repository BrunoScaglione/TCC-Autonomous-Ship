// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from path_following_interfaces:msg\Position.idl
// generated code does not contain a copyright notice

#ifndef PATH_FOLLOWING_INTERFACES__MSG__DETAIL__POSITION__BUILDER_HPP_
#define PATH_FOLLOWING_INTERFACES__MSG__DETAIL__POSITION__BUILDER_HPP_

#include "path_following_interfaces/msg/detail/position__struct.hpp"
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <utility>


namespace path_following_interfaces
{

namespace msg
{

namespace builder
{

class Init_Position_theta
{
public:
  explicit Init_Position_theta(::path_following_interfaces::msg::Position & msg)
  : msg_(msg)
  {}
  ::path_following_interfaces::msg::Position theta(::path_following_interfaces::msg::Position::_theta_type arg)
  {
    msg_.theta = std::move(arg);
    return std::move(msg_);
  }

private:
  ::path_following_interfaces::msg::Position msg_;
};

class Init_Position_y
{
public:
  explicit Init_Position_y(::path_following_interfaces::msg::Position & msg)
  : msg_(msg)
  {}
  Init_Position_theta y(::path_following_interfaces::msg::Position::_y_type arg)
  {
    msg_.y = std::move(arg);
    return Init_Position_theta(msg_);
  }

private:
  ::path_following_interfaces::msg::Position msg_;
};

class Init_Position_x
{
public:
  Init_Position_x()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_Position_y x(::path_following_interfaces::msg::Position::_x_type arg)
  {
    msg_.x = std::move(arg);
    return Init_Position_y(msg_);
  }

private:
  ::path_following_interfaces::msg::Position msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::path_following_interfaces::msg::Position>()
{
  return path_following_interfaces::msg::builder::Init_Position_x();
}

}  // namespace path_following_interfaces

#endif  // PATH_FOLLOWING_INTERFACES__MSG__DETAIL__POSITION__BUILDER_HPP_
