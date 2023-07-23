from PyQt5.QtWidgets import QFileDialog


def open_file_func(self):
    self.parsed_proxy = []
    try:
        self.proxy_file_path, _ = QFileDialog.getOpenFileName(None, 'Open File', './', 'TXT File (*.txt)')
        if self.proxy_file_path:
            self.Textline.setText(str(self.proxy_file_path))
            self.Textline.end(False)

            with open(self.proxy_file_path, 'r') as file:
                lines = file.readlines()
            self.parsed_proxy.clear()
            for line in lines:
                line = line.strip()  # Удалить лишние пробелы и символы новой строки
                self.parsed_proxy.append(line)  # Добавить обработанную строку
            self.all_proxy.setText(f"{len(self.parsed_proxy)}")
            self.unchecked_proxy.setText(f"{len(self.parsed_proxy)}")
            self.unchecked_proxy_stat = len(self.parsed_proxy)
        else:
            return
    except Exception as message:
        self.plainTextEdit.appendPlainText(f'[-] Ошибка: {str(message)}')
