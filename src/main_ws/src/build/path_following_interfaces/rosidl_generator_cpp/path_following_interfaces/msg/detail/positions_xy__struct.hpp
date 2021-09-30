// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from path_following_interfaces:msg\PositionsXY.idl
// generated code does not contain a copyright notice

#ifndef PATH_FOLLOWING_INTERFACES__MSG__DETAIL__POSITIONS_XY__STRUCT_HPP_
#define PATH_FOLLOWING_INTERFACES__MSG__DETAIL__POSITIONS_XY__STRUCT_HPP_

#include <rosidl_runtime_cpp/bounded_vector.hpp>
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>


#ifndef _WIN32
# define DEPRECATED__path_following_interfaces__msg__PositionsXY __attribute__((deprecated))
#else
# define DEPRECATED__path_following_interfaces__msg__PositionsXY __declspec(deprecated)
#endif

namespace path_following_interfaces
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct PositionsXY_
{
  using Type = PositionsXY_<ContainerAllocator>;

  explicit PositionsXY_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_init;
  }

  explicit PositionsXY_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_init;
    (void)_alloc;
  }

  // field types and members
  using _x_type =
    std::vector<float, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<float>>;
  _x_type x;
  using _y_type =
    std::vector<float, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<float>>;
  _y_type y;

  // setters for named parameter idiom
  Type & set__x(
    const std::vector<float, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<float>> & _arg)
  {
    this->x = _arg;
    return *this;
  }
  Type & set__y(
    const std::vector<float, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<float>> & _arg)
  {
    this->y = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    path_following_interfaces::msg::PositionsXY_<ContainerAllocator> *;
  using ConstRawPtr =
    const path_following_interfaces::msg::PositionsXY_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<path_following_interfaces::msg::PositionsXY_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<path_following_interfaces::msg::PositionsXY_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      path_following_interfaces::msg::PositionsXY_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<path_following_interfaces::msg::PositionsXY_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      path_following_interfaces::msg::PositionsXY_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<path_following_interfaces::msg::PositionsXY_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<path_following_interfaces::msg::PositionsXY_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<path_following_interfaces::msg::PositionsXY_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__path_following_interfaces__msg__PositionsXY
    std::shared_ptr<path_following_interfaces::msg::PositionsXY_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__path_following_interfaces__msg__PositionsXY
    std::shared_ptr<path_following_interfaces::msg::PositionsXY_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const PositionsXY_ & other) const
  {
    if (this->x != other.x) {
      return false;
    }
    if (this->y != other.y) {
      return false;
    }
    return true;
  }
  bool operator!=(const PositionsXY_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct PositionsXY_

// alias to use template instance with default allocator
using PositionsXY =
  path_following_interfaces::msg::PositionsXY_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace path_following_interfaces

#endif  // PATH_FOLLOWING_INTERFACES__MSG__DETAIL__POSITIONS_XY__STRUCT_HPP_
