from tkinter import *

root = Tk()
root.title("canvas Tk")

class MyCanvas(Canvas):
    def __init__(self, master):
        super().__init__()
        self["width"] = 200
        self["height"] = 200
        # self["bg"] = "gray"
        self["bd"] = 5
        self["relief"] = RAISED

my_canvas_1 = MyCanvas(root)
my_canvas_2 = MyCanvas(root)
my_canvas_2.configure(bg='red', relief=SUNKEN)

my_canvas_1.create_line(0, 0, 250, 250, fill="blue", width=5)
my_canvas_2.create_line(210, 0, 0, 210, fill="yellow", width=5)

my_canvas_1.grid(row=0, column=0)
my_canvas_2.grid(row=1, column=1)

root.mainloop()
