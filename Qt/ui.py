# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainui/mainwindow.ui'
#
# Created: Wed Sep 23 22:52:13 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 400)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralWidget = QtGui.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.centralWidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName("verticalLayout")
        self.filters = QtGui.QHBoxLayout()
        self.filters.setSizeConstraint(QtGui.QLayout.SetMinimumSize)
        self.filters.setObjectName("filters")
        self.label_4 = QtGui.QLabel(self.centralWidget)
        self.label_4.setObjectName("label_4")
        self.filters.addWidget(self.label_4)
        self.numPackets = QtGui.QSpinBox(self.centralWidget)
        self.numPackets.setMinimum(1)
        self.numPackets.setMaximum(25)
        self.numPackets.setProperty("value", 10)
        self.numPackets.setObjectName("numPackets")
        self.filters.addWidget(self.numPackets)
        self.label = QtGui.QLabel(self.centralWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.filters.addWidget(self.label)
        self.ipAddress = QtGui.QLineEdit(self.centralWidget)
        self.ipAddress.setMinimumSize(QtCore.QSize(100, 0))
        self.ipAddress.setInputMethodHints(QtCore.Qt.ImhNone)
        self.ipAddress.setMaxLength(15)
        self.ipAddress.setCursorPosition(0)
        self.ipAddress.setObjectName("ipAddress")
        self.filters.addWidget(self.ipAddress)
        self.label_2 = QtGui.QLabel(self.centralWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setObjectName("label_2")
        self.filters.addWidget(self.label_2)
        self.protocol = QtGui.QLineEdit(self.centralWidget)
        self.protocol.setMinimumSize(QtCore.QSize(30, 0))
        self.protocol.setInputMask("")
        self.protocol.setMaxLength(3)
        self.protocol.setObjectName("protocol")
        self.filters.addWidget(self.protocol)
        self.label_3 = QtGui.QLabel(self.centralWidget)
        self.label_3.setObjectName("label_3")
        self.filters.addWidget(self.label_3)
        self.port = QtGui.QLineEdit(self.centralWidget)
        self.port.setMinimumSize(QtCore.QSize(50, 0))
        self.port.setInputMethodHints(QtCore.Qt.ImhNone)
        self.port.setMaxLength(5)
        self.port.setObjectName("port")
        self.filters.addWidget(self.port)
        self.verticalLayout.addLayout(self.filters)
        self.startButton = QtGui.QPushButton(self.centralWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.startButton.sizePolicy().hasHeightForWidth())
        self.startButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.startButton.setFont(font)
        self.startButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.startButton.setAutoFillBackground(False)
        self.startButton.setDefault(True)
        self.startButton.setFlat(False)
        self.startButton.setObjectName("startButton")
        self.verticalLayout.addWidget(self.startButton)
        self.buttons = QtGui.QHBoxLayout()
        self.buttons.setObjectName("buttons")
        self.verticalLayout.addLayout(self.buttons)
        self.tableView = QtGui.QTableView(self.centralWidget)
        self.tableView.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.tableView.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tableView.setObjectName("tableView")
        self.verticalLayout.addWidget(self.tableView)
        self.payLoad = QtGui.QPlainTextEdit(self.centralWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.payLoad.sizePolicy().hasHeightForWidth())
        self.payLoad.setSizePolicy(sizePolicy)
        self.payLoad.setMaximumSize(QtCore.QSize(16777215, 400))
        self.payLoad.setReadOnly(True)
        self.payLoad.setObjectName("payLoad")
        self.verticalLayout.addWidget(self.payLoad)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtGui.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 600, 20))
        self.menuBar.setObjectName("menuBar")
        MainWindow.setMenuBar(self.menuBar)
        self.statusBar = QtGui.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Cyprin", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("MainWindow", "Paquets", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Adresse IP", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "Protocole", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("MainWindow", "Port", None, QtGui.QApplication.UnicodeUTF8))
        self.startButton.setText(QtGui.QApplication.translate("MainWindow", "Lancer la capture", None, QtGui.QApplication.UnicodeUTF8))
