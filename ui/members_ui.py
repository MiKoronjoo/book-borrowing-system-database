# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'members.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MembersWindow(object):
    def setupUi(self, MembersWindow):
        MembersWindow.setObjectName("MembersWindow")
        MembersWindow.resize(700, 400)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("bbs-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MembersWindow.setWindowIcon(icon)
        MembersWindow.setStyleSheet("background-color: rgb(148, 226, 194);")
        self.centralwidget = QtWidgets.QWidget(MembersWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.IDEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.IDEdit.setGeometry(QtCore.QRect(60, 110, 91, 25))
        self.IDEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.IDEdit.setInputMask("")
        self.IDEdit.setText("")
        self.IDEdit.setObjectName("IDEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60, 90, 121, 17))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(170, 90, 121, 17))
        self.label_2.setObjectName("label_2")
        self.NameEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.NameEdit.setGeometry(QtCore.QRect(170, 110, 221, 25))
        self.NameEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.NameEdit.setInputMask("")
        self.NameEdit.setText("")
        self.NameEdit.setObjectName("NameEdit")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(60, 150, 121, 17))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(500, 90, 151, 17))
        self.label_4.setObjectName("label_4")
        self.MaxCreditEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.MaxCreditEdit.setGeometry(QtCore.QRect(500, 110, 151, 25))
        self.MaxCreditEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.MaxCreditEdit.setInputMask("")
        self.MaxCreditEdit.setText("")
        self.MaxCreditEdit.setObjectName("MaxCreditEdit")
        self.AddressEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.AddressEdit.setGeometry(QtCore.QRect(270, 170, 381, 25))
        self.AddressEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.AddressEdit.setInputMask("")
        self.AddressEdit.setText("")
        self.AddressEdit.setObjectName("AddressEdit")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(280, 150, 121, 17))
        self.label_5.setObjectName("label_5")
        self.mainLabel = QtWidgets.QLabel(self.centralwidget)
        self.mainLabel.setGeometry(QtCore.QRect(0, 20, 701, 51))
        font = QtGui.QFont()
        font.setPointSize(35)
        font.setBold(True)
        font.setWeight(75)
        self.mainLabel.setFont(font)
        self.mainLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.mainLabel.setStyleSheet("background-color: rgba(0, 0, 0, 0);")
        self.mainLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.mainLabel.setObjectName("mainLabel")
        self.console = QtWidgets.QTextBrowser(self.centralwidget)
        self.console.setGeometry(QtCore.QRect(60, 280, 591, 91))
        self.console.setObjectName("console")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(410, 90, 81, 20))
        self.label_8.setObjectName("label_8")
        self.AgeEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.AgeEdit.setGeometry(QtCore.QRect(410, 110, 71, 25))
        self.AgeEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.AgeEdit.setInputMask("")
        self.AgeEdit.setText("")
        self.AgeEdit.setObjectName("AgeEdit")
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(self.centralwidget)
        self.dateTimeEdit.setGeometry(QtCore.QRect(60, 170, 194, 26))
        self.dateTimeEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.dateTimeEdit.setDate(QtCore.QDate(2021, 1, 1))
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.submitButton = QtWidgets.QPushButton(self.centralwidget)
        self.submitButton.setGeometry(QtCore.QRect(610, 220, 41, 41))
        self.submitButton.setStyleSheet("QPushButton {\n"
                                        "border-image: url(icons/plus.png);\n"
                                        "}\n"
                                        "QPushButton:hover {\n"
                                        "border-image: url(icons/plus-hover.png);\n"
                                        "}\n"
                                        "QPushButton:pressed {\n"
                                        "border-image: url(icons/plus-pressed.png);\n"
                                        "}")
        self.submitButton.setText("")
        self.submitButton.setObjectName("submitButton")
        self.deleteButton = QtWidgets.QPushButton(self.centralwidget)
        self.deleteButton.setGeometry(QtCore.QRect(610, 40, 41, 41))
        self.deleteButton.setStyleSheet("QPushButton {\n"
                                        "border-image: url(icons/remove.png);\n"
                                        "}\n"
                                        "QPushButton:hover {\n"
                                        "border-image: url(icons/remove-hover.png);\n"
                                        "}\n"
                                        "QPushButton:pressed {\n"
                                        "border-image: url(icons/remove-pressed.png);\n"
                                        "}")
        self.deleteButton.setText("")
        self.deleteButton.setObjectName("deleteButton")
        self.refreshButton = QtWidgets.QPushButton(self.centralwidget)
        self.refreshButton.setGeometry(QtCore.QRect(550, 40, 41, 41))
        self.refreshButton.setStyleSheet("QPushButton {\n"
                                         "border-image: url(icons/undo.png);\n"
                                         "}\n"
                                         "QPushButton:hover {\n"
                                         "border-image: url(icons/undo-hover.png);\n"
                                         "}\n"
                                         "QPushButton:pressed {\n"
                                         "border-image: url(icons/undo-pressed.png);\n"
                                         "}")
        self.refreshButton.setText("")
        self.refreshButton.setObjectName("refreshButton")
        self.backButton = QtWidgets.QPushButton(self.centralwidget)
        self.backButton.setGeometry(QtCore.QRect(30, 30, 51, 51))
        self.backButton.setStyleSheet("QPushButton {\n"
                                      "border-image: url(icons/back.png);\n"
                                      "}\n"
                                      "QPushButton:hover {\n"
                                      "border-image: url(icons/back-hover.png);\n"
                                      "}\n"
                                      "QPushButton:pressed {\n"
                                      "border-image: url(icons/back-pressed.png);\n"
                                      "}")
        self.backButton.setText("")
        self.backButton.setObjectName("backButton")
        MembersWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MembersWindow)
        self.statusbar.setObjectName("statusbar")
        MembersWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MembersWindow)
        from main_ui import ui as ui_main
        self.backButton.clicked.connect(lambda: ui_main.setupUi(MembersWindow))
        QtCore.QMetaObject.connectSlotsByName(MembersWindow)

    def retranslateUi(self, MembersWindow):
        _translate = QtCore.QCoreApplication.translate
        MembersWindow.setWindowTitle(_translate("MembersWindow", "Members"))
        self.label.setText(_translate("MembersWindow", "ID"))
        self.label_2.setText(_translate("MembersWindow", "Name"))
        self.label_3.setText(_translate("MembersWindow", "Registration Date"))
        self.label_4.setText(_translate("MembersWindow", "Max Credit"))
        self.label_5.setText(_translate("MembersWindow", "Address"))
        self.mainLabel.setText(_translate("MembersWindow", "Members"))
        self.label_8.setText(_translate("MembersWindow", "Age"))


ui = Ui_MembersWindow()
if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MembersWindow = QtWidgets.QMainWindow()
    ui.setupUi(MembersWindow)
    MembersWindow.show()
    sys.exit(app.exec_())
