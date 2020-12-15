# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 21:36:16 2020

@author: user
"""

import pyautogui,time
time.sleep(5)
f=open("bee.txt","r")

for word in f:
    pyautogui.typewrite(word)
    pyautogui.press("enter")
    