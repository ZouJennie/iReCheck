#! /usr/bin/env python

import sys
import copy
import rospy
from std_msgs.msg import String, Float64MultiArray, Float64, Int32
from comportement_control.msg import GestureCommand
from PyQt5 import QtWidgets, uic
from mainwindow_2 import Ui_MainWindow
from logindlg import Ui_loginDlg
from control_publisher import RobotBehaviour
import datetime

Prenom = ""
Nom = ""

class loginDlg(QtWidgets.QDialog,Ui_loginDlg):
	def __init__(self):
		super(loginDlg, self).__init__()
		self.setupUi(self)
		self.LoginBtn.setEnabled(False)
		self.lineedit_init()
		self.pushbutton()
		self.mainWindow = QtWidgets.QMainWindow

	def check_input_func(self):
		if self.usrLineEdit.text() and self.usrLineEdit_2.text():
			self.LoginBtn.setEnabled(True)
			global Prenom, Nom
			Nom = self.usrLineEdit.text() 
			Prenom = self.usrLineEdit_2.text()
		else:
			self.LoginBtn.setEnabled(False)

	def lineedit_init(self):
		self.usrLineEdit.textChanged.connect(self.check_input_func)
		self.usrLineEdit_2.textChanged.connect(self.check_input_func)


	def pushbutton(self):
		self.LoginBtn.clicked.connect(self.show_main_page)

	def show_main_page(self):
		self.mainWindow = MainWindow()
		self.mainWindow.show()
		self.close()
			
class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow,RobotBehaviour):
	def __init__(self, *args, **kwargs):
		super(MainWindow, self).__init__(*args, **kwargs)
		self.setupUi(self)
		self.gesture_name= ""
		self.speed = 0
		self.emotion = []
		self.speech = []

		self.show_nom.setText(Nom)
		self.show_prenom.setText(Prenom)
		self.show_date.setText(str(datetime.date.today()))
	
		# set action when button is clicked
		# tab interaction
		self.je_mappelle_qt.clicked.connect(lambda:self.Action("je_mappelle_qt"))
		self.tu_veux_maider.clicked.connect(lambda:self.Action("tu_veux_maider"))
		self.tu_maides_encore.clicked.connect(lambda:self.Action("tu_maides_encore"))
		self.tu_viens.clicked.connect(lambda:self.Action("tu_viens"))
		self.clique_ton_nom.clicked.connect(lambda:self.Action("ton_nom"))
		self.bonjour.clicked.connect(lambda:self.Action("bonjour"))
		self.au_revoir.clicked.connect(lambda:self.Action("au_revoir"))
		self.comment.clicked.connect(lambda:self.Action("repete"))
		self.oui.clicked.connect(lambda:self.Action("oui"))
		self.non.clicked.connect(lambda:self.Action("non"))
		self.ca_va.clicked.connect(lambda:self.Action("ca_va"))
		self.merci.clicked.connect(lambda:self.Action("merci"))
		self.bravo.clicked.connect(lambda:self.Action("bravo"))
		self.cest_bien.clicked.connect(lambda:self.Action("cest_bien"))
		self.tu_es_fort.clicked.connect(lambda:self.Action( "tu_es_fort"))
		self.jsuis_fort.clicked.connect(lambda:self.Action( "je_suis_fort"))
		self.nous_sommes_forts.clicked.connect(lambda:self.Action( "nous_sommes_fort"))
		self.respire.clicked.connect(lambda:self.Action("respire"))
		self.pas_grave.clicked.connect(lambda:self.Action("cest_pas_grave"))
		self.reessayons.clicked.connect(lambda:self.Action("reessayons"))
		self.ecris_mal.clicked.connect(lambda:self.Action("ecris_mal"))
		self.fera_mieux.clicked.connect(lambda:self.Action("fera_mieux"))
		self.courage.clicked.connect(lambda:self.Action("courage"))
		self.nous_avons_rate.clicked.connect(lambda:self.Action("rate"))
		self.aie.clicked.connect(lambda:self.Action("aie"))
		self.muscle_plastique.clicked.connect(lambda:self.Action("muscle"))
		self.ahahah.clicked.connect(lambda:self.Action("ahahah"))
		self.tu_es_sur.clicked.connect(lambda:self.Action("tu_es_sur"))
		self.je_trouve_pas.clicked.connect(lambda:self.Action("je_trouve_pas"))
		self.fais_effort.clicked.connect(lambda:self.Action("fais_mon_mieux"))
		self.progresse.clicked.connect(lambda:self.Action("jai_progresse"))
		self.et_alors.clicked.connect(lambda:self.Action("et_alors"))
		self.ma_tablette.clicked.connect(lambda:self.Action("ma_tablette"))
		self.difficile.clicked.connect(lambda:self.Action("cest_difficile"))
		self.pas_mal.clicked.connect(lambda:self.Action("pas_mal"))
		self.je_bugue.clicked.connect(lambda:self.Action("je_bugue"))
		self.gagne.clicked.connect(lambda:self.Action("tas_gagne"))
		self.attends.clicked.connect(lambda:self.Action("attends"))
		self.tu_relance.clicked.connect(lambda:self.Action("tu_relances"))
		self.je_fatigue.clicked.connect(lambda:self.Action("fatigue"))
		self.je_malade.clicked.connect(lambda:self.Action( "malade"))
		self.je_rouille.clicked.connect(lambda:self.Action("je_rouille"))
		self.la_colere.clicked.connect(lambda:self.Action( "la_colere"))
		self.la_fatigue.clicked.connect(lambda:self.Action( "la_fatigue"))
		self.la_motivation.clicked.connect(lambda:self.Action( "la_motivation"))
		self.la_joie.clicked.connect(lambda:self.Action( "la_joie"))
		self.la_tristesse.clicked.connect(lambda:self.Action( "la_tristesse"))
		self.etonnement.clicked.connect(lambda:self.Action( "etonnement"))
		self.la_fierte.clicked.connect(lambda:self.Action( "la_fierte"))
		self.amusement.clicked.connect(lambda:self.Action("amusement"))
		self.bcp_travaille.clicked.connect(lambda:self.Action( "bcp_travaille"))
		self.mes_progres.clicked.connect(lambda:self.Action( "mes_progres"))
		self.tu_maide.clicked.connect(lambda:self.Action( "tu_maide"))
		self.il_est_lheure.clicked.connect(lambda:self.Action( "il_est_lheure"))
		self.on_arrete.clicked.connect(lambda:self.Action( "arrete"))
		self.cetait_bien.clicked.connect(lambda:self.Action( "cetait_bien"))
		self.on_essaye.clicked.connect(lambda:self.Action("on_essaye"))
		self.tu_mexplique.clicked.connect(lambda:self.Action( "tu_mexplique"))
		self.ensuite.clicked.connect(lambda:self.Action( "ensuite"))
		self.bien.clicked.connect(lambda:self.Action( "bien"))
		self.pk_pas_bien.clicked.connect(lambda:self.Action( "pk_pas_bien"))
		self.cest_mieux.clicked.connect(lambda:self.Action( "cest_mieux"))
		self.plus_important.clicked.connect(lambda:self.Action("important"))
		
		# tab jeu
		self.poursuite_lance.clicked.connect(lambda:self.Action("poursuite_lance"))
		self.poursuite_expli.clicked.connect(lambda:self.Action("poursuite_expli"))
		self.pression_lance.clicked.connect(lambda:self.Action("pression_lance"))
		self.pression_expli.clicked.connect(lambda:self.Action("pression_expli"))
		self.tilt_lance.clicked.connect(lambda:self.Action("tilt_lance"))
		self.tilt_expli.clicked.connect(lambda:self.Action("tilt_expli"))
		self.twister_lance.clicked.connect(lambda:self.Action("twister_lance"))
		self.twister_expli.clicked.connect(lambda:self.Action("twister_expli"))
		self.triche.clicked.connect(lambda:self.Action("triche"))
		self.facile.clicked.connect(lambda:self.Action("facile"))
		self.trop_difficile.clicked.connect(lambda:self.Action("difficle"))
		self.boum.clicked.connect(lambda:self.Action("boum"))
		self.pas_trop_vite.clicked.connect(lambda:self.Action("pas_trop_vite"))



	def Action(self,name):
		# run the control_publisher.py to control the robot and delete the content of every parameter when another button is clicked

		self.load_info(name,Prenom)
		self.realisation()




if __name__ == '__main__':
	
	app = QtWidgets.QApplication(sys.argv)
	window = loginDlg()
	window.exec_()
	app.exec_()
