from tkinter import *
from tkinter import ttk

root = Tk()
root.title("My GUI project")
root.iconbitmap("./python_icon.ico")

root_width = 800
root_hight = 600
screen_with = root.winfo_screenwidth()
screen_hight = root.winfo_screenheight()
root_xcor = screen_with / 2 - root_width / 2
root_ycor = screen_hight / 2 - root_hight / 2
# root.configure(width=root_width, height=root_hight)
# root.geometry("600x400+200+150")
root.geometry("%dx%d+%d+%d" % (root_width, root_hight, root_xcor, root_ycor))




root.mainloop()

