from modules.checker import ProxyChecker


def Start(self):
    if self.Textline.text() == '':
        self.plainTextEdit.appendPlainText('Выберите файл с прокси!')
        return

    parsed_proxy = self.parsed_proxy
    threads = self.spinBox_2.value()
    protocol = self.comboBox.currentText()

    self.plainTextEdit.appendPlainText('Начинаю проверку прокси...\n')

    self.valid_proxy_stat = 0
    self.invalid_proxy_stat = 0
    self.checked_proxy_stat = 0

    self.checker = ProxyChecker(parsed_proxy, threads, protocol)
    self.checker.update_log.connect(self.update_log)
    self.checker.stat_log.connect(self.update_stat)
    self.checker.finished_signal.connect(self.finished)
    self.checker.start()

    self.Start.setEnabled(False)
    self.Start.setText('В работе...')
