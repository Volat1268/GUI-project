from tkinter import *
from tkinter import ttk


root = Tk()
root.title("My GUI project")
root.geometry("600x400+1200+100")
root.resizable(width=False, height=False)
root.iconbitmap("./python_icon.ico")
root_icon = PhotoImage(file="./python.png")
# root.iconphoto(False, root_icon)



root.mainloop()

