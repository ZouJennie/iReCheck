#! /usr/bin/env python

import sys
import copy
import rospy
from std_msgs.msg import String
from std_msgs.msg import Float64MultiArray
from std_msgs.msg import Float64
from std_msgs.msg import Int32
from comportement_control.msg import GestureCommand


class RobotBehaviour(object):
	'''
	def __init__(self):
		self.head_yaw = []
		self.head_pitch = []
		self.head_vel =[]
		self.gesture_name= ""
		self.speed = 0
		self.emotion = []
		self.speech = []
	'''
		
	def load_info(self,name):
		# import the file of behaviours
		f = open("/home/isir/iReCheck/QT_ws/src/comportement_control/comportement/"+name+".txt", "r")
		line = f.readline()
		a=line.split(";") 
		# first line is infomation of gesture 
		self.gesture_name = a[0]
		#print self.gesture_name
		self.speed = float(a[1])
		
		# next lines are info of speech, emotion and head position
		line = f.readline()
		# save information
		while line:
			a = line.split(";")   
			self.emotion.append(eval(a[3]))
			self.speech.append(eval(a[4]))		
			line = f.readline()
		f.close()

	
	def realisation(self):
		rospy.init_node('behaviour_command', anonymous=True)
		# creat publisher
		say = rospy.Publisher('/qt_robot/speech/say', String, queue_size=10)
		emo = rospy.Publisher('/qt_robot/emotion/show',String, queue_size=10)
		language = rospy.Publisher('language',String,queue_size=10)
		language.publish('"fr-FR"')
		gesture = rospy.Publisher('comportement/gesture_name',GestureCommand,queue_size=10)
	
		#while (say.get_num_connections() == 0) :
		#	rospy.loginfo("waiting for subscriber connections...")
		#	rospy.sleep(1)
		
		# initialisation of gesture
		target_gesture = GestureCommand()
		# command gesture
		target_gesture.name = self.gesture_name
		target_gesture.speed = self.speed
		gesture.publish(target_gesture)
		# command emotion and speech
		for i in range(len(self.head_yaw)):
			#print self.speech[i]
			rospy.sleep(1)
			emo.publish(self.emotion[i])
			#rospy.sleep(1)
			say.publish(self.speech[i])
			
			
			
			

#if __name__ == "__main__":
    
    # create a publisher
    

    
    #test connection
    
    
    #say.publish("hello")
    #change language
    
    
    #behaviour command

    #behaviour = RobotBehaviour()
    #name = "bien" 
    #behaviour.load_info(name)
    #behaviour.realisation(say,emo,head_pub,head_vel,gesture)
    
    #print(behaviour.emotion)
    
    

		
	
    
    
    
