def Set_Stat(self, valid_proxy_stat, invalid_proxy_stat, checked_proxy_stat, unchecked_proxy_stat):
    self.ui.valid_proxy.setText(str(valid_proxy_stat))
    self.ui.invalid_proxy.setText(str(invalid_proxy_stat))
    self.ui.checked_proxy.setText(str(checked_proxy_stat))
    self.ui.unchecked_proxy.setText(str(unchecked_proxy_stat))
