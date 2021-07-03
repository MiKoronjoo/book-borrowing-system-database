from PyQt5 import QtCore, QtGui, QtWidgets

from .books_ui import ui as ui_books
from .borrowed_books_ui import ui as ui_borrowed_books
from .issues_ui import ui as ui_issues
from .members_ui import ui as ui_members
from .returned_books_ui import ui as ui_returned_books
from .returns_ui import ui as ui_returns


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(700, 400)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/bbs-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("background-color: rgb(32, 215, 146);")
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
        self.booksButton.clicked.connect(lambda: ui_books.setupUi(MainWindow))
        self.MemberButton.clicked.connect(lambda: ui_members.setupUi(MainWindow))
        self.IssuesButton.clicked.connect(lambda: ui_issues.setupUi(MainWindow))
        self.ReturnsButton.clicked.connect(lambda: ui_returns.setupUi(MainWindow))
        self.BorBButton.clicked.connect(lambda: ui_borrowed_books.setupUi(MainWindow))
        self.RetBButton.clicked.connect(lambda: ui_returned_books.setupUi(MainWindow))
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Book Borrowing System"))
        self.label.setText(_translate("MainWindow", "Select a table"))


def lunch_app():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


ui = Ui_MainWindow()
