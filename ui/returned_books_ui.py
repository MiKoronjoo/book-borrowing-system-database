from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIntValidator


class Ui_ReturnedBooksWindow(object):
    def setupUi(self, ReturnedBooksWindow):
        ReturnedBooksWindow.setObjectName("ReturnedBooksWindow")
        ReturnedBooksWindow.resize(700, 400)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/bbs-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        ReturnedBooksWindow.setWindowIcon(icon)
        ReturnedBooksWindow.setStyleSheet("background-color: rgb(148, 226, 194);")
        self.centralwidget = QtWidgets.QWidget(ReturnedBooksWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.IDEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.IDEdit.setValidator(QIntValidator())
        self.IDEdit.setGeometry(QtCore.QRect(60, 140, 111, 25))
        self.IDEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.IDEdit.setInputMask("")
        self.IDEdit.setText("")
        self.IDEdit.setObjectName("IDEdit")
        self.BooksComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.BooksComboBox.setGeometry(QtCore.QRect(190, 140, 461, 25))
        self.BooksComboBox.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                         "selection-background-color: rgb(32, 215, 146);")
        self.BooksComboBox.setObjectName("BooksComboBox")
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
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(190, 119, 461, 21))
        self.label_4.setObjectName("label_4")
        self.backButton = QtWidgets.QPushButton(self.centralwidget)
        self.backButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
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
        self.searchButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
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
        from .main_ui import ui as ui_main
        self.backButton.clicked.connect(lambda: ui_main.setupUi(ReturnedBooksWindow))
        self.BooksComboBox.currentIndexChanged.connect(self.show_selected_book)
        self.searchButton.clicked.connect(self.search)
        QtCore.QMetaObject.connectSlotsByName(ReturnedBooksWindow)

    def retranslateUi(self, ReturnedBooksWindow):
        _translate = QtCore.QCoreApplication.translate
        ReturnedBooksWindow.setWindowTitle(_translate("ReturnedBooksWindow", "Returned Books"))
        self.label.setText(_translate("ReturnedBooksWindow", "Member ID"))
        self.mainLabel.setText(_translate("ReturnedBooksWindow", "Returned Books"))
        self.label_4.setText(_translate("ReturnedBooksWindow", "Books"))

    def search(self):
        from tables.return_status import ReturnStatus
        from tables.book import Book
        ID = self.IDEdit.text().strip()
        self.BooksComboBox.clear()
        self.console.clear()
        if ID:
            books = ReturnStatus.returned_books(int(ID))
            for book in books:
                book: Book
                self.BooksComboBox.addItem(f'{book.ISBN} | {book.title} | {book.author}', book.ISBN)
            self.BooksComboBox.setCurrentIndex(-1)
            self.console.setText(f'{len(books)} book(s) found for member with ID {ID}')
        else:
            self.console.setText('Fill the ID field first')

    def show_selected_book(self):
        from tables.book import Book
        isbn = self.BooksComboBox.currentData()
        if isbn is None:
            return
        book = Book.find_via_pk(isbn)
        _translate = QtCore.QCoreApplication.translate
        prestr = '<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">'
        self.console.setHtml(_translate("BorrowedBooksWindow",
                                        "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                        "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                        "p, li { white-space: pre-wrap; }\n"
                                        "</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
                                        f"{prestr}ISBN: <span style=\" font-weight:600;\">{book.ISBN}</span></p>\n"
                                        f"{prestr}Title: <span style=\" font-weight:600;\">{book.title}</span></p>\n"
                                        f"{prestr}Category: {book.category}</p>\n"
                                        f"{prestr}Price: {book.price} $</p>\n"
                                        f"{prestr}Author: <span style=\" font-weight:600;\">{book.author}</span></p>\n"
                                        f"{prestr}Publisher: {book.publisher}</p>\n"
                                        f"{prestr}Status: {book.status}</p></body></html>"))


ui = Ui_ReturnedBooksWindow()
