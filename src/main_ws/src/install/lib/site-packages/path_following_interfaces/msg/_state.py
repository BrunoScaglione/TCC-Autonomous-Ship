# generated from rosidl_generator_py/resource/_idl.py.em
# with input from path_following_interfaces:msg\State.idl
# generated code does not contain a copyright notice


# Import statements for member types

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_State(type):
    """Metaclass of message 'State'."""

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
                'path_following_interfaces.msg.State')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__msg__state
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__msg__state
            cls._CONVERT_TO_PY = module.convert_to_py_msg__msg__state
            cls._TYPE_SUPPORT = module.type_support_msg__msg__state
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__msg__state

            from path_following_interfaces.msg import Position
            if Position.__class__._TYPE_SUPPORT is None:
                Position.__class__.__import_type_support__()

            from path_following_interfaces.msg import Velocity
            if Velocity.__class__._TYPE_SUPPORT is None:
                Velocity.__class__.__import_type_support__()

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
            'TIME__DEFAULT': 0.0,
        }

    @property
    def TIME__DEFAULT(cls):
        """Return default value for message field 'time'."""
        return 0.0


class State(metaclass=Metaclass_State):
    """Message class 'State'."""

    __slots__ = [
        '_position',
        '_velocity',
        '_time',
    ]

    _fields_and_field_types = {
        'position': 'path_following_interfaces/Position',
        'velocity': 'path_following_interfaces/Velocity',
        'time': 'float',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.NamespacedType(['path_following_interfaces', 'msg'], 'Position'),  # noqa: E501
        rosidl_parser.definition.NamespacedType(['path_following_interfaces', 'msg'], 'Velocity'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        from path_following_interfaces.msg import Position
        self.position = kwargs.get('position', Position())
        from path_following_interfaces.msg import Velocity
        self.velocity = kwargs.get('velocity', Velocity())
        self.time = kwargs.get(
            'time', State.TIME__DEFAULT)

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
        if self.time != other.time:
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
            from path_following_interfaces.msg import Position
            assert \
                isinstance(value, Position), \
                "The 'position' field must be a sub message of type 'Position'"
        self._position = value

    @property
    def velocity(self):
        """Message field 'velocity'."""
        return self._velocity

    @velocity.setter
    def velocity(self, value):
        if __debug__:
            from path_following_interfaces.msg import Velocity
            assert \
                isinstance(value, Velocity), \
                "The 'velocity' field must be a sub message of type 'Velocity'"
        self._velocity = value

    @property
    def time(self):
        """Message field 'time'."""
        return self._time

    @time.setter
    def time(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'time' field must be of type 'float'"
        self._time = value
