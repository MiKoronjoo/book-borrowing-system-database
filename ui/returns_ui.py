from datetime import datetime

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
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(self.centralwidget)
        self.dateTimeEdit.setGeometry(QtCore.QRect(170, 140, 141, 26))
        self.dateTimeEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.dateTimeEdit.setDateTime(datetime.now())
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.IssueComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.IssueComboBox.setGeometry(QtCore.QRect(330, 140, 321, 25))
        self.IssueComboBox.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                         "selection-background-color: rgb(32, 215, 146);")
        self.IssueComboBox.setObjectName("IssueComboBox")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(330, 120, 321, 17))
        self.label_4.setObjectName("label_4")
        self.console = QtWidgets.QTextBrowser(self.centralwidget)
        self.console.setGeometry(QtCore.QRect(60, 280, 591, 91))
        self.console.setObjectName("console")
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
        ReturnStatusWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(ReturnStatusWindow)
        self.statusbar.setObjectName("statusbar")
        ReturnStatusWindow.setStatusBar(self.statusbar)

        self.retranslateUi(ReturnStatusWindow)
        from .main_ui import ui as ui_main
        self.backButton.clicked.connect(lambda: ui_main.setupUi(ReturnStatusWindow))
        self.refreshButton.clicked.connect(self.find_via_pk)
        self.deleteButton.clicked.connect(self.delete_via_pk)
        self.submitButton.clicked.connect(lambda: self.update_return() if self.update else self.insert_return())
        self.IDEdit.editingFinished.connect(self.find_via_pk)
        QtCore.QMetaObject.connectSlotsByName(ReturnStatusWindow)
        self.update = False
        self._load_data()

    def retranslateUi(self, ReturnStatusWindow):
        _translate = QtCore.QCoreApplication.translate
        ReturnStatusWindow.setWindowTitle(_translate("ReturnStatusWindow", "Return status"))
        self.label.setText(_translate("ReturnStatusWindow", "ID"))
        self.label_3.setText(_translate("ReturnStatusWindow", "Date"))
        self.mainLabel.setText(_translate("ReturnStatusWindow", "Return status"))
        self.label_4.setText(_translate("ReturnStatusWindow", "Issue"))

    def _load_data(self):
        from tables import IssueStatus
        for issue in IssueStatus.find({}):
            issue: IssueStatus
            member_name = issue.member.name if len(issue.member.name) < 16 else issue.member.name[:14] + '…'
            book_title = issue.book.title if len(issue.book.title) < 16 else issue.book.title[:14] + '…'
            text = f'{issue.issue_id} | {issue.member_id}({member_name}) | {issue.book_ISBN}({book_title})'
            self.IssueComboBox.addItem(text, str(issue.issue_id))
        self.IssueComboBox.setCurrentIndex(-1)

    def clear(self):
        self.IDEdit.setText('')
        self.dateTimeEdit.setDateTime(datetime.now())
        self.IssueComboBox.setCurrentIndex(-1)
        self.update = False

    def find_via_pk(self):
        from tables import ReturnStatus
        ID = self.IDEdit.text().strip()
        if not ID:
            return
        returned = ReturnStatus.find_via_pk(int(ID))
        if returned:
            self.dateTimeEdit.setDateTime(datetime.fromtimestamp(returned.date))
            issue_index = self.IssueComboBox.findData(str(returned.issue_id))
            self.IssueComboBox.setCurrentIndex(issue_index)
            self.update = True
            # TODO: change 'add' icon to 'update'
            self.console.setText(f'Return status with ID {ID} loaded from database')
        else:
            self.update = False

    def insert_return(self):
        from tables import ReturnStatus, IssueStatus
        ID = self.IDEdit.text().strip()
        warning = f'Ignoring ID {ID} for new return status\n' if ID else ''
        issue_id = self.IssueComboBox.currentData()
        if not issue_id:
            self.console.setText('Select an issue to insert the return status')
            return
        issue = IssueStatus.find_via_pk(issue_id)
        ReturnStatus.insert(dict(
            issue_id=int(issue_id),
            date=int(self.dateTimeEdit.dateTime().toPyDateTime().timestamp()),
            member_id=int(issue.member_id),
            book_ISBN=issue.book_ISBN
        ))
        seq = ReturnStatus.last_seq()
        self.clear()
        self.console.setText(warning +
                             'The return state inserted successfully\n'
                             f'Inserted return state ID: {seq}')

    def update_return(self):
        from tables import ReturnStatus, IssueStatus
        ID = self.IDEdit.text().strip()
        issue_id = self.IssueComboBox.currentData()
        if not issue_id:
            self.console.setText('Select an issue to insert the return status')
            return
        if ID:
            issue = IssueStatus.find_via_pk(issue_id)
            ReturnStatus.update_via_pk(dict(
                issue_id=int(issue_id),
                date=int(self.dateTimeEdit.dateTime().toPyDateTime().timestamp()),
                member_id=int(issue.member_id),
                book_ISBN=issue.book_ISBN
            ), int(ID))
            self.clear()
            self.console.setText(f'The return status with ID {ID} updated successfully')
        else:
            self.console.setText('Fill the ID field first')

    def delete_via_pk(self):
        from tables import ReturnStatus
        ID = self.IDEdit.text().strip()
        if ID:
            ReturnStatus.delete_via_pk(int(ID))
            self.clear()
            self.console.setText(f'The return status with ID {ID} deleted successfully')
        else:
            self.console.setText('For deleting, fill the ID field first')


ui = Ui_ReturnStatusWindow()
