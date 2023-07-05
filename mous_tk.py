from tkinter import *
import random

def display_coordinates(event):
    label["text"] = f"x={event.x}, y={event.y}"

def draw_line(event):
    x1 = random.randint(0, 400)
    y1 = random.randint(0, 400)
    x2 = random.randint(0, 400)
    y2 = random.randint(0, 400)
    line_width = random.randint(1, 10)
    line_fill = f"#{random.randint(0, 0xffffff):06x}"
    canvas.create_line(x1, y1, x2, y2, width=line_width, fill=line_fill)
    
def delete_lines(event):
    canvas.delete("all")

root = Tk()
main_frame = Frame(root)
canvas = Canvas(main_frame, width=400, height=400, background="white")
label = Label(main_frame, bd=4, relief=SOLID, font=("Arial", 22, "normal"))
canvas.bind("<Button-1>", display_coordinates)
canvas.bind("<Button-3>", draw_line)
canvas.bind("<Button-2>", delete_lines)

main_frame.pack()
canvas.grid(row=0, column=0)
label.grid(row=1, column=0)




root.mainloop()