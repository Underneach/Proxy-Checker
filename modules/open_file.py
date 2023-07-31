from PySide6.QtWidgets import QFileDialog


def open_file_func(self):
    self.parsed_proxy = []
    try:
        self.proxy_file_path, _ = QFileDialog.getOpenFileName(
            parent=self,
            caption='Open File',
            dir='./',
            filter='TXT File (*.txt)'
            )
        if self.proxy_file_path:
            self.ui.Textline.setText(str(self.proxy_file_path))
            self.ui.Textline.end(False)

            with open(self.proxy_file_path, 'r') as file:
                lines = file.readlines()
            self.parsed_proxy.clear()
            for line in lines:
                line = line.strip()
                self.parsed_proxy.append(line)
            self.ui.all_proxy.setText(f"{len(self.parsed_proxy)}")
            self.ui.unchecked_proxy.setText(f"{len(self.parsed_proxy)}")
            self.unchecked_proxy_stat = len(self.parsed_proxy)
        else:
            return
    except Exception as message:
        self.ui.plainTextEdit.appendPlainText(f'[-] Ошибка: {str(message)}')
