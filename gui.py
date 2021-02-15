try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

def mainScreen(master):
    master.geometry("320x240")
    #master.minsize(120, 1)
    #master.maxsize(3844, 1061)
    master.title("Todo List")
    master.config(background="#d9d9d9", cursor='none')
    master.resizable(0, 0)
    # top.attributes("-fullscreen", True)
    # create a frame
    frame1 = tk.Frame(master)
    frame1.place(relx=0.0, rely=0.0,height=20, width=320)
    frame1.configure(background="#d9d9d9")

    # label 1 == Title
    appTitle = tk.Label(frame1)
    appTitle.place(relx=0.0, rely=0.0, height=20, width=320)
    appTitle.configure(text='Current to do list: ')
    appTitle.configure(bg='grey')
    appTitle.configure(fg='white')

def changingScreen(master, text, pageNr):

    # second frame
    frame2 = tk.Frame(master)
    frame2.place(relx=0.0, rely=0.1, relheight=0.95, relwidth=1.00,)
    frame2.configure(background="white")

    # text
    text1 = tk.Message(frame2)
    text1.place(relx=0.0, rely=0.0)
    text1.configure(background="white")
    text1.configure(text= text)
    text1.pack()

    # label2
    label2 = tk.Label(frame2)
    label2.place(relx=0, rely=0.8, height=20, width=320)
    label2.configure(font="Helvetica 9 italic")
    label2.configure(text='Page: x' + ' of Page: '+ str(pageNr))

