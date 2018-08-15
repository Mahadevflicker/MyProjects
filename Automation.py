# -*- coding: utf-8 -*-
"""
Created on Fri Mar  9 09:16:46 2018

@author: appu
"""

from pywinauto import application
import time

app = application.Application()
app.start('Notepad.exe')
time.sleep(1)
app.Notepad.edit.TypeKeys("Hello World")

app.Notepad.MenuSelect("File -> SaveAs")
app.SaveAs.edit.SetText("hello.txt")
time.sleep(1)
app.SaveAs.Save.Click()
app.Notepad.MenuSelect("File -> Exit")