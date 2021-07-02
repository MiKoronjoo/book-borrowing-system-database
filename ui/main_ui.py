# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bbs.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(700, 400)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("bbs-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("background-color: rgb(32, 215, 146);\n"
                                 "")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.booksButton = QtWidgets.QPushButton(self.centralwidget)
        self.booksButton.setGeometry(QtCore.QRect(180, 130, 171, 91))
        self.booksButton.setStyleSheet("QPushButton {\n"
                                       "border-image: url(icons/buttons/Books.png);\n"
                                       "}\n"
                                       "QPushButton:hover {\n"
                                       "border-image: url(icons/buttons/Books-hover.png);\n"
                                       "}\n"
                                       "QPushButton:pressed {\n"
                                       "border-image: url(icons/buttons/Books-pressed.png);\n"
                                       "}")
        self.booksButton.setText("")
        self.booksButton.setObjectName("booksButton")
        self.MemberButton = QtWidgets.QPushButton(self.centralwidget)
        self.MemberButton.setGeometry(QtCore.QRect(360, 130, 171, 91))
        self.MemberButton.setStyleSheet("QPushButton {\n"
                                        "border-image: url(icons/buttons/Members.png);\n"
                                        "}\n"
                                        "QPushButton:hover {\n"
                                        "border-image: url(icons/buttons/Members-hover.png);\n"
                                        "}\n"
                                        "QPushButton:pressed {\n"
                                        "border-image: url(icons/buttons/Members-pressed.png);\n"
                                        "}")
        self.MemberButton.setText("")
        self.MemberButton.setObjectName("MemberButton")
        self.IssuesButton = QtWidgets.QPushButton(self.centralwidget)
        self.IssuesButton.setGeometry(QtCore.QRect(180, 230, 171, 91))
        self.IssuesButton.setStyleSheet("QPushButton {\n"
                                        "border-image: url(icons/buttons/Issues.png);\n"
                                        "}\n"
                                        "QPushButton:hover {\n"
                                        "border-image: url(icons/buttons/Issues-hover.png);\n"
                                        "}\n"
                                        "QPushButton:pressed {\n"
                                        "border-image: url(icons/buttons/Issues-pressed.png);\n"
                                        "}")
        self.IssuesButton.setText("")
        self.IssuesButton.setObjectName("IssuesButton")
        self.ReturnsButton = QtWidgets.QPushButton(self.centralwidget)
        self.ReturnsButton.setGeometry(QtCore.QRect(360, 230, 171, 91))
        self.ReturnsButton.setStyleSheet("QPushButton {\n"
                                         "border-image: url(icons/buttons/Returns.png);\n"
                                         "}\n"
                                         "QPushButton:hover {\n"
                                         "border-image: url(icons/buttons/Returns-hover.png);\n"
                                         "}\n"
                                         "QPushButton:pressed {\n"
                                         "border-image: url(icons/buttons/Returns-pressed.png);\n"
                                         "}")
        self.ReturnsButton.setText("")
        self.ReturnsButton.setObjectName("ReturnsButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 50, 701, 51))
        font = QtGui.QFont()
        font.setPointSize(35)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setStyleSheet("color: rgb(5, 18, 4);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.BorBButton = QtWidgets.QPushButton(self.centralwidget)
        self.BorBButton.setGeometry(QtCore.QRect(180, 330, 171, 31))
        self.BorBButton.setStyleSheet("QPushButton {\n"
                                      "border-image: url(icons/buttons/BorrowedBooks.png);\n"
                                      "}\n"
                                      "QPushButton:hover {\n"
                                      "border-image: url(icons/buttons/BorrowedBooks-hover.png);\n"
                                      "}\n"
                                      "QPushButton:pressed {\n"
                                      "border-image: url(icons/buttons/BorrowedBooks-pressed.png);\n"
                                      "}")
        self.BorBButton.setText("")
        self.BorBButton.setObjectName("BorBButton")
        self.RetBButton = QtWidgets.QPushButton(self.centralwidget)
        self.RetBButton.setGeometry(QtCore.QRect(360, 330, 171, 31))
        self.RetBButton.setStyleSheet("QPushButton {\n"
                                      "border-image: url(icons/buttons/ReturnedBooks.png);\n"
                                      "}\n"
                                      "QPushButton:hover {\n"
                                      "border-image: url(icons/buttons/ReturnedBooks-hover.png);\n"
                                      "}\n"
                                      "QPushButton:pressed {\n"
                                      "border-image: url(icons/buttons/ReturnedBooks-pressed.png);\n"
                                      "}")
        self.RetBButton.setText("")
        self.RetBButton.setObjectName("RetBButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.booksButton.clicked.connect(MainWindow.show)
        self.MemberButton.clicked.connect(MainWindow.show)
        self.IssuesButton.clicked.connect(MainWindow.show)
        self.ReturnsButton.clicked.connect(MainWindow.show)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Book Borrowing System"))
        self.label.setText(_translate("MainWindow", "Select a table"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
