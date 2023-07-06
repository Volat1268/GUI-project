from tkinter import *
import random

root = Tk()
root.title("Draw and clear lines")
root.iconbitmap("./assets/brush.ico")



def random_color_cod():
		return f'#{random.randint(0, 0xffffff):06x}'

def make_line():
	xcor_start = random.randint(0, 600)
	ycor_start = random.randint(0, 600)
	xcor_finish = random.randint(0, 600)
	ycor_finish = random.randint(0, 600)
	canvas.create_line(xcor_start, ycor_start, xcor_finish, ycor_finish, fill=random_color_cod(), width=5)

def clear_lines():
	canvas.delete("all")

display_frame = Frame(root, bd=3, relief=RAISED)
controle_frame = Frame(root)
canvas = Canvas(display_frame,  width=600, height=600)
# canvas.create_line(xcor_start, ycor_start, xcor_finish, ycor_finish, fill=random_color_cod(), width=5)


draw_button = Button(controle_frame, text="Click for a random coloured line", command=make_line)
clear_button = Button(controle_frame, text="Click to clear coloured lines", command=clear_lines)



display_frame.grid(row=0, column=0)
controle_frame.grid(row=1, column=0)
draw_button.grid(row=0, column=0)
clear_button.grid(row=1, column=0)
canvas.grid(row=0, column=0)




root.mainloop()

