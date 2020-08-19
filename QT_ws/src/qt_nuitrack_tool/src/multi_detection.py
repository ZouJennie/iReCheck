#! /usr/bin/env python
import rospy
import tf
import numpy as np
import usb.core
import usb.util
import time
import sys 
from std_msgs.msg import Float64MultiArray
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint
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
		self.goal = JointTrajectory()
		self.goal.joint_names = ["HeadYaw","HeadPitch"]
		self.point_init = JointTrajectoryPoint()
		self.point_init.positions = [0,0]
		self.point_final = JointTrajectoryPoint()
		self.point_final.positions = [0,0]
		self.goal.points.append(self.point_init)
		self.goal.points.append(self.point_final)
		self.record = [0,0]
	
	def load_info(self,data):
		""" Load data heard from nuitrack"""
		#print(len(data.skeletons))
		for n in range(0,len(data.skeletons)):
		#	print("test 0")
			if data.skeletons[n].id in self.id:
		#		print("test 1")
				i = self.id.index(data.skeletons[n].id)
					#print("test 2")
				self.joints[i] = data.skeletons[n].joints[1]
				self.translation[i,:] = (np.array(self.joints[i].real)/1000.0).tolist()
				self.angle[i] = np.arctan2(self.translation[i,0],self.translation[i,1])
			else:
				print("test 3")
				self.id.append(data.skeletons[n].id)
				i = len(self.id)-1
				self.joints.append(data.skeletons[n].joints[1])
				self.translation[i,:] = (np.array(self.joints[i].real)/1000.0).tolist()
				self.angle.append(np.arctan2(self.translation[i,0],self.translation[i,1]))
		#print (self.id)
		min_angle = 180
		for i in range(0,len(self.angle)):
			if abs(self.angle[i]) < abs(min_angle):
				min_angle = self.angle[i]
		angle = min_angle/180.0*np.pi
		self.head_control(angle)


	def msg_listener(self):
		""" subscibe nuitrack msg"""
		rospy.Subscriber('/qt_nuitrack_app/skeletons',Skeletons,self.load_info)
		

	def do(self):
		microphone = Tuning(dev)
		print("tunning succes")
		while not rospy.is_shutdown():
			if microphone.is_voice():
				mic = abs(microphone.direction - 180)
				angle = (mic - 90.0)/180.0*np.pi
				rospy.loginfo("mic: %d , head: %d" % (mic, angle))
				self.head_control(angle)
				self.msg_listener()
			else:
				#print("debug else")
				continue
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

		self.point_init.positions = self.record
		self.point_final.positions = [self.record[0]+angle,0]
		self.goal.points[0] = self.point_init
		self.goal.points[1] = self.point_final
		self.goal.points[1].time_from_start.secs = 2
		print(self.goal)
		head_goal.publish(self.goal)
		self.record = self.point_final.positions
		



if __name__ == '__main__':
	rospy.init_node('multi_detection', anonymous=True)
	dev = usb.core.find(idVendor=0x2886, idProduct=0x0018)
	if not dev:
		rospy.logerr("Cannot establish connection!")
		sys.exit()


   
	detection=MultiDetection(dev)
	detection.do()

