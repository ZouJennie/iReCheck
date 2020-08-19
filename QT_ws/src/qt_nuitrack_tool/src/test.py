#! /usr/bin/env python
import rospy
import tf
import numpy as np
import sys 
from std_msgs.msg import Float64MultiArray
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint

if __name__ == '__main__':
	rospy.init_node("head_test",anonymous=True)
	head_goal = rospy.Publisher('/qt_robot/head_controller/command',JointTrajectory,queue_size=10)
		 # wait for publisher connections
	wtime_begin = rospy.get_time()
	while (head_goal.get_num_connections() == 0) :
		rospy.loginfo("waiting for publisher connections...")
		if rospy.get_time() - wtime_begin > 10.0:
			rospy.logerr("Timeout while waiting for publisher connection!")
			sys.exit()
		rospy.sleep(1)
	point = JointTrajectoryPoint()
	print(type(point.positions))
	point.positions = [1,0]
	pointf = JointTrajectoryPoint()
	pointf.positions = [0,0]
	goal = JointTrajectory()
	goal.points.append(point)
	goal.points.append(pointf)
	goal.points[1].time_from_start.secs = 5
	goal.joint_names = ['HeadYaw','HeadPitch']
	print(goal)

	head_goal.publish(goal)
