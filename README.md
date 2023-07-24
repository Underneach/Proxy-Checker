# Proxy-Checker

![image](https://github.com/Underneach/Proxy-Checker/assets/137613889/cc51b568-839d-4fda-b81a-d984086caca7)


### HTTP/Socks прокси чекер с многопоточной реализацией

    * Работает с socks4/5 и http/s прокси
    * Определение GEO и ISP IP
    * Мультипоточность (Асинхронный пул потоков ThreadPoolExecutor)
    * Запись валидных проксей в "valid.txt" и невалидных в "invalid.txt"

### Потоки
    12 Ядер - 1000 потоков
    8 Ядер - 600 потоков
    4 Ядра - 300 потоков

### Стек:
    UI - PyQT5
    Net - httpx + sosksio

### Собранный EXE
https://github.com/Underneach/Proxy-Checker/releases/
