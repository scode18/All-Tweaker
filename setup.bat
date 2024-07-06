@echo off && title Install All Tweaker && mode con: cols=100 lines=25 && color a

Utils\busybox wget https://github.com/scode18/All-Tweaker/raw/main/update.bat
Utils\busybox wget https://github.com/scode18/All-Tweaker/raw/main/tabs_data.py

update.bat
