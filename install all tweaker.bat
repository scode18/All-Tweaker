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
    Files\busybox wget https://www.python.org/ftp/python/3.12.3/python-3.12.3-amd64.exe
    
    echo Устанавливаем Python без графического интерфейса
    python-3.12.3-amd64.exe /quiet InstallAllUsers=1 PrependPath=1
    
    REM Удаляем загруженный установочный файл
    del python-3.12.3-amd64.exe
    
    echo Python успешно установлен.
)

REM Загружаем репозиторий с GitHub
Files\busybox wget https://scode18.github.io/All-Tweaker/Tweaks.7z

REM Распаковываем архив с помощью 7z
Files\7za x Tweaks.7z

REM Удаляем загруженный архив
del Tweaks.7z

REM Запускаем скрипт main.py
C:\Windows\py.exe "Files\make.py"

REM Создаем ярлык на рабочем столе с иконкой icon.ico
echo Set oWS = WScript.CreateObject("WScript.Shell") > CreateShortcut.vbs
echo sLinkFile = oWS.ExpandEnvironmentStrings("%USERPROFILE%\Desktop\All Tweaker.lnk") >> CreateShortcut.vbs
echo Set oLink = oWS.CreateShortcut(sLinkFile) >> CreateShortcut.vbs
echo oLink.TargetPath = "%CD%\All Tweaker.py" >> CreateShortcut.vbs
echo oLink.IconLocation = "%CD%\Files\icon.ico" >> CreateShortcut.vbs
echo oLink.Save >> CreateShortcut.vbs
cscript CreateShortcut.vbs

REM Удаляем временный файл CreateShortcut.vbs
del CreateShortcut.vbs

rem echo Скрипт выполнен успешно.
rem pause