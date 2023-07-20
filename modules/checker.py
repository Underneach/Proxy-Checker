import concurrent.futures

import httpx
import socksio
from PyQt5.QtCore import QThread, pyqtSignal


class ProxyChecker(QThread):
    update_log = pyqtSignal(str)
    finished_signal = pyqtSignal()

    def __init__(self, parsed_proxy, threads, protocol):
        super().__init__()
        self.parsed_proxy = parsed_proxy
        self.threads = threads
        self.protocol = protocol

    def run(self):
        with concurrent.futures.ThreadPoolExecutor(max_workers=self.threads) as executor:
            futures = []  # Создаем пустой список futures
            for proxy in self.parsed_proxy:
                future = executor.submit(self.checker, proxy)
                futures.append(future)  # Добавляем future в список

            concurrent.futures.wait(futures)

        self.finished_signal.emit()

    def checker(self, proxy):
        url = 'https://www.example.com'
        with httpx.Client(http2=True, timeout=10) as client, open('valid.txt', 'a') as valid_file, open(
                'invalid.txt', 'a'
                ) as invalid_file:
            try:
                client.proxies = {f'{self.protocol}://{proxy}'}
                response = client.get(url)
                if response.status_code == 200:

                    ip = proxy.split('@')[-1].split(':')[0]
                    geo_url = f"http://ip-api.com/json/{ip}"
                    geo_response = client.get(geo_url)
                    if geo_response.status_code == 200:
                        geo_data = geo_response.json()
                        valid_file.write(f"{proxy}\n")
                        self.update_log.emit(
                            str(
                                "|{:^23}|{:^29}|{:^28}|{:^32}|".format(
                                    ip, geo_data['country'][:26], geo_data['city'][:28], geo_data['isp'][:30]
                                    )
                                )
                        )
                else:
                    ip = proxy.split('@')[-1].split(':')[0]
                    invalid_file.write(f"{proxy}\n")
                    self.update_log.emit(f"{ip} Невалид")

            except (httpx.ProxyError, httpx.ConnectError, httpx.ConnectTimeout, httpx.ReadTimeout) as e:
                invalid_file.write(f"{proxy}\n")
                self.update_log.emit(f"{proxy} Невалид")

            except (socksio.ProxyConnectionError, socksio.ProxyTimeoutError) as e:
                invalid_file.write(f"{proxy}\n")
                self.update_log.emit(f"{proxy} Невалид")

            except Exception as e:
                invalid_file.write(f"{proxy}\n")
                self.update_log.emit(f"{proxy} Невалид: {e}")