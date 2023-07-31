from modules.checker import ProxyChecker


def Start(self):
    if self.ui.Textline.text() == '':
        self.ui.plainTextEdit.appendPlainText('Выберите файл с прокси!')
        return

    parsed_proxy = self.parsed_proxy
    threads = self.ui.spinBox_2.value()
    protocol = str(self.ui.comboBox.currentText())

    self.ui.plainTextEdit.appendPlainText('Начинаю проверку прокси...\n')

    self.valid_proxy_stat = 0
    self.invalid_proxy_stat = 0
    self.checked_proxy_stat = 0

    self.checker = ProxyChecker(parsed_proxy, protocol, threads)
    self.checker.update_log.connect(self.update_log)
    self.checker.stat_log.connect(self.update_stat)
    self.checker.finished_signal.connect(self.finished)
    self.checker.start()

    self.ui.Start.setEnabled(False)
    self.ui.spinBox_2.setEnabled(False)
    self.ui.comboBox.setEnabled(False)
    self.ui.Select_proxy_button.setEnabled(False)
    self.ui.Textline.setEnabled(False)
    self.ui.all_proxy.setEnabled(False)
    self.ui.Start.setText('В работе...')
