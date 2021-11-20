# generated from rosidl_generator_py/resource/_idl.py.em
# with input from path_following_interfaces:srv\InitValues.idl
# generated code does not contain a copyright notice


# Import statements for member types

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_InitValues_Request(type):
    """Metaclass of message 'InitValues_Request'."""

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
                'path_following_interfaces.srv.InitValues_Request')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__srv__init_values__request
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__srv__init_values__request
            cls._CONVERT_TO_PY = module.convert_to_py_msg__srv__init_values__request
            cls._TYPE_SUPPORT = module.type_support_msg__srv__init_values__request
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__srv__init_values__request

            from path_following_interfaces.msg import State
            if State.__class__._TYPE_SUPPORT is None:
                State.__class__.__import_type_support__()

            from path_following_interfaces.msg import Waypoints
            if Waypoints.__class__._TYPE_SUPPORT is None:
                Waypoints.__class__.__import_type_support__()

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
            'SURGE__DEFAULT': 0.0,
            'YAW__DEFAULT': 0.0,
        }

    @property
    def SURGE__DEFAULT(cls):
        """Return default value for message field 'surge'."""
        return 0.0

    @property
    def YAW__DEFAULT(cls):
        """Return default value for message field 'yaw'."""
        return 0.0


class InitValues_Request(metaclass=Metaclass_InitValues_Request):
    """Message class 'InitValues_Request'."""

    __slots__ = [
        '_initial_state',
        '_waypoints',
        '_surge',
        '_yaw',
    ]

    _fields_and_field_types = {
        'initial_state': 'path_following_interfaces/State',
        'waypoints': 'path_following_interfaces/Waypoints',
        'surge': 'float',
        'yaw': 'float',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.NamespacedType(['path_following_interfaces', 'msg'], 'State'),  # noqa: E501
        rosidl_parser.definition.NamespacedType(['path_following_interfaces', 'msg'], 'Waypoints'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        from path_following_interfaces.msg import State
        self.initial_state = kwargs.get('initial_state', State())
        from path_following_interfaces.msg import Waypoints
        self.waypoints = kwargs.get('waypoints', Waypoints())
        self.surge = kwargs.get(
            'surge', InitValues_Request.SURGE__DEFAULT)
        self.yaw = kwargs.get(
            'yaw', InitValues_Request.YAW__DEFAULT)

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
        if self.initial_state != other.initial_state:
            return False
        if self.waypoints != other.waypoints:
            return False
        if self.surge != other.surge:
            return False
        if self.yaw != other.yaw:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @property
    def initial_state(self):
        """Message field 'initial_state'."""
        return self._initial_state

    @initial_state.setter
    def initial_state(self, value):
        if __debug__:
            from path_following_interfaces.msg import State
            assert \
                isinstance(value, State), \
                "The 'initial_state' field must be a sub message of type 'State'"
        self._initial_state = value

    @property
    def waypoints(self):
        """Message field 'waypoints'."""
        return self._waypoints

    @waypoints.setter
    def waypoints(self, value):
        if __debug__:
            from path_following_interfaces.msg import Waypoints
            assert \
                isinstance(value, Waypoints), \
                "The 'waypoints' field must be a sub message of type 'Waypoints'"
        self._waypoints = value

    @property
    def surge(self):
        """Message field 'surge'."""
        return self._surge

    @surge.setter
    def surge(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'surge' field must be of type 'float'"
        self._surge = value

    @property
    def yaw(self):
        """Message field 'yaw'."""
        return self._yaw

    @yaw.setter
    def yaw(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'yaw' field must be of type 'float'"
        self._yaw = value


# Import statements for member types

# already imported above
# import rosidl_parser.definition


class Metaclass_InitValues_Response(type):
    """Metaclass of message 'InitValues_Response'."""

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
                'path_following_interfaces.srv.InitValues_Response')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__srv__init_values__response
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__srv__init_values__response
            cls._CONVERT_TO_PY = module.convert_to_py_msg__srv__init_values__response
            cls._TYPE_SUPPORT = module.type_support_msg__srv__init_values__response
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__srv__init_values__response

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
            'SURGE__DEFAULT': 0.0,
            'YAW__DEFAULT': 0.0,
        }

    @property
    def SURGE__DEFAULT(cls):
        """Return default value for message field 'surge'."""
        return 0.0

    @property
    def YAW__DEFAULT(cls):
        """Return default value for message field 'yaw'."""
        return 0.0


class InitValues_Response(metaclass=Metaclass_InitValues_Response):
    """Message class 'InitValues_Response'."""

    __slots__ = [
        '_surge',
        '_yaw',
    ]

    _fields_and_field_types = {
        'surge': 'float',
        'yaw': 'float',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        self.surge = kwargs.get(
            'surge', InitValues_Response.SURGE__DEFAULT)
        self.yaw = kwargs.get(
            'yaw', InitValues_Response.YAW__DEFAULT)

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
        if self.surge != other.surge:
            return False
        if self.yaw != other.yaw:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @property
    def surge(self):
        """Message field 'surge'."""
        return self._surge

    @surge.setter
    def surge(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'surge' field must be of type 'float'"
        self._surge = value

    @property
    def yaw(self):
        """Message field 'yaw'."""
        return self._yaw

    @yaw.setter
    def yaw(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'yaw' field must be of type 'float'"
        self._yaw = value


class Metaclass_InitValues(type):
    """Metaclass of service 'InitValues'."""

    _TYPE_SUPPORT = None

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('path_following_interfaces')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'path_following_interfaces.srv.InitValues')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._TYPE_SUPPORT = module.type_support_srv__srv__init_values

            from path_following_interfaces.srv import _init_values
            if _init_values.Metaclass_InitValues_Request._TYPE_SUPPORT is None:
                _init_values.Metaclass_InitValues_Request.__import_type_support__()
            if _init_values.Metaclass_InitValues_Response._TYPE_SUPPORT is None:
                _init_values.Metaclass_InitValues_Response.__import_type_support__()


class InitValues(metaclass=Metaclass_InitValues):
    from path_following_interfaces.srv._init_values import InitValues_Request as Request
    from path_following_interfaces.srv._init_values import InitValues_Response as Response

    def __init__(self):
        raise NotImplementedError('Service classes can not be instantiated')
