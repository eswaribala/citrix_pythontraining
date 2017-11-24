'''
Created on 21-Aug-2017

@author: BALASUBRAMANIAM
'''
from datetime import date
import pyautogui
print(pyautogui.screenshot())
#save to file
datestr=date.today().strftime("%d-%m-%Y")

pyautogui.screenshot('screentest'+datestr+'.png')  