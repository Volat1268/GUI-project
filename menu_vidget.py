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





def border_width_1():
    main_frame.config(bd=1)
def border_width_5():
    main_frame.config(bd=5)
def border_width_7():
    main_frame.config(bd=7)
def border_width_random():
    main_frame.config(bd=random.randint(10,20))

def green():
    main_frame.config(bg="green")
def blue():
    main_frame.config(bg="blue")
def red():
    main_frame.config(bg="red")
def yellow():
    main_frame.config(bg="yellow")
def grey():
    main_frame.config(bg="grey")


def solid():
    main_frame.config(relief="solid")
def raised():
    main_frame.config(relief="raised")
def sunken():
    main_frame.config(relief="sunken")
def groove():
    main_frame.config(relief="groove")

menu = tk.Menu(root)
root.config(menu=menu)
sub_menu_border = tk.Menu(menu, tearoff=0)
sub_menu_colour = tk.Menu(menu, tearoff=0)
sub_menu_relief = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="border", menu=sub_menu_border)
menu.add_cascade(label="colour", menu=sub_menu_colour)
menu.add_cascade(label="relief", menu=sub_menu_relief)

sub_menu_border.add_command(label="1", command=border_width_1)
sub_menu_border.add_command(label="5", command=border_width_5)
sub_menu_border.add_command(label="7", command=border_width_7)
sub_menu_border.add_command(label="10-20", command=border_width_random)

sub_menu_colour.add_command(label="green", command=green)
sub_menu_colour.add_command(label="yellow", command=yellow)
sub_menu_colour.add_command(label="blue", command=blue)
sub_menu_colour.add_command(label="red", command=red)
sub_menu_colour.add_command(label="grey", command=grey)

sub_menu_relief.add_command(label="raised", command=raised)
sub_menu_relief.add_command(label="groove", command=groove)
sub_menu_relief.add_command(label="sunken", command=sunken)
sub_menu_relief.add_command(label="solid", command=solid)

root.mainloop()