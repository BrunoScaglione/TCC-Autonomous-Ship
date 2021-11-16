// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from path_following_interfaces:msg\Position.idl
// generated code does not contain a copyright notice

#ifndef PATH_FOLLOWING_INTERFACES__MSG__DETAIL__POSITION__STRUCT_HPP_
#define PATH_FOLLOWING_INTERFACES__MSG__DETAIL__POSITION__STRUCT_HPP_

#include <rosidl_runtime_cpp/bounded_vector.hpp>
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>


#ifndef _WIN32
# define DEPRECATED__path_following_interfaces__msg__Position __attribute__((deprecated))
#else
# define DEPRECATED__path_following_interfaces__msg__Position __declspec(deprecated)
#endif

namespace path_following_interfaces
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct Position_
{
  using Type = Position_<ContainerAllocator>;

  explicit Position_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::DEFAULTS_ONLY == _init)
    {
      this->x = 0.0f;
      this->y = 0.0f;
      this->theta = 1.57079632679f;
    } else if (rosidl_runtime_cpp::MessageInitialization::ZERO == _init) {
      this->x = 0.0f;
      this->y = 0.0f;
      this->theta = 0.0f;
    }
  }

  explicit Position_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::DEFAULTS_ONLY == _init)
    {
      this->x = 0.0f;
      this->y = 0.0f;
      this->theta = 1.57079632679f;
    } else if (rosidl_runtime_cpp::MessageInitialization::ZERO == _init) {
      this->x = 0.0f;
      this->y = 0.0f;
      this->theta = 0.0f;
    }
  }

  // field types and members
  using _x_type =
    float;
  _x_type x;
  using _y_type =
    float;
  _y_type y;
  using _theta_type =
    float;
  _theta_type theta;

  // setters for named parameter idiom
  Type & set__x(
    const float & _arg)
  {
    this->x = _arg;
    return *this;
  }
  Type & set__y(
    const float & _arg)
  {
    this->y = _arg;
    return *this;
  }
  Type & set__theta(
    const float & _arg)
  {
    this->theta = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    path_following_interfaces::msg::Position_<ContainerAllocator> *;
  using ConstRawPtr =
    const path_following_interfaces::msg::Position_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<path_following_interfaces::msg::Position_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<path_following_interfaces::msg::Position_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      path_following_interfaces::msg::Position_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<path_following_interfaces::msg::Position_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      path_following_interfaces::msg::Position_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<path_following_interfaces::msg::Position_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<path_following_interfaces::msg::Position_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<path_following_interfaces::msg::Position_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__path_following_interfaces__msg__Position
    std::shared_ptr<path_following_interfaces::msg::Position_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__path_following_interfaces__msg__Position
    std::shared_ptr<path_following_interfaces::msg::Position_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const Position_ & other) const
  {
    if (this->x != other.x) {
      return false;
    }
    if (this->y != other.y) {
      return false;
    }
    if (this->theta != other.theta) {
      return false;
    }
    return true;
  }
  bool operator!=(const Position_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct Position_

// alias to use template instance with default allocator
using Position =
  path_following_interfaces::msg::Position_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace path_following_interfaces

#endif  // PATH_FOLLOWING_INTERFACES__MSG__DETAIL__POSITION__STRUCT_HPP_
