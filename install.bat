@echo off && title Install All Tweaker && mode con: cols=100 lines=25 && color a

REM Загружаем библиотеку ttkbootstrap
pip install ttkbootstrap

REM Загружаем All Tweaker с GitHub
Utils\\busybox wget https://github.com/scode18/All-Tweaker/raw/main/All.Tweaker.py
Utils\\busybox wget https://github.com/scode18/All-Tweaker/raw/main/tabs_data.py

Utils\\busybox wget https://github.com/scode18/All-Tweaker/raw/main/All.Tweaker.featuring.Howdy.Ho.py
Utils\\busybox wget https://github.com/scode18/All-Tweaker/raw/main/All.Tweaker.Start.bat
Utils\\busybox wget https://github.com/scode18/All-Tweaker/raw/main/elevator.exe
Utils\\busybox wget https://github.com/scode18/All-Tweaker/raw/main/launcher.exe

REM Создаем ярлык на рабочем столе с иконкой icon.ico
echo Set oWS = WScript.CreateObject("WScript.Shell") > CreateShortcut.vbs
echo sLinkFile = oWS.ExpandEnvironmentStrings("%USERPROFILE%\Desktop\All Tweaker.lnk") >> CreateShortcut.vbs
echo Set oLink = oWS.CreateShortcut(sLinkFile) >> CreateShortcut.vbs
echo oLink.TargetPath = "%CD%\All.Tweaker.Start.bat" >> CreateShortcut.vbs
echo oLink.IconLocation = "%CD%\icon.ico" >> CreateShortcut.vbs
echo oLink.WorkingDirectory = "%CD%" >> CreateShortcut.vbs
echo oLink.Save >> CreateShortcut.vbs
cscript CreateShortcut.vbs

REM Удаляем временный файл CreateShortcut.vbs
del CreateShortcut.vbs

REM Запускаем All Tweaker
All.Tweaker.Start.bat
