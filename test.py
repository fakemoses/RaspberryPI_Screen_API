import tkinter as tk
root = tk.Tk()

money = 100
label = tk.Label(root, text = str(money)+"$")
label.grid()

def countup(money):
    money += 1
    label['text'] = str(money)+"$"
    if money < 300:
        root.after(100, countup, money)

root.after(100, countup, money)
root.mainloop()