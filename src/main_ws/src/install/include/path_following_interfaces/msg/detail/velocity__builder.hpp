// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from path_following_interfaces:msg\Velocity.idl
// generated code does not contain a copyright notice

#ifndef PATH_FOLLOWING_INTERFACES__MSG__DETAIL__VELOCITY__BUILDER_HPP_
#define PATH_FOLLOWING_INTERFACES__MSG__DETAIL__VELOCITY__BUILDER_HPP_

#include "path_following_interfaces/msg/detail/velocity__struct.hpp"
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <utility>


namespace path_following_interfaces
{

namespace msg
{

namespace builder
{

class Init_Velocity_r
{
public:
  explicit Init_Velocity_r(::path_following_interfaces::msg::Velocity & msg)
  : msg_(msg)
  {}
  ::path_following_interfaces::msg::Velocity r(::path_following_interfaces::msg::Velocity::_r_type arg)
  {
    msg_.r = std::move(arg);
    return std::move(msg_);
  }

private:
  ::path_following_interfaces::msg::Velocity msg_;
};

class Init_Velocity_v
{
public:
  explicit Init_Velocity_v(::path_following_interfaces::msg::Velocity & msg)
  : msg_(msg)
  {}
  Init_Velocity_r v(::path_following_interfaces::msg::Velocity::_v_type arg)
  {
    msg_.v = std::move(arg);
    return Init_Velocity_r(msg_);
  }

private:
  ::path_following_interfaces::msg::Velocity msg_;
};

class Init_Velocity_u
{
public:
  Init_Velocity_u()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_Velocity_v u(::path_following_interfaces::msg::Velocity::_u_type arg)
  {
    msg_.u = std::move(arg);
    return Init_Velocity_v(msg_);
  }

private:
  ::path_following_interfaces::msg::Velocity msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::path_following_interfaces::msg::Velocity>()
{
  return path_following_interfaces::msg::builder::Init_Velocity_u();
}

}  // namespace path_following_interfaces

#endif  // PATH_FOLLOWING_INTERFACES__MSG__DETAIL__VELOCITY__BUILDER_HPP_
