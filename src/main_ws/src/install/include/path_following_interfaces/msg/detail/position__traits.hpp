// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from path_following_interfaces:msg\Position.idl
// generated code does not contain a copyright notice

#ifndef PATH_FOLLOWING_INTERFACES__MSG__DETAIL__POSITION__TRAITS_HPP_
#define PATH_FOLLOWING_INTERFACES__MSG__DETAIL__POSITION__TRAITS_HPP_

#include "path_following_interfaces/msg/detail/position__struct.hpp"
#include <stdint.h>
#include <rosidl_runtime_cpp/traits.hpp>
#include <sstream>
#include <string>
#include <type_traits>

namespace rosidl_generator_traits
{

inline void to_yaml(
  const path_following_interfaces::msg::Position & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: x
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "x: ";
    value_to_yaml(msg.x, out);
    out << "\n";
  }

  // member: y
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "y: ";
    value_to_yaml(msg.y, out);
    out << "\n";
  }

  // member: psi
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "psi: ";
    value_to_yaml(msg.psi, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const path_following_interfaces::msg::Position & msg)
{
  std::ostringstream out;
  to_yaml(msg, out);
  return out.str();
}

template<>
inline const char * data_type<path_following_interfaces::msg::Position>()
{
  return "path_following_interfaces::msg::Position";
}

template<>
inline const char * name<path_following_interfaces::msg::Position>()
{
  return "path_following_interfaces/msg/Position";
}

template<>
struct has_fixed_size<path_following_interfaces::msg::Position>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<path_following_interfaces::msg::Position>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<path_following_interfaces::msg::Position>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // PATH_FOLLOWING_INTERFACES__MSG__DETAIL__POSITION__TRAITS_HPP_
