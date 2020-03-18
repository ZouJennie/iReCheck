# Install script for directory: /home/jennie/irecheck/iReCheck/qtrobot_ws/src/moveit_tutorials/doc/kinematics

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
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/moveit_tutorials/ros_api_tutorial" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/moveit_tutorials/ros_api_tutorial")
    file(RPATH_CHECK
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/moveit_tutorials/ros_api_tutorial"
         RPATH "")
  endif()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/moveit_tutorials" TYPE EXECUTABLE FILES "/home/jennie/irecheck/iReCheck/qtrobot_ws/devel_isolated/moveit_tutorials/lib/moveit_tutorials/ros_api_tutorial")
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/moveit_tutorials/ros_api_tutorial" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/moveit_tutorials/ros_api_tutorial")
    file(RPATH_CHANGE
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/moveit_tutorials/ros_api_tutorial"
         OLD_RPATH "/home/jennie/irecheck/iReCheck/qtrobot_ws/devel_isolated/geometric_shapes/lib:/opt/ros/kinetic/lib:/home/jennie/irecheck/iReCheck/qtrobot_ws/devel_isolated/moveit_visual_tools/lib:/home/jennie/irecheck/iReCheck/qtrobot_ws/devel_isolated/rviz_visual_tools/lib:/home/jennie/irecheck/iReCheck/qtrobot_ws/devel_isolated/moveit_ros_planning_interface/lib:/home/jennie/irecheck/iReCheck/qtrobot_ws/devel_isolated/moveit_ros_warehouse/lib:/home/jennie/irecheck/iReCheck/qtrobot_ws/devel_isolated/moveit_ros_manipulation/lib:/home/jennie/irecheck/iReCheck/qtrobot_ws/devel_isolated/moveit_ros_move_group/lib:/home/jennie/irecheck/iReCheck/qtrobot_ws/devel_isolated/moveit_ros_planning/lib:/home/jennie/irecheck/iReCheck/qtrobot_ws/devel_isolated/moveit_ros_perception/lib:/home/jennie/irecheck/iReCheck/qtrobot_ws/devel_isolated/moveit_ros_occupancy_map_monitor/lib:/home/jennie/irecheck/iReCheck/qtrobot_ws/devel_isolated/moveit_core/lib:/usr/lib/x86_64-linux-gnu/hdf5/serial/lib:"
         NEW_RPATH "")
    if(CMAKE_INSTALL_DO_STRIP)
      execute_process(COMMAND "/usr/bin/strip" "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/moveit_tutorials/ros_api_tutorial")
    endif()
  endif()
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/moveit_tutorials" TYPE DIRECTORY FILES "/home/jennie/irecheck/iReCheck/qtrobot_ws/src/moveit_tutorials/doc/kinematics/launch")
endif()

