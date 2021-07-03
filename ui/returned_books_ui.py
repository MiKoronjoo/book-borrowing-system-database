# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'returned_books.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ReturnedBooksWindow(object):
    def setupUi(self, ReturnedBooksWindow):
        ReturnedBooksWindow.setObjectName("ReturnedBooksWindow")
        ReturnedBooksWindow.resize(700, 400)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("bbs-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        ReturnedBooksWindow.setWindowIcon(icon)
        ReturnedBooksWindow.setStyleSheet("background-color: rgb(148, 226, 194);")
        self.centralwidget = QtWidgets.QWidget(ReturnedBooksWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.IDEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.IDEdit.setGeometry(QtCore.QRect(60, 140, 111, 25))
        self.IDEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.IDEdit.setInputMask("")
        self.IDEdit.setText("")
        self.IDEdit.setObjectName("IDEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60, 117, 91, 20))
        self.label.setObjectName("label")
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
        ReturnedBooksWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(ReturnedBooksWindow)
        self.statusbar.setObjectName("statusbar")
        ReturnedBooksWindow.setStatusBar(self.statusbar)

        self.retranslateUi(ReturnedBooksWindow)
        from main_ui import ui as ui_main
        self.backButton.clicked.connect(lambda: ui_main.setupUi(ReturnedBooksWindow))
        self.BooksComboBox.currentIndexChanged['int'].connect(self.console.clear)
        QtCore.QMetaObject.connectSlotsByName(ReturnedBooksWindow)

    def retranslateUi(self, ReturnedBooksWindow):
        _translate = QtCore.QCoreApplication.translate
        ReturnedBooksWindow.setWindowTitle(_translate("ReturnedBooksWindow", "Returned Books"))
        self.label.setText(_translate("ReturnedBooksWindow", "Member ID"))
        self.mainLabel.setText(_translate("ReturnedBooksWindow", "Returned Books"))
        self.console.setHtml(_translate("ReturnedBooksWindow",
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
        self.BooksComboBox.setItemText(0, _translate("ReturnedBooksWindow", "0 | miko | Python"))
        self.BooksComboBox.setItemText(1,
                                       _translate("ReturnedBooksWindow", "1 | Nader Shah Afshar | How to rule a relm"))
        self.label_4.setText(_translate("ReturnedBooksWindow", "Books"))


ui = Ui_ReturnedBooksWindow()
if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    ReturnedBooksWindow = QtWidgets.QMainWindow()
    ui.setupUi(ReturnedBooksWindow)
    ReturnedBooksWindow.show()
    sys.exit(app.exec_())
