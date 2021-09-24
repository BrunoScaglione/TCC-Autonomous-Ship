// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from path_following_interfaces:msg\State.idl
// generated code does not contain a copyright notice

#ifndef PATH_FOLLOWING_INTERFACES__MSG__DETAIL__STATE__TRAITS_HPP_
#define PATH_FOLLOWING_INTERFACES__MSG__DETAIL__STATE__TRAITS_HPP_

#include "path_following_interfaces/msg/detail/state__struct.hpp"
#include <stdint.h>
#include <rosidl_runtime_cpp/traits.hpp>
#include <sstream>
#include <string>
#include <type_traits>

// Include directives for member types
// Member 'position'
#include "path_following_interfaces/msg/detail/position__traits.hpp"
// Member 'velocity'
#include "path_following_interfaces/msg/detail/velocity__traits.hpp"

namespace rosidl_generator_traits
{

inline void to_yaml(
  const path_following_interfaces::msg::State & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: position
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "position:\n";
    to_yaml(msg.position, out, indentation + 2);
  }

  // member: velocity
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "velocity:\n";
    to_yaml(msg.velocity, out, indentation + 2);
  }

  // member: time
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "time: ";
    value_to_yaml(msg.time, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const path_following_interfaces::msg::State & msg)
{
  std::ostringstream out;
  to_yaml(msg, out);
  return out.str();
}

template<>
inline const char * data_type<path_following_interfaces::msg::State>()
{
  return "path_following_interfaces::msg::State";
}

template<>
inline const char * name<path_following_interfaces::msg::State>()
{
  return "path_following_interfaces/msg/State";
}

template<>
struct has_fixed_size<path_following_interfaces::msg::State>
  : std::integral_constant<bool, has_fixed_size<path_following_interfaces::msg::Position>::value && has_fixed_size<path_following_interfaces::msg::Velocity>::value> {};

template<>
struct has_bounded_size<path_following_interfaces::msg::State>
  : std::integral_constant<bool, has_bounded_size<path_following_interfaces::msg::Position>::value && has_bounded_size<path_following_interfaces::msg::Velocity>::value> {};

template<>
struct is_message<path_following_interfaces::msg::State>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // PATH_FOLLOWING_INTERFACES__MSG__DETAIL__STATE__TRAITS_HPP_
