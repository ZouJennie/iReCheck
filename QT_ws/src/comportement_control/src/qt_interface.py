#! /usr/bin/env python

import sys
import copy
import rospy
from std_msgs.msg import String, Float64MultiArray, Float64, Int32
from comportement_control.msg import GestureCommand
from PyQt5 import QtWidgets, uic
from mainwindow import Ui_MainWindow
from control_publisher import RobotBehaviour

			
class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow,RobotBehaviour):
	def __init__(self, *args, **kwargs):
		super(MainWindow, self).__init__(*args, **kwargs)
		self.setupUi(self)
		self.head_yaw = []
		self.head_pitch = []
		self.head_vel =[]
		self.gesture_name= ""
		self.speed = 0
		self.emotion = []
		self.speech = []

		# set action when button is clicked
		self.muscle.clicked.connect(lambda:self.Action("muscle"))
		self.colere.clicked.connect(lambda:self.Action("air_en_colere"))
		self.progresse.clicked.connect(lambda:self.Action("progresse"))
		self.alors.clicked.connect(lambda:self.Action("alors"))
		self.fai_mon_mieux.clicked.connect(lambda:self.Action("fais_mon_mieux"))
		self.bien.clicked.connect(lambda:self.Action("bien"))
		self.bien_joue.clicked.connect(lambda:self.Action("bien_joue"))
		self.felicitation.clicked.connect(lambda:self.Action("felicitation"))
		self.bcp_travaille.clicked.connect(lambda:self.Action("bcp_travaille"))
		self.trop_fort.clicked.connect(lambda:self.Action("trop_fort"))
		self.bravo.clicked.connect(lambda:self.Action("bravo"))
		self.moi_trop_fort.clicked.connect(lambda:self.Action("moi_trop_fort"))
		self.malade.clicked.connect(lambda:self.Action("malade"))
		self.ecris_mal.clicked.connect(lambda:self.Action("ecris_mal"))
		self.pas_compris.clicked.connect(lambda:self.Action("pas_compris"))
		self.bien.clicked.connect(lambda:self.Action("bien"))
		self.repete.clicked.connect(lambda:self.Action("repete"))
		self.fatigue.clicked.connect(lambda:self.Action("fatigue"))
		self.sort_traj.clicked.connect(lambda:self.Action("sort_traj"))
		self.montre_traj.clicked.connect(lambda:self.Action("montre_traj"))
		self.touche_bomb.clicked.connect(lambda:self.Action("touche_bomb"))
		self.oui.clicked.connect(lambda:self.Action("oui"))
		self.non.clicked.connect(lambda:self.Action("non"))
		self.au_revoir.clicked.connect(lambda:self.Action("au_revoir"))
		self.cest_pas_grave.clicked.connect(lambda:self.Action("cest_pas_grave"))
		self.pause.clicked.connect(lambda:self.Action("pause"))
		self.respire.clicked.connect(lambda:self.Action("respire"))


	def Action(self,name):
		# run the control_publisher.py to control the robot and delete the content of every parameter when another button is clicked
		self.head_yaw = []
		self.head_pitch = []
		self.head_vel =[]
		self.gesture_name= ""
		self.speed = 0
		self.emotion = []
		self.speech = []
		self.load_info(name)
		self.realisation()


if __name__ == '__main__':
	
	app = QtWidgets.QApplication(sys.argv)
	window = MainWindow()
	window.show()
	app.exec_()