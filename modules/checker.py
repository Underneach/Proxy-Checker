import concurrent.futures

import httpx
import socksio
from PySide6.QtCore import Signal, QThread


class ProxyChecker(QThread):
    update_log = Signal(str)
    stat_log = Signal(str)
    finished_signal = Signal()

    def __init__(self, parsed_proxy, protocol, threads):
        super().__init__()
        self.parsed_proxy = parsed_proxy
        self.threads = threads
        self.protocol = protocol

    def run(self):
        with concurrent.futures.ThreadPoolExecutor(max_workers=self.threads) as executor:
            futures = []
            for proxy in self.parsed_proxy:
                future = executor.submit(self.checker, self.protocol, proxy)
                futures.append(future)

            concurrent.futures.wait(futures)

        self.finished_signal.emit()

    def checker(self, protocol, proxy):
        with httpx.Client(http2=True, timeout=5) as client, open('valid.txt', 'a') as valid_file, open(
                'invalid.txt', 'a'
        ) as invalid_file:
            try:
                ip = proxy.split(':')[0]

                client.proxies = {'https': f'{protocol}://{proxy}'}
                response = client.get('http://www.example.com')

                if response.status_code == 200:

                    geo_response = client.get(f"http://ip-api.com/json/{ip}")

                    try:
                        geo_data = geo_response.json()
                    except Exception:
                        geo_data = {'country': 'Неизвестно', 'city': 'Неизвестно', 'isp': 'Неизвестно'}

                    valid_file.write(f"{proxy}\n")
                    self.update_log.emit(
                        str(
                            "|{:^21}|{:^28}|{:^28}|{:^32}|".format(
                                ip, geo_data['country'][:30], geo_data['city'][:30], geo_data['isp'][:34]
                            )
                        )
                    )
                    self.stat_log.emit("valid")

                else:
                    invalid_file.write(f"{proxy}\n")
                    self.update_log.emit(f" {ip} | Невалид")
                    self.stat_log.emit("invalid")

            except Exception as e:
                invalid_file.write(f"{proxy} {e}\n")
                self.update_log.emit(f" {ip} | Невалид | {str(e)}")
                self.stat_log.emit("invalid")
