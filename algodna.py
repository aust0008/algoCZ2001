# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Sandra\Desktop\algodna.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(819, 598)
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 16777213))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.input_lbl = QtWidgets.QLabel(self.centralwidget)
        self.input_lbl.setGeometry(QtCore.QRect(180, 260, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.input_lbl.setFont(font)
        self.input_lbl.setObjectName("input_lbl")
        self.uploadBtn = QtWidgets.QToolButton(self.centralwidget)
        self.uploadBtn.setGeometry(QtCore.QRect(530, 180, 111, 31))
        self.uploadBtn.setObjectName("uploadBtn")
        self.file_lbl = QtWidgets.QLabel(self.centralwidget)
        self.file_lbl.setGeometry(QtCore.QRect(180, 120, 100, 20))
        self.file_lbl.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.file_lbl.setFont(font)
        self.file_lbl.setObjectName("file_lbl")
        self.submitBtn = QtWidgets.QPushButton(self.centralwidget)
        self.submitBtn.setGeometry(QtCore.QRect(530, 322, 111, 31))
        self.submitBtn.setObjectName("submitBtn")
        self.fileUploadTxt = QtWidgets.QLineEdit(self.centralwidget)
        self.fileUploadTxt.setGeometry(QtCore.QRect(340, 100, 301, 71))
        self.fileUploadTxt.setObjectName("fileUploadTxt")
        self.output_lbl = QtWidgets.QLabel(self.centralwidget)
        self.output_lbl.setGeometry(QtCore.QRect(180, 380, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.output_lbl.setFont(font)
        self.output_lbl.setObjectName("output_lbl")
        self.outputTxt = QtWidgets.QTextEdit(self.centralwidget)
        self.outputTxt.setEnabled(False)
        self.outputTxt.setGeometry(QtCore.QRect(340, 385, 301, 141))
        self.outputTxt.setObjectName("outputTxt")
        self.inputTxt = QtWidgets.QLineEdit(self.centralwidget)
        self.inputTxt.setGeometry(QtCore.QRect(340, 240, 301, 71))
        self.inputTxt.setObjectName("inputTxt")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 819, 18))
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
        self.input_lbl.setText(_translate("MainWindow", "Input:"))
        self.uploadBtn.setText(_translate("MainWindow", "Choose File"))
        self.file_lbl.setText(_translate("MainWindow", "File Name:"))
        self.submitBtn.setText(_translate("MainWindow", "Submit"))
        self.output_lbl.setText(_translate("MainWindow", "Output:"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
