from tkinter import *
from tkinter import ttk

root = Tk()
root.title("My GUI project")
root.iconbitmap("./python_icon.ico")
root.geometry("600x400+200+150")

def print_text():
    print("Hello, you ckicked the button 'Enter'")
enter_button = Button(
    root,
    text="Enter",
    bg="#FFFAD7",
    font=("Lucida Console", 16, "normal"),
    fg="green",
    relief="raised",
    activebackground="yellow",
    activeforeground="red",
    command=print_text
)
enter_button.pack()

label = Label(root, text=enter_button.winfo_rootx())
label.pack()



root.mainloop()

