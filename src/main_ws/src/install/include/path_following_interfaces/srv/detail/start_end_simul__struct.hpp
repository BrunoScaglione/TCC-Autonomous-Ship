// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from path_following_interfaces:srv\StartEndSimul.idl
// generated code does not contain a copyright notice

#ifndef PATH_FOLLOWING_INTERFACES__SRV__DETAIL__START_END_SIMUL__STRUCT_HPP_
#define PATH_FOLLOWING_INTERFACES__SRV__DETAIL__START_END_SIMUL__STRUCT_HPP_

#include <rosidl_runtime_cpp/bounded_vector.hpp>
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>


// Include directives for member types
// Member 'initial_state'
#include "path_following_interfaces/msg/detail/state__struct.hpp"

#ifndef _WIN32
# define DEPRECATED__path_following_interfaces__srv__StartEndSimul_Request __attribute__((deprecated))
#else
# define DEPRECATED__path_following_interfaces__srv__StartEndSimul_Request __declspec(deprecated)
#endif

namespace path_following_interfaces
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct StartEndSimul_Request_
{
  using Type = StartEndSimul_Request_<ContainerAllocator>;

  explicit StartEndSimul_Request_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : initial_state(_init)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::DEFAULTS_ONLY == _init)
    {
      this->end_simul = false;
    } else if (rosidl_runtime_cpp::MessageInitialization::ZERO == _init) {
      this->end_simul = false;
    }
  }

  explicit StartEndSimul_Request_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : initial_state(_alloc, _init)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::DEFAULTS_ONLY == _init)
    {
      this->end_simul = false;
    } else if (rosidl_runtime_cpp::MessageInitialization::ZERO == _init) {
      this->end_simul = false;
    }
  }

  // field types and members
  using _initial_state_type =
    path_following_interfaces::msg::State_<ContainerAllocator>;
  _initial_state_type initial_state;
  using _end_simul_type =
    bool;
  _end_simul_type end_simul;

  // setters for named parameter idiom
  Type & set__initial_state(
    const path_following_interfaces::msg::State_<ContainerAllocator> & _arg)
  {
    this->initial_state = _arg;
    return *this;
  }
  Type & set__end_simul(
    const bool & _arg)
  {
    this->end_simul = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    path_following_interfaces::srv::StartEndSimul_Request_<ContainerAllocator> *;
  using ConstRawPtr =
    const path_following_interfaces::srv::StartEndSimul_Request_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<path_following_interfaces::srv::StartEndSimul_Request_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<path_following_interfaces::srv::StartEndSimul_Request_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      path_following_interfaces::srv::StartEndSimul_Request_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<path_following_interfaces::srv::StartEndSimul_Request_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      path_following_interfaces::srv::StartEndSimul_Request_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<path_following_interfaces::srv::StartEndSimul_Request_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<path_following_interfaces::srv::StartEndSimul_Request_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<path_following_interfaces::srv::StartEndSimul_Request_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__path_following_interfaces__srv__StartEndSimul_Request
    std::shared_ptr<path_following_interfaces::srv::StartEndSimul_Request_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__path_following_interfaces__srv__StartEndSimul_Request
    std::shared_ptr<path_following_interfaces::srv::StartEndSimul_Request_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const StartEndSimul_Request_ & other) const
  {
    if (this->initial_state != other.initial_state) {
      return false;
    }
    if (this->end_simul != other.end_simul) {
      return false;
    }
    return true;
  }
  bool operator!=(const StartEndSimul_Request_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct StartEndSimul_Request_

// alias to use template instance with default allocator
using StartEndSimul_Request =
  path_following_interfaces::srv::StartEndSimul_Request_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace path_following_interfaces


#ifndef _WIN32
# define DEPRECATED__path_following_interfaces__srv__StartEndSimul_Response __attribute__((deprecated))
#else
# define DEPRECATED__path_following_interfaces__srv__StartEndSimul_Response __declspec(deprecated)
#endif

namespace path_following_interfaces
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct StartEndSimul_Response_
{
  using Type = StartEndSimul_Response_<ContainerAllocator>;

  explicit StartEndSimul_Response_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->reporting = "";
    }
  }

  explicit StartEndSimul_Response_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : reporting(_alloc)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->reporting = "";
    }
  }

  // field types and members
  using _reporting_type =
    std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>;
  _reporting_type reporting;

  // setters for named parameter idiom
  Type & set__reporting(
    const std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>> & _arg)
  {
    this->reporting = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    path_following_interfaces::srv::StartEndSimul_Response_<ContainerAllocator> *;
  using ConstRawPtr =
    const path_following_interfaces::srv::StartEndSimul_Response_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<path_following_interfaces::srv::StartEndSimul_Response_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<path_following_interfaces::srv::StartEndSimul_Response_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      path_following_interfaces::srv::StartEndSimul_Response_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<path_following_interfaces::srv::StartEndSimul_Response_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      path_following_interfaces::srv::StartEndSimul_Response_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<path_following_interfaces::srv::StartEndSimul_Response_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<path_following_interfaces::srv::StartEndSimul_Response_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<path_following_interfaces::srv::StartEndSimul_Response_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__path_following_interfaces__srv__StartEndSimul_Response
    std::shared_ptr<path_following_interfaces::srv::StartEndSimul_Response_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__path_following_interfaces__srv__StartEndSimul_Response
    std::shared_ptr<path_following_interfaces::srv::StartEndSimul_Response_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const StartEndSimul_Response_ & other) const
  {
    if (this->reporting != other.reporting) {
      return false;
    }
    return true;
  }
  bool operator!=(const StartEndSimul_Response_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct StartEndSimul_Response_

// alias to use template instance with default allocator
using StartEndSimul_Response =
  path_following_interfaces::srv::StartEndSimul_Response_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace path_following_interfaces

namespace path_following_interfaces
{

namespace srv
{

struct StartEndSimul
{
  using Request = path_following_interfaces::srv::StartEndSimul_Request;
  using Response = path_following_interfaces::srv::StartEndSimul_Response;
};

}  // namespace srv

}  // namespace path_following_interfaces

#endif  // PATH_FOLLOWING_INTERFACES__SRV__DETAIL__START_END_SIMUL__STRUCT_HPP_
