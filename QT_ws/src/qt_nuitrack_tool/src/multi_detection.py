#! /usr/bin/env python
import rospy
import tf
import numpy as np
import usb.core
import usb.util
import time
import sys 
from std_msgs.msg import Float64MultiArray
from trajectory_msgs.msg import JointTrajectory
from qt_multi_detection.msg import * 
from tuning import Tuning

# microphone orientation
MICROPHONE_ANGLE_OFFSET = 90

class MultiDetection(object):
	"""docstring for MultiDetection"""
	def __init__(self, dev):
		super(MultiDetection, self).__init__()
		self.id = []
		self.joints = []
		self.translation = np.zeros([10,3])
		self.angle = []
		self.dev = dev
		self.goal = JointTrajectory
		self.goal.joint_names = ['HeadPitch']
		self.goal.points = [0]*2
	
	def load_info(self,data):
		""" Load data heard from nuitrack"""
		#print(len(data.skeletons))
		for n in range(0,len(data.skeletons)):
		#	print("test 0")
			if data.skeletons[n].id in self.id:
		#		print("test 1")
				i = self.id.index(data.skeletons[n].id)
					#print("test 2")
				self.translation[i,:] = (np.array(self.joints[i].real)/1000.0).tolist()
				self.joints[i] = data.skeletons[n].joints[1]
				self.angle[i] = np.arctan2(self.translation[i,0],self.translation[i,1])
			else:
				print("test 3")
				self.id.append(data.skeletons[n].id)
				i = len(self.id)-1
				self.joints.append(data.skeletons[n].joints[1])
				self.translation[i,:] = (np.array(self.joints[i].real)/1000.0).tolist()
				self.angle.append(np.arctan2(self.translation[i,0],self.translation[i,1]))
		#print (self.id)
		angle = min(abs(self.angle))/180*np.pi
		self.head_control(angle)
		self.goal.points[0]=angle


	def msg_listener(self):
		""" subscibe nuitrack msg"""
		rospy.Subscriber('/qt_nuitrack_app/skeletons',Skeletons,self.load_info)
		

	def do(self):
		microphone = Tuning(dev)
		while not rospy.is_shutdown():
			if not microphone.is_voice():
				continue
		mic = abs(microphone.direction - 180)
		angle = (mic - MICROPHONE_ANGLE_OFFSET)/180*np.pi
		rospy.loginfo("mic: %d , head: %d" % (mic, angle))
		self.head_control(angle)
		self.msg_listener()
		rospy.spin()


	def head_control(self,angle):
		head_goal = rospy.Publisher('/qt_robot/head_controller/command',JointTrajectory,queue_size=10)
		 # wait for publisher connections
		wtime_begin = rospy.get_time()
		while (head_goal.get_num_connections() == 0) :
			rospy.loginfo("waiting for publisher connections...")
			if rospy.get_time() - wtime_begin > 10.0:
				rospy.logerr("Timeout while waiting for publisher connection!")
				sys.exit()
			rospy.sleep(1)
		self.goal.points[1] = angle
		head_goal.publish(goal)
		self.goal.points[0] = self.goal.points[1]



if __name__ == '__main__':
	rospy.init_node('multi_detection', anonymous=True)
	dev = usb.core.find(idVendor=0x2886, idProduct=0x0018)
	if not dev:
		rospy.logerr("Cannot establish connection!")
		sys.exit()


   
	detection=MultiDetection(dev)
	detection.do()

