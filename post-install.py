import os

os.system('@echo off && title Install All Tweaker && mode con: cols=100 lines=25 && color a')
os.system('pip install ttkbootstrap')
os.system('Utils\\busybox wget https://github.com/scode18/All-Tweaker/raw/main/All.Tweaker.py')
os.system('python All.Tweaker.py.py')
