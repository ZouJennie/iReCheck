#! /usr/bin/env python

import sys
import copy
import rospy
import moveit_commander
from std_msgs.msg import String
from std_msgs.msg import Float64MultiArray
from qt_motors_controller.srv import *

class RobotBehaviour(object):
	
	def __init__(self):
		self.head_yaw = []
		self.head_pitch = []
		self.left_shoulder_pitch = []
		self.left_shoulder_roll = []
		self.left_elbow_roll = []
		self.right_shoulder_pitch = []
		self.right_shoulder_roll = []
		self.right_elbow_roll = []
		self.emotion = []
		self.speech = []
		self.velocity = []
		
	def load_info(self,name):
		# import la fichier de comportement 
		f = open("/home/jennie/irecheck/iReCheck/qtrobot_ws/src/comportement_control/textfile/"+name+".txt", "r")
		line = f.readline()   
		
		while line:
			a = line.split(";")   
			print a
			self.head_yaw.append(float(a[0]))
			self.head_pitch.append(float(a[1]))
			self.left_shoulder_pitch.append(float(a[2]))
			self.left_shoulder_roll.append(float(a[3]))
			self.left_elbow_roll.append(float(a[4]))
			self.right_shoulder_pitch.append(float(a[5]))
			self.right_shoulder_roll.append(float(a[6]))
			self.right_elbow_roll.append(float(a[7]))
			self.emotion.append(eval(a[8]))
			self.speech.append(eval(a[9]))
			self.velocity.append(float(a[10]))
			line = f.readline()
		f.close()
		
	def realisation(self,say,emo,head_pub):
		joint_goal_left = [None]*3
		joint_goal_right = [None]*3
		joint_goal_head = Float64MultiArray()
		
		for i in range(len(self.emotion)):
			if self.velocity[i] < 0:
				joint_goal_left[0] = self.left_shoulder_pitch[i]
				joint_goal_left[1] = self.left_shoulder_roll[i]
				joint_goal_left[2] = self.left_elbow_roll[i]
				joint_goal_right[0] = self.right_shoulder_pitch[i]
				joint_goal_right[1] = self.right_shoulder_roll[i]
				joint_goal_right[2] = self.right_elbow_roll[i]
				#joint_goal_head.data = [self.head_yaw[i],self.head_pitch[i]]
		
				#print(joint_goal_left)
				#print(joint_goal_right)
				say.publish(self.speech[i])
				emo.publish(self.emotion[i])
				left_arm.go(joint_goal_left, wait=True)
				right_arm.go(joint_goal_right, wait=True)
				#left_arm.set_joint_value_target(joint_goal_left)
				#right_arm.set_joint_value_target(joint_goal_right)
				#left_arm.plan()
				#right_arm.plan()
				#head_pub.publish(joint_goal_head)
				#print self.speech[i]
			else:
				rospy.wait_for_service('/qt_robot/motors/setVelocity')
				try:
					setVelocity=rospy.ServiceProxy('/qt_robot/motors/setVelocity',set_velocity)
					setVelocity(['left_arm','right_arm'],self.velocity[i])
					joint_goal_left[0] = self.left_shoulder_pitch[i]
					joint_goal_left[1] = self.left_shoulder_roll[i]
					joint_goal_left[2] = self.left_elbow_roll[i]
					joint_goal_right[0] = self.right_shoulder_pitch[i]
					joint_goal_right[1] = self.right_shoulder_roll[i]
					joint_goal_right[2] = self.right_elbow_roll[i]
					#joint_goal_head.data = [self.head_yaw[i],self.head_pitch[i]]
		
					#print(joint_goal_left)
					#print(joint_goal_right)
					say.publish(self.speech[i])
					emo.publish(self.emotion[i])
					left_arm.go(joint_goal_left, wait=True)
					right_arm.go(joint_goal_right, wait=True)
				except rospy.ServiceException, e:
					print "Service call failed: %s"%e
		

if __name__ == "__main__":
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
    
    behaviour = RobotBehaviour()
    name = "pause" 
    behaviour.load_info(name)
    behaviour.realisation(say,emo,head_pub)
    #print(behaviour.emotion)
    
    

		
	
    
    
    
