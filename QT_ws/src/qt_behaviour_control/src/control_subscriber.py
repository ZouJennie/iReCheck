#! /usr/bin/env python

import sys
import copy
import rospy
from std_msgs.msg import String
from std_msgs.msg import Float64MultiArray
from std_msgs.msg import Float64
from qt_behaviour_control.msg import GestureCommand
from qt_gesture_controller.srv import *
from qt_robot_interface.srv import *
from qt_motors_controller.srv import *

def lang_callback(data):
   	rospy.loginfo(rospy.get_caller_id()+"I heard %s",data.data)
#	print type(eval(data.data))
	try:
		rospy.wait_for_service('/qt_robot/speech/config')
		language_config = rospy.ServiceProxy('/qt_robot/speech/config', speech_config)
		res_language = language_config(eval(data.data),0,0)
		if not res_language.status:
			print("Could not change language")
	except rospy.ServiceException, e:
                print "Service call failed: %s." % e

def gesture_command(data):
	rospy.loginfo(rospy.get_caller_id()+"I heard %s with speed %f",data.name, data.speed)
	try:
		rospy.wait_for_service('/qt_robot/gesture/play')
		rospy.wait_for_service('/qt_robot/motors/home')
		gesture_com = rospy.ServiceProxy('/qt_robot/gesture/play', gesture_play)
		res_gesture = gesture_com(eval(data.name), data.speed)
		home_pose = rospy.ServiceProxy('/qt_robot/motors/home',home)
		res_home = home_pose(['head','left_arm','right_arm'])
		if not res_gesture.status:
			print("Could not play gesture '%s'." % data.name)			
	except rospy.ServiceException, e:
                print "Service call failed: %s." % e

def set_head_velocity(data):
	try:
		rospy.wait_for_service('/qt_robot/motors/setVelocity')
		setvelocity = rospy.ServiceProxy('/qt_robot/motors/setVelocity',set_velocity)
		res_vel = setvelocity(['head'],data.data)
		if not res_vel.status:
			print("Could not change velocity of head")
	except rospy.ServiceException, e:
		print "Service call failed: %s." % e

def command_listener(arg):
	#creat ros node
	rospy.init_node('behaviour_control', anonymous=True)
	#load patient info

	#creat ros subscriber
	rospy.Subscriber('language',String,lang_callback)
	rospy.Subscriber('comportement/gesture_name',GestureCommand, gesture_command
	rospy.Subscriber('head_velocity',Float64,set_head_velocity)
	
	rospy.spin()


if __name__ == "__main__":


	command_listener()
	
