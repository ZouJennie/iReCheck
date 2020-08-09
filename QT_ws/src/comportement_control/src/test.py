#! /usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import copy
import rospy
from std_msgs.msg import String
from std_msgs.msg import Float64MultiArray
from std_msgs.msg import Float64
from std_msgs.msg import Int32


if __name__ == '__main__':
	
	rospy.init_node('test', anonymous=True)
		# creat publisher
	say = rospy.Publisher('/qt_robot/speech/say', String, queue_size=10)

	say.publish("Je suis content de te rencontrer. J'ai besoin de ton aide pour apprendre à écrire, car je ne suis pas très fort. Est-ce que tu es d'accord pour m'aider? On s'améliorera ensemble!")