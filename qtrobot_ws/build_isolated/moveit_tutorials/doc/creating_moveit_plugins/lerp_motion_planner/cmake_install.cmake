# Install script for directory: /home/jennie/irecheck/iReCheck/qtrobot_ws/src/moveit_tutorials/doc/creating_moveit_plugins/lerp_motion_planner

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/home/jennie/irecheck/iReCheck/qtrobot_ws/install_isolated")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Install shared libraries without execute permission?
if(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  set(CMAKE_INSTALL_SO_NO_EXE "1")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  foreach(file
      "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libmoveit_lerp_planner_plugin.so.0.1.0"
      "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libmoveit_lerp_planner_plugin.so"
      )
    if(EXISTS "${file}" AND
       NOT IS_SYMLINK "${file}")
      file(RPATH_CHECK
           FILE "${file}"
           RPATH "")
    endif()
  endforeach()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib" TYPE SHARED_LIBRARY FILES
    "/home/jennie/irecheck/iReCheck/qtrobot_ws/devel_isolated/moveit_tutorials/lib/libmoveit_lerp_planner_plugin.so.0.1.0"
    "/home/jennie/irecheck/iReCheck/qtrobot_ws/devel_isolated/moveit_tutorials/lib/libmoveit_lerp_planner_plugin.so"
    )
  foreach(file
      "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libmoveit_lerp_planner_plugin.so.0.1.0"
      "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libmoveit_lerp_planner_plugin.so"
      )
    if(EXISTS "${file}" AND
       NOT IS_SYMLINK "${file}")
      file(RPATH_CHANGE
           FILE "${file}"
           OLD_RPATH "/home/jennie/irecheck/iReCheck/qtrobot_ws/devel_isolated/moveit_tutorials/lib:/home/jennie/irecheck/iReCheck/qtrobot_ws/devel_isolated/geometric_shapes/lib:/opt/ros/kinetic/lib:/home/jennie/irecheck/iReCheck/qtrobot_ws/devel_isolated/moveit_visual_tools/lib:/home/jennie/irecheck/iReCheck/qtrobot_ws/devel_isolated/rviz_visual_tools/lib:/home/jennie/irecheck/iReCheck/qtrobot_ws/devel_isolated/moveit_ros_planning_interface/lib:/home/jennie/irecheck/iReCheck/qtrobot_ws/devel_isolated/moveit_ros_warehouse/lib:/home/jennie/irecheck/iReCheck/qtrobot_ws/devel_isolated/moveit_ros_manipulation/lib:/home/jennie/irecheck/iReCheck/qtrobot_ws/devel_isolated/moveit_ros_move_group/lib:/home/jennie/irecheck/iReCheck/qtrobot_ws/devel_isolated/moveit_ros_planning/lib:/home/jennie/irecheck/iReCheck/qtrobot_ws/devel_isolated/moveit_ros_perception/lib:/home/jennie/irecheck/iReCheck/qtrobot_ws/devel_isolated/moveit_ros_occupancy_map_monitor/lib:/home/jennie/irecheck/iReCheck/qtrobot_ws/devel_isolated/moveit_core/lib:/usr/lib/x86_64-linux-gnu/hdf5/serial/lib:"
           NEW_RPATH "")
      if(CMAKE_INSTALL_DO_STRIP)
        execute_process(COMMAND "/usr/bin/strip" "${file}")
      endif()
    endif()
  endforeach()
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/moveit_tutorials" TYPE DIRECTORY FILES "/home/jennie/irecheck/iReCheck/qtrobot_ws/src/moveit_tutorials/doc/creating_moveit_plugins/lerp_motion_planner/include")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/moveit_tutorials" TYPE DIRECTORY FILES "/home/jennie/irecheck/iReCheck/qtrobot_ws/src/moveit_tutorials/doc/creating_moveit_plugins/lerp_motion_planner/launch")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/moveit_tutorials/doc/creating_moveit_plugins/lerp_motion_planner" TYPE FILE FILES "/home/jennie/irecheck/iReCheck/qtrobot_ws/src/moveit_tutorials/doc/creating_moveit_plugins/lerp_motion_planner/lerp_interface_plugin_description.xml")
endif()

