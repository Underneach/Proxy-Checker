def Set_Stat(self, valid_proxy_stat, invalid_proxy_stat, checked_proxy_stat, unchecked_proxy_stat):
    self.valid_proxy.setText(str(valid_proxy_stat))
    self.invalid_proxy.setText(str(invalid_proxy_stat))
    self.checked_proxy.setText(str(checked_proxy_stat))
    self.unchecked_proxy.setText(str(unchecked_proxy_stat))
