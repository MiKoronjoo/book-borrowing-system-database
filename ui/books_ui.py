from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIntValidator


class Ui_BooksWindow(object):
    def setupUi(self, BooksWindow):
        BooksWindow.setObjectName("BooksWindow")
        BooksWindow.resize(700, 400)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/bbs-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        BooksWindow.setWindowIcon(icon)
        BooksWindow.setStyleSheet("background-color: rgb(148, 226, 194);")
        self.centralwidget = QtWidgets.QWidget(BooksWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.ISBNEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.ISBNEdit.setGeometry(QtCore.QRect(60, 110, 121, 25))
        self.ISBNEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.ISBNEdit.setInputMask("")
        self.ISBNEdit.setText("")
        self.ISBNEdit.setObjectName("ISBNEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60, 90, 121, 17))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(200, 90, 121, 17))
        self.label_2.setObjectName("label_2")
        self.TitleEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.TitleEdit.setGeometry(QtCore.QRect(200, 110, 451, 25))
        self.TitleEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.TitleEdit.setInputMask("")
        self.TitleEdit.setText("")
        self.TitleEdit.setObjectName("TitleEdit")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(60, 150, 121, 17))
        self.label_3.setObjectName("label_3")
        self.CategoryEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.CategoryEdit.setGeometry(QtCore.QRect(60, 170, 191, 25))
        self.CategoryEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.CategoryEdit.setInputMask("")
        self.CategoryEdit.setText("")
        self.CategoryEdit.setObjectName("CategoryEdit")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(270, 150, 121, 17))
        self.label_4.setObjectName("label_4")
        self.PriceEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.PriceEdit.setValidator(QIntValidator())
        self.PriceEdit.setGeometry(QtCore.QRect(270, 170, 121, 25))
        self.PriceEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.PriceEdit.setInputMask("")
        self.PriceEdit.setText("")
        self.PriceEdit.setObjectName("PriceEdit")
        self.AuthorEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.AuthorEdit.setGeometry(QtCore.QRect(410, 170, 241, 25))
        self.AuthorEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.AuthorEdit.setInputMask("")
        self.AuthorEdit.setText("")
        self.AuthorEdit.setObjectName("AuthorEdit")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(410, 150, 121, 17))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(60, 210, 121, 17))
        self.label_6.setObjectName("label_6")
        self.PublisherEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.PublisherEdit.setGeometry(QtCore.QRect(60, 230, 241, 25))
        self.PublisherEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.PublisherEdit.setInputMask("")
        self.PublisherEdit.setText("")
        self.PublisherEdit.setObjectName("PublisherEdit")
        self.StatusEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.StatusEdit.setValidator(QIntValidator())
        self.StatusEdit.setGeometry(QtCore.QRect(320, 230, 121, 25))
        self.StatusEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.StatusEdit.setInputMask("")
        self.StatusEdit.setText("")
        self.StatusEdit.setObjectName("StatusEdit")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(320, 210, 121, 17))
        self.label_7.setObjectName("label_7")
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
        self.deleteButton = QtWidgets.QPushButton(self.centralwidget)
        self.deleteButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
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
        self.submitButton = QtWidgets.QPushButton(self.centralwidget)
        self.submitButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
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
        self.refreshButton = QtWidgets.QPushButton(self.centralwidget)
        self.refreshButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.refreshButton.setGeometry(QtCore.QRect(560, 40, 41, 41))
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
        BooksWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(BooksWindow)
        self.statusbar.setObjectName("statusbar")
        BooksWindow.setStatusBar(self.statusbar)

        self.retranslateUi(BooksWindow)
        from .main_ui import ui as ui_main
        self.backButton.clicked.connect(lambda: ui_main.setupUi(BooksWindow))
        self.deleteButton.clicked.connect(self.delete_via_pk)
        self.refreshButton.clicked.connect(self.find_via_pk)
        self.submitButton.clicked.connect(lambda: self.update_book() if self.update else self.insert_book())
        self.ISBNEdit.editingFinished.connect(self.find_via_pk)
        QtCore.QMetaObject.connectSlotsByName(BooksWindow)
        self.update = False

    def retranslateUi(self, BooksWindow):
        _translate = QtCore.QCoreApplication.translate
        BooksWindow.setWindowTitle(_translate("BooksWindow", "Books"))
        self.label.setText(_translate("BooksWindow", "ISBN"))
        self.label_2.setText(_translate("BooksWindow", "Title"))
        self.label_3.setText(_translate("BooksWindow", "Category"))
        self.label_4.setText(_translate("BooksWindow", "Price"))
        self.label_5.setText(_translate("BooksWindow", "Author"))
        self.label_6.setText(_translate("BooksWindow", "Publisher"))
        self.label_7.setText(_translate("BooksWindow", "Status"))
        self.mainLabel.setText(_translate("BooksWindow", "Books"))

    def clear(self):
        self.ISBNEdit.setText('')
        self.TitleEdit.setText('')
        self.CategoryEdit.setText('')
        self.PriceEdit.setText('')
        self.AuthorEdit.setText('')
        self.PublisherEdit.setText('')
        self.StatusEdit.setText('')
        self.console.setText('')
        self.update = False

    def find_via_pk(self):
        from tables import Book
        isbn = self.ISBNEdit.text().strip()
        book = Book.find_via_pk(isbn)
        if book:
            self.TitleEdit.setText(book.title)
            self.CategoryEdit.setText(book.category)
            self.PriceEdit.setText(str(book.price))
            self.AuthorEdit.setText(book.author)
            self.PublisherEdit.setText(book.publisher)
            self.StatusEdit.setText(str(book.status))
            self.update = True
            # TODO: change 'add' icon to 'update'
            self.console.setText(f'Member with ISBN {isbn} loaded from database')
        else:
            self.update = False

    def insert_book(self):
        from tables import Book
        isbn = self.ISBNEdit.text().strip()
        if isbn:
            Book.insert(dict(
                ISBN=self.ISBNEdit.text(),
                title=self.TitleEdit.text(),
                category=self.CategoryEdit.text(),
                price=int(self.PriceEdit.text() or '0'),
                author=self.AuthorEdit.text(),
                publisher=self.PublisherEdit.text(),
                status=int(self.StatusEdit.text() or '0')
            ))
            self.clear()
            self.console.setText('The book inserted successfully')
        else:
            self.console.setText('Fill the ISBN field first')

    def update_book(self):
        from tables import Book
        isbn = self.ISBNEdit.text().strip()
        if isbn:
            Book.update_via_pk(dict(
                ISBN=isbn,
                title=self.TitleEdit.text(),
                category=self.CategoryEdit.text(),
                price=int(self.PriceEdit.text() or '0'),
                author=self.AuthorEdit.text(),
                publisher=self.PublisherEdit.text(),
                status=int(self.StatusEdit.text() or '0')
            ), isbn)
            self.clear()
            self.console.setText('The book updated successfully')
        else:
            self.console.setText('Fill the ISBN field first')

    def delete_via_pk(self):
        from tables import Book
        isbn = self.ISBNEdit.text().strip()
        if isbn:
            Book.delete_via_pk(isbn)
            self.clear()
            self.console.setText(f'The book with ISBN {isbn} deleted successfully')
        else:
            self.console.setText('Fill the ISBN field first')


ui = Ui_BooksWindow()
