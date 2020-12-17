# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 21:36:16 2020

@author: user
"""


import pyautogui,time
import random
## before started let it sleep for a while.
time.sleep(5)
##f=open("bee.txt","r")
file=open("spamming.txt","r").read()
file=file.splitlines()

for _ in range(20):
    pyautogui.typewrite(random.choice(file))
    pyautogui.press("enter")
    