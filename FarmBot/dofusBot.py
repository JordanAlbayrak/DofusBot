from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

time.sleep(2)


def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


while 1:
    try:

        # Paysan--------------------------------------------------------------------
        while pyautogui.locateOnScreen('images/ble.png', confidence=0.6) != None:
            ble = pyautogui.locateOnScreen('images/ble.png', confidence=0.6)
            location = pyautogui.center(ble)
            pyautogui.click(location)
            print("I can see ble")
            time.sleep(6)

        while pyautogui.locateOnScreen('images/ble2.png', confidence=0.6) != None:
            ble = pyautogui.locateOnScreen('images/ble2.png', confidence=0.6)
            location = pyautogui.center(ble)
            pyautogui.click(location)
            print("I can see ble2")
            time.sleep(6)

        while pyautogui.locateOnScreen('images/orge.png', confidence=0.6) != None:
            orge = pyautogui.locateOnScreen('images/orge.png', confidence=0.6)
            location = pyautogui.center(orge)
            pyautogui.click(location)
            print("I can see orge")
            time.sleep(6)

        while pyautogui.locateOnScreen('images/orge2.png', confidence=0.6) != None:
            orge = pyautogui.locateOnScreen('images/orge2.png', confidence=0.6)
            location = pyautogui.center(orge)
            pyautogui.click(location)
            print("I can see orge2")
            time.sleep(6)

        while pyautogui.locateOnScreen('images/avoine.png', confidence=0.5) != None:
            avoine = pyautogui.locateOnScreen('images/avoine.png', confidence=0.5)
            location = pyautogui.center(avoine)
            pyautogui.click(location)
            print("I can see avoine")
            time.sleep(6)
        while pyautogui.locateOnScreen('images/avoine2.png', confidence=0.5) != None:
            avoine2 = pyautogui.locateOnScreen('images/avoine2.png', confidence=0.5)
            location = pyautogui.center(avoine2)
            pyautogui.click(location)
            print("I can see avoine2")
            time.sleep(6)
        while pyautogui.locateOnScreen('images/avoine3.png', confidence=0.5) != None:
            avoine3 = pyautogui.locateOnScreen('images/avoine3.png', confidence=0.5)
            location = pyautogui.center(avoine3)
            pyautogui.click(location)
            print("I can see avoine3")
            time.sleep(6)
        # Alchimiste--------------------------------------------------------------------
        while pyautogui.locateOnScreen('images/sauge.png', confidence=0.6) != None:
            sauge = pyautogui.locateOnScreen('images/sauge.png', confidence=0.6)
            location = pyautogui.center(sauge)
            pyautogui.click(location)
            print("I can see sauge")
            time.sleep()
        while pyautogui.locateOnScreen('images/sauge2.png', confidence=0.6) != None:
            sauge2 = pyautogui.locateOnScreen('images/sauge2.png', confidence=0.6)
            location = pyautogui.center(sauge2)
            pyautogui.click(location)
            print("I can see sauge2")
            time.sleep(8)
        while pyautogui.locateOnScreen('images/clover.png', confidence=0.5) != None:
            clover = pyautogui.locateOnScreen('images/clover.png', confidence=0.5)
            location = pyautogui.center(clover)
            pyautogui.click(location)
            print("I can see clover")
            time.sleep(8)
        while pyautogui.locateOnScreen('images/ortie.png', confidence=0.6) != None:
            ortie = pyautogui.locateOnScreen('images/ortie.png', confidence=0.6)
            location = pyautogui.center(ortie)
            pyautogui.click(location)
            print("I can see ortie")
            time.sleep(8)
        while pyautogui.locateOnScreen('images/ortie2.png', confidence=0.8) != None:
            ortie2 = pyautogui.locateOnScreen('images/ortie2.png', confidence=0.8)
            location = pyautogui.center(ortie2)
            pyautogui.click(location)
            print("I can see ortie2")
            time.sleep(8)
        while pyautogui.locateOnScreen('images/flower.png', confidence=0.6) != None:
            flower = pyautogui.locateOnScreen('images/flower.png', confidence=0.6)
            location = pyautogui.center(flower)
            pyautogui.click(location)
            print("I can see flower")
            time.sleep(8)
        while pyautogui.locateOnScreen('images/plant.png', confidence=0.7) != None:
            plant = pyautogui.locateOnScreen('images/plant.png', confidence=0.7)
            location = pyautogui.center(plant)
            pyautogui.click(location)
            print("I can see plant")
            time.sleep(8)
        while pyautogui.locateOnScreen('images/mint.png', confidence=0.65) != None:
            mint = pyautogui.locateOnScreen('images/mint.png', confidence=0.65)
            location = pyautogui.center(mint)
            pyautogui.click(location)
            print("I can see mint")
            time.sleep(8)
        while pyautogui.locateOnScreen('images/plant2.png', confidence=0.85) != None:
            plant2 = pyautogui.locateOnScreen('images/plant2.png', confidence=0.85)
            location = pyautogui.center(plant2)
            pyautogui.click(location)
            print("I can see plant2")
            time.sleep(8)
        while pyautogui.locateOnScreen('images/flower2.png', confidence=0.9) != None:
            flower2 = pyautogui.locateOnScreen('images/flower2.png', confidence=0.9)
            location = pyautogui.center(flower2)
            pyautogui.click(location)
            print("I can see flower2")
            time.sleep(8)
        while pyautogui.locateOnScreen('images/mint2.png', confidence=0.7) != None:
            mint2 = pyautogui.locateOnScreen('images/mint2.png', confidence=0.7)
            location = pyautogui.center(mint2)
            pyautogui.click(location)
            print("I can see mint2")
            time.sleep(8)
        while pyautogui.locateOnScreen('images/clover2.png', confidence=0.7) != None:
            clover2 = pyautogui.locateOnScreen('images/clover2.png', confidence=0.7)
            location = pyautogui.center(clover2)
            pyautogui.click(location)
            print("I can see clover2")
            time.sleep(6)
        while pyautogui.locateOnScreen('images/clover3.png', confidence=0.65) != None:
            clover3 = pyautogui.locateOnScreen('images/clover3.png', confidence=0.65)
            location = pyautogui.center(clover3)
            pyautogui.click(location)
            print("I can see clover3")
            time.sleep(6)
        while pyautogui.locateOnScreen('images/clover4.png', confidence=0.65) != None:
            clover4 = pyautogui.locateOnScreen('images/clover4.png', confidence=0.65)
            location = pyautogui.center(clover4)
            pyautogui.click(location)
            print("I can see clover4")
            time.sleep(6)
        while pyautogui.locateOnScreen('images/mint3.png', confidence=0.7) != None:
            mint3 = pyautogui.locateOnScreen('images/mint3.png', confidence=0.7)
            location = pyautogui.center(mint3)
            pyautogui.click(location)
            print("I can see mint3")
            time.sleep(6)
        while pyautogui.locateOnScreen('images/clover5.png', confidence=0.75) != None:
            clover5 = pyautogui.locateOnScreen('images/clover5.png', confidence=0.75)
            location = pyautogui.center(clover5)
            pyautogui.click(location)
            print("I can see clover5")
            time.sleep(6)
        # Bucheron--------------------------------------------------------------------
        while pyautogui.locateOnScreen('images/frene1.png', confidence=0.85) != None:
            frene1 = pyautogui.locateOnScreen('images/frene1.png', confidence=0.85)
            location = pyautogui.center(frene1)
            pyautogui.click(location)
            print("I can see frene1")
            time.sleep(8)
        while pyautogui.locateOnScreen('images/frene2.png', confidence=0.65) != None:
            frene2 = pyautogui.locateOnScreen('images/frene2.png', confidence=0.65)
            location = pyautogui.center(frene2)
            pyautogui.click(location)
            print("I can see frene2")
            time.sleep(8)
        while pyautogui.locateOnScreen('images/chat.png', confidence=0.75) != None:
            chat = pyautogui.locateOnScreen('images/chat.png', confidence=0.75)
            location = pyautogui.center(chat)
            pyautogui.click(location)
            print("I can see chat")
            time.sleep(8)
        while pyautogui.locateOnScreen('images/chat2.png', confidence=0.7) != None:
            chat2 = pyautogui.locateOnScreen('images/chat2.png', confidence=0.7)
            location = pyautogui.center(chat2)
            pyautogui.click(location)
            print("I can see chat2")
            time.sleep(8)
        # Combat--------------------------------------------------------------------
        while pyautogui.locateOnScreen('images/combat.png', confidence=0.8) is not None:
            pyautogui.press('f1')
            time.sleep(2)
            pyautogui.press('f1')
            while pyautogui.locateOnScreen('images/spell2.png', confidence=0.8) != None:
                spell2 = pyautogui.locateOnScreen('images/spell2.png', confidence=0.8)
                location = pyautogui.center(spell2)
                pyautogui.click(location)
                time.sleep(1)
                spellthere = pyautogui.locateOnScreen('images/spellthere.png', confidence=0.7)
                location = pyautogui.center(spellthere)
                time.sleep(1)
                pyautogui.click(location)
                time.sleep(8)

        if pyautogui.locateOnScreen('images/fermerCombat.png', confidence=0.8) != None:
            fermerCombat = pyautogui.locateOnScreen('images/fermerCombat.png', confidence=0.8)
            print("I will close the battle screen now")
            location = pyautogui.center(fermerCombat)
            pyautogui.click(location)
            time.sleep(5)
        else:
            print("I am unable to see anything")
            time.sleep(3.3)

    except Exception as ex:
        print(ex)
        print("Exception raised, restarting...")
