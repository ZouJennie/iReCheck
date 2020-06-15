#! /usr/bin/env python


import sys
import copy
import rospy
import moveit_commander
from std_msgs.msg import String
from std_msgs.msg import Float64MultiArray
import geometry_msgs

""" Qt control test """
def Test():
    moveit_commander.roscpp_initialize(sys.argv)
    rospy.init_node('comportement_controller', anonymous=True)
    # create a publisher
    say = rospy.Publisher('/qt_robot/speech/say', String, queue_size=10)
    emo = rospy.Publisher('/qt_robot/emotion/show',String, queue_size=15)
    head_pub = rospy.Publisher('/qt_robot/head_position/command',Float64MultiArray, queue_size=1)

    robot = moveit_commander.RobotCommander()
    scene = moveit_commander.PlanningSceneInterface()
    right_arm = moveit_commander.MoveGroupCommander("right_arm")
    left_arm = moveit_commander.MoveGroupCommander("left_arm")
   # head = moveit_commander.MoveGroupCommander("head")

    rospy.sleep(3)

    # We can get the name of the reference frame for this robot:
    planning_frame_left = left_arm.get_planning_frame()
    planning_frame_right= right_arm.get_planning_frame()
    print "============Left reference frame: %s " % planning_frame_left
    print "============Right reference frame: %s " %planning_frame_right

    # We can also print the name of the end-effector link for this group:
    eef_link_left = left_arm.get_end_effector_link()
    eef_link_right = right_arm.get_end_effector_link()
    print "============Left end effector: %s " % eef_link_left
    print "============Right end effector: %s " % eef_link_right
	
    # We can get a list of all the groups in the robot:
    group_names = robot.get_group_names()
    print "============ Robot Groups:", robot.get_group_names()
    
    left_arm.allow_replanning(True)
    left_arm.set_pose_reference_frame("base_link")
    left_arm.set_planning_time(3.0)
    left_arm.clear_path_constraints()
    left_arm.clear_pose_targets()
    
    right_arm.allow_replanning(True)
    right_arm.set_pose_reference_frame("base_link")
    right_arm.set_planning_time(3.0)
    right_arm.clear_path_constraints()
    right_arm.clear_pose_targets()


    # Sometimes for debugging it is useful to print the entire state of the
    # robot:
    print "============ Printing robot state"
    print robot.get_current_state()
    print ""
    ## END_SUB_TUTORIAL

    print "============ Generating plan 1"
    pose_target = geometry_msgs.msg.Pose()
    pose_target.orientation.w = 1.0
    pose_target.position.x = 0.7
    pose_target.position.y = -0.05
    pose_target.position.z = 1.1
    group.set_pose_target(pose_target)
    ## to actually move the robot
    plan1 = left_arm.plan()
    print "============ Waiting while RVIZ displays plan1..."
    rospy.sleep(5)
    
  

if __name__ == '__main__':
    Test()
