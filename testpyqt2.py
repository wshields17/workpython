# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test2.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1800, 1000)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Compbutton = QtWidgets.QPushButton(self.centralwidget)
        self.Compbutton.setGeometry(QtCore.QRect(460, 90, 191, 71))
        self.Compbutton.setObjectName("Compbutton")
        self.Max = QtWidgets.QTextEdit(self.centralwidget)
        self.Max.setGeometry(QtCore.QRect(9, 9, 351, 167))
        self.Max.setObjectName("Max")
        self.Percentage = QtWidgets.QTextEdit(self.centralwidget)
        self.Percentage.setGeometry(QtCore.QRect(9, 182, 351, 166))
        self.Percentage.setObjectName("Percentage")
        self.OutWeight = QtWidgets.QTextEdit(self.centralwidget)
        self.OutWeight.setGeometry(QtCore.QRect(9, 354, 351, 167))
        self.OutWeight.setObjectName("OutWeight")
        self.table1 = QtWidgets.QTableWidget(self.centralwidget)
        self.table1.setGeometry(QtCore.QRect(430, 240, 900, 600))
        self.table1.setObjectName("table1")
        self.table1.setColumnCount(0)
        self.table1.setRowCount(0)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 937, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Compbutton.setText(_translate("MainWindow", "Compute"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))

