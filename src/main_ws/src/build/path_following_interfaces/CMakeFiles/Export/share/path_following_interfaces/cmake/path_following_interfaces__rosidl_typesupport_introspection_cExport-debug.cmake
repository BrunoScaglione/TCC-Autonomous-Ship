#----------------------------------------------------------------
# Generated CMake target import file for configuration "Debug".
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "path_following_interfaces::path_following_interfaces__rosidl_typesupport_introspection_c" for configuration "Debug"
set_property(TARGET path_following_interfaces::path_following_interfaces__rosidl_typesupport_introspection_c APPEND PROPERTY IMPORTED_CONFIGURATIONS DEBUG)
set_target_properties(path_following_interfaces::path_following_interfaces__rosidl_typesupport_introspection_c PROPERTIES
  IMPORTED_IMPLIB_DEBUG "${_IMPORT_PREFIX}/lib/path_following_interfaces__rosidl_typesupport_introspection_c.lib"
  IMPORTED_LOCATION_DEBUG "${_IMPORT_PREFIX}/bin/path_following_interfaces__rosidl_typesupport_introspection_c.dll"
  )

list(APPEND _IMPORT_CHECK_TARGETS path_following_interfaces::path_following_interfaces__rosidl_typesupport_introspection_c )
list(APPEND _IMPORT_CHECK_FILES_FOR_path_following_interfaces::path_following_interfaces__rosidl_typesupport_introspection_c "${_IMPORT_PREFIX}/lib/path_following_interfaces__rosidl_typesupport_introspection_c.lib" "${_IMPORT_PREFIX}/bin/path_following_interfaces__rosidl_typesupport_introspection_c.dll" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)