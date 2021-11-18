// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from path_following_interfaces:msg\Velocity.idl
// generated code does not contain a copyright notice

#ifndef PATH_FOLLOWING_INTERFACES__MSG__DETAIL__VELOCITY__TRAITS_HPP_
#define PATH_FOLLOWING_INTERFACES__MSG__DETAIL__VELOCITY__TRAITS_HPP_

#include "path_following_interfaces/msg/detail/velocity__struct.hpp"
#include <stdint.h>
#include <rosidl_runtime_cpp/traits.hpp>
#include <sstream>
#include <string>
#include <type_traits>

namespace rosidl_generator_traits
{

inline void to_yaml(
  const path_following_interfaces::msg::Velocity & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: u
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "u: ";
    value_to_yaml(msg.u, out);
    out << "\n";
  }

  // member: v
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "v: ";
    value_to_yaml(msg.v, out);
    out << "\n";
  }

  // member: r
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "r: ";
    value_to_yaml(msg.r, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const path_following_interfaces::msg::Velocity & msg)
{
  std::ostringstream out;
  to_yaml(msg, out);
  return out.str();
}

template<>
inline const char * data_type<path_following_interfaces::msg::Velocity>()
{
  return "path_following_interfaces::msg::Velocity";
}

template<>
inline const char * name<path_following_interfaces::msg::Velocity>()
{
  return "path_following_interfaces/msg/Velocity";
}

template<>
struct has_fixed_size<path_following_interfaces::msg::Velocity>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<path_following_interfaces::msg::Velocity>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<path_following_interfaces::msg::Velocity>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // PATH_FOLLOWING_INTERFACES__MSG__DETAIL__VELOCITY__TRAITS_HPP_
