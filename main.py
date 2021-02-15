try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk
from gui import (mainScreen, changingScreen)
import os
from getFromServer import getRequests
import time

if os.environ.get('DISPLAY', '') == '':
    print('no display found. Using :0.0')
    os.environ.__setitem__('DISPLAY', ':0.0')


def split(arr, size):
    arrs = []
    while len(arr) > size:
        pice = arr[:size]
        arrs.append(pice)
        arr = arr[size:]
    arrs.append(arr)
    return arrs


def getData():
    onlyOnePage = False
    # first time show
    responses = getRequests()

    if len(responses) > 4:
        onlyOnePage = True
        resText = split(responses, 4)
        page = len(resText)

        return resText, onlyOnePage
    else:
        text = ""
        page = 1
        for item in responses:
            text += '# ' + item['task'] + '\n'
            # text += '\n'
        return text, onlyOnePage


def updateTheScreen():
    # Process data
    text = ""
    print('Refreshing screen')
    textRes, boolPages = getData()
    if not boolPages:
        changingScreen(master, textRes, len(textRes))
        master.after(1000, updateTheScreen)

    else:
        # here is to be updated -> more than one pages
        for i in range(len(textRes)):
            #append all text into one string
            text = ""
            for j in range(len(textRes[i])):
                text += "->" + textRes[i][j]['task'] + '\n \n'

            changingScreen(master, 'Loading..\n', 0)
            time.sleep(15)
            master.after(10000, changingScreen, master, text, i+1)
        #changingScreen(master, 'Loading..\n', 0)
        master.after(50000, updateTheScreen)

#   create main window
master = tk.Tk()

#   show the static main screen + frames
mainScreen(master)
updateTheScreen()
# master.after(3000, updateTheScreen, money)
# Run forever!
master.mainloop()
