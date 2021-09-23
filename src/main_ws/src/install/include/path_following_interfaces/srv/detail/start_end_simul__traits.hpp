// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from path_following_interfaces:srv\StartEndSimul.idl
// generated code does not contain a copyright notice

#ifndef PATH_FOLLOWING_INTERFACES__SRV__DETAIL__START_END_SIMUL__TRAITS_HPP_
#define PATH_FOLLOWING_INTERFACES__SRV__DETAIL__START_END_SIMUL__TRAITS_HPP_

#include "path_following_interfaces/srv/detail/start_end_simul__struct.hpp"
#include <stdint.h>
#include <rosidl_runtime_cpp/traits.hpp>
#include <sstream>
#include <string>
#include <type_traits>

// Include directives for member types
// Member 'initial_state'
#include "path_following_interfaces/msg/detail/state__traits.hpp"

namespace rosidl_generator_traits
{

inline void to_yaml(
  const path_following_interfaces::srv::StartEndSimul_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: initial_state
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "initial_state:\n";
    to_yaml(msg.initial_state, out, indentation + 2);
  }

  // member: end_simul
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "end_simul: ";
    value_to_yaml(msg.end_simul, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const path_following_interfaces::srv::StartEndSimul_Request & msg)
{
  std::ostringstream out;
  to_yaml(msg, out);
  return out.str();
}

template<>
inline const char * data_type<path_following_interfaces::srv::StartEndSimul_Request>()
{
  return "path_following_interfaces::srv::StartEndSimul_Request";
}

template<>
inline const char * name<path_following_interfaces::srv::StartEndSimul_Request>()
{
  return "path_following_interfaces/srv/StartEndSimul_Request";
}

template<>
struct has_fixed_size<path_following_interfaces::srv::StartEndSimul_Request>
  : std::integral_constant<bool, has_fixed_size<path_following_interfaces::msg::State>::value> {};

template<>
struct has_bounded_size<path_following_interfaces::srv::StartEndSimul_Request>
  : std::integral_constant<bool, has_bounded_size<path_following_interfaces::msg::State>::value> {};

template<>
struct is_message<path_following_interfaces::srv::StartEndSimul_Request>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace rosidl_generator_traits
{

inline void to_yaml(
  const path_following_interfaces::srv::StartEndSimul_Response & msg,
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

inline std::string to_yaml(const path_following_interfaces::srv::StartEndSimul_Response & msg)
{
  std::ostringstream out;
  to_yaml(msg, out);
  return out.str();
}

template<>
inline const char * data_type<path_following_interfaces::srv::StartEndSimul_Response>()
{
  return "path_following_interfaces::srv::StartEndSimul_Response";
}

template<>
inline const char * name<path_following_interfaces::srv::StartEndSimul_Response>()
{
  return "path_following_interfaces/srv/StartEndSimul_Response";
}

template<>
struct has_fixed_size<path_following_interfaces::srv::StartEndSimul_Response>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<path_following_interfaces::srv::StartEndSimul_Response>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<path_following_interfaces::srv::StartEndSimul_Response>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<path_following_interfaces::srv::StartEndSimul>()
{
  return "path_following_interfaces::srv::StartEndSimul";
}

template<>
inline const char * name<path_following_interfaces::srv::StartEndSimul>()
{
  return "path_following_interfaces/srv/StartEndSimul";
}

template<>
struct has_fixed_size<path_following_interfaces::srv::StartEndSimul>
  : std::integral_constant<
    bool,
    has_fixed_size<path_following_interfaces::srv::StartEndSimul_Request>::value &&
    has_fixed_size<path_following_interfaces::srv::StartEndSimul_Response>::value
  >
{
};

template<>
struct has_bounded_size<path_following_interfaces::srv::StartEndSimul>
  : std::integral_constant<
    bool,
    has_bounded_size<path_following_interfaces::srv::StartEndSimul_Request>::value &&
    has_bounded_size<path_following_interfaces::srv::StartEndSimul_Response>::value
  >
{
};

template<>
struct is_service<path_following_interfaces::srv::StartEndSimul>
  : std::true_type
{
};

template<>
struct is_service_request<path_following_interfaces::srv::StartEndSimul_Request>
  : std::true_type
{
};

template<>
struct is_service_response<path_following_interfaces::srv::StartEndSimul_Response>
  : std::true_type
{
};

}  // namespace rosidl_generator_traits

#endif  // PATH_FOLLOWING_INTERFACES__SRV__DETAIL__START_END_SIMUL__TRAITS_HPP_
