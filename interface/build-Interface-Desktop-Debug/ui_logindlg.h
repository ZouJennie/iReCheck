/********************************************************************************
** Form generated from reading UI file 'logindlg.ui'
**
** Created by: Qt User Interface Compiler version 4.8.7
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_LOGINDLG_H
#define UI_LOGINDLG_H

#include <QtCore/QVariant>
#include <QtGui/QAction>
#include <QtGui/QApplication>
#include <QtGui/QButtonGroup>
#include <QtGui/QDialog>
#include <QtGui/QGridLayout>
#include <QtGui/QHeaderView>
#include <QtGui/QLabel>
#include <QtGui/QLineEdit>
#include <QtGui/QPushButton>
#include <QtGui/QWidget>

QT_BEGIN_NAMESPACE

class Ui_loginDlg
{
public:
    QWidget *gridLayoutWidget;
    QGridLayout *gridLayout;
    QLineEdit *usrLineEdit;
    QLabel *label;
    QLabel *label_2;
    QLineEdit *usrLineEdit_2;
    QPushButton *LoginBtn;

    void setupUi(QDialog *loginDlg)
    {
        if (loginDlg->objectName().isEmpty())
            loginDlg->setObjectName(QString::fromUtf8("loginDlg"));
        loginDlg->resize(400, 300);
        gridLayoutWidget = new QWidget(loginDlg);
        gridLayoutWidget->setObjectName(QString::fromUtf8("gridLayoutWidget"));
        gridLayoutWidget->setGeometry(QRect(110, 80, 181, 101));
        gridLayout = new QGridLayout(gridLayoutWidget);
        gridLayout->setObjectName(QString::fromUtf8("gridLayout"));
        gridLayout->setContentsMargins(0, 0, 0, 0);
        usrLineEdit = new QLineEdit(gridLayoutWidget);
        usrLineEdit->setObjectName(QString::fromUtf8("usrLineEdit"));

        gridLayout->addWidget(usrLineEdit, 0, 1, 1, 1);

        label = new QLabel(gridLayoutWidget);
        label->setObjectName(QString::fromUtf8("label"));

        gridLayout->addWidget(label, 0, 0, 1, 1);

        label_2 = new QLabel(gridLayoutWidget);
        label_2->setObjectName(QString::fromUtf8("label_2"));

        gridLayout->addWidget(label_2, 1, 0, 1, 1);

        usrLineEdit_2 = new QLineEdit(gridLayoutWidget);
        usrLineEdit_2->setObjectName(QString::fromUtf8("usrLineEdit_2"));

        gridLayout->addWidget(usrLineEdit_2, 1, 1, 1, 1);

        LoginBtn = new QPushButton(loginDlg);
        LoginBtn->setObjectName(QString::fromUtf8("LoginBtn"));
        LoginBtn->setGeometry(QRect(140, 210, 99, 27));

        retranslateUi(loginDlg);

        QMetaObject::connectSlotsByName(loginDlg);
    } // setupUi

    void retranslateUi(QDialog *loginDlg)
    {
        loginDlg->setWindowTitle(QApplication::translate("loginDlg", "Dialog", 0, QApplication::UnicodeUTF8));
        label->setText(QApplication::translate("loginDlg", "Nom:", 0, QApplication::UnicodeUTF8));
        label_2->setText(QApplication::translate("loginDlg", "Prenom:", 0, QApplication::UnicodeUTF8));
        LoginBtn->setText(QApplication::translate("loginDlg", "Login", 0, QApplication::UnicodeUTF8));
    } // retranslateUi

};

namespace Ui {
    class loginDlg: public Ui_loginDlg {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_LOGINDLG_H
