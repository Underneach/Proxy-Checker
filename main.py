from PyQt5 import QtWidgets, uic

from modules.checker import ProxyChecker
from modules.open_file import open_file_func


class Ui_MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("modules/app.ui", self)

        self.comboBox.addItems(['http', 'socks4', 'socks5'])

        self.Select_proxy_button.clicked.connect(self.open_file)
        self.Start.clicked.connect(self.start)

    def open_file(self):
        open_file_func(self)

    def start(self):

        if self.Textline.text() == '':
            self.plainTextEdit.appendPlainText('Выберите файл с прокси!')
            return

        parsed_proxy = self.parsed_proxy
        threads = self.spinBox_2.value()
        protocol = self.comboBox.currentText()

        self.plainTextEdit.appendPlainText('Начинаю проверку прокси...\n')

        self.checker = ProxyChecker(parsed_proxy, threads, protocol)
        self.checker.update_log.connect(self.update_log)
        self.checker.finished_signal.connect(self.finished)
        self.checker.start()

        self.Start.setEnabled(False)
        self.Start.setText('В работе...')

    def update_log(self, data):
        self.plainTextEdit.appendPlainText(data)

    def finished(self):
        self.plainTextEdit.appendPlainText('\n\n\nПроверка прокси завершена!')
        self.Start.setEnabled(True)
        self.Start.setText('Начать')


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = Ui_MainWindow()
    window.show()
    app.exec_()
