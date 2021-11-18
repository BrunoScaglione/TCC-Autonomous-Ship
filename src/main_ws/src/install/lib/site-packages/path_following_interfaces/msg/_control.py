# generated from rosidl_generator_py/resource/_idl.py.em
# with input from path_following_interfaces:msg\Control.idl
# generated code does not contain a copyright notice


# Import statements for member types

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_Control(type):
    """Metaclass of message 'Control'."""

    _CREATE_ROS_MESSAGE = None
    _CONVERT_FROM_PY = None
    _CONVERT_TO_PY = None
    _DESTROY_ROS_MESSAGE = None
    _TYPE_SUPPORT = None

    __constants = {
    }

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('path_following_interfaces')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'path_following_interfaces.msg.Control')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__msg__control
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__msg__control
            cls._CONVERT_TO_PY = module.convert_to_py_msg__msg__control
            cls._TYPE_SUPPORT = module.type_support_msg__msg__control
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__msg__control

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
            'DESIRED_VALUE__DEFAULT': 0.0,
            'DISTANCE_WAYPOINTS__DEFAULT': 707.0,
        }

    @property
    def DESIRED_VALUE__DEFAULT(cls):
        """Return default value for message field 'desired_value'."""
        return 0.0

    @property
    def DISTANCE_WAYPOINTS__DEFAULT(cls):
        """Return default value for message field 'distance_waypoints'."""
        return 707.0


class Control(metaclass=Metaclass_Control):
    """Message class 'Control'."""

    __slots__ = [
        '_desired_value',
        '_distance_waypoints',
    ]

    _fields_and_field_types = {
        'desired_value': 'float',
        'distance_waypoints': 'float',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        self.desired_value = kwargs.get(
            'desired_value', Control.DESIRED_VALUE__DEFAULT)
        self.distance_waypoints = kwargs.get(
            'distance_waypoints', Control.DISTANCE_WAYPOINTS__DEFAULT)

    def __repr__(self):
        typename = self.__class__.__module__.split('.')
        typename.pop()
        typename.append(self.__class__.__name__)
        args = []
        for s, t in zip(self.__slots__, self.SLOT_TYPES):
            field = getattr(self, s)
            fieldstr = repr(field)
            # We use Python array type for fields that can be directly stored
            # in them, and "normal" sequences for everything else.  If it is
            # a type that we store in an array, strip off the 'array' portion.
            if (
                isinstance(t, rosidl_parser.definition.AbstractSequence) and
                isinstance(t.value_type, rosidl_parser.definition.BasicType) and
                t.value_type.typename in ['float', 'double', 'int8', 'uint8', 'int16', 'uint16', 'int32', 'uint32', 'int64', 'uint64']
            ):
                if len(field) == 0:
                    fieldstr = '[]'
                else:
                    assert fieldstr.startswith('array(')
                    prefix = "array('X', "
                    suffix = ')'
                    fieldstr = fieldstr[len(prefix):-len(suffix)]
            args.append(s[1:] + '=' + fieldstr)
        return '%s(%s)' % ('.'.join(typename), ', '.join(args))

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        if self.desired_value != other.desired_value:
            return False
        if self.distance_waypoints != other.distance_waypoints:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @property
    def desired_value(self):
        """Message field 'desired_value'."""
        return self._desired_value

    @desired_value.setter
    def desired_value(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'desired_value' field must be of type 'float'"
        self._desired_value = value

    @property
    def distance_waypoints(self):
        """Message field 'distance_waypoints'."""
        return self._distance_waypoints

    @distance_waypoints.setter
    def distance_waypoints(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'distance_waypoints' field must be of type 'float'"
        self._distance_waypoints = value
