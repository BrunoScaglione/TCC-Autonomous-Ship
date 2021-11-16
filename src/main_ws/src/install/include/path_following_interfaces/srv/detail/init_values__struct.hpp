// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from path_following_interfaces:srv\InitValues.idl
// generated code does not contain a copyright notice

#ifndef PATH_FOLLOWING_INTERFACES__SRV__DETAIL__INIT_VALUES__STRUCT_HPP_
#define PATH_FOLLOWING_INTERFACES__SRV__DETAIL__INIT_VALUES__STRUCT_HPP_

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
// Member 'waypoints'
#include "path_following_interfaces/msg/detail/waypoints__struct.hpp"

#ifndef _WIN32
# define DEPRECATED__path_following_interfaces__srv__InitValues_Request __attribute__((deprecated))
#else
# define DEPRECATED__path_following_interfaces__srv__InitValues_Request __declspec(deprecated)
#endif

namespace path_following_interfaces
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct InitValues_Request_
{
  using Type = InitValues_Request_<ContainerAllocator>;

  explicit InitValues_Request_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : initial_state(_init),
    waypoints(_init)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::DEFAULTS_ONLY == _init)
    {
      this->surge = 0.0f;
      this->yaw = 0.0f;
    } else if (rosidl_runtime_cpp::MessageInitialization::ZERO == _init) {
      this->surge = 0.0f;
      this->yaw = 0.0f;
    }
  }

  explicit InitValues_Request_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : initial_state(_alloc, _init),
    waypoints(_alloc, _init)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::DEFAULTS_ONLY == _init)
    {
      this->surge = 0.0f;
      this->yaw = 0.0f;
    } else if (rosidl_runtime_cpp::MessageInitialization::ZERO == _init) {
      this->surge = 0.0f;
      this->yaw = 0.0f;
    }
  }

  // field types and members
  using _initial_state_type =
    path_following_interfaces::msg::State_<ContainerAllocator>;
  _initial_state_type initial_state;
  using _waypoints_type =
    path_following_interfaces::msg::Waypoints_<ContainerAllocator>;
  _waypoints_type waypoints;
  using _surge_type =
    float;
  _surge_type surge;
  using _yaw_type =
    float;
  _yaw_type yaw;

  // setters for named parameter idiom
  Type & set__initial_state(
    const path_following_interfaces::msg::State_<ContainerAllocator> & _arg)
  {
    this->initial_state = _arg;
    return *this;
  }
  Type & set__waypoints(
    const path_following_interfaces::msg::Waypoints_<ContainerAllocator> & _arg)
  {
    this->waypoints = _arg;
    return *this;
  }
  Type & set__surge(
    const float & _arg)
  {
    this->surge = _arg;
    return *this;
  }
  Type & set__yaw(
    const float & _arg)
  {
    this->yaw = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    path_following_interfaces::srv::InitValues_Request_<ContainerAllocator> *;
  using ConstRawPtr =
    const path_following_interfaces::srv::InitValues_Request_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<path_following_interfaces::srv::InitValues_Request_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<path_following_interfaces::srv::InitValues_Request_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      path_following_interfaces::srv::InitValues_Request_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<path_following_interfaces::srv::InitValues_Request_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      path_following_interfaces::srv::InitValues_Request_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<path_following_interfaces::srv::InitValues_Request_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<path_following_interfaces::srv::InitValues_Request_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<path_following_interfaces::srv::InitValues_Request_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__path_following_interfaces__srv__InitValues_Request
    std::shared_ptr<path_following_interfaces::srv::InitValues_Request_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__path_following_interfaces__srv__InitValues_Request
    std::shared_ptr<path_following_interfaces::srv::InitValues_Request_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const InitValues_Request_ & other) const
  {
    if (this->initial_state != other.initial_state) {
      return false;
    }
    if (this->waypoints != other.waypoints) {
      return false;
    }
    if (this->surge != other.surge) {
      return false;
    }
    if (this->yaw != other.yaw) {
      return false;
    }
    return true;
  }
  bool operator!=(const InitValues_Request_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct InitValues_Request_

// alias to use template instance with default allocator
using InitValues_Request =
  path_following_interfaces::srv::InitValues_Request_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace path_following_interfaces


#ifndef _WIN32
# define DEPRECATED__path_following_interfaces__srv__InitValues_Response __attribute__((deprecated))
#else
# define DEPRECATED__path_following_interfaces__srv__InitValues_Response __declspec(deprecated)
#endif

namespace path_following_interfaces
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct InitValues_Response_
{
  using Type = InitValues_Response_<ContainerAllocator>;

  explicit InitValues_Response_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::DEFAULTS_ONLY == _init)
    {
      this->surge = 0.0f;
      this->yaw = 0.0f;
    } else if (rosidl_runtime_cpp::MessageInitialization::ZERO == _init) {
      this->surge = 0.0f;
      this->yaw = 0.0f;
    }
  }

  explicit InitValues_Response_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::DEFAULTS_ONLY == _init)
    {
      this->surge = 0.0f;
      this->yaw = 0.0f;
    } else if (rosidl_runtime_cpp::MessageInitialization::ZERO == _init) {
      this->surge = 0.0f;
      this->yaw = 0.0f;
    }
  }

  // field types and members
  using _surge_type =
    float;
  _surge_type surge;
  using _yaw_type =
    float;
  _yaw_type yaw;

  // setters for named parameter idiom
  Type & set__surge(
    const float & _arg)
  {
    this->surge = _arg;
    return *this;
  }
  Type & set__yaw(
    const float & _arg)
  {
    this->yaw = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    path_following_interfaces::srv::InitValues_Response_<ContainerAllocator> *;
  using ConstRawPtr =
    const path_following_interfaces::srv::InitValues_Response_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<path_following_interfaces::srv::InitValues_Response_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<path_following_interfaces::srv::InitValues_Response_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      path_following_interfaces::srv::InitValues_Response_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<path_following_interfaces::srv::InitValues_Response_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      path_following_interfaces::srv::InitValues_Response_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<path_following_interfaces::srv::InitValues_Response_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<path_following_interfaces::srv::InitValues_Response_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<path_following_interfaces::srv::InitValues_Response_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__path_following_interfaces__srv__InitValues_Response
    std::shared_ptr<path_following_interfaces::srv::InitValues_Response_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__path_following_interfaces__srv__InitValues_Response
    std::shared_ptr<path_following_interfaces::srv::InitValues_Response_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const InitValues_Response_ & other) const
  {
    if (this->surge != other.surge) {
      return false;
    }
    if (this->yaw != other.yaw) {
      return false;
    }
    return true;
  }
  bool operator!=(const InitValues_Response_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct InitValues_Response_

// alias to use template instance with default allocator
using InitValues_Response =
  path_following_interfaces::srv::InitValues_Response_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace path_following_interfaces

namespace path_following_interfaces
{

namespace srv
{

struct InitValues
{
  using Request = path_following_interfaces::srv::InitValues_Request;
  using Response = path_following_interfaces::srv::InitValues_Response;
};

}  // namespace srv

}  // namespace path_following_interfaces

#endif  // PATH_FOLLOWING_INTERFACES__SRV__DETAIL__INIT_VALUES__STRUCT_HPP_
