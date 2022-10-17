import pyautogui
from tkinter import *


def accept():
    accept_img = pyautogui.locateCenterOnScreen('accept.png', confidence=0.70)
    if accept_img is not None:
        updated_label = Label(text="Game found!", font=("Times New Roman", 20))
        updated_label.pack()
        pyautogui.moveTo(accept_img, duration=0.1)
        pyautogui.click()
    window.after(5000, accept)


window = Tk()
window.minsize(width=400, height=100)
window.title("Lol Accept")
label_status = Label(text="Searching for a game ...", font=("Times New Roman", 20))
label_status.pack()

window.after(5000, accept)
window.mainloop()
