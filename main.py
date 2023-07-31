import os
import sys

from PySide6 import QtGui
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QApplication, QMainWindow

from modules.finished import Finished
from modules.open_file import open_file_func
from modules.set_stat import Set_Stat
from modules.start import Start
from modules.update_stat import Update_stat


def resource_path(relative_path):
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)


class Checker(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = QUiLoader().load(resource_path("modules/app.ui"), self)
        self.setWindowIcon(QtGui.QIcon(resource_path('modules/icon.ico')))

        self.ui.comboBox.addItems(['http', 'socks4', 'socks5'])
        self.ui.Select_proxy_button.clicked.connect(self.open_file)
        self.ui.Start.clicked.connect(self.start)

        self.ui.show()

    def open_file(self):
        open_file_func(self)

    def start(self):
        Start(self)

    def update_log(self, data):
        self.ui.plainTextEdit.appendPlainText(data)

    def update_stat(self, info):
        Update_stat(self, info)

    def set_stat(self, valid_proxy_stat, invalid_proxy_stat, checked_proxy_stat, unchecked_proxy_stat):
        Set_Stat(self, valid_proxy_stat, invalid_proxy_stat, checked_proxy_stat, unchecked_proxy_stat)

    def finished(self):
        Finished(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Checker()
    sys.exit(app.exec())
