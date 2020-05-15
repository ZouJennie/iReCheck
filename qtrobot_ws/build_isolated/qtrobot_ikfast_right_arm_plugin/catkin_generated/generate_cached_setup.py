# -*- coding: utf-8 -*-
from __future__ import print_function
import argparse
import os
import stat
import sys

# find the import for catkin's python package - either from source space or from an installed underlay
if os.path.exists(os.path.join('/opt/ros/kinetic/share/catkin/cmake', 'catkinConfig.cmake.in')):
    sys.path.insert(0, os.path.join('/opt/ros/kinetic/share/catkin/cmake', '..', 'python'))
try:
    from catkin.environment_cache import generate_environment_script
except ImportError:
    # search for catkin package in all workspaces and prepend to path
    for workspace in "/home/jennie/irecheck/iReCheck/qtrobot_ws/devel_isolated/comportement_control;/home/jennie/irecheck/iReCheck/qtrobot_ws/devel_isolated/qtrobot_ikfast_right_arm_plugin;/home/jennie/irecheck/iReCheck/qtrobot_ws/devel_isolated/qtrobot_ikfast_left_arm_plugin;/home/jennie/irecheck/iReCheck/qtrobot_ws/devel_isolated/motors_moveit;/home/jennie/irecheck/iReCheck/qtrobot_ws/devel_isolated/left_arm_config;/home/jennie/irecheck/iReCheck/qtrobot_ws/devel_isolated/left_arm_description;/home/jennie/irecheck/iReCheck/qtrobot_ws/devel_isolated/moveit_tutorials;/home/jennie/irecheck/iReCheck/qtrobot_ws/devel_isolated/moveit_visual_tools;/home/jennie/irecheck/iReCheck/qtrobot_ws/devel_isolated/rviz_visual_tools;/home/jennie/irecheck/iReCheck/qtrobot_ws/devel_isolated/qtrobot_config;/home/jennie/irecheck/iReCheck/qtrobot_ws/devel_isolated/qt_control;/home/jennie/irecheck/iReCheck/qtrobot_ws/devel_isolated/panda_moveit_config;/home/jennie/irecheck/iReCheck/qtrobot_ws/devel_isolated/new_qt;/home/jennie/irecheck/iReCheck/qtrobot_ws/devel_isolated/moveit_ros_control_interface;/home/jennie/irecheck/iReCheck/qtrobot_ws/devel_isolated/moveit_simple_controller_manager;/home/jennie/irecheck/iReCheck/qtrobot_ws/devel_isolated/moveit_setup_assistant;/home/jennie/irecheck/iReCheck/qtrobot_ws/devel_isolated/moveit_runtime;/home/jennie/irecheck/iReCheck/qtrobot_ws/devel_isolated/moveit_ros_visualization;/home/jennie/irecheck/iReCheck/qtrobot_ws/devel_isolated/moveit_planners_chomp;/home/jennie/irecheck/iReCheck/qtrobot_ws/devel_isolated/moveit_jog_arm;/home/jennie/irecheck/iReCheck/qtrobot_ws/devel_isolated/moveit_ros_planning_interface;/home/jennie/irecheck/iReCheck/qtrobot_ws/devel_isolated/moveit_ros_benchmarks;/home/jennie/irecheck/iReCheck/qtrobot_ws/devel_isolated/moveit_ros_warehouse;/home/jennie/irecheck/iReCheck/qtrobot_ws/devel_isolated/moveit_ros_robot_interaction;/home/jennie/irecheck/iReCheck/qtrobot_ws/devel_isolated/moveit_ros_manipulation;/home/jennie/irecheck/iReCheck/qtrobot_ws/devel_isolated/moveit_ros_move_group;/home/jennie/irecheck/iReCheck/qtrobot_ws/devel_isolated/moveit_planners_ompl;/home/jennie/irecheck/iReCheck/qtrobot_ws/devel_isolated/moveit_kinematics;/home/jennie/irecheck/iReCheck/qtrobot_ws/devel_isolated/moveit_fake_controller_manager;/home/jennie/irecheck/iReCheck/qtrobot_ws/devel_isolated/moveit_ros_planning;/home/jennie/irecheck/iReCheck/qtrobot_ws/devel_isolated/moveit_ros_perception;/home/jennie/irecheck/iReCheck/qtrobot_ws/devel_isolated/moveit_ros_occupancy_map_monitor;/home/jennie/irecheck/iReCheck/qtrobot_ws/devel_isolated/moveit_ros;/home/jennie/irecheck/iReCheck/qtrobot_ws/devel_isolated/moveit_plugins;/home/jennie/irecheck/iReCheck/qtrobot_ws/devel_isolated/moveit_planners;/home/jennie/irecheck/iReCheck/qtrobot_ws/devel_isolated/moveit_chomp_optimizer_adapter;/home/jennie/irecheck/iReCheck/qtrobot_ws/devel_isolated/chomp_motion_planner;/home/jennie/irecheck/iReCheck/qtrobot_ws/devel_isolated/moveit_core;/home/jennie/irecheck/iReCheck/qtrobot_ws/devel_isolated/moveit_msgs;/home/jennie/irecheck/iReCheck/qtrobot_ws/devel_isolated/moveit_commander;/home/jennie/irecheck/iReCheck/qtrobot_ws/devel_isolated/moveit;/home/jennie/irecheck/iReCheck/qtrobot_ws/devel_isolated/geometric_shapes;/opt/ros/kinetic".split(';'):
        python_path = os.path.join(workspace, 'lib/python2.7/dist-packages')
        if os.path.isdir(os.path.join(python_path, 'catkin')):
            sys.path.insert(0, python_path)
            break
    from catkin.environment_cache import generate_environment_script

code = generate_environment_script('/home/jennie/irecheck/iReCheck/qtrobot_ws/devel_isolated/qtrobot_ikfast_right_arm_plugin/env.sh')

output_filename = '/home/jennie/irecheck/iReCheck/qtrobot_ws/build_isolated/qtrobot_ikfast_right_arm_plugin/catkin_generated/setup_cached.sh'
with open(output_filename, 'w') as f:
    #print('Generate script for cached setup "%s"' % output_filename)
    f.write('\n'.join(code))

mode = os.stat(output_filename).st_mode
os.chmod(output_filename, mode | stat.S_IXUSR)
