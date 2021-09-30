# generated from rosidl_generator_py/resource/_idl.py.em
# with input from path_following_interfaces:msg\Velocity.idl
# generated code does not contain a copyright notice


# Import statements for member types

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_Velocity(type):
    """Metaclass of message 'Velocity'."""

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
                'path_following_interfaces.msg.Velocity')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__msg__velocity
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__msg__velocity
            cls._CONVERT_TO_PY = module.convert_to_py_msg__msg__velocity
            cls._TYPE_SUPPORT = module.type_support_msg__msg__velocity
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__msg__velocity

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
            'U__DEFAULT': 0.0,
            'V__DEFAULT': 0.0,
            'R__DEFAULT': 0.0,
        }

    @property
    def U__DEFAULT(cls):
        """Return default value for message field 'u'."""
        return 0.0

    @property
    def V__DEFAULT(cls):
        """Return default value for message field 'v'."""
        return 0.0

    @property
    def R__DEFAULT(cls):
        """Return default value for message field 'r'."""
        return 0.0


class Velocity(metaclass=Metaclass_Velocity):
    """Message class 'Velocity'."""

    __slots__ = [
        '_u',
        '_v',
        '_r',
    ]

    _fields_and_field_types = {
        'u': 'float',
        'v': 'float',
        'r': 'float',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        self.u = kwargs.get(
            'u', Velocity.U__DEFAULT)
        self.v = kwargs.get(
            'v', Velocity.V__DEFAULT)
        self.r = kwargs.get(
            'r', Velocity.R__DEFAULT)

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
        if self.u != other.u:
            return False
        if self.v != other.v:
            return False
        if self.r != other.r:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @property
    def u(self):
        """Message field 'u'."""
        return self._u

    @u.setter
    def u(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'u' field must be of type 'float'"
        self._u = value

    @property
    def v(self):
        """Message field 'v'."""
        return self._v

    @v.setter
    def v(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'v' field must be of type 'float'"
        self._v = value

    @property
    def r(self):
        """Message field 'r'."""
        return self._r

    @r.setter
    def r(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'r' field must be of type 'float'"
        self._r = value
