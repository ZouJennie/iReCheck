execute_process(COMMAND "/home/jennie/irecheck/iReCheck/qtrobot_ws/build_isolated/moveit_ros_planning_interface/catkin_generated/python_distutils_install.sh" RESULT_VARIABLE res)

if(NOT res EQUAL 0)
  message(FATAL_ERROR "execute_process(/home/jennie/irecheck/iReCheck/qtrobot_ws/build_isolated/moveit_ros_planning_interface/catkin_generated/python_distutils_install.sh) returned error code ")
endif()
