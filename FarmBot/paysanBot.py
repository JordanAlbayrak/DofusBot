from pyautogui import * 
import pyautogui 
import time 
import keyboard 
import random
import win32api, win32con


time.sleep(2)

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
try:
    while 1:


            while pyautogui.locateOnScreen('ble.png', confidence=0.6) != None:
                ble = pyautogui.locateOnScreen('ble.png', confidence = 0.6)
                location = pyautogui.center(ble)
                pyautogui.click(location)
                print("I can see ble")       
                time.sleep(6)
                
            while pyautogui.locateOnScreen('ble2.png', confidence=0.6) != None:
                ble = pyautogui.locateOnScreen('ble2.png', confidence = 0.6)
                location = pyautogui.center(ble)
                pyautogui.click(location)
                print("I can see ble2")       
                time.sleep(6)

            while pyautogui.locateOnScreen('orge.png', confidence=0.6) != None:
                orge = pyautogui.locateOnScreen('orge.png', confidence = 0.6)
                location = pyautogui.center(orge)
                pyautogui.click(location)
                print("I can see orge")       
                time.sleep(6)
                
            while pyautogui.locateOnScreen('orge2.png', confidence=0.6) != None:
                orge = pyautogui.locateOnScreen('orge2.png', confidence = 0.6)
                location = pyautogui.center(orge)
                pyautogui.click(location)
                print("I can see orge2")       
                time.sleep(6)
                
            while pyautogui.locateOnScreen('avoine.png', confidence=0.5) != None:
                avoine = pyautogui.locateOnScreen('avoine.png', confidence = 0.5)
                location = pyautogui.center(avoine)
                pyautogui.click(location)
                print("I can see avoine")       
                time.sleep(6)
            while pyautogui.locateOnScreen('avoine2.png', confidence=0.5) != None:
                avoine2 = pyautogui.locateOnScreen('avoine2.png', confidence = 0.5)
                location = pyautogui.center(avoine2)
                pyautogui.click(location)
                print("I can see avoine2")       
                time.sleep(6)
            while pyautogui.locateOnScreen('avoine3.png', confidence=0.5) != None:
                avoine3 = pyautogui.locateOnScreen('avoine3.png', confidence = 0.5)
                location = pyautogui.center(avoine3)
                pyautogui.click(location)
                print("I can see avoine3")       
                time.sleep(6)

                    
            while   pyautogui.locateOnScreen('combat.png', confidence=0.8) != None:
                pyautogui.press('f1')
                time.sleep(2)
                pyautogui.press('f1')
                while   pyautogui.locateOnScreen('spell2.png', confidence=0.8) != None:
                        spell2 = pyautogui.locateOnScreen('spell2.png', confidence = 0.8)
                        location = pyautogui.center(spell2)
                        pyautogui.click(location)
                        time.sleep(2)
                        spellthere = pyautogui.locateOnScreen('spellthere.png', confidence = 0.75)
                        location = pyautogui.center(spellthere)
                        time.sleep(1)
                        pyautogui.click(location)
                        time.sleep(2)
                        
                

            if pyautogui.locateOnScreen('fermerCombat.png', confidence=0.8) != None:
                print("I will close the battle screen now")
                fermerCombat = pyautogui.locateOnScreen('fermerCombat.png', confidence = 0.8)
                location = pyautogui.center(fermerCombat)
                pyautogui.click(location)
                time.sleep(4)

            else:
                print("I am unable to see anything")
                time.sleep(3)
except:
        raise
else:
    commit()
