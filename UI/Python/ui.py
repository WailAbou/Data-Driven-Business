# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../QT/ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 720)
        MainWindow.setMinimumSize(QtCore.QSize(1280, 720))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_2.setContentsMargins(-1, 0, -1, -1)
        self.gridLayout_2.setVerticalSpacing(15)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.plusButton = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plusButton.sizePolicy().hasHeightForWidth())
        self.plusButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setKerning(True)
        self.plusButton.setFont(font)
        self.plusButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.plusButton.setObjectName("plusButton")
        self.gridLayout_2.addWidget(self.plusButton, 2, 1, 1, 1)
        self.minusButton = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.minusButton.sizePolicy().hasHeightForWidth())
        self.minusButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.minusButton.setFont(font)
        self.minusButton.setObjectName("minusButton")
        self.gridLayout_2.addWidget(self.minusButton, 2, 0, 1, 1)
        self.overviewList = QtWidgets.QListWidget(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.overviewList.sizePolicy().hasHeightForWidth())
        self.overviewList.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.overviewList.setFont(font)
        self.overviewList.setObjectName("overviewList")
        self.gridLayout_2.addWidget(self.overviewList, 1, 0, 1, 2)
        self.incidentsLabel = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.incidentsLabel.setFont(font)
        self.incidentsLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.incidentsLabel.setObjectName("incidentsLabel")
        self.gridLayout_2.addWidget(self.incidentsLabel, 0, 0, 1, 2)
        self.gridLayout_2.setRowStretch(0, 1)
        self.gridLayout_2.setRowStretch(1, 9)
        self.gridLayout_2.setRowStretch(2, 1)
        self.gridLayout_4.addWidget(self.frame, 0, 0, 1, 1)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_3.setContentsMargins(-1, 0, -1, -1)
        self.gridLayout_3.setVerticalSpacing(15)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.mapLabel = QtWidgets.QLabel(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mapLabel.sizePolicy().hasHeightForWidth())
        self.mapLabel.setSizePolicy(sizePolicy)
        self.mapLabel.setMinimumSize(QtCore.QSize(0, 0))
        self.mapLabel.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.mapLabel.setText("")
        self.mapLabel.setPixmap(QtGui.QPixmap("../QT\\../../Data/Images/base.jpg"))
        self.mapLabel.setScaledContents(True)
        self.mapLabel.setObjectName("mapLabel")
        self.gridLayout_3.addWidget(self.mapLabel, 1, 0, 1, 1)
        self.oorzaakcode = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.oorzaakcode.setFont(font)
        self.oorzaakcode.setAlignment(QtCore.Qt.AlignCenter)
        self.oorzaakcode.setObjectName("oorzaakcode")
        self.gridLayout_3.addWidget(self.oorzaakcode, 0, 0, 1, 1)
        self.gridLayout_3.setRowStretch(0, 1)
        self.gridLayout_3.setRowStretch(1, 10)
        self.gridLayout_4.addWidget(self.frame_2, 0, 1, 1, 1)
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_3)
        self.gridLayout.setContentsMargins(-1, 0, -1, -1)
        self.gridLayout.setVerticalSpacing(15)
        self.gridLayout.setObjectName("gridLayout")
        self.frame_4 = QtWidgets.QFrame(self.frame_3)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.frame_4)
        self.gridLayout_5.setVerticalSpacing(12)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_6 = QtWidgets.QLabel(self.frame_4)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.gridLayout_5.addWidget(self.label_6, 4, 0, 1, 1)
        self.beschrijving = QtWidgets.QTextEdit(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.beschrijving.sizePolicy().hasHeightForWidth())
        self.beschrijving.setSizePolicy(sizePolicy)
        self.beschrijving.setMaximumSize(QtCore.QSize(16777215, 100))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.beschrijving.setFont(font)
        self.beschrijving.setObjectName("beschrijving")
        self.gridLayout_5.addWidget(self.beschrijving, 4, 1, 1, 2)
        self.saveButton = QtWidgets.QPushButton(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.saveButton.sizePolicy().hasHeightForWidth())
        self.saveButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setUnderline(False)
        self.saveButton.setFont(font)
        self.saveButton.setObjectName("saveButton")
        self.gridLayout_5.addWidget(self.saveButton, 5, 1, 1, 2)
        self.prioriteit = QtWidgets.QTextEdit(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.prioriteit.sizePolicy().hasHeightForWidth())
        self.prioriteit.setSizePolicy(sizePolicy)
        self.prioriteit.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.prioriteit.setFont(font)
        self.prioriteit.setReadOnly(False)
        self.prioriteit.setObjectName("prioriteit")
        self.gridLayout_5.addWidget(self.prioriteit, 0, 1, 1, 2)
        self.label_2 = QtWidgets.QLabel(self.frame_4)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout_5.addWidget(self.label_2, 0, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.frame_4)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout_5.addWidget(self.label_3, 1, 0, 1, 1)
        self.geocode = QtWidgets.QTextEdit(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.geocode.sizePolicy().hasHeightForWidth())
        self.geocode.setSizePolicy(sizePolicy)
        self.geocode.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.geocode.setFont(font)
        self.geocode.setObjectName("geocode")
        self.gridLayout_5.addWidget(self.geocode, 3, 1, 1, 2)
        self.label_4 = QtWidgets.QLabel(self.frame_4)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout_5.addWidget(self.label_4, 2, 0, 1, 1)
        self.hersteltijd = QtWidgets.QTextEdit(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.hersteltijd.sizePolicy().hasHeightForWidth())
        self.hersteltijd.setSizePolicy(sizePolicy)
        self.hersteltijd.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.hersteltijd.setFont(font)
        self.hersteltijd.setObjectName("hersteltijd")
        self.gridLayout_5.addWidget(self.hersteltijd, 2, 1, 1, 2)
        self.label_5 = QtWidgets.QLabel(self.frame_4)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout_5.addWidget(self.label_5, 3, 0, 1, 1)
        self.melddatum = QtWidgets.QTextEdit(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.melddatum.sizePolicy().hasHeightForWidth())
        self.melddatum.setSizePolicy(sizePolicy)
        self.melddatum.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.melddatum.setFont(font)
        self.melddatum.setObjectName("melddatum")
        self.gridLayout_5.addWidget(self.melddatum, 1, 1, 1, 2)
        self.gridLayout.addWidget(self.frame_4, 2, 0, 1, 2)
        self.logoLabel = QtWidgets.QLabel(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.logoLabel.sizePolicy().hasHeightForWidth())
        self.logoLabel.setSizePolicy(sizePolicy)
        self.logoLabel.setMinimumSize(QtCore.QSize(125, 0))
        self.logoLabel.setMaximumSize(QtCore.QSize(150, 16777215))
        self.logoLabel.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.logoLabel.setText("")
        self.logoLabel.setPixmap(QtGui.QPixmap("../QT\\../../Data/Images/ns.png"))
        self.logoLabel.setScaledContents(True)
        self.logoLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.logoLabel.setObjectName("logoLabel")
        self.gridLayout.addWidget(self.logoLabel, 3, 1, 1, 1)
        self.dataLabel = QtWidgets.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.dataLabel.setFont(font)
        self.dataLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.dataLabel.setObjectName("dataLabel")
        self.gridLayout.addWidget(self.dataLabel, 0, 0, 1, 2)
        self.frame_5 = QtWidgets.QFrame(self.frame_3)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.frame_5)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.hersteltijd_lr = QtWidgets.QLabel(self.frame_5)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.hersteltijd_lr.setFont(font)
        self.hersteltijd_lr.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.hersteltijd_lr.setObjectName("hersteltijd_lr")
        self.gridLayout_6.addWidget(self.hersteltijd_lr, 3, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.frame_5)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout_6.addWidget(self.label, 2, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.frame_5)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.gridLayout_6.addWidget(self.label_8, 4, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.frame_5)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.gridLayout_6.addWidget(self.label_7, 3, 0, 1, 1)
        self.hersteltijd_knn = QtWidgets.QLabel(self.frame_5)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.hersteltijd_knn.setFont(font)
        self.hersteltijd_knn.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.hersteltijd_knn.setObjectName("hersteltijd_knn")
        self.gridLayout_6.addWidget(self.hersteltijd_knn, 4, 1, 1, 1)
        self.hersteltijd_dt = QtWidgets.QLabel(self.frame_5)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.hersteltijd_dt.setFont(font)
        self.hersteltijd_dt.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.hersteltijd_dt.setObjectName("hersteltijd_dt")
        self.gridLayout_6.addWidget(self.hersteltijd_dt, 2, 1, 1, 1)
        self.line_2 = QtWidgets.QFrame(self.frame_5)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout_6.addWidget(self.line_2, 1, 0, 1, 2)
        self.line = QtWidgets.QFrame(self.frame_5)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout_6.addWidget(self.line, 5, 0, 1, 2)
        self.gridLayout.addWidget(self.frame_5, 1, 0, 1, 2)
        self.gridLayout.setRowStretch(0, 1)
        self.gridLayout.setRowStretch(1, 2)
        self.gridLayout.setRowStretch(2, 7)
        self.gridLayout.setRowStretch(3, 1)
        self.gridLayout_4.addWidget(self.frame_3, 0, 2, 1, 1)
        self.gridLayout_4.setColumnStretch(0, 2)
        self.gridLayout_4.setColumnStretch(1, 3)
        self.gridLayout_4.setColumnStretch(2, 2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.plusButton.setText(_translate("MainWindow", "+"))
        self.minusButton.setText(_translate("MainWindow", "-"))
        self.incidentsLabel.setText(_translate("MainWindow", "Incidenten"))
        self.oorzaakcode.setText(_translate("MainWindow", "Oorzaak"))
        self.label_6.setText(_translate("MainWindow", "Beschrijving:"))
        self.saveButton.setText(_translate("MainWindow", "Opslaan"))
        self.label_2.setText(_translate("MainWindow", "Prioriteit:"))
        self.label_3.setText(_translate("MainWindow", "Melddatum:"))
        self.label_4.setText(_translate("MainWindow", "Hersteltijd:"))
        self.label_5.setText(_translate("MainWindow", "Geocode:"))
        self.dataLabel.setText(_translate("MainWindow", "Gegevens"))
        self.hersteltijd_lr.setText(_translate("MainWindow", "N.V.T."))
        self.label.setText(_translate("MainWindow", "Decision Tree:"))
        self.label_8.setText(_translate("MainWindow", "KNN:"))
        self.label_7.setText(_translate("MainWindow", "Logistic Regression:"))
        self.hersteltijd_knn.setText(_translate("MainWindow", "N.V.T."))
        self.hersteltijd_dt.setText(_translate("MainWindow", "N.V.T."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
