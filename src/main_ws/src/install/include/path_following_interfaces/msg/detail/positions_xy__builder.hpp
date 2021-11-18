// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from path_following_interfaces:msg\PositionsXY.idl
// generated code does not contain a copyright notice

#ifndef PATH_FOLLOWING_INTERFACES__MSG__DETAIL__POSITIONS_XY__BUILDER_HPP_
#define PATH_FOLLOWING_INTERFACES__MSG__DETAIL__POSITIONS_XY__BUILDER_HPP_

#include "path_following_interfaces/msg/detail/positions_xy__struct.hpp"
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <utility>


namespace path_following_interfaces
{

namespace msg
{

namespace builder
{

class Init_PositionsXY_y
{
public:
  explicit Init_PositionsXY_y(::path_following_interfaces::msg::PositionsXY & msg)
  : msg_(msg)
  {}
  ::path_following_interfaces::msg::PositionsXY y(::path_following_interfaces::msg::PositionsXY::_y_type arg)
  {
    msg_.y = std::move(arg);
    return std::move(msg_);
  }

private:
  ::path_following_interfaces::msg::PositionsXY msg_;
};

class Init_PositionsXY_x
{
public:
  Init_PositionsXY_x()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_PositionsXY_y x(::path_following_interfaces::msg::PositionsXY::_x_type arg)
  {
    msg_.x = std::move(arg);
    return Init_PositionsXY_y(msg_);
  }

private:
  ::path_following_interfaces::msg::PositionsXY msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::path_following_interfaces::msg::PositionsXY>()
{
  return path_following_interfaces::msg::builder::Init_PositionsXY_x();
}

}  // namespace path_following_interfaces

#endif  // PATH_FOLLOWING_INTERFACES__MSG__DETAIL__POSITIONS_XY__BUILDER_HPP_
