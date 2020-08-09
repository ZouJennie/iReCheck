#! /usr/bin/env python
import rospy
import tf
from qt_nuitrack_app.msg import * 
import numpy as np

class NuitrackTfTool(object):
	"""docstring for NuitrackTool"""
	def __init__(self):
		"""initialisation of class"""
		super(NuitrackTfTool, self).__init__()
		self.id = []
		self.joints = []
		self.translation = np.zeros([10,25,3])
		self.rotation = np.zeros([10,25,9])
		self.br = tf.TransformBroadcaster()
		
	def load_info(self,data):
		""" Load data heard from nuitrack"""
		#print(len(data.skeletons))
		for n in range(0,len(data.skeletons)):
		#	print("test 0")
			if data.skeletons[n].id in self.id:
		#		print("test 1")
				i = self.id.index(data.skeletons[n].id)
				for j in range(0,25):
					#print("test 2")
					self.translation[i,j,:] = (np.array(self.joints[i][j].real)/1000.0).tolist()
					self.rotation[i,j,:] = self.joints[i][j].orientation
				self.joints[i] = data.skeletons[n].joints
			else:
				print("test 3")
				self.id.append(data.skeletons[n].id)
				i = len(self.id)-1
				self.joints.append(data.skeletons[n].joints)
				for j in range(0,25):
					#print("test 2")
					self.translation[i,j,:] = (np.array(self.joints[i][j].real)/1000.0).tolist()
					self.rotation[i,j,:] = self.joints[i][j].orientation
		print (self.id)
		self.do()


	def msg_listener(self):
		""" subscibe nuitrack msg"""
		rospy.init_node("tf_skeletons",anonymous=True)
		rospy.Subscriber('/qt_nuitrack_app/skeletons',Skeletons,self.load_info)
		rospy.spin()

	def do(self):
		print("test do func")
		print(self.id)
		for i in self.id:
			print(i)
			self.handle_tf(self.id.index(i))

	def handle_tf(self,i):
		""" Send Transform of every point of skeletons"""
		print("test TF")

		joint_name = ["Head","Neck","Torso","Waist","Left_Collar","Left_Shoulder","Left_Elbow","Left_Wrist","Left_Hand","Right_Collar","Right_Shoulder","Right_Elbow","Right_Wrist","Right_Hand",
					"Left_Hip","Left_Knee","Left_Ankle","Right_Hip","Right_Knee","Right_Ankle"]
		joints_number = [1,2,3,4,5,6,7,8,9,11,12,13,14,15,17,18,19,21,22,23]

		rot_euler = np.zeros([20,3])
		for (j,n) in zip(joints_number,range(20)): 
			r = self.rotation[i,j,:]
			m = np.mat([[r[0],r[1],r[2]],[r[3],r[4],r[5]],[r[6],r[7],r[8]]])
			rot = tf.transformations.euler_from_matrix(m,"rxyz")
			rot_euler[n,:] = rot
		
		for (k,j) in zip(joints_number, range(len(joint_name))):
			self.br.sendTransform( self.translation[i,k,:],tf.transformations.quaternion_from_euler(rot_euler[j,0],rot_euler[j,1],rot_euler[j,2]), rospy.Time.now(),joint_name[j]+"_"+str(i),"/nuitrack_frame")


if __name__ == '__main__':
	TF=NuitrackTfTool()
	TF.msg_listener()
	#TF.do()