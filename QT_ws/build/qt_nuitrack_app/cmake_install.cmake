# Install script for directory: /home/jennie/irecheck/iReCheck/QT_ws/src/qt_nuitrack_app

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/home/jennie/irecheck/iReCheck/QT_ws/install")
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
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/qt_nuitrack_app/msg" TYPE FILE FILES
    "/home/jennie/irecheck/iReCheck/QT_ws/src/qt_nuitrack_app/msg/FaceInfo.msg"
    "/home/jennie/irecheck/iReCheck/QT_ws/src/qt_nuitrack_app/msg/Faces.msg"
    "/home/jennie/irecheck/iReCheck/QT_ws/src/qt_nuitrack_app/msg/GestureInfo.msg"
    "/home/jennie/irecheck/iReCheck/QT_ws/src/qt_nuitrack_app/msg/Gestures.msg"
    "/home/jennie/irecheck/iReCheck/QT_ws/src/qt_nuitrack_app/msg/HandInfo.msg"
    "/home/jennie/irecheck/iReCheck/QT_ws/src/qt_nuitrack_app/msg/Hands.msg"
    "/home/jennie/irecheck/iReCheck/QT_ws/src/qt_nuitrack_app/msg/JointInfo.msg"
    "/home/jennie/irecheck/iReCheck/QT_ws/src/qt_nuitrack_app/msg/SkeletonInfo.msg"
    "/home/jennie/irecheck/iReCheck/QT_ws/src/qt_nuitrack_app/msg/Skeletons.msg"
    )
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/qt_nuitrack_app/cmake" TYPE FILE FILES "/home/jennie/irecheck/iReCheck/QT_ws/build/qt_nuitrack_app/catkin_generated/installspace/qt_nuitrack_app-msg-paths.cmake")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include" TYPE DIRECTORY FILES "/home/jennie/irecheck/iReCheck/QT_ws/devel/include/qt_nuitrack_app")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/roseus/ros" TYPE DIRECTORY FILES "/home/jennie/irecheck/iReCheck/QT_ws/devel/share/roseus/ros/qt_nuitrack_app")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/common-lisp/ros" TYPE DIRECTORY FILES "/home/jennie/irecheck/iReCheck/QT_ws/devel/share/common-lisp/ros/qt_nuitrack_app")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/gennodejs/ros" TYPE DIRECTORY FILES "/home/jennie/irecheck/iReCheck/QT_ws/devel/share/gennodejs/ros/qt_nuitrack_app")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  execute_process(COMMAND "/usr/bin/python2" -m compileall "/home/jennie/irecheck/iReCheck/QT_ws/devel/lib/python2.7/dist-packages/qt_nuitrack_app")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/python2.7/dist-packages" TYPE DIRECTORY FILES "/home/jennie/irecheck/iReCheck/QT_ws/devel/lib/python2.7/dist-packages/qt_nuitrack_app")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/pkgconfig" TYPE FILE FILES "/home/jennie/irecheck/iReCheck/QT_ws/build/qt_nuitrack_app/catkin_generated/installspace/qt_nuitrack_app.pc")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/qt_nuitrack_app/cmake" TYPE FILE FILES "/home/jennie/irecheck/iReCheck/QT_ws/build/qt_nuitrack_app/catkin_generated/installspace/qt_nuitrack_app-msg-extras.cmake")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/qt_nuitrack_app/cmake" TYPE FILE FILES
    "/home/jennie/irecheck/iReCheck/QT_ws/build/qt_nuitrack_app/catkin_generated/installspace/qt_nuitrack_appConfig.cmake"
    "/home/jennie/irecheck/iReCheck/QT_ws/build/qt_nuitrack_app/catkin_generated/installspace/qt_nuitrack_appConfig-version.cmake"
    )
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/qt_nuitrack_app" TYPE FILE FILES "/home/jennie/irecheck/iReCheck/QT_ws/src/qt_nuitrack_app/package.xml")
endif()

