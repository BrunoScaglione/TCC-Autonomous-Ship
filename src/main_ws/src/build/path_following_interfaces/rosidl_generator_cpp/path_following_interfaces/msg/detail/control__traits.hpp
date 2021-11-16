// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from path_following_interfaces:msg\Control.idl
// generated code does not contain a copyright notice

#ifndef PATH_FOLLOWING_INTERFACES__MSG__DETAIL__CONTROL__TRAITS_HPP_
#define PATH_FOLLOWING_INTERFACES__MSG__DETAIL__CONTROL__TRAITS_HPP_

#include "path_following_interfaces/msg/detail/control__struct.hpp"
#include <stdint.h>
#include <rosidl_runtime_cpp/traits.hpp>
#include <sstream>
#include <string>
#include <type_traits>

namespace rosidl_generator_traits
{

inline void to_yaml(
  const path_following_interfaces::msg::Control & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: desired_value
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "desired_value: ";
    value_to_yaml(msg.desired_value, out);
    out << "\n";
  }

  // member: distance_waypoints
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "distance_waypoints: ";
    value_to_yaml(msg.distance_waypoints, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const path_following_interfaces::msg::Control & msg)
{
  std::ostringstream out;
  to_yaml(msg, out);
  return out.str();
}

template<>
inline const char * data_type<path_following_interfaces::msg::Control>()
{
  return "path_following_interfaces::msg::Control";
}

template<>
inline const char * name<path_following_interfaces::msg::Control>()
{
  return "path_following_interfaces/msg/Control";
}

template<>
struct has_fixed_size<path_following_interfaces::msg::Control>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<path_following_interfaces::msg::Control>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<path_following_interfaces::msg::Control>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // PATH_FOLLOWING_INTERFACES__MSG__DETAIL__CONTROL__TRAITS_HPP_
