import tkinter as tk
from PIL import ImageTk, Image

root = tk.Tk()
root.title('rounded button')
root.iconbitmap('./assets/python_icon.ico')
root.geometry('400x400')

my_img = Image.open('./assets/tomato.png')
tomato_img = ImageTk.PhotoImage(my_img)
my_label = tk.Label(root, image=tomato_img)
my_label.pack(pady=20)


root.mainloop()