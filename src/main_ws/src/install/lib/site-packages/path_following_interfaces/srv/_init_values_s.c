// generated from rosidl_generator_py/resource/_idl_support.c.em
// with input from path_following_interfaces:srv\InitValues.idl
// generated code does not contain a copyright notice
#define NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION
#include <Python.h>
#include <stdbool.h>
#ifndef _WIN32
# pragma GCC diagnostic push
# pragma GCC diagnostic ignored "-Wunused-function"
#endif
#include "numpy/ndarrayobject.h"
#ifndef _WIN32
# pragma GCC diagnostic pop
#endif
#include "rosidl_runtime_c/visibility_control.h"
#include "path_following_interfaces/srv/detail/init_values__struct.h"
#include "path_following_interfaces/srv/detail/init_values__functions.h"

bool path_following_interfaces__msg__state__convert_from_py(PyObject * _pymsg, void * _ros_message);
PyObject * path_following_interfaces__msg__state__convert_to_py(void * raw_ros_message);
bool path_following_interfaces__msg__waypoints__convert_from_py(PyObject * _pymsg, void * _ros_message);
PyObject * path_following_interfaces__msg__waypoints__convert_to_py(void * raw_ros_message);

ROSIDL_GENERATOR_C_EXPORT
bool path_following_interfaces__srv__init_values__request__convert_from_py(PyObject * _pymsg, void * _ros_message)
{
  // check that the passed message is of the expected Python class
  {
    char full_classname_dest[62];
    {
      char * class_name = NULL;
      char * module_name = NULL;
      {
        PyObject * class_attr = PyObject_GetAttrString(_pymsg, "__class__");
        if (class_attr) {
          PyObject * name_attr = PyObject_GetAttrString(class_attr, "__name__");
          if (name_attr) {
            class_name = (char *)PyUnicode_1BYTE_DATA(name_attr);
            Py_DECREF(name_attr);
          }
          PyObject * module_attr = PyObject_GetAttrString(class_attr, "__module__");
          if (module_attr) {
            module_name = (char *)PyUnicode_1BYTE_DATA(module_attr);
            Py_DECREF(module_attr);
          }
          Py_DECREF(class_attr);
        }
      }
      if (!class_name || !module_name) {
        return false;
      }
      snprintf(full_classname_dest, sizeof(full_classname_dest), "%s.%s", module_name, class_name);
    }
    assert(strncmp("path_following_interfaces.srv._init_values.InitValues_Request", full_classname_dest, 61) == 0);
  }
  path_following_interfaces__srv__InitValues_Request * ros_message = _ros_message;
  {  // initial_state
    PyObject * field = PyObject_GetAttrString(_pymsg, "initial_state");
    if (!field) {
      return false;
    }
    if (!path_following_interfaces__msg__state__convert_from_py(field, &ros_message->initial_state)) {
      Py_DECREF(field);
      return false;
    }
    Py_DECREF(field);
  }
  {  // waypoints
    PyObject * field = PyObject_GetAttrString(_pymsg, "waypoints");
    if (!field) {
      return false;
    }
    if (!path_following_interfaces__msg__waypoints__convert_from_py(field, &ros_message->waypoints)) {
      Py_DECREF(field);
      return false;
    }
    Py_DECREF(field);
  }
  {  // surge
    PyObject * field = PyObject_GetAttrString(_pymsg, "surge");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->surge = (float)PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // yaw
    PyObject * field = PyObject_GetAttrString(_pymsg, "yaw");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->yaw = (float)PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }

  return true;
}

ROSIDL_GENERATOR_C_EXPORT
PyObject * path_following_interfaces__srv__init_values__request__convert_to_py(void * raw_ros_message)
{
  /* NOTE(esteve): Call constructor of InitValues_Request */
  PyObject * _pymessage = NULL;
  {
    PyObject * pymessage_module = PyImport_ImportModule("path_following_interfaces.srv._init_values");
    assert(pymessage_module);
    PyObject * pymessage_class = PyObject_GetAttrString(pymessage_module, "InitValues_Request");
    assert(pymessage_class);
    Py_DECREF(pymessage_module);
    _pymessage = PyObject_CallObject(pymessage_class, NULL);
    Py_DECREF(pymessage_class);
    if (!_pymessage) {
      return NULL;
    }
  }
  path_following_interfaces__srv__InitValues_Request * ros_message = (path_following_interfaces__srv__InitValues_Request *)raw_ros_message;
  {  // initial_state
    PyObject * field = NULL;
    field = path_following_interfaces__msg__state__convert_to_py(&ros_message->initial_state);
    if (!field) {
      return NULL;
    }
    {
      int rc = PyObject_SetAttrString(_pymessage, "initial_state", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // waypoints
    PyObject * field = NULL;
    field = path_following_interfaces__msg__waypoints__convert_to_py(&ros_message->waypoints);
    if (!field) {
      return NULL;
    }
    {
      int rc = PyObject_SetAttrString(_pymessage, "waypoints", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // surge
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->surge);
    {
      int rc = PyObject_SetAttrString(_pymessage, "surge", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // yaw
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->yaw);
    {
      int rc = PyObject_SetAttrString(_pymessage, "yaw", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }

  // ownership of _pymessage is transferred to the caller
  return _pymessage;
}

#define NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION
// already included above
// #include <Python.h>
// already included above
// #include <stdbool.h>
// already included above
// #include "numpy/ndarrayobject.h"
// already included above
// #include "rosidl_runtime_c/visibility_control.h"
// already included above
// #include "path_following_interfaces/srv/detail/init_values__struct.h"
// already included above
// #include "path_following_interfaces/srv/detail/init_values__functions.h"


ROSIDL_GENERATOR_C_EXPORT
bool path_following_interfaces__srv__init_values__response__convert_from_py(PyObject * _pymsg, void * _ros_message)
{
  // check that the passed message is of the expected Python class
  {
    char full_classname_dest[63];
    {
      char * class_name = NULL;
      char * module_name = NULL;
      {
        PyObject * class_attr = PyObject_GetAttrString(_pymsg, "__class__");
        if (class_attr) {
          PyObject * name_attr = PyObject_GetAttrString(class_attr, "__name__");
          if (name_attr) {
            class_name = (char *)PyUnicode_1BYTE_DATA(name_attr);
            Py_DECREF(name_attr);
          }
          PyObject * module_attr = PyObject_GetAttrString(class_attr, "__module__");
          if (module_attr) {
            module_name = (char *)PyUnicode_1BYTE_DATA(module_attr);
            Py_DECREF(module_attr);
          }
          Py_DECREF(class_attr);
        }
      }
      if (!class_name || !module_name) {
        return false;
      }
      snprintf(full_classname_dest, sizeof(full_classname_dest), "%s.%s", module_name, class_name);
    }
    assert(strncmp("path_following_interfaces.srv._init_values.InitValues_Response", full_classname_dest, 62) == 0);
  }
  path_following_interfaces__srv__InitValues_Response * ros_message = _ros_message;
  {  // surge
    PyObject * field = PyObject_GetAttrString(_pymsg, "surge");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->surge = (float)PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // yaw
    PyObject * field = PyObject_GetAttrString(_pymsg, "yaw");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->yaw = (float)PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }

  return true;
}

ROSIDL_GENERATOR_C_EXPORT
PyObject * path_following_interfaces__srv__init_values__response__convert_to_py(void * raw_ros_message)
{
  /* NOTE(esteve): Call constructor of InitValues_Response */
  PyObject * _pymessage = NULL;
  {
    PyObject * pymessage_module = PyImport_ImportModule("path_following_interfaces.srv._init_values");
    assert(pymessage_module);
    PyObject * pymessage_class = PyObject_GetAttrString(pymessage_module, "InitValues_Response");
    assert(pymessage_class);
    Py_DECREF(pymessage_module);
    _pymessage = PyObject_CallObject(pymessage_class, NULL);
    Py_DECREF(pymessage_class);
    if (!_pymessage) {
      return NULL;
    }
  }
  path_following_interfaces__srv__InitValues_Response * ros_message = (path_following_interfaces__srv__InitValues_Response *)raw_ros_message;
  {  // surge
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->surge);
    {
      int rc = PyObject_SetAttrString(_pymessage, "surge", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // yaw
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->yaw);
    {
      int rc = PyObject_SetAttrString(_pymessage, "yaw", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }

  // ownership of _pymessage is transferred to the caller
  return _pymessage;
}
