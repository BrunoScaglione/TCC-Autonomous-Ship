// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from path_following_interfaces:msg\PositionsXY.idl
// generated code does not contain a copyright notice

#ifndef PATH_FOLLOWING_INTERFACES__MSG__DETAIL__POSITIONS_XY__TRAITS_HPP_
#define PATH_FOLLOWING_INTERFACES__MSG__DETAIL__POSITIONS_XY__TRAITS_HPP_

#include "path_following_interfaces/msg/detail/positions_xy__struct.hpp"
#include <stdint.h>
#include <rosidl_runtime_cpp/traits.hpp>
#include <sstream>
#include <string>
#include <type_traits>

namespace rosidl_generator_traits
{

inline void to_yaml(
  const path_following_interfaces::msg::PositionsXY & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: x
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    if (msg.x.size() == 0) {
      out << "x: []\n";
    } else {
      out << "x:\n";
      for (auto item : msg.x) {
        if (indentation > 0) {
          out << std::string(indentation, ' ');
        }
        out << "- ";
        value_to_yaml(item, out);
        out << "\n";
      }
    }
  }

  // member: y
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    if (msg.y.size() == 0) {
      out << "y: []\n";
    } else {
      out << "y:\n";
      for (auto item : msg.y) {
        if (indentation > 0) {
          out << std::string(indentation, ' ');
        }
        out << "- ";
        value_to_yaml(item, out);
        out << "\n";
      }
    }
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const path_following_interfaces::msg::PositionsXY & msg)
{
  std::ostringstream out;
  to_yaml(msg, out);
  return out.str();
}

template<>
inline const char * data_type<path_following_interfaces::msg::PositionsXY>()
{
  return "path_following_interfaces::msg::PositionsXY";
}

template<>
inline const char * name<path_following_interfaces::msg::PositionsXY>()
{
  return "path_following_interfaces/msg/PositionsXY";
}

template<>
struct has_fixed_size<path_following_interfaces::msg::PositionsXY>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<path_following_interfaces::msg::PositionsXY>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<path_following_interfaces::msg::PositionsXY>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // PATH_FOLLOWING_INTERFACES__MSG__DETAIL__POSITIONS_XY__TRAITS_HPP_
