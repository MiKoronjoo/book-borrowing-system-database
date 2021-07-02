# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'returns.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ReturnStatusWindow(object):
    def setupUi(self, ReturnStatusWindow):
        ReturnStatusWindow.setObjectName("ReturnStatusWindow")
        ReturnStatusWindow.resize(700, 400)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("bbs-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        ReturnStatusWindow.setWindowIcon(icon)
        ReturnStatusWindow.setStyleSheet("background-color: rgb(148, 226, 194);")
        self.centralwidget = QtWidgets.QWidget(ReturnStatusWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.IDEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.IDEdit.setGeometry(QtCore.QRect(60, 140, 91, 25))
        self.IDEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.IDEdit.setInputMask("")
        self.IDEdit.setText("")
        self.IDEdit.setObjectName("IDEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60, 120, 91, 17))
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(170, 120, 141, 17))
        self.label_3.setObjectName("label_3")
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
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(self.centralwidget)
        self.dateTimeEdit.setGeometry(QtCore.QRect(170, 140, 141, 26))
        self.dateTimeEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.dateTimeEdit.setDate(QtCore.QDate(2021, 1, 1))
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.IssueComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.IssueComboBox.setGeometry(QtCore.QRect(330, 140, 321, 25))
        self.IssueComboBox.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                         "selection-background-color: rgb(32, 215, 146);")
        self.IssueComboBox.setObjectName("IssueComboBox")
        self.IssueComboBox.addItem("")
        self.IssueComboBox.addItem("")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(330, 120, 321, 17))
        self.label_4.setObjectName("label_4")
        self.deleteButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.deleteButton_2.setGeometry(QtCore.QRect(610, 60, 41, 41))
        self.deleteButton_2.setStyleSheet("QPushButton {\n"
                                          "border-image: url(icons/remove.png);\n"
                                          "}\n"
                                          "QPushButton:hover {\n"
                                          "border-image: url(icons/remove-hover.png);\n"
                                          "}\n"
                                          "QPushButton:pressed {\n"
                                          "border-image: url(icons/remove-pressed.png);\n"
                                          "}")
        self.deleteButton_2.setText("")
        self.deleteButton_2.setObjectName("deleteButton_2")
        self.refreshButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.refreshButton_2.setGeometry(QtCore.QRect(550, 60, 41, 41))
        self.refreshButton_2.setStyleSheet("QPushButton {\n"
                                           "border-image: url(icons/undo.png);\n"
                                           "}\n"
                                           "QPushButton:hover {\n"
                                           "border-image: url(icons/undo-hover.png);\n"
                                           "}\n"
                                           "QPushButton:pressed {\n"
                                           "border-image: url(icons/undo-pressed.png);\n"
                                           "}")
        self.refreshButton_2.setText("")
        self.refreshButton_2.setObjectName("refreshButton_2")
        self.submitButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.submitButton_2.setGeometry(QtCore.QRect(610, 210, 41, 41))
        self.submitButton_2.setStyleSheet("QPushButton {\n"
                                          "border-image: url(icons/plus.png);\n"
                                          "}\n"
                                          "QPushButton:hover {\n"
                                          "border-image: url(icons/plus-hover.png);\n"
                                          "}\n"
                                          "QPushButton:pressed {\n"
                                          "border-image: url(icons/plus-pressed.png);\n"
                                          "}")
        self.submitButton_2.setText("")
        self.submitButton_2.setObjectName("submitButton_2")
        self.backButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.backButton_2.setGeometry(QtCore.QRect(30, 30, 51, 51))
        self.backButton_2.setStyleSheet("QPushButton {\n"
                                        "border-image: url(icons/back.png);\n"
                                        "}\n"
                                        "QPushButton:hover {\n"
                                        "border-image: url(icons/back-hover.png);\n"
                                        "}\n"
                                        "QPushButton:pressed {\n"
                                        "border-image: url(icons/back-pressed.png);\n"
                                        "}")
        self.backButton_2.setText("")
        self.backButton_2.setObjectName("backButton_2")
        ReturnStatusWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(ReturnStatusWindow)
        self.statusbar.setObjectName("statusbar")
        ReturnStatusWindow.setStatusBar(self.statusbar)

        self.retranslateUi(ReturnStatusWindow)
        QtCore.QMetaObject.connectSlotsByName(ReturnStatusWindow)

    def retranslateUi(self, ReturnStatusWindow):
        _translate = QtCore.QCoreApplication.translate
        ReturnStatusWindow.setWindowTitle(_translate("ReturnStatusWindow", "Return status"))
        self.label.setText(_translate("ReturnStatusWindow", "ID"))
        self.label_3.setText(_translate("ReturnStatusWindow", "Date"))
        self.mainLabel.setText(_translate("ReturnStatusWindow", "Return status"))
        self.IssueComboBox.setItemText(0, _translate("ReturnStatusWindow", "0 | miko | Python"))
        self.IssueComboBox.setItemText(1,
                                       _translate("ReturnStatusWindow", "1 | Nader Shah Afshar | How to rule a relm"))
        self.label_4.setText(_translate("ReturnStatusWindow", "Issue"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    ReturnStatusWindow = QtWidgets.QMainWindow()
    ui = Ui_ReturnStatusWindow()
    ui.setupUi(ReturnStatusWindow)
    ReturnStatusWindow.show()
    sys.exit(app.exec_())
