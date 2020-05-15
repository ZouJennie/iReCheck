#FFA500#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import sys
import copy
import rospy
import moveit_commander
# import moveit_msgs.msg
# import geometry_msgs.msg
# from std_msgs.msg import String
# from moveit_commander.conversions import pose_to_list

if __name__ == "__main__":
    moveit_commander.roscpp_initialize(sys.argv)
    rospy.init_node('draw_rectangle', anonymous=True)

    robot = moveit_commander.RobotCommander()
    scene = moveit_commander.PlanningSceneInterface()
    group = moveit_commander.MoveGroupCommander("right_arm")
    print(group.get_current_joint_values())

