#! /usr/bin/env python

import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import copy
import rospy
import random
from std_msgs.msg import String
from std_msgs.msg import Float64MultiArray
from std_msgs.msg import Float64
from std_msgs.msg import Int32
from comportement_control.msg import GestureCommand

Prenom = ""


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
		
	def load_info(self,name,prenom):
		self.gesture_name= ""
		self.speed = 0
		self.emotion = []
		self.speech = []
		global Prenom 
		Prenom = prenom
		# import the file of behaviours
		f = open("/home/jennie/irecheck/iReCheck/QT_ws/src/comportement_control/comportement/"+name+".txt", "r")
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
			self.emotion.append(eval(a[0]))
			self.speech.append(eval(a[1]))	
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
		Prenom = "David"
	
		#while (say.get_num_connections() == 0) :
		#	rospy.loginfo("waiting for subscriber connections...")
		#	rospy.sleep(1)
		
		# initialisation of gesture
		target_gesture = GestureCommand()
		# command gesture
		target_gesture.name = self.gesture_name
		target_gesture.speed = self.speed
		print(target_gesture)
		gesture.publish(target_gesture)

		# command emotion and speech
		if len(self.emotion) == 1:
			#print self.speech[i]
			rospy.sleep(1)
			emo.publish(self.emotion[0])
			#rospy.sleep(1)
			say.publish(self.speech[0])
		else :
			i = random.randint(0,len(self.emotion)-1)
			rospy.sleep(1)
			emo.publish(self.emotion[i])
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
    #behaviour.realisation()
    
    #print(behaviour.emotion)
    
    

		
	
    
    
    
