import tkinter as tk
import pyautogui, time, keyboard

pyautogui.PAUSE = 0.01
HEIGHT = 500
WIDTH = 600
hotkey = 'q'
speed = 0.01
on = 0
click = 'left'

def setHotkey(newHotkey):
    global hotkey
    if(newHotkey == 'reset'):
        hotkey = 'f6'
    hotkey = newHotkey
    hotkeyLab['text'] = 'Current Hotkey: ' + hotkey
    hotkeyEntry.delete(0, 'end')

def setSpeed(newSpeed):
    global speed
    if(newSpeed == 'reset'):
        speed = 0.01
    speed = newSpeed
    speedLab['text'] = 'Current Speed: ' + str(speed) + ' seconds'
    speedEntry.delete(0, 'end')

def leftClick():
    global click
    rightButton.deselect()
    click = 'left'

def rightClick():
    global click
    leftButton.deselect()
    click = 'right'

def loop():
    global speed
    global on
    speedt = int(float(speed) * 100)
    if on == 0:
        if keyboard.is_pressed(hotkey):
            time.sleep(0.1)
            on = 1
        root.after(speedt, loop)
    else:
        if keyboard.is_pressed(hotkey):
            time.sleep(0.1)
            on = 0
        if click == 'right':
            pyautogui.rightClick()
        else:
            pyautogui.leftClick()
        root.after(speedt, loop)
root = tk.Tk()
root.title('AutoClicker')
root.resizable(False, False)
#root.iconbitmap('C:/Users/Faisal/Desktop/Thing/Papirus-Team-Papirus-Devices-Input-mouse.ico')

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

#TO SET HOTKEY

hotkeyFrame = tk.Frame(root, bg='#80c1ff', bd=5)
hotkeyFrame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

hotkeyButton = tk.Button(hotkeyFrame,  text='Set Hotkey', font=40, command=lambda: setHotkey(hotkeyEntry.get()))
hotkeyButton.place(relx=0.7, relheight=1, relwidth=0.3)

hotkeyEntry = tk.Entry(hotkeyFrame, font=40)
hotkeyEntry.place(relwidth=0.65, relheight=1)

hotkeyLab = tk.Label(root, text='Current Hotkey: ' + hotkey, anchor='n')
hotkeyLab.place(relx=0.42, rely=0.03)

#TO SET SPEED

speedFrame = tk.Frame(root, bg='#80c1ff', bd=5)
speedFrame.place(relx=0.5, rely=0.3, relwidth=0.75, relheight=0.1, anchor='n')

speedButton = tk.Button(speedFrame,  text='Set Speed', font=40, command=lambda: setSpeed(speedEntry.get()))
speedButton.place(relx=0.7, relheight=1, relwidth=0.3)

speedEntry = tk.Entry(speedFrame, font=40)
speedEntry.place(relwidth=0.65, relheight=1)

speedLab = tk.Label(root, text='Current Speed: ' + str(speed) + ' seconds', anchor='n')
speedLab.place(relx=0.35, rely=0.23)

#TO SET CLICK

clickFrame = tk.Frame(root, bg='#80c1ff', bd=5)
clickFrame.place(relx=0.5, rely=0.5, relwidth=0.75, relheight=0.1, anchor='n')

leftButton = tk.Checkbutton(clickFrame, text='Left Click', command=lambda: leftClick())
leftButton.place(relx=0.15, relheight=1, relwidth=0.3)

rightButton = tk.Checkbutton(clickFrame, text='Right Click', command=lambda: rightClick())
rightButton.place(relx=0.55, relheight=1, relwidth=0.3)

leftButton.select()

root.after(1, loop)

root.mainloop()
