from tkinter import *

root = Tk()
root.title("fahrenheit to celsius")

fahrenheit_var = StringVar()
celsius_var = StringVar()

fahrenheit_label = Label(root,
                        text="Enter Fahrenheit:" )
fahrenheit_enter = Entry(root,
                         borderwidth=1,
                         relief="solid",
                         width=20,                         
                         textvariable=fahrenheit_var,
                         )
tocelcius_button = Button(root,
                          text="Convert")
celsius_label = Label(root,
                      text="Celsius temperatur")
result_label = Label()

fahrenheit_label.grid(row=0, column=0)
fahrenheit_enter.grid(row=0, column=1)
celsius_label.grid(row=1, column=0)
result_label.grid(row=1, column=1)
tocelcius_button.grid(row=2, column=0)



root.mainloop()




