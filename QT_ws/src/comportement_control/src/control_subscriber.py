#! /usr/bin/env python

import sys
import copy
import rospy
from std_msgs.msg import String
from std_msgs.msg import Float64MultiArray
from std_msgs.msg import Float64
import GestureCommand.msg
from qt_gesture_controller.srv import *
from qt_robot_interface.srv import *


def lang_callback(data):
   	rospy.loginfo(rospy.get_caller_id()+"I heard %s",data.data)
	try:
		rospy.wait_for_service('/qt_robot/speech/config')
		language_config = rospy.ServiceProxy('/qt_robot/speech/config', speech_config)
		res_language = language_config(data.data,0,0)
		if not res_language.status:
			print("Could not change language")
	except rospy.ServiceException, e:
                print "Service call failed: %s." % e

def gesture_command(data):
	rospy.loginfo(rospy.get_caller_id()+"I heard %s with speed %f",data.name, data.speed)
	try:
		rospy.wait_for_service('/qt_robot/gesture/play')
		gesture_play = rospy.ServiceProxy('/qt_robot/gesture/play', gesture_play)
		res_gesture = gesture_play(data.name, data.speed)
		if not res_gesture.status:
			print("Could not play gesture '%s'." % data.name)			
	except rospy.ServiceException, e:
                print "Service call failed: %s." % e
			
def command_listener():
	language = None
	gesture_name = None
	velocity = None
	#creat ros node
	rospy.init_node('behaviour_control', anonymous=True)
	#creat ros subscriber
	rospy.Subscriber('language',String,lang_callback)
	rospy.Subscriber('comportement/gesture_name',GestureCommand, gesture_command)

	
	rospy.spin()
	

if __name__ == "__main__":
	command_listener()
	
