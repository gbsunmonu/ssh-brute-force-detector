# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'myui.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(860, 751)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButtonOpenPcap = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonOpenPcap.setGeometry(QtCore.QRect(230, 550, 113, 32))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.pushButtonOpenPcap.setFont(font)
        self.pushButtonOpenPcap.setObjectName("pushButtonOpenPcap")
        self.pushButtonDetail = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonDetail.setGeometry(QtCore.QRect(510, 550, 113, 32))
        self.pushButtonDetail.setObjectName("pushButtonCancel")
        self.packetNumberDprocessNumber = QtWidgets.QLabel(self.centralwidget)
        self.packetNumberDprocessNumber.setEnabled(True)
        self.packetNumberDprocessNumber.setGeometry(QtCore.QRect(50, 10, 300, 16))
        self.packetNumberDprocessNumber.setObjectName("packetNumberDprocessNumber")
        self.packetSizeDpacketCount = QtWidgets.QLabel(self.centralwidget)
        self.packetSizeDpacketCount.setEnabled(True)
        self.packetSizeDpacketCount.setGeometry(QtCore.QRect(50, 280, 300, 16))
        self.packetSizeDpacketCount.setObjectName("packetSizeDpacketCount")
        self.packetSizeDpacketCount_frame = QtWidgets.QGraphicsView(self.centralwidget)
        self.packetSizeDpacketCount_frame.setEnabled(True)
        self.packetSizeDpacketCount_frame.setGeometry(QtCore.QRect(10, 30, 831, 251))
        self.packetSizeDpacketCount_frame.setObjectName("packetSizeDpacketCount_frame")
        self.packetNumberDprocessNumber_frame = QtWidgets.QGraphicsView(self.centralwidget)
        self.packetNumberDprocessNumber_frame.setEnabled(True)
        self.packetNumberDprocessNumber_frame.setGeometry(QtCore.QRect(10, 300, 831, 241))
        self.packetNumberDprocessNumber_frame.setObjectName("packetNumberDprocessNumber_frame")
        self.summary = QtWidgets.QTextBrowser(self.centralwidget)
        self.summary.setGeometry(QtCore.QRect(390, 590, 451, 111))
        self.summary.setObjectName("summary")
        self.pcapSelected = QtWidgets.QTextBrowser(self.centralwidget)
        self.pcapSelected.setEnabled(True)
        self.pcapSelected.setGeometry(QtCore.QRect(10, 590, 361, 111))
        self.pcapSelected.setObjectName("pcapSelected")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 860, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButtonOpenPcap.setText(_translate("MainWindow", "Open Pcap"))
        self.pushButtonDetail.setText(_translate("MainWindow", "Detail"))
        self.packetNumberDprocessNumber.setText(_translate("MainWindow", "avgpacketsizebycount"))
        self.packetSizeDpacketCount.setText(_translate("MainWindow", "avgpacketsizebythread"))
