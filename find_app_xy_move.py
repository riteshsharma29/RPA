#!/usr/bin/python

import pygetwindow as gw
from pywinauto import application
import pyautogui
import time
import win32api

app = application.Application()
app.start('calc.exe')
time.sleep(8)

#Move app to x,y position
calwindow = gw.getWindowsWithTitle('Calculator')[0]
calwindow.moveTo(0,0)

#Loop to find Button Positions

while True:
    time.sleep(5)
    x,y = win32api.GetCursorPos()
    print(x,y)

