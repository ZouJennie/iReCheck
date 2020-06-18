#! /usr/bin/env python

import sys
import copy
import rospy
from std_msgs.msg import String
from std_msgs.msg import Float64MultiArray
from std_msgs.msg import Float64
from std_msgs.msg import Int32
from comportement_control.msg import GestureCommand
#import threading


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
		# import la fichier de comportement 
		f = open("/home/isir/iReCheck/QT_ws/src/comportement_control/comportement/"+name+".txt", "r")
		line = f.readline()
		a=line.split(";") 
		# first line is infomation of gesture 
		self.gesture_name = a[0]
		#print self.gesture_name
		self.speed = float(a[1])
		
		# next lines are info of speech, emotion and head position
		line = f.readline()
		while line:
			a = line.split(";")   
			self.head_yaw.append(float(a[0]))
			self.head_pitch.append(float(a[1]))
			self.head_vel.append(float(a[2]))
			self.emotion.append(eval(a[3]))
			self.speech.append(eval(a[4]))		
			line = f.readline()
		f.close()

		print (self.head_yaw)

	'''def speech(self,say):
		for i in len(self.speech):
			say.publish(self.speech[i])
	
	def emotion(self,emo):
		for i in len(self.emotion):
			emo.publish(self.emotion[i])
			
	def head_command(self,head_pub):
		for i in len(self.head_yaw):
			joint_goal_head.data = [self.head_yaw[i],self.head_pitch[i]]
			head_pub.publish(joint_goal_head)
	
	def gesture_pub(self):
		gesture.publish(self.gesture_name)
		
	def velocity_pub(self):
		velocity.publish(self.speed)
			
	def realisation(self,say,emo,head_pub,gesture_name,velocity):
		thread = []
		try:
			t1 = threading.Thread(target=behaviour.speech,args=(say))
			t2 = threading.Thread(target=behaviour.emotion,args=(emo))
			t3 = threading.Thread(target=behaviour.head_command,args=(head_pub))
			t4 = threading.Thread(target=behaviour.gesture_pub,args=())
			t5 = threading.Thread(target=behaviour.velocity_pub,args=())
			thread.extend([t1,t2,t3,t4,t5])
			
			for t in thread:
				t.start()
			
		except rospy.ServiceException, e:
			print "Service call failed: %s"%e'''
			
	def realisation(self):
		rospy.init_node('behaviour_command', anonymous=True)
		say = rospy.Publisher('/qt_robot/speech/say', String, queue_size=10)
		emo = rospy.Publisher('/qt_robot/emotion/show',String, queue_size=10)
		head_pub = rospy.Publisher('/qt_robot/head_position/command',Float64MultiArray, queue_size=1)
		head_vel = rospy.Publisher('head_velocity',Float64,queue_size=1)
		language = rospy.Publisher('language',String,queue_size=10)
		language.publish('"fr-FR"')
		gesture = rospy.Publisher('comportement/gesture_name',GestureCommand,queue_size=10)
	
		#while (say.get_num_connections() == 0) :
		#	rospy.loginfo("waiting for subscriber connections...")
		#	rospy.sleep(1)
		
		joint_goal_head = Float64MultiArray()
		target_gesture = GestureCommand()
		target_gesture.name = self.gesture_name
		target_gesture.speed = self.speed
		#print(target_gesture)
		gesture.publish(target_gesture)
		for i in range(len(self.head_yaw)):
			head_vel.publish(self.head_vel[i])
			joint_goal_head.data = [self.head_yaw[i],self.head_pitch[i]]
			head_pub.publish(joint_goal_head)
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
    
    

		
	
    
    
    
