# generated from rosidl_generator_py/resource/_idl.py.em
# with input from path_following_interfaces:msg\PositionsXY.idl
# generated code does not contain a copyright notice


# Import statements for member types

# Member 'x'
# Member 'y'
import array  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_PositionsXY(type):
    """Metaclass of message 'PositionsXY'."""

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
                'path_following_interfaces.msg.PositionsXY')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__msg__positions_xy
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__msg__positions_xy
            cls._CONVERT_TO_PY = module.convert_to_py_msg__msg__positions_xy
            cls._TYPE_SUPPORT = module.type_support_msg__msg__positions_xy
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__msg__positions_xy

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
            'X__DEFAULT': array.array('f', (500.0, 1000.0, 1500.0, 2000.0, 2500.0, )),
            'Y__DEFAULT': array.array('f', (500.0, 1000.0, 1500.0, 2000.0, 2500.0, )),
        }

    @property
    def X__DEFAULT(cls):
        """Return default value for message field 'x'."""
        return array.array('f', (500.0, 1000.0, 1500.0, 2000.0, 2500.0, ))

    @property
    def Y__DEFAULT(cls):
        """Return default value for message field 'y'."""
        return array.array('f', (500.0, 1000.0, 1500.0, 2000.0, 2500.0, ))


class PositionsXY(metaclass=Metaclass_PositionsXY):
    """Message class 'PositionsXY'."""

    __slots__ = [
        '_x',
        '_y',
    ]

    _fields_and_field_types = {
        'x': 'sequence<float>',
        'y': 'sequence<float>',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.UnboundedSequence(rosidl_parser.definition.BasicType('float')),  # noqa: E501
        rosidl_parser.definition.UnboundedSequence(rosidl_parser.definition.BasicType('float')),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        self.x = kwargs.get(
            'x', PositionsXY.X__DEFAULT)
        self.y = kwargs.get(
            'y', PositionsXY.Y__DEFAULT)

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
        if self.x != other.x:
            return False
        if self.y != other.y:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @property
    def x(self):
        """Message field 'x'."""
        return self._x

    @x.setter
    def x(self, value):
        if isinstance(value, array.array):
            assert value.typecode == 'f', \
                "The 'x' array.array() must have the type code of 'f'"
            self._x = value
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
                "The 'x' field must be a set or sequence and each value of type 'float'"
        self._x = array.array('f', value)

    @property
    def y(self):
        """Message field 'y'."""
        return self._y

    @y.setter
    def y(self, value):
        if isinstance(value, array.array):
            assert value.typecode == 'f', \
                "The 'y' array.array() must have the type code of 'f'"
            self._y = value
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
                "The 'y' field must be a set or sequence and each value of type 'float'"
        self._y = array.array('f', value)
