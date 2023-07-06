from tkinter import *
import random

def display_coordinates(event):
    label_1["text"] = f"x={event.x}, y={event.y}"

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

def drow_line_by_click (event):
    global click_number
    global x1, y1
    if click_number == 0:
        x1 = event.x
        y1 = event.y
        label_1["text"] = f"x1={event.x}, y1={event.y}"
        click_number = 1
    else:
        x2 = event.x
        y2 = event.y
        label_2["text"] = f"x2={event.x}, y2={event.y}"
        canvas.create_line(x1, y1, x2, y2, fill=f"#{random.randint(0, 0xffffff):06x}", width=random.randint(1, 10))
        click_number = 0 


root = Tk()
main_frame = Frame(root)
canvas = Canvas(main_frame, width=400, height=400, background="white")
label_1 = Label(main_frame, bd=4, relief= RAISED, font=("Franclin Gothic Heavy", 14, "normal"))
label_2 = Label(main_frame, bd=4, relief= RAISED, font=("Calibri", 14, "normal"), fg="brown")

canvas.bind("<Button-1>", drow_line_by_click)
canvas.bind("<Button-3>", display_coordinates)
canvas.bind("<Button-2>", delete_lines)
click_number = 0

main_frame.pack()
canvas.grid(row=0, columnspan=2)
label_1.grid(row=1, column=0)
label_2.grid(row=1, column=1)




root.mainloop()