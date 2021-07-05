from datetime import datetime

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIntValidator, QCursor


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
        self.IDEdit.setValidator(QIntValidator())
        self.IDEdit.setGeometry(QtCore.QRect(60, 140, 91, 25))
        self.IDEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.IDEdit.setInputMask("")
        self.IDEdit.setText("")
        self.IDEdit.setObjectName("IDEdit")
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(self.centralwidget)
        self.dateTimeEdit.setGeometry(QtCore.QRect(170, 140, 141, 26))
        self.dateTimeEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.dateTimeEdit.setDateTime(datetime.now())
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.MemberComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.MemberComboBox.setGeometry(QtCore.QRect(330, 140, 151, 25))
        self.MemberComboBox.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                          "selection-background-color: rgb(32, 215, 146);")
        self.MemberComboBox.setObjectName("MemberComboBox")
        self.BookComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.BookComboBox.setGeometry(QtCore.QRect(500, 140, 151, 25))
        self.BookComboBox.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                        "selection-background-color: rgb(32, 215, 146);")
        self.BookComboBox.setObjectName("BookComboBox")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60, 120, 91, 17))
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(170, 120, 141, 17))
        self.label_3.setObjectName("label_3")
        self.submitButton = QtWidgets.QPushButton(self.centralwidget)
        self.submitButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
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
        self.refreshButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
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
        self.deleteButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
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
        self.refreshButton.clicked.connect(self.find_via_pk)
        self.deleteButton.clicked.connect(self.delete_via_pk)
        self.submitButton.clicked.connect(lambda: self.update_issue() if self.update else self.insert_issue())
        self.IDEdit.editingFinished.connect(self.find_via_pk)
        QtCore.QMetaObject.connectSlotsByName(IssueStatusWindow)
        self.update = False
        self._load_data()

    def retranslateUi(self, IssueStatusWindow):
        _translate = QtCore.QCoreApplication.translate
        IssueStatusWindow.setWindowTitle(_translate("IssueStatusWindow", "Issue status"))
        self.label.setText(_translate("IssueStatusWindow", "ID"))
        self.label_3.setText(_translate("IssueStatusWindow", "Date"))
        self.mainLabel.setText(_translate("IssueStatusWindow", "Issue status"))
        self.label_4.setText(_translate("IssueStatusWindow", "Member"))
        self.label_5.setText(_translate("IssueStatusWindow", "Book"))

    def _load_data(self):
        from tables.member import Member
        from tables.book import Book
        for member in Member.find({}):
            member: Member
            text = f'{member.ID} | {member.name}'
            if len(text) > 20:
                text = text[:19] + '…'
            self.MemberComboBox.addItem(text, str(member.ID))
        for book in Book.find({}):
            book: Book
            text = f'{book.ISBN} | {book.title}'
            if len(text) > 20:
                text = text[:19] + '…'
            self.BookComboBox.addItem(text, book.ISBN)
        self.MemberComboBox.setCurrentIndex(-1)
        self.BookComboBox.setCurrentIndex(-1)

    def clear(self):
        self.IDEdit.setText('')
        self.dateTimeEdit.setDateTime(datetime.now())
        self.MemberComboBox.setCurrentIndex(-1)
        self.BookComboBox.setCurrentIndex(-1)
        self.update = False

    def find_via_pk(self):
        from tables.issue_status import IssueStatus
        ID = self.IDEdit.text().strip()
        if not ID:
            return
        issue = IssueStatus.find_via_pk(int(ID))
        if issue:
            self.dateTimeEdit.setDateTime(datetime.fromtimestamp(issue.date))
            member_index = self.MemberComboBox.findData(str(issue.member.ID))
            self.MemberComboBox.setCurrentIndex(member_index)
            book_index = self.BookComboBox.findData(issue.book.ISBN)
            self.BookComboBox.setCurrentIndex(book_index)
            self.update = True
            # TODO: change 'add' icon to 'update'
            self.console.setText(f'Issue status with ID {ID} loaded from database')
        else:
            self.update = False

    def insert_issue(self):
        from tables.issue_status import IssueStatus
        ID = self.IDEdit.text().strip()
        warning = f'Ignoring ID {ID} for new issue status\n' if ID else ''
        member_id = self.MemberComboBox.currentData()
        book_isbn = self.BookComboBox.currentData()
        if not member_id:
            self.console.setText('Select a member to insert the issue status')
            return
        if not book_isbn:
            self.console.setText('Select a book to insert the issue status')
            return
        IssueStatus.insert(dict(
            date=int(self.dateTimeEdit.dateTime().toPyDateTime().timestamp()),
            member_id=int(member_id),
            book_ISBN=book_isbn
        ))
        seq = IssueStatus.last_seq()
        self.clear()
        self.console.setText(warning +
                             'The issue state inserted successfully\n'
                             f'Inserted issue state ID: {seq}')

    def update_issue(self):
        from tables.issue_status import IssueStatus
        ID = self.IDEdit.text().strip()
        member_id = self.MemberComboBox.currentData()
        book_isbn = self.BookComboBox.currentData()
        if not member_id:
            self.console.setText('Select a member to update the issue status')
            return
        if not book_isbn:
            self.console.setText('Select a book to update the issue status')
            return
        if ID:
            IssueStatus.update_via_pk(dict(
                date=int(self.dateTimeEdit.dateTime().toPyDateTime().timestamp()),
                member_id=int(member_id),
                book_ISBN=book_isbn
            ), int(ID))
            self.clear()
            self.console.setText(f'The issue status with ID {ID} updated successfully')
        else:
            self.console.setText('Fill the ID field first')

    def delete_via_pk(self):
        from tables.issue_status import IssueStatus
        ID = self.IDEdit.text().strip()
        if ID:
            IssueStatus.delete_via_pk(int(ID))
            self.clear()
            self.console.setText(f'The member with ID {ID} deleted successfully')
        else:
            self.console.setText('For deleting, fill the ID field first')


ui = Ui_IssueStatusWindow()
