# Form implementation generated from reading ui file '/Users/kzz6991/Nutstore Files/.symlinks/坚果云/scripts/MultimeterController/MultimeterWindow.ui'
#
# Created by: PyQt6 UI code generator 6.4.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MultimeterMainWindow(object):
    def setupUi(self, MultimeterMainWindow):
        MultimeterMainWindow.setObjectName("MultimeterMainWindow")
        MultimeterMainWindow.resize(676, 366)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MultimeterMainWindow.sizePolicy().hasHeightForWidth())
        MultimeterMainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MultimeterMainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.figure_box = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.figure_box.sizePolicy().hasHeightForWidth())
        self.figure_box.setSizePolicy(sizePolicy)
        self.figure_box.setObjectName("figure_box")
        self.horizontalLayout.addWidget(self.figure_box)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.start_button = QtWidgets.QPushButton(self.centralwidget)
        self.start_button.setObjectName("start_button")
        self.verticalLayout.addWidget(self.start_button)
        self.close_button = QtWidgets.QPushButton(self.centralwidget)
        self.close_button.setObjectName("close_button")
        self.verticalLayout.addWidget(self.close_button)
        self.camera_combo = QtWidgets.QComboBox(self.centralwidget)
        self.camera_combo.setObjectName("camera_combo")
        self.verticalLayout.addWidget(self.camera_combo)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.vertival_scale_dial = QtWidgets.QDial(self.centralwidget)
        self.vertival_scale_dial.setWrapping(True)
        self.vertival_scale_dial.setObjectName("vertival_scale_dial")
        self.horizontalLayout_2.addWidget(self.vertival_scale_dial)
        self.vertical_scale_label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.vertical_scale_label.sizePolicy().hasHeightForWidth())
        self.vertical_scale_label.setSizePolicy(sizePolicy)
        self.vertical_scale_label.setObjectName("vertical_scale_label")
        self.horizontalLayout_2.addWidget(self.vertical_scale_label)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout.addLayout(self.verticalLayout)
        MultimeterMainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MultimeterMainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 676, 24))
        self.menubar.setObjectName("menubar")
        MultimeterMainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MultimeterMainWindow)
        self.statusbar.setObjectName("statusbar")
        MultimeterMainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MultimeterMainWindow)
        QtCore.QMetaObject.connectSlotsByName(MultimeterMainWindow)

    def retranslateUi(self, MultimeterMainWindow):
        _translate = QtCore.QCoreApplication.translate
        MultimeterMainWindow.setWindowTitle(_translate("MultimeterMainWindow", "MainWindow"))
        self.figure_box.setTitle(_translate("MultimeterMainWindow", "plot view"))
        self.start_button.setText(_translate("MultimeterMainWindow", "Start/Stop"))
        self.close_button.setText(_translate("MultimeterMainWindow", "Close"))
        self.vertical_scale_label.setText(_translate("MultimeterMainWindow", "vertical Scale"))