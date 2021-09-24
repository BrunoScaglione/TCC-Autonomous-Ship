// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from path_following_interfaces:msg\State.idl
// generated code does not contain a copyright notice

#ifndef PATH_FOLLOWING_INTERFACES__MSG__DETAIL__STATE__BUILDER_HPP_
#define PATH_FOLLOWING_INTERFACES__MSG__DETAIL__STATE__BUILDER_HPP_

#include "path_following_interfaces/msg/detail/state__struct.hpp"
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <utility>


namespace path_following_interfaces
{

namespace msg
{

namespace builder
{

class Init_State_time
{
public:
  explicit Init_State_time(::path_following_interfaces::msg::State & msg)
  : msg_(msg)
  {}
  ::path_following_interfaces::msg::State time(::path_following_interfaces::msg::State::_time_type arg)
  {
    msg_.time = std::move(arg);
    return std::move(msg_);
  }

private:
  ::path_following_interfaces::msg::State msg_;
};

class Init_State_velocity
{
public:
  explicit Init_State_velocity(::path_following_interfaces::msg::State & msg)
  : msg_(msg)
  {}
  Init_State_time velocity(::path_following_interfaces::msg::State::_velocity_type arg)
  {
    msg_.velocity = std::move(arg);
    return Init_State_time(msg_);
  }

private:
  ::path_following_interfaces::msg::State msg_;
};

class Init_State_position
{
public:
  Init_State_position()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_State_velocity position(::path_following_interfaces::msg::State::_position_type arg)
  {
    msg_.position = std::move(arg);
    return Init_State_velocity(msg_);
  }

private:
  ::path_following_interfaces::msg::State msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::path_following_interfaces::msg::State>()
{
  return path_following_interfaces::msg::builder::Init_State_position();
}

}  // namespace path_following_interfaces

#endif  // PATH_FOLLOWING_INTERFACES__MSG__DETAIL__STATE__BUILDER_HPP_
