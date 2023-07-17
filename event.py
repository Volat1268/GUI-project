import tkinter as tk

def x_cor(event):
    cor_label.config(text=f"X = {event.x}")
def y_cor(event):
    cor_label.config(text=f"Y = {event.y}")

def exit_root(event):
    root.destroy()

root = tk.Tk()
root.title('Mouse event')
main_frame = tk.Frame(root)
main_frame.grid(row=0, column=0)

canvas = tk.Canvas(main_frame, width=500, height=300, bg='black')
canvas.grid(row=0, column=0)

label_frame = tk.Frame(main_frame)
label_frame.grid(row=0, column=1)

cor_label = tk.Label(label_frame, bg='yellow', fg='blue', font='Arial 20 italic', text='Click on the screen!', bd=5, relief='solid', padx=15)
cor_label.grid(row=0, column=0)

canvas.bind('<Button-1>', x_cor)
canvas.bind('<Button-3>', y_cor)
canvas.bind('<Button-2>', exit_root)




root.mainloop()