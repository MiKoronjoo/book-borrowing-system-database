from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_IssueStatusWindow(object):
    def setupUi(self, IssueStatusWindow):
        IssueStatusWindow.setObjectName("IssueStatusWindow")
        IssueStatusWindow.resize(700, 400)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/bbs-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        IssueStatusWindow.setWindowIcon(icon)
        IssueStatusWindow.setStyleSheet("background-color: rgb(148, 226, 194);")
        self.centralwidget = QtWidgets.QWidget(IssueStatusWindow)
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
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(self.centralwidget)
        self.dateTimeEdit.setGeometry(QtCore.QRect(170, 140, 141, 26))
        self.dateTimeEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.dateTimeEdit.setDate(QtCore.QDate(2021, 1, 1))
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.MemberComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.MemberComboBox.setGeometry(QtCore.QRect(330, 140, 151, 25))
        self.MemberComboBox.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                          "selection-background-color: rgb(32, 215, 146);")
        self.MemberComboBox.setObjectName("MemberComboBox")
        self.MemberComboBox.addItem("")
        self.MemberComboBox.addItem("")
        self.MemberComboBox.addItem("")
        self.BookComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.BookComboBox.setGeometry(QtCore.QRect(500, 140, 151, 25))
        self.BookComboBox.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                        "selection-background-color: rgb(32, 215, 146);")
        self.BookComboBox.setObjectName("BookComboBox")
        self.BookComboBox.addItem("")
        self.BookComboBox.addItem("")
        self.BookComboBox.addItem("")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(330, 120, 151, 17))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(500, 120, 151, 17))
        self.label_5.setObjectName("label_5")
        IssueStatusWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(IssueStatusWindow)
        self.statusbar.setObjectName("statusbar")
        IssueStatusWindow.setStatusBar(self.statusbar)

        self.retranslateUi(IssueStatusWindow)
        from .main_ui import ui as ui_main
        self.backButton.clicked.connect(lambda: ui_main.setupUi(IssueStatusWindow))
        QtCore.QMetaObject.connectSlotsByName(IssueStatusWindow)

    def retranslateUi(self, IssueStatusWindow):
        _translate = QtCore.QCoreApplication.translate
        IssueStatusWindow.setWindowTitle(_translate("IssueStatusWindow", "Issue status"))
        self.label.setText(_translate("IssueStatusWindow", "ID"))
        self.label_3.setText(_translate("IssueStatusWindow", "Date"))
        self.mainLabel.setText(_translate("IssueStatusWindow", "Issue status"))
        self.MemberComboBox.setItemText(0, _translate("IssueStatusWindow", "0 | miko"))
        self.MemberComboBox.setItemText(1, _translate("IssueStatusWindow", "1 | ali"))
        self.MemberComboBox.setItemText(2, _translate("IssueStatusWindow", "2 | reza jafar abadi"))
        self.BookComboBox.setItemText(0, _translate("IssueStatusWindow", "1234567890123 | miko"))
        self.BookComboBox.setItemText(1, _translate("IssueStatusWindow", "9876543210 | ali"))
        self.BookComboBox.setItemText(2, _translate("IssueStatusWindow", "Uno Uno"))
        self.label_4.setText(_translate("IssueStatusWindow", "Member"))
        self.label_5.setText(_translate("IssueStatusWindow", "Book"))


ui = Ui_IssueStatusWindow()
