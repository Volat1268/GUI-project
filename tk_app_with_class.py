from tkinter import *
import random

root = Tk()
root.title('my first Tk app')
main_frame = Frame(root).grid(row=0, column=0)

class DrawLineApp(Canvas):
    def __init__(self, master):
        super().__init__()
        self.bind("<Button-1>", self.draw_line)
        self.bind("<Button-3>", self.clear_all)
        self.click_number = 0
        self.x1 = 0
        self.y1 = 0
        self.x2 = 0
        self.y2 = 0
    def draw_line(self, event):
        if self.click_number == 0:
            self.x1 = event.x 
            self.y1 = event.y 
            self.click_number = 1
        else:
            self.x2 = event.x 
            self.y2 = event.y
            self.canva 
        





root.mainloop()