from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIntValidator


class Ui_BorrowedBooksWindow(object):
    def setupUi(self, BorrowedBooksWindow):
        BorrowedBooksWindow.setObjectName("BorrowedBooksWindow")
        BorrowedBooksWindow.resize(700, 400)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/bbs-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        BorrowedBooksWindow.setWindowIcon(icon)
        BorrowedBooksWindow.setStyleSheet("background-color: rgb(148, 226, 194);")
        self.centralwidget = QtWidgets.QWidget(BorrowedBooksWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.IDEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.IDEdit.setValidator(QIntValidator())
        self.IDEdit.setGeometry(QtCore.QRect(60, 140, 111, 25))
        self.IDEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.IDEdit.setInputMask("")
        self.IDEdit.setText("")
        self.IDEdit.setObjectName("IDEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60, 117, 91, 20))
        self.label.setObjectName("label")
        self.searchButton = QtWidgets.QPushButton(self.centralwidget)
        self.searchButton.setGeometry(QtCore.QRect(70, 170, 51, 51))
        self.searchButton.setStyleSheet("QPushButton {\n"
                                        "border-image: url(icons/search.png);\n"
                                        "}\n"
                                        "QPushButton:hover {\n"
                                        "border-image: url(icons/search-hover.png);\n"
                                        "}\n"
                                        "QPushButton:pressed {\n"
                                        "border-image: url(icons/search-pressed.png);\n"
                                        "}")
        self.searchButton.setText("")
        self.searchButton.setObjectName("searchButton")
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
        self.console.setGeometry(QtCore.QRect(60, 240, 591, 131))
        self.console.setObjectName("console")
        self.BooksComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.BooksComboBox.setGeometry(QtCore.QRect(190, 140, 461, 25))
        self.BooksComboBox.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                         "selection-background-color: rgb(32, 215, 146);")
        self.BooksComboBox.setObjectName("BooksComboBox")
        self.BooksComboBox.addItem("")
        self.BooksComboBox.addItem("")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(190, 119, 461, 21))
        self.label_4.setObjectName("label_4")
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
        BorrowedBooksWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(BorrowedBooksWindow)
        self.statusbar.setObjectName("statusbar")
        BorrowedBooksWindow.setStatusBar(self.statusbar)

        self.retranslateUi(BorrowedBooksWindow)
        from .main_ui import ui as ui_main
        self.backButton.clicked.connect(lambda: ui_main.setupUi(BorrowedBooksWindow))
        self.BooksComboBox.currentIndexChanged['int'].connect(self.console.clear)
        self.searchButton.clicked.connect(self.BooksComboBox.clear)
        QtCore.QMetaObject.connectSlotsByName(BorrowedBooksWindow)

    def retranslateUi(self, BorrowedBooksWindow):
        _translate = QtCore.QCoreApplication.translate
        BorrowedBooksWindow.setWindowTitle(_translate("BorrowedBooksWindow", "Borrowed Books"))
        self.label.setText(_translate("BorrowedBooksWindow", "Member ID"))
        self.mainLabel.setText(_translate("BorrowedBooksWindow", "Borrowed Books"))
        self.console.setHtml(_translate("BorrowedBooksWindow",
                                        "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                        "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                        "p, li { white-space: pre-wrap; }\n"
                                        "</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
                                        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">ISBN: <span style=\" font-weight:600;\">1234567845214</span></p>\n"
                                        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Title: <span style=\" font-weight:600;\">Python is Fun</span></p>\n"
                                        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Category: Fun, Programming</p>\n"
                                        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Price: 99.99 $</p>\n"
                                        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Auther: <span style=\" font-weight:600;\">Ahmad Towhidi</span></p>\n"
                                        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Publisher: Shiraz University Pub.</p>\n"
                                        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Status: 475</p></body></html>"))
        self.BooksComboBox.setItemText(0, _translate("BorrowedBooksWindow", "0 | miko | Python"))
        self.BooksComboBox.setItemText(1,
                                       _translate("BorrowedBooksWindow", "1 | Nader Shah Afshar | How to rule a relm"))
        self.label_4.setText(_translate("BorrowedBooksWindow", "Books"))


ui = Ui_BorrowedBooksWindow()
