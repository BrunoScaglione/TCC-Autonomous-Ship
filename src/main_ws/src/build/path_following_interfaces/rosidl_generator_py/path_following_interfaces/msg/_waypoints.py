# generated from rosidl_generator_py/resource/_idl.py.em
# with input from path_following_interfaces:msg\Waypoints.idl
# generated code does not contain a copyright notice


# Import statements for member types

# Member 'velocity'
import array  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_Waypoints(type):
    """Metaclass of message 'Waypoints'."""

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
                'path_following_interfaces.msg.Waypoints')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__msg__waypoints
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__msg__waypoints
            cls._CONVERT_TO_PY = module.convert_to_py_msg__msg__waypoints
            cls._TYPE_SUPPORT = module.type_support_msg__msg__waypoints
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__msg__waypoints

            from path_following_interfaces.msg import PositionsXY
            if PositionsXY.__class__._TYPE_SUPPORT is None:
                PositionsXY.__class__.__import_type_support__()

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
            'VELOCITY__DEFAULT': array.array('f', (3.0, 3.5, 4.0, 4.5, 5.0, )),
        }

    @property
    def VELOCITY__DEFAULT(cls):
        """Return default value for message field 'velocity'."""
        return array.array('f', (3.0, 3.5, 4.0, 4.5, 5.0, ))


class Waypoints(metaclass=Metaclass_Waypoints):
    """Message class 'Waypoints'."""

    __slots__ = [
        '_position',
        '_velocity',
    ]

    _fields_and_field_types = {
        'position': 'path_following_interfaces/PositionsXY',
        'velocity': 'sequence<float>',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.NamespacedType(['path_following_interfaces', 'msg'], 'PositionsXY'),  # noqa: E501
        rosidl_parser.definition.UnboundedSequence(rosidl_parser.definition.BasicType('float')),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        from path_following_interfaces.msg import PositionsXY
        self.position = kwargs.get('position', PositionsXY())
        self.velocity = kwargs.get(
            'velocity', Waypoints.VELOCITY__DEFAULT)

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
        if self.position != other.position:
            return False
        if self.velocity != other.velocity:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @property
    def position(self):
        """Message field 'position'."""
        return self._position

    @position.setter
    def position(self, value):
        if __debug__:
            from path_following_interfaces.msg import PositionsXY
            assert \
                isinstance(value, PositionsXY), \
                "The 'position' field must be a sub message of type 'PositionsXY'"
        self._position = value

    @property
    def velocity(self):
        """Message field 'velocity'."""
        return self._velocity

    @velocity.setter
    def velocity(self, value):
        if isinstance(value, array.array):
            assert value.typecode == 'f', \
                "The 'velocity' array.array() must have the type code of 'f'"
            self._velocity = value
            return
        if __debug__:
            from collections.abc import Sequence
            from collections.abc import Set
            from collections import UserList
            from collections import UserString
            assert \
                ((isinstance(value, Sequence) or
                  isinstance(value, Set) or
                  isinstance(value, UserList)) and
                 not isinstance(value, str) and
                 not isinstance(value, UserString) and
                 all(isinstance(v, float) for v in value) and
                 True), \
                "The 'velocity' field must be a set or sequence and each value of type 'float'"
        self._velocity = array.array('f', value)