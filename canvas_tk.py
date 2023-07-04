from tkinter import *
import random 

root = Tk()
root.title("canvas Tk")

class MyCanvas(Canvas):
    def __init__(self, master):
        super().__init__()
        self["width"] = 500
        self["height"] = 500
        self["bd"] = 5
        self["bg"] = "white"
        self["relief"] = RAISED

def random_color_cod():
    return f'#{random.randint(0, 0xffffff):06x}'


my_canvas = MyCanvas(root)
my_canvas.grid(row=0, column=0)
my_canvas.create_line(100,100,300,100,200,300,100,100, fill="blue", width=5)

# for i in range(200):
#     my_canvas.create_line(random.randint(0, 500), random.randint(0, 500), random.randint(0, 500), random.randint(0, 500), fill=random_color_cod(), width=random.randint(1, 10))
    
#     my_canvas.update()



root.mainloop()
