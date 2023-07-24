from modules.checker import ProxyChecker


def Start(self):
    if self.Textline.text() == '':
        self.plainTextEdit.appendPlainText('Выберите файл с прокси!')
        return

    parsed_proxy = self.parsed_proxy
    threads = self.spinBox_2.value()
    protocol = str(self.comboBox.currentText())

    self.plainTextEdit.appendPlainText('Начинаю проверку прокси...\n')

    self.valid_proxy_stat = 0
    self.invalid_proxy_stat = 0
    self.checked_proxy_stat = 0

    self.checker = ProxyChecker(parsed_proxy, protocol, threads)
    self.checker.update_log.connect(self.update_log)
    self.checker.stat_log.connect(self.update_stat)
    self.checker.finished_signal.connect(self.finished)
    self.checker.start()

    self.Start.setEnabled(False)
    self.spinBox_2.setEnabled(False)
    self.comboBox.setEnabled(False)
    self.Select_proxy_button.setEnabled(False)
    self.Textline.setEnabled(False)
    self.all_proxy.setEnabled(False)
    self.Start.setText('В работе...')
