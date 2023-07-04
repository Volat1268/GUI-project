from tkinter import *
import random as rd

root = Tk()
root.title("canvas Tk")

class MyCanvas(Canvas):
    def __init__(self, master):
        super().__init__()
        self["width"] = 500
        self["height"] = 500
        self["bd"] = 5
        self["relief"] = RAISED

for_color = ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
def random_color_maker():
    random_color = "#"
    for i in range(6):
        random_color += rd.choice(for_color)
    return random_color


my_canvas = MyCanvas(root)
my_canvas.grid(row=0, column=0)

for i in range(200):
    my_canvas.create_line(rd.randint(0, 500), rd.randint(0, 500), rd.randint(0, 500), rd.randint(0, 500), fill=random_color_maker(), width=rd.randint(1, 10))
    
    my_canvas.update()




root.mainloop()
