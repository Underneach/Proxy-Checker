# Proxy-Checker
![image](https://github.com/Underneach/Proxy-Checker/assets/137613889/46e90b39-b0f0-4316-b462-f5f8d3dcc45c)

### HTTP/Socks прокси чекер с многопоточной реализацией

UI - PyQT5

Net - httpx + sosksio

* Работает с socks4/5 и http/s прокси
* Мультипоточность (Асинхронный пул потоков ThreadPoolExecutor)
* Запись валидных проксей в "valid.txt" и невалидных в "invalid.txt"
