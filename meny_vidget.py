import tkinter as tk
import random

def quit_app():
    root.destroy()
    
def change_colour():
    main_frame.config(bg=f"#{random.randint(0, 0xffffff):06x}")

def change_border():
    main_frame.config(bd=random.randint(3, 12))  

def change_relief():
    reliefs = ["raised", "sunken", "solid", "flat", "ridge", "groove"]
    main_frame.config(relief=random.choice(reliefs))

def r_solid():
    main_frame.config(relief="solid") 
def r_raised():
    main_frame.config(relief="raised") 
def r_sunken():
    main_frame.config(relief="sunken") 
def r_groove():
    main_frame.config(relief="groove") 
def r_flat():
    main_frame.config(relief="flat") 

root = tk.Tk()
root.title('Menu vidget')
main_frame = tk.Frame(root, width=400, height=400, bg="red")
main_frame.grid(row=0, column=0)


my_menu = tk.Menu(root)
relief_menu = tk.Menu(my_menu)
my_menu.add_command(label="Quit", command=quit_app)
my_menu.add_command(label="Colour", command=change_colour)
my_menu.add_cascade(label="Relief", menu=relief_menu)
my_menu.add_command(label="Edge", command=change_border)

relief_menu.add_command(label="solid", command=r_solid)
relief_menu.add_command(label="raised", command=r_raised)
relief_menu.add_command(label="sunken", command=r_sunken)
relief_menu.add_command(label="groove", command=r_groove)
relief_menu.add_command(label="flat", command=r_flat)

root.config(menu=my_menu)






root.mainloop()