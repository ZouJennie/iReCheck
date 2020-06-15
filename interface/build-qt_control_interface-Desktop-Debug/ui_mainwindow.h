/********************************************************************************
** Form generated from reading UI file 'mainwindow.ui'
**
** Created by: Qt User Interface Compiler version 4.8.7
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_MAINWINDOW_H
#define UI_MAINWINDOW_H

#include <QtCore/QVariant>
#include <QtGui/QAction>
#include <QtGui/QApplication>
#include <QtGui/QButtonGroup>
#include <QtGui/QHBoxLayout>
#include <QtGui/QHeaderView>
#include <QtGui/QLabel>
#include <QtGui/QMainWindow>
#include <QtGui/QMenuBar>
#include <QtGui/QPushButton>
#include <QtGui/QStatusBar>
#include <QtGui/QToolBar>
#include <QtGui/QVBoxLayout>
#include <QtGui/QWidget>

QT_BEGIN_NAMESPACE

class Ui_MainWindow
{
public:
    QWidget *centralWidget;
    QWidget *horizontalLayoutWidget;
    QHBoxLayout *horizontalLayout;
    QWidget *verticalLayoutWidget;
    QVBoxLayout *verticalLayout;
    QVBoxLayout *verticalLayout_8;
    QLabel *label;
    QHBoxLayout *horizontalLayout_2;
    QPushButton *muscle;
    QPushButton *progresse;
    QPushButton *alors;
    QPushButton *fai_mon_mieux;
    QVBoxLayout *verticalLayout_7;
    QLabel *label_5;
    QHBoxLayout *horizontalLayout_9;
    QPushButton *bien;
    QPushButton *bien_joue;
    QPushButton *felicitation;
    QHBoxLayout *horizontalLayout_7;
    QPushButton *bcp_travaille;
    QPushButton *trop_fort;
    QPushButton *bravo;
    QPushButton *moi_trop_fort;
    QHBoxLayout *horizontalLayout_5;
    QVBoxLayout *verticalLayout_3;
    QLabel *label_2;
    QHBoxLayout *horizontalLayout_3;
    QPushButton *malade;
    QPushButton *ecris_mal;
    QPushButton *pas_compris;
    QPushButton *repete;
    QPushButton *fatigue;
    QVBoxLayout *verticalLayout_9;
    QLabel *label_3;
    QHBoxLayout *horizontalLayout_4;
    QPushButton *sort_traj;
    QPushButton *montre_traj;
    QPushButton *touche_bomb;
    QVBoxLayout *verticalLayout_10;
    QLabel *label_6;
    QHBoxLayout *horizontalLayout_10;
    QPushButton *oui;
    QPushButton *non;
    QPushButton *au_revoir;
    QVBoxLayout *verticalLayout_5;
    QLabel *label_4;
    QHBoxLayout *horizontalLayout_6;
    QPushButton *cest_pas_grave;
    QPushButton *pause;
    QPushButton *respire;
    QPushButton *air_en_colere;
    QWidget *verticalLayoutWidget_9;
    QVBoxLayout *verticalLayout_11;
    QLabel *label_7;
    QMenuBar *menuBar;
    QToolBar *mainToolBar;
    QStatusBar *statusBar;

    void setupUi(QMainWindow *MainWindow)
    {
        if (MainWindow->objectName().isEmpty())
            MainWindow->setObjectName(QString::fromUtf8("MainWindow"));
        MainWindow->resize(1267, 730);
        centralWidget = new QWidget(MainWindow);
        centralWidget->setObjectName(QString::fromUtf8("centralWidget"));
        horizontalLayoutWidget = new QWidget(centralWidget);
        horizontalLayoutWidget->setObjectName(QString::fromUtf8("horizontalLayoutWidget"));
        horizontalLayoutWidget->setGeometry(QRect(0, 0, 631, 721));
        horizontalLayout = new QHBoxLayout(horizontalLayoutWidget);
        horizontalLayout->setSpacing(6);
        horizontalLayout->setContentsMargins(11, 11, 11, 11);
        horizontalLayout->setObjectName(QString::fromUtf8("horizontalLayout"));
        horizontalLayout->setContentsMargins(0, 0, 0, 0);
        verticalLayoutWidget = new QWidget(centralWidget);
        verticalLayoutWidget->setObjectName(QString::fromUtf8("verticalLayoutWidget"));
        verticalLayoutWidget->setGeometry(QRect(630, 30, 601, 591));
        verticalLayout = new QVBoxLayout(verticalLayoutWidget);
        verticalLayout->setSpacing(6);
        verticalLayout->setContentsMargins(11, 11, 11, 11);
        verticalLayout->setObjectName(QString::fromUtf8("verticalLayout"));
        verticalLayout->setContentsMargins(0, 0, 0, 0);
        verticalLayout_8 = new QVBoxLayout();
        verticalLayout_8->setSpacing(6);
        verticalLayout_8->setObjectName(QString::fromUtf8("verticalLayout_8"));
        label = new QLabel(verticalLayoutWidget);
        label->setObjectName(QString::fromUtf8("label"));
        QFont font;
        font.setBold(true);
        font.setWeight(75);
        label->setFont(font);

        verticalLayout_8->addWidget(label);

        horizontalLayout_2 = new QHBoxLayout();
        horizontalLayout_2->setSpacing(6);
        horizontalLayout_2->setObjectName(QString::fromUtf8("horizontalLayout_2"));
        muscle = new QPushButton(verticalLayoutWidget);
        muscle->setObjectName(QString::fromUtf8("muscle"));

        horizontalLayout_2->addWidget(muscle);

        progresse = new QPushButton(verticalLayoutWidget);
        progresse->setObjectName(QString::fromUtf8("progresse"));

        horizontalLayout_2->addWidget(progresse);

        alors = new QPushButton(verticalLayoutWidget);
        alors->setObjectName(QString::fromUtf8("alors"));

        horizontalLayout_2->addWidget(alors);

        fai_mon_mieux = new QPushButton(verticalLayoutWidget);
        fai_mon_mieux->setObjectName(QString::fromUtf8("fai_mon_mieux"));

        horizontalLayout_2->addWidget(fai_mon_mieux);


        verticalLayout_8->addLayout(horizontalLayout_2);


        verticalLayout->addLayout(verticalLayout_8);

        verticalLayout_7 = new QVBoxLayout();
        verticalLayout_7->setSpacing(6);
        verticalLayout_7->setObjectName(QString::fromUtf8("verticalLayout_7"));
        label_5 = new QLabel(verticalLayoutWidget);
        label_5->setObjectName(QString::fromUtf8("label_5"));
        label_5->setFont(font);

        verticalLayout_7->addWidget(label_5);

        horizontalLayout_9 = new QHBoxLayout();
        horizontalLayout_9->setSpacing(6);
        horizontalLayout_9->setObjectName(QString::fromUtf8("horizontalLayout_9"));
        bien = new QPushButton(verticalLayoutWidget);
        bien->setObjectName(QString::fromUtf8("bien"));

        horizontalLayout_9->addWidget(bien);

        bien_joue = new QPushButton(verticalLayoutWidget);
        bien_joue->setObjectName(QString::fromUtf8("bien_joue"));

        horizontalLayout_9->addWidget(bien_joue);

        felicitation = new QPushButton(verticalLayoutWidget);
        felicitation->setObjectName(QString::fromUtf8("felicitation"));

        horizontalLayout_9->addWidget(felicitation);


        verticalLayout_7->addLayout(horizontalLayout_9);

        horizontalLayout_7 = new QHBoxLayout();
        horizontalLayout_7->setSpacing(6);
        horizontalLayout_7->setObjectName(QString::fromUtf8("horizontalLayout_7"));
        bcp_travaille = new QPushButton(verticalLayoutWidget);
        bcp_travaille->setObjectName(QString::fromUtf8("bcp_travaille"));

        horizontalLayout_7->addWidget(bcp_travaille);

        trop_fort = new QPushButton(verticalLayoutWidget);
        trop_fort->setObjectName(QString::fromUtf8("trop_fort"));

        horizontalLayout_7->addWidget(trop_fort);

        bravo = new QPushButton(verticalLayoutWidget);
        bravo->setObjectName(QString::fromUtf8("bravo"));

        horizontalLayout_7->addWidget(bravo);

        moi_trop_fort = new QPushButton(verticalLayoutWidget);
        moi_trop_fort->setObjectName(QString::fromUtf8("moi_trop_fort"));

        horizontalLayout_7->addWidget(moi_trop_fort);


        verticalLayout_7->addLayout(horizontalLayout_7);


        verticalLayout->addLayout(verticalLayout_7);

        horizontalLayout_5 = new QHBoxLayout();
        horizontalLayout_5->setSpacing(6);
        horizontalLayout_5->setObjectName(QString::fromUtf8("horizontalLayout_5"));
        verticalLayout_3 = new QVBoxLayout();
        verticalLayout_3->setSpacing(6);
        verticalLayout_3->setObjectName(QString::fromUtf8("verticalLayout_3"));
        label_2 = new QLabel(verticalLayoutWidget);
        label_2->setObjectName(QString::fromUtf8("label_2"));
        label_2->setFont(font);

        verticalLayout_3->addWidget(label_2);

        horizontalLayout_3 = new QHBoxLayout();
        horizontalLayout_3->setSpacing(6);
        horizontalLayout_3->setObjectName(QString::fromUtf8("horizontalLayout_3"));
        malade = new QPushButton(verticalLayoutWidget);
        malade->setObjectName(QString::fromUtf8("malade"));

        horizontalLayout_3->addWidget(malade);

        ecris_mal = new QPushButton(verticalLayoutWidget);
        ecris_mal->setObjectName(QString::fromUtf8("ecris_mal"));

        horizontalLayout_3->addWidget(ecris_mal);

        pas_compris = new QPushButton(verticalLayoutWidget);
        pas_compris->setObjectName(QString::fromUtf8("pas_compris"));

        horizontalLayout_3->addWidget(pas_compris);

        repete = new QPushButton(verticalLayoutWidget);
        repete->setObjectName(QString::fromUtf8("repete"));

        horizontalLayout_3->addWidget(repete);

        fatigue = new QPushButton(verticalLayoutWidget);
        fatigue->setObjectName(QString::fromUtf8("fatigue"));

        horizontalLayout_3->addWidget(fatigue);


        verticalLayout_3->addLayout(horizontalLayout_3);


        horizontalLayout_5->addLayout(verticalLayout_3);


        verticalLayout->addLayout(horizontalLayout_5);

        verticalLayout_9 = new QVBoxLayout();
        verticalLayout_9->setSpacing(6);
        verticalLayout_9->setObjectName(QString::fromUtf8("verticalLayout_9"));
        label_3 = new QLabel(verticalLayoutWidget);
        label_3->setObjectName(QString::fromUtf8("label_3"));
        label_3->setFont(font);

        verticalLayout_9->addWidget(label_3);

        horizontalLayout_4 = new QHBoxLayout();
        horizontalLayout_4->setSpacing(6);
        horizontalLayout_4->setObjectName(QString::fromUtf8("horizontalLayout_4"));
        sort_traj = new QPushButton(verticalLayoutWidget);
        sort_traj->setObjectName(QString::fromUtf8("sort_traj"));

        horizontalLayout_4->addWidget(sort_traj);

        montre_traj = new QPushButton(verticalLayoutWidget);
        montre_traj->setObjectName(QString::fromUtf8("montre_traj"));

        horizontalLayout_4->addWidget(montre_traj);

        touche_bomb = new QPushButton(verticalLayoutWidget);
        touche_bomb->setObjectName(QString::fromUtf8("touche_bomb"));

        horizontalLayout_4->addWidget(touche_bomb);


        verticalLayout_9->addLayout(horizontalLayout_4);


        verticalLayout->addLayout(verticalLayout_9);

        verticalLayout_10 = new QVBoxLayout();
        verticalLayout_10->setSpacing(6);
        verticalLayout_10->setObjectName(QString::fromUtf8("verticalLayout_10"));
        label_6 = new QLabel(verticalLayoutWidget);
        label_6->setObjectName(QString::fromUtf8("label_6"));
        label_6->setFont(font);

        verticalLayout_10->addWidget(label_6);

        horizontalLayout_10 = new QHBoxLayout();
        horizontalLayout_10->setSpacing(6);
        horizontalLayout_10->setObjectName(QString::fromUtf8("horizontalLayout_10"));
        oui = new QPushButton(verticalLayoutWidget);
        oui->setObjectName(QString::fromUtf8("oui"));

        horizontalLayout_10->addWidget(oui);

        non = new QPushButton(verticalLayoutWidget);
        non->setObjectName(QString::fromUtf8("non"));

        horizontalLayout_10->addWidget(non);

        au_revoir = new QPushButton(verticalLayoutWidget);
        au_revoir->setObjectName(QString::fromUtf8("au_revoir"));

        horizontalLayout_10->addWidget(au_revoir);


        verticalLayout_10->addLayout(horizontalLayout_10);


        verticalLayout->addLayout(verticalLayout_10);

        verticalLayout_5 = new QVBoxLayout();
        verticalLayout_5->setSpacing(6);
        verticalLayout_5->setObjectName(QString::fromUtf8("verticalLayout_5"));
        label_4 = new QLabel(verticalLayoutWidget);
        label_4->setObjectName(QString::fromUtf8("label_4"));
        label_4->setFont(font);

        verticalLayout_5->addWidget(label_4);

        horizontalLayout_6 = new QHBoxLayout();
        horizontalLayout_6->setSpacing(6);
        horizontalLayout_6->setObjectName(QString::fromUtf8("horizontalLayout_6"));
        cest_pas_grave = new QPushButton(verticalLayoutWidget);
        cest_pas_grave->setObjectName(QString::fromUtf8("cest_pas_grave"));

        horizontalLayout_6->addWidget(cest_pas_grave);

        pause = new QPushButton(verticalLayoutWidget);
        pause->setObjectName(QString::fromUtf8("pause"));

        horizontalLayout_6->addWidget(pause);

        respire = new QPushButton(verticalLayoutWidget);
        respire->setObjectName(QString::fromUtf8("respire"));

        horizontalLayout_6->addWidget(respire);

        air_en_colere = new QPushButton(verticalLayoutWidget);
        air_en_colere->setObjectName(QString::fromUtf8("air_en_colere"));

        horizontalLayout_6->addWidget(air_en_colere);


        verticalLayout_5->addLayout(horizontalLayout_6);


        verticalLayout->addLayout(verticalLayout_5);

        verticalLayoutWidget_9 = new QWidget(centralWidget);
        verticalLayoutWidget_9->setObjectName(QString::fromUtf8("verticalLayoutWidget_9"));
        verticalLayoutWidget_9->setGeometry(QRect(620, 0, 611, 41));
        verticalLayout_11 = new QVBoxLayout(verticalLayoutWidget_9);
        verticalLayout_11->setSpacing(6);
        verticalLayout_11->setContentsMargins(11, 11, 11, 11);
        verticalLayout_11->setObjectName(QString::fromUtf8("verticalLayout_11"));
        verticalLayout_11->setContentsMargins(0, 0, 0, 0);
        label_7 = new QLabel(verticalLayoutWidget_9);
        label_7->setObjectName(QString::fromUtf8("label_7"));
        QFont font1;
        font1.setPointSize(20);
        font1.setBold(true);
        font1.setWeight(75);
        label_7->setFont(font1);

        verticalLayout_11->addWidget(label_7, 0, Qt::AlignHCenter|Qt::AlignVCenter);

        MainWindow->setCentralWidget(centralWidget);
        menuBar = new QMenuBar(MainWindow);
        menuBar->setObjectName(QString::fromUtf8("menuBar"));
        menuBar->setGeometry(QRect(0, 0, 1267, 25));
        MainWindow->setMenuBar(menuBar);
        mainToolBar = new QToolBar(MainWindow);
        mainToolBar->setObjectName(QString::fromUtf8("mainToolBar"));
        MainWindow->addToolBar(Qt::TopToolBarArea, mainToolBar);
        statusBar = new QStatusBar(MainWindow);
        statusBar->setObjectName(QString::fromUtf8("statusBar"));
        MainWindow->setStatusBar(statusBar);

        retranslateUi(MainWindow);

        QMetaObject::connectSlotsByName(MainWindow);
    } // setupUi

    void retranslateUi(QMainWindow *MainWindow)
    {
        MainWindow->setWindowTitle(QApplication::translate("MainWindow", "MainWindow", 0, QApplication::UnicodeUTF8));
        label->setText(QApplication::translate("MainWindow", "SE DEFEND", 0, QApplication::UnicodeUTF8));
        muscle->setText(QApplication::translate("MainWindow", "muscle", 0, QApplication::UnicodeUTF8));
        progresse->setText(QApplication::translate("MainWindow", "progresse", 0, QApplication::UnicodeUTF8));
        alors->setText(QApplication::translate("MainWindow", "et alors", 0, QApplication::UnicodeUTF8));
        fai_mon_mieux->setText(QApplication::translate("MainWindow", "fais mon mieux", 0, QApplication::UnicodeUTF8));
        label_5->setText(QApplication::translate("MainWindow", "VALORISATION", 0, QApplication::UnicodeUTF8));
        bien->setText(QApplication::translate("MainWindow", "c'est bien", 0, QApplication::UnicodeUTF8));
        bien_joue->setText(QApplication::translate("MainWindow", "bien joue", 0, QApplication::UnicodeUTF8));
        felicitation->setText(QApplication::translate("MainWindow", "felicitation", 0, QApplication::UnicodeUTF8));
        bcp_travaille->setText(QApplication::translate("MainWindow", "bcp travaille", 0, QApplication::UnicodeUTF8));
        trop_fort->setText(QApplication::translate("MainWindow", "trop fort", 0, QApplication::UnicodeUTF8));
        bravo->setText(QApplication::translate("MainWindow", "bravo", 0, QApplication::UnicodeUTF8));
        moi_trop_fort->setText(QApplication::translate("MainWindow", "moi trop fort", 0, QApplication::UnicodeUTF8));
        label_2->setText(QApplication::translate("MainWindow", "PAS EN FORME", 0, QApplication::UnicodeUTF8));
        malade->setText(QApplication::translate("MainWindow", "malade", 0, QApplication::UnicodeUTF8));
        ecris_mal->setText(QApplication::translate("MainWindow", "ecris mal", 0, QApplication::UnicodeUTF8));
        pas_compris->setText(QApplication::translate("MainWindow", "pas compris", 0, QApplication::UnicodeUTF8));
        repete->setText(QApplication::translate("MainWindow", "repeter", 0, QApplication::UnicodeUTF8));
        fatigue->setText(QApplication::translate("MainWindow", "fatigue", 0, QApplication::UnicodeUTF8));
        label_3->setText(QApplication::translate("MainWindow", "META-COG", 0, QApplication::UnicodeUTF8));
        sort_traj->setText(QApplication::translate("MainWindow", "sort traj", 0, QApplication::UnicodeUTF8));
        montre_traj->setText(QApplication::translate("MainWindow", "montre traj", 0, QApplication::UnicodeUTF8));
        touche_bomb->setText(QApplication::translate("MainWindow", "touche bomb", 0, QApplication::UnicodeUTF8));
        label_6->setText(QApplication::translate("MainWindow", "BAVARD", 0, QApplication::UnicodeUTF8));
        oui->setText(QApplication::translate("MainWindow", "oui", 0, QApplication::UnicodeUTF8));
        non->setText(QApplication::translate("MainWindow", "non", 0, QApplication::UnicodeUTF8));
        au_revoir->setText(QApplication::translate("MainWindow", "au revoir", 0, QApplication::UnicodeUTF8));
        label_4->setText(QApplication::translate("MainWindow", "ENCOURAGEMENT", 0, QApplication::UnicodeUTF8));
        cest_pas_grave->setText(QApplication::translate("MainWindow", "c'est pas grave", 0, QApplication::UnicodeUTF8));
        pause->setText(QApplication::translate("MainWindow", "pause", 0, QApplication::UnicodeUTF8));
        respire->setText(QApplication::translate("MainWindow", "respirer", 0, QApplication::UnicodeUTF8));
        air_en_colere->setText(QApplication::translate("MainWindow", "air en colere", 0, QApplication::UnicodeUTF8));
        label_7->setText(QApplication::translate("MainWindow", "CONTROLE ROBOT", 0, QApplication::UnicodeUTF8));
    } // retranslateUi

};

namespace Ui {
    class MainWindow: public Ui_MainWindow {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_MAINWINDOW_H
