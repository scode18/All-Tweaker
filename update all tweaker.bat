@echo off && title Install All Tweaker && mode con: cols=100 lines=25 && color a
chcp 65001
cls

REM Проверяем, установлен ли Python
python --version >nul 2>&1
if %errorlevel% equ 0 (
    echo Python уже установлен.
) else (
    echo Python не установлен. Загрузка и установка...
    
    REM Загружаем Python
    Utils\busybox wget https://www.python.org/ftp/python/3.12.3/python-3.12.3-amd64.exe
    
    echo Устанавливаем Python без графического интерфейса
    python-3.12.3-amd64.exe /quiet InstallAllUsers=1 PrependPath=1
    
    REM Удаляем загруженный установочный файл
    del python-3.12.3-amd64.exe
    
    echo Python успешно установлен.
)

REM Загружаем All Tweaker с GitHub
Utils\busybox wget https://scode18.github.io/All-Tweaker/Tweaks.7z
Utils\busybox wget https://scode18.github.io/All-Tweaker/icon.ico
Utils\busybox wget https://scode18.github.io/All-Tweaker/All Tweaker.py

REM Распаковываем архив с помощью 7z
Utils\7za x tweaks.7z

REM Удаляем загруженный архив
del tweaks.7z

REM Запускаем скрипт All Tweaker.py
C:\Windows\py.exe "All Tweaker.py"