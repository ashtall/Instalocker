import pyautogui
import mouse
import numpy as np
import cv2 as cv
from PIL import ImageGrab, Image
from pynput.mouse import Button, Controller
import tkinter as tk
from tkinter import ttk
import tkinter.font as tkfont
import threading
import time


#window config
root = tk.Tk()
root.geometry("250x100")
root.title("Instalocker")
root.configure(bg="#FD4556")
root.maxsize(250,100)
root.iconbitmap("pics/valologo.ico")

curAgent = "NoneSelected"


#lockin coords
lxcoord = 961
lycoord = 826

mouse= Controller()

checkRegion = (900, 800, 20, 30)
imagecheck = cv.imread("pics/lockimage.png")

def benchmark_opencv_pil():
    while True:
        img = ImageGrab.grab(bbox=None)
        img = np.array(img)
        img_cv = cv.cvtColor(img, cv.COLOR_RGB2BGR)
        res = cv.matchTemplate(img_cv, imagecheck, cv.TM_CCOEFF_NORMED)
        min_val,max_val,min_loc,max_loc = cv.minMaxLoc(res)

        threshold = 0.8

        if max_val >= threshold:
            return True

def click_mouse(x, y):
    mouse.position = (x,y)
    mouse.click(button=Button.left)
    print('click')

def startChecking():
    print("started")
    global isRunning
    isRunning = threading.Event()
    threading.Thread(target=checking,args=(isRunning,)).start()
    root.configure(bg='#3be0c3')

def stopChecking():
    print("stopped")
    global isRunning
    isRunning.set()
    root.configure(bg="#FD4556")

def checking(isRunning):
        while not isRunning.is_set():
            #check for match found
            islogo = benchmark_opencv_pil()
            print(islogo)
            if(islogo != None):
                movecur()
                stopChecking()
            isRunning.wait(.3)


def movecur():
    global curAgent
    time.sleep(.05)
    match curAgent:
        case "Jett":
            coords = pyautogui.locateCenterOnScreen('pics/jett.png',confidence=.7)
        case "Astra":
            coords = pyautogui.locateCenterOnScreen('pics/astra.png',confidence=.7)
        case "Breach":
            coords = pyautogui.locateCenterOnScreen('pics/breach.png',confidence=.7)
        case "Brimstone":
            coords = pyautogui.locateCenterOnScreen('pics/brimstone.png',confidence=.7)
        case "Chamber":
            coords = pyautogui.locateCenterOnScreen('pics/chamber.png',confidence=.7)
        case "Cypher":
            coords = pyautogui.locateCenterOnScreen('pics/cypher.png',confidence=.7)
        case "Fade":
            coords = pyautogui.locateCenterOnScreen('pics/fade.png',confidence=.7)
        case "Gekko":
            coords = pyautogui.locateCenterOnScreen('pics/gekko.png',confidence=.7)
        case "Harbour":
            coords = pyautogui.locateCenterOnScreen('pics/harbour.png',confidence=.7)
        case "KAY/O":
            coords = pyautogui.locateCenterOnScreen('pics/kayo.png',confidence=.7)
        case "Killjoy":
            coords = pyautogui.locateCenterOnScreen('pics/killjoy.png',confidence=.7)
        case "Neon":
            coords = pyautogui.locateCenterOnScreen('pics/neon.png',confidence=.7)
        case "Omen":
            coords = pyautogui.locateCenterOnScreen('pics/omen.png',confidence=.7)
        case "Phoenix":
            coords = pyautogui.locateCenterOnScreen('pics/phoenix.png',confidence=.7)
        case "Raze":
            coords = pyautogui.locateCenterOnScreen('pics/raze.png',confidence=.7)
        case "Reyna":
            coords = pyautogui.locateCenterOnScreen('pics/reyna.png',confidence=.7)
        case "Sage":
            coords = pyautogui.locateCenterOnScreen('pics/sage.png',confidence=.7)
        case "Skye":
            coords = pyautogui.locateCenterOnScreen('pics/skye.png',confidence=.7)
        case "Sova":
            coords = pyautogui.locateCenterOnScreen('pics/sova.png',confidence=.7)
        case "Viper":
            coords = pyautogui.locateCenterOnScreen('pics/viper.png',confidence=.7)
        case "Yoru":
            coords = pyautogui.locateCenterOnScreen('pics/yoru.png',confidence=.7)
            
    xcoord, ycoord = coords
    click_mouse(xcoord,ycoord)
    time.sleep(.05)
    pyautogui.moveTo(lxcoord,lycoord,duration=.001)
    click_mouse(lxcoord,lycoord)
    

currentAgent = tk.StringVar()

def on_selection_change(event):
    global curAgent 
    curAgent= currentAgent.get()
    print(curAgent)


agentlist = ["Jett","Astra","Breach","Brimstone","Chamber","Cypher","Fade","Gekko","Harbour","KAY/O","Killjoy","Neon","Omen","Phoenix","Raze","Reyna","Sage","Skye","Sova","Viper","Yoru"]
agentlistbox = ttk.OptionMenu(root,currentAgent,"Select an agent",*agentlist,command=on_selection_change)
agentlistbox.pack(pady=5)
agentlistbox.config(width=15)

start = ttk.Button(root,text="Start",command=startChecking)
start.pack(pady=1)
start.config(width=5)

stop = ttk.Button(root,text="Stop",command=stopChecking)
stop.pack(pady=1)
stop.config(width=5)


root.mainloop()