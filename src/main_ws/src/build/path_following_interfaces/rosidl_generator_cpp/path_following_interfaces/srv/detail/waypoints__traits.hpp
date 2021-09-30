// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from path_following_interfaces:srv\Waypoints.idl
// generated code does not contain a copyright notice

#ifndef PATH_FOLLOWING_INTERFACES__SRV__DETAIL__WAYPOINTS__TRAITS_HPP_
#define PATH_FOLLOWING_INTERFACES__SRV__DETAIL__WAYPOINTS__TRAITS_HPP_

#include "path_following_interfaces/srv/detail/waypoints__struct.hpp"
#include <stdint.h>
#include <rosidl_runtime_cpp/traits.hpp>
#include <sstream>
#include <string>
#include <type_traits>

// Include directives for member types
// Member 'position'
#include "path_following_interfaces/msg/detail/positions_xy__traits.hpp"

namespace rosidl_generator_traits
{

inline void to_yaml(
  const path_following_interfaces::srv::Waypoints_Request & msg,
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
    if (msg.velocity.size() == 0) {
      out << "velocity: []\n";
    } else {
      out << "velocity:\n";
      for (auto item : msg.velocity) {
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

inline std::string to_yaml(const path_following_interfaces::srv::Waypoints_Request & msg)
{
  std::ostringstream out;
  to_yaml(msg, out);
  return out.str();
}

template<>
inline const char * data_type<path_following_interfaces::srv::Waypoints_Request>()
{
  return "path_following_interfaces::srv::Waypoints_Request";
}

template<>
inline const char * name<path_following_interfaces::srv::Waypoints_Request>()
{
  return "path_following_interfaces/srv/Waypoints_Request";
}

template<>
struct has_fixed_size<path_following_interfaces::srv::Waypoints_Request>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<path_following_interfaces::srv::Waypoints_Request>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<path_following_interfaces::srv::Waypoints_Request>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace rosidl_generator_traits
{

inline void to_yaml(
  const path_following_interfaces::srv::Waypoints_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: reporting
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "reporting: ";
    value_to_yaml(msg.reporting, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const path_following_interfaces::srv::Waypoints_Response & msg)
{
  std::ostringstream out;
  to_yaml(msg, out);
  return out.str();
}

template<>
inline const char * data_type<path_following_interfaces::srv::Waypoints_Response>()
{
  return "path_following_interfaces::srv::Waypoints_Response";
}

template<>
inline const char * name<path_following_interfaces::srv::Waypoints_Response>()
{
  return "path_following_interfaces/srv/Waypoints_Response";
}

template<>
struct has_fixed_size<path_following_interfaces::srv::Waypoints_Response>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<path_following_interfaces::srv::Waypoints_Response>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<path_following_interfaces::srv::Waypoints_Response>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<path_following_interfaces::srv::Waypoints>()
{
  return "path_following_interfaces::srv::Waypoints";
}

template<>
inline const char * name<path_following_interfaces::srv::Waypoints>()
{
  return "path_following_interfaces/srv/Waypoints";
}

template<>
struct has_fixed_size<path_following_interfaces::srv::Waypoints>
  : std::integral_constant<
    bool,
    has_fixed_size<path_following_interfaces::srv::Waypoints_Request>::value &&
    has_fixed_size<path_following_interfaces::srv::Waypoints_Response>::value
  >
{
};

template<>
struct has_bounded_size<path_following_interfaces::srv::Waypoints>
  : std::integral_constant<
    bool,
    has_bounded_size<path_following_interfaces::srv::Waypoints_Request>::value &&
    has_bounded_size<path_following_interfaces::srv::Waypoints_Response>::value
  >
{
};

template<>
struct is_service<path_following_interfaces::srv::Waypoints>
  : std::true_type
{
};

template<>
struct is_service_request<path_following_interfaces::srv::Waypoints_Request>
  : std::true_type
{
};

template<>
struct is_service_response<path_following_interfaces::srv::Waypoints_Response>
  : std::true_type
{
};

}  // namespace rosidl_generator_traits

#endif  // PATH_FOLLOWING_INTERFACES__SRV__DETAIL__WAYPOINTS__TRAITS_HPP_
