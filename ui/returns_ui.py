from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIntValidator


class Ui_ReturnStatusWindow(object):
    def setupUi(self, ReturnStatusWindow):
        ReturnStatusWindow.setObjectName("ReturnStatusWindow")
        ReturnStatusWindow.resize(700, 400)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/bbs-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        ReturnStatusWindow.setWindowIcon(icon)
        ReturnStatusWindow.setStyleSheet("background-color: rgb(148, 226, 194);")
        self.centralwidget = QtWidgets.QWidget(ReturnStatusWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.IDEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.IDEdit.setValidator(QIntValidator())
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
        self.deleteButton = QtWidgets.QPushButton(self.centralwidget)
        self.deleteButton.setGeometry(QtCore.QRect(610, 60, 41, 41))
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
        self.refreshButton.setGeometry(QtCore.QRect(550, 60, 41, 41))
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
        self.submitButton = QtWidgets.QPushButton(self.centralwidget)
        self.submitButton.setGeometry(QtCore.QRect(610, 210, 41, 41))
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
        ReturnStatusWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(ReturnStatusWindow)
        self.statusbar.setObjectName("statusbar")
        ReturnStatusWindow.setStatusBar(self.statusbar)

        self.retranslateUi(ReturnStatusWindow)
        from .main_ui import ui as ui_main
        self.backButton.clicked.connect(lambda: ui_main.setupUi(ReturnStatusWindow))
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


ui = Ui_ReturnStatusWindow()
