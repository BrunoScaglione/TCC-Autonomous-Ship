# generated from rosidl_generator_py/resource/_idl.py.em
# with input from path_following_interfaces:srv\StartEndSimul.idl
# generated code does not contain a copyright notice


# Import statements for member types

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_StartEndSimul_Request(type):
    """Metaclass of message 'StartEndSimul_Request'."""

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
                'path_following_interfaces.srv.StartEndSimul_Request')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__srv__start_end_simul__request
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__srv__start_end_simul__request
            cls._CONVERT_TO_PY = module.convert_to_py_msg__srv__start_end_simul__request
            cls._TYPE_SUPPORT = module.type_support_msg__srv__start_end_simul__request
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__srv__start_end_simul__request

            from path_following_interfaces.msg import State
            if State.__class__._TYPE_SUPPORT is None:
                State.__class__.__import_type_support__()

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
            'END_SIMUL__DEFAULT': False,
        }

    @property
    def END_SIMUL__DEFAULT(cls):
        """Return default value for message field 'end_simul'."""
        return False


class StartEndSimul_Request(metaclass=Metaclass_StartEndSimul_Request):
    """Message class 'StartEndSimul_Request'."""

    __slots__ = [
        '_initial_state',
        '_end_simul',
    ]

    _fields_and_field_types = {
        'initial_state': 'path_following_interfaces/State',
        'end_simul': 'boolean',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.NamespacedType(['path_following_interfaces', 'msg'], 'State'),  # noqa: E501
        rosidl_parser.definition.BasicType('boolean'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        from path_following_interfaces.msg import State
        self.initial_state = kwargs.get('initial_state', State())
        self.end_simul = kwargs.get(
            'end_simul', StartEndSimul_Request.END_SIMUL__DEFAULT)

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
        if self.end_simul != other.end_simul:
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
    def end_simul(self):
        """Message field 'end_simul'."""
        return self._end_simul

    @end_simul.setter
    def end_simul(self, value):
        if __debug__:
            assert \
                isinstance(value, bool), \
                "The 'end_simul' field must be of type 'bool'"
        self._end_simul = value


# Import statements for member types

# already imported above
# import rosidl_parser.definition


class Metaclass_StartEndSimul_Response(type):
    """Metaclass of message 'StartEndSimul_Response'."""

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
                'path_following_interfaces.srv.StartEndSimul_Response')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__srv__start_end_simul__response
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__srv__start_end_simul__response
            cls._CONVERT_TO_PY = module.convert_to_py_msg__srv__start_end_simul__response
            cls._TYPE_SUPPORT = module.type_support_msg__srv__start_end_simul__response
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__srv__start_end_simul__response

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class StartEndSimul_Response(metaclass=Metaclass_StartEndSimul_Response):
    """Message class 'StartEndSimul_Response'."""

    __slots__ = [
        '_reporting',
    ]

    _fields_and_field_types = {
        'reporting': 'string',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.UnboundedString(),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        self.reporting = kwargs.get('reporting', str())

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
        if self.reporting != other.reporting:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @property
    def reporting(self):
        """Message field 'reporting'."""
        return self._reporting

    @reporting.setter
    def reporting(self, value):
        if __debug__:
            assert \
                isinstance(value, str), \
                "The 'reporting' field must be of type 'str'"
        self._reporting = value


class Metaclass_StartEndSimul(type):
    """Metaclass of service 'StartEndSimul'."""

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
                'path_following_interfaces.srv.StartEndSimul')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._TYPE_SUPPORT = module.type_support_srv__srv__start_end_simul

            from path_following_interfaces.srv import _start_end_simul
            if _start_end_simul.Metaclass_StartEndSimul_Request._TYPE_SUPPORT is None:
                _start_end_simul.Metaclass_StartEndSimul_Request.__import_type_support__()
            if _start_end_simul.Metaclass_StartEndSimul_Response._TYPE_SUPPORT is None:
                _start_end_simul.Metaclass_StartEndSimul_Response.__import_type_support__()


class StartEndSimul(metaclass=Metaclass_StartEndSimul):
    from path_following_interfaces.srv._start_end_simul import StartEndSimul_Request as Request
    from path_following_interfaces.srv._start_end_simul import StartEndSimul_Response as Response

    def __init__(self):
        raise NotImplementedError('Service classes can not be instantiated')
