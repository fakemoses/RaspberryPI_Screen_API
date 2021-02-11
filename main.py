try:
    from Tkinter import *
except ImportError:
    from tkinter import *
import sys
import os
from getFromServer import getRequests

if os.environ.get('DISPLAY','') == '':
    print('no display found. Using :0.0')
    os.environ.__setitem__('DISPLAY', ':0.0')


#create main window
master = Tk()
master.title("Todo List")
master.geometry("240x320")
#master.attributes("-fullscreen", True)
master.config(cursor='none')
#master.lift


#make a label for the window
label1 = Label(master, text='Current to do list: ')
# Lay out label
label1.pack()

t = Text(master)

#Process data
res = getRequests()['data'][0]
for item in res:
    t.insert(END, '# ' + item['task'] + '\n')

t.pack()
# Run forever!
master.mainloop()
