#----------------------------------------------------------------
# Generated CMake target import file for configuration "RelWithDebInfo".
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "path_following_interfaces::path_following_interfaces__rosidl_typesupport_cpp" for configuration "RelWithDebInfo"
set_property(TARGET path_following_interfaces::path_following_interfaces__rosidl_typesupport_cpp APPEND PROPERTY IMPORTED_CONFIGURATIONS RELWITHDEBINFO)
set_target_properties(path_following_interfaces::path_following_interfaces__rosidl_typesupport_cpp PROPERTIES
  IMPORTED_IMPLIB_RELWITHDEBINFO "${_IMPORT_PREFIX}/lib/path_following_interfaces__rosidl_typesupport_cpp.lib"
  IMPORTED_LOCATION_RELWITHDEBINFO "${_IMPORT_PREFIX}/bin/path_following_interfaces__rosidl_typesupport_cpp.dll"
  )

list(APPEND _IMPORT_CHECK_TARGETS path_following_interfaces::path_following_interfaces__rosidl_typesupport_cpp )
list(APPEND _IMPORT_CHECK_FILES_FOR_path_following_interfaces::path_following_interfaces__rosidl_typesupport_cpp "${_IMPORT_PREFIX}/lib/path_following_interfaces__rosidl_typesupport_cpp.lib" "${_IMPORT_PREFIX}/bin/path_following_interfaces__rosidl_typesupport_cpp.dll" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
