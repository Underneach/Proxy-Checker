def Update_stat(self, info):
    if info == "valid":
        self.valid_proxy_stat += 1
    elif info == "invalid":
        self.invalid_proxy_stat += 1

    self.checked_proxy_stat += 1
    self.unchecked_proxy_stat -= 1

    self.set_stat(
        self.valid_proxy_stat, self.invalid_proxy_stat, self.checked_proxy_stat, self.unchecked_proxy_stat
    )
