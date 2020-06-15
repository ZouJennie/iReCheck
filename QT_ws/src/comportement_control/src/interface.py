#! /usr/bin/env python

import sys
import copy
import rospy
from std_msgs.msg import String, Float64MultiArray, Float64, Int32
from comportement_control.msg import GestureCommand
from PyQt5 import QtWidgets, uic
from mainwindow import Ui_MainWindow
from control_publisher import RobotBehaviour

			
class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow, behaviour):
	def __init__(self, *args, **kwargs):
		super(MainWindow, self).__init__(*args, **kwargs)
		self.setupUi(self)
	
		self.colere.clicked.connect(self.Action("air_en_colere"))
		self.muscle.clicked.connect(self.Action("muscle"))
		self.progresse.clicked.connect(self.Action("progresse"))
		self.alors.clicked.connect(self.Action("alors"))
		self.fais_mon_mieux.clicked.connect(self.Action("fais_mon_mieux"))
		self.bien.clicked.connect(self.Action("bien"))
		self.bien_joue.clicked.connect(self.Action("bien_joue"))
		self.felicitation.clicked.connect(self.Action("felicitation"))
		self.bcp_travaille.clicked.connect(self.Action("bcp_travaille"))
		self.trop_fort.clicked.connect(self.Action("trop_fort"))
		self.bravo.clicked.connect(self.Action("bravo"))
		self.moi_trop_fort.clicked.connect(self.Action("moi_trop_fort"))
		self.malade.clicked.connect(self.Action("malade"))
		self.ecris_mal.clicked.connect(self.Action("ecris_mal"))
		self.pas_compris.clicked.connect(self.Action("pas_compris"))
		self.bien.clicked.connect(self.Action("bien"))
		self.repete.clicked.connect(self.Action("repete"))
		self.fatigue.clicked.connect(self.Action("fatigue"))
		self.sort_traj.clicked.connect(self.Action("sort_traj"))
		self.montre_traj.clicked.connect(self.Action("montre_traj"))
		self.touche_bomb.clicked.connect(self.Action("touche_bomb"))
		self.oui.clicked.connect(self.Action("oui"))
		self.non.clicked.connect(self.Action("non"))
		self.au_revoir.clicked.connect(self.Action("au_revoir"))
		self.cest_pas_grave.clicked.connect(self.Action("cest_pas_grave"))
		self.pause.clicked.connect(self.Action("pause"))
		self.respire.clicked.connect(self.Action("respire")
	
	def Action(self,name):
		load_info(name)
		realisation()



if __name__ == "__main__":
	rospy.init_node('behaviour_command', anonymous=True)
	

	
	#test connection
	while (say.get_num_connections() == 0) :
	rospy.loginfo("waiting for subscriber connections...")
	rospy.sleep(1)
	
	#say.publish("hello")
	
	
	#behaviour command
	'''behaviour = RobotBehaviour()
	name = "bien" 
	behaviour.load_info(name)
	behaviour.realisation(say,emo,head_pub,head_vel,gesture)'''
	app = QtWidgets.QApplication(sys.argv)
	window = MainWindow()
	window.show()
	app.exec_()
	#print(behaviour.emotion)
	
	
