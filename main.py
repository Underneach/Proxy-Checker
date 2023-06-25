import sys

from PyQt5 import QtCore, QtGui, QtWidgets

from checker import ProxyChecker
from open_file import open_file_func


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.parsed_proxy = []
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(730, 500)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(730, 500))
        MainWindow.setMaximumSize(QtCore.QSize(730, 500))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(-1, -1, 925, 505))
        self.frame.setStyleSheet("background-color: rgb(44, 58, 71);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(15, 15, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Variable Small Semibol")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAutoFillBackground(False)
        self.label_3.setStyleSheet(
            "background-color:rgb(73, 92, 108);\n"
            "color: #37ae85;\n"
            "border-radius: 10px;"
        )
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setIndent(0)
        self.label_3.setObjectName("label_3")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(15, 75, 106, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Variable Small Semibol")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setAutoFillBackground(False)
        self.label_5.setStyleSheet(
            "background-color:rgb(73, 92, 108);\n"
            "color: #37ae85;\n"
            "border-radius: 10px;"
        )
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setIndent(0)
        self.label_5.setObjectName("label_5")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.frame)
        self.plainTextEdit.setGeometry(QtCore.QRect(15, 185, 701, 305))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Variable Small Semibol")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.plainTextEdit.setFont(font)
        self.plainTextEdit.setStyleSheet(
            "background-color: #36434f;\n"
            "color: #37ae85;\n"
            "border-radius: 10px;\n"
            ""
        )
        self.plainTextEdit.setReadOnly(True)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.Select_proxy_button = QtWidgets.QPushButton(self.frame)
        self.Select_proxy_button.setGeometry(QtCore.QRect(610, 15, 106, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Variable Small Semibol")
        font.setPointSize(14)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.Select_proxy_button.setFont(font)
        self.Select_proxy_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Select_proxy_button.setStyleSheet(
            "QPushButton {\n"
            "    background-color:rgb(73, 92, 108);\n"
            "    color: #37ae85;\n"
            "    border-radius: 10px;\n"
            "}\n"
            "QPushButton:pressed {\n"
            "    background-color:rgb(40, 40, 40);\n"
            "    color: rgb(205, 205, 205);\n"
            "    border-style: outset;\n"
            "    border-radius: 10px;\n"
            "}"
        )
        self.Select_proxy_button.setObjectName("Select_proxy_button")
        self.Textline = QtWidgets.QLineEdit(self.frame)
        self.Textline.setGeometry(QtCore.QRect(215, 15, 376, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Variable Small Semibol")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.Textline.setFont(font)
        self.Textline.setStyleSheet(
            "background-color: #2d5b57; \n"
            "color: #37ae85;\n"
            "border-radius: 10px;\n"
            "padding-left: 3px;\n"
            "padding-right: 3px;"
        )
        self.Textline.setText("")
        self.Textline.setObjectName("Textline")
        self.Select_proxy_button_2 = QtWidgets.QPushButton(self.frame)
        self.Select_proxy_button_2.setGeometry(QtCore.QRect(500, 75, 216, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Variable Small Semibol")
        font.setPointSize(14)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.Select_proxy_button_2.setFont(font)
        self.Select_proxy_button_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Select_proxy_button_2.setStyleSheet(
            "QPushButton {\n"
            "    background-color:rgb(73, 92, 108);\n"
            "    color: #37ae85;\n"
            "    border-radius: 10px;\n"
            "}\n"
            "QPushButton:pressed {\n"
            "    background-color:rgb(40, 40, 40);\n"
            "    color: rgb(205, 205, 205);\n"
            "    border-style: outset;\n"
            "    border-radius: 10px;\n"
            "}"
        )
        self.Select_proxy_button_2.setObjectName("Select_proxy_button_2")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(260, 75, 106, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Variable Small Semibol")
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet(
            "background-color:rgb(73, 92, 108);\n"
            "color: #37ae85;\n"
            "border-radius: 10px;"
        )
        self.label_4.setTextFormat(QtCore.Qt.RichText)
        self.label_4.setScaledContents(False)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setWordWrap(False)
        self.label_4.setIndent(0)
        self.label_4.setObjectName("label_4")
        self.spinBox_2 = QtWidgets.QSpinBox(self.frame)
        self.spinBox_2.setGeometry(QtCore.QRect(375, 75, 106, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Variable Small Semibol")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.spinBox_2.setFont(font)
        self.spinBox_2.setStyleSheet(
            "background-color:rgb(73, 92, 108);\n"
            "color: #37ae85;\n"
            "border-radius: 10px;"
        )
        self.spinBox_2.setAlignment(QtCore.Qt.AlignCenter)
        self.spinBox_2.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
        self.spinBox_2.setObjectName("spinBox_2")
        self.all_proxy = QtWidgets.QLineEdit(self.frame)
        self.all_proxy.setGeometry(QtCore.QRect(130, 75, 106, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Variable Small Semibol")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.all_proxy.setFont(font)
        self.all_proxy.setStyleSheet(
            "background-color:rgb(73, 92, 108);\n"
            "color: #37ae85;\n"
            "border-radius: 10px;"
        )
        self.all_proxy.setAlignment(QtCore.Qt.AlignCenter)
        self.all_proxy.setReadOnly(True)
        self.all_proxy.setObjectName("all_proxy")
        self.all_proxy.setText('0')
        MainWindow.setCentralWidget(self.centralwidget)
        """
        """
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(15, 135, 700, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Variable Small Semibol")
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet(
            "background-color:rgb(73, 92, 108);\n"
            "color: #37ae85;\n"
            "border-radius: 10px;"
        )
        self.label_6.setTextFormat(QtCore.Qt.RichText)
        self.label_6.setScaledContents(False)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setWordWrap(False)
        self.label_6.setIndent(0)
        self.label_6.setObjectName("label_6")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.Select_proxy_button.clicked.connect(self.open_file)
        self.Select_proxy_button_2.clicked.connect(self.start)

        self.spinBox_2.setValue(50)
        self.spinBox_2.setMaximum(9999)
        self.spinBox_2.setMinimum(1)

        self.label_6.raise_()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Ахуеть не встать хттпс прокси чекер"))
        self.label_3.setText(
            _translate(
                "MainWindow",
                "<html><head/><body><p><span style=\" font-size:14pt;\">Файл с прокси: </span></p></body></html>"
            )
        )
        self.label_5.setText(
            _translate(
                "MainWindow", "<html><head/><body><p><span style=\" font-size:14pt;\">Всего:</span></p></body></html>"
            )
        )
        self.Select_proxy_button.setText(_translate("MainWindow", "Выбрать"))
        self.Select_proxy_button_2.setText(_translate("MainWindow", "Начать"))
        self.label_4.setText(
            _translate(
                "MainWindow", "<html><head/><body><p><span style=\" font-size:14pt;\">Потоки:</span></p></body></html>"
            )
        )
        self.label_6.setText(
            _translate(
                "MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">|---------IP---------|-----------Страна-----------|---------Город---------|--------ISP--------|</span></p></body></html>"
            )
        )

    def open_file(self):
        open_file_func(self)

    def start(self):
        if self.Textline.text() == '':
            self.plainTextEdit.appendPlainText('Выберите файл с прокси!')
            return
        parsed_proxy = self.parsed_proxy
        threads = self.spinBox_2.value()
        self.plainTextEdit.appendPlainText('Начинаю проверку прокси...\n')

        self.checker = ProxyChecker(parsed_proxy, threads)
        self.checker.update_log.connect(self.update_log)
        self.checker.finished_signal.connect(self.finished)
        self.checker.start()
        self.Select_proxy_button_2.setEnabled(False)

    def update_log(self, data):
        self.plainTextEdit.appendPlainText(data)

    def finished(self):
        self.plainTextEdit.appendPlainText('\n\n\nПроверка прокси завершена!')
        self.Select_proxy_button_2.setEnabled(True)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
