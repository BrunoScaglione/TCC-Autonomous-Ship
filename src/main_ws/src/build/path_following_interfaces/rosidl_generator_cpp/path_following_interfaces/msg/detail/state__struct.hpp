// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from path_following_interfaces:msg\State.idl
// generated code does not contain a copyright notice

#ifndef PATH_FOLLOWING_INTERFACES__MSG__DETAIL__STATE__STRUCT_HPP_
#define PATH_FOLLOWING_INTERFACES__MSG__DETAIL__STATE__STRUCT_HPP_

#include <rosidl_runtime_cpp/bounded_vector.hpp>
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>


// Include directives for member types
// Member 'position'
#include "path_following_interfaces/msg/detail/position__struct.hpp"
// Member 'velocity'
#include "path_following_interfaces/msg/detail/velocity__struct.hpp"

#ifndef _WIN32
# define DEPRECATED__path_following_interfaces__msg__State __attribute__((deprecated))
#else
# define DEPRECATED__path_following_interfaces__msg__State __declspec(deprecated)
#endif

namespace path_following_interfaces
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct State_
{
  using Type = State_<ContainerAllocator>;

  explicit State_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : position(_init),
    velocity(_init)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::DEFAULTS_ONLY == _init)
    {
      this->time = 0.0f;
    } else if (rosidl_runtime_cpp::MessageInitialization::ZERO == _init) {
      this->time = 0.0f;
    }
  }

  explicit State_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : position(_alloc, _init),
    velocity(_alloc, _init)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::DEFAULTS_ONLY == _init)
    {
      this->time = 0.0f;
    } else if (rosidl_runtime_cpp::MessageInitialization::ZERO == _init) {
      this->time = 0.0f;
    }
  }

  // field types and members
  using _position_type =
    path_following_interfaces::msg::Position_<ContainerAllocator>;
  _position_type position;
  using _velocity_type =
    path_following_interfaces::msg::Velocity_<ContainerAllocator>;
  _velocity_type velocity;
  using _time_type =
    float;
  _time_type time;

  // setters for named parameter idiom
  Type & set__position(
    const path_following_interfaces::msg::Position_<ContainerAllocator> & _arg)
  {
    this->position = _arg;
    return *this;
  }
  Type & set__velocity(
    const path_following_interfaces::msg::Velocity_<ContainerAllocator> & _arg)
  {
    this->velocity = _arg;
    return *this;
  }
  Type & set__time(
    const float & _arg)
  {
    this->time = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    path_following_interfaces::msg::State_<ContainerAllocator> *;
  using ConstRawPtr =
    const path_following_interfaces::msg::State_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<path_following_interfaces::msg::State_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<path_following_interfaces::msg::State_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      path_following_interfaces::msg::State_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<path_following_interfaces::msg::State_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      path_following_interfaces::msg::State_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<path_following_interfaces::msg::State_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<path_following_interfaces::msg::State_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<path_following_interfaces::msg::State_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__path_following_interfaces__msg__State
    std::shared_ptr<path_following_interfaces::msg::State_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__path_following_interfaces__msg__State
    std::shared_ptr<path_following_interfaces::msg::State_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const State_ & other) const
  {
    if (this->position != other.position) {
      return false;
    }
    if (this->velocity != other.velocity) {
      return false;
    }
    if (this->time != other.time) {
      return false;
    }
    return true;
  }
  bool operator!=(const State_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct State_

// alias to use template instance with default allocator
using State =
  path_following_interfaces::msg::State_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace path_following_interfaces

#endif  // PATH_FOLLOWING_INTERFACES__MSG__DETAIL__STATE__STRUCT_HPP_
