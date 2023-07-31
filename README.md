# Proxy-Checker

![image](https://github.com/Underneach/Proxy-Checker/assets/137613889/6a0efbab-9a0f-45f4-a651-7fdfb5aed735)


### HTTP/Socks прокси чекер с многопоточной реализацией

    * Работает с socks4/5 и http/s прокси
    * Определение GEO и ISP IP
    * Мультипоточность (Асинхронный пул потоков ThreadPoolExecutor)
    * Запись валидных проксей в "valid.txt" и невалидных в "invalid.txt"
    * Time out 10 секунд

### Производительность
    12 Ядер - 800 потоков - 1 Gb Ram
    8 Ядер - 600 потоков - 0.8 Gb Ram
    4 Ядра - 300 потоков - 0.3 Gb Ram

### Стек:
    UI - PySide6
    Net - httpx + sosksio
    Build - Nuitka / Pyinstaller
    

### Собранный EXE
https://github.com/Underneach/Proxy-Checker/releases/
