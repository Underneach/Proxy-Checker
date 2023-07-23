import os
import sys

from PyQt5 import QtWidgets, uic, QtGui

from modules.open_file import open_file_func
from modules.start import Start
from modules.update_stat import Update_stat


def resource_path(relative_path):
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)


class Ui_MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(resource_path("modules/app.ui"), self)
        self.setWindowIcon(QtGui.QIcon(resource_path('modules/icon.ico')))

        self.comboBox.addItems(['http', 'socks4', 'socks5'])

        self.Select_proxy_button.clicked.connect(self.open_file)
        self.Start.clicked.connect(self.start)

    def open_file(self):
        open_file_func(self)

    def start(self):
        Start(self)

    def update_log(self, data):
        self.plainTextEdit.appendPlainText(data)

    def update_stat(self, info):
        Update_stat(self, info)

    def set_stat(self, valid_proxy_stat, invalid_proxy_stat, checked_proxy_stat, unchecked_proxy_stat):
        self.valid_proxy.setText(str(valid_proxy_stat))
        self.invalid_proxy.setText(str(invalid_proxy_stat))
        self.checked_proxy.setText(str(checked_proxy_stat))
        self.unchecked_proxy.setText(str(unchecked_proxy_stat))

    def finished(self):
        self.plainTextEdit.appendPlainText('\n\n\nПроверка прокси завершена!')
        self.Start.setEnabled(True)
        self.Start.setText('Начать')
        self.plainTextEdit.appendPlainText('\n\nРезультаты проверки сохранены в файлы valid.txt и invalid.txt')


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = Ui_MainWindow()
    window.show()
    app.exec_()
