from tkinter import *

root = Tk()
root.title("fahrenheit to celsius")
root.configure(padx=10, pady=5)

celsius = StringVar()
fahrenheit = StringVar()

def convert():
    fahren_temp = float(fahrenheit.get())
    cels_temp = round((fahren_temp - 32) * 5 / 9, 2)
    celsius.set(str(cels_temp))

fahrenheit_label = Label(root,
                        text="Enter Fahrenheit:",
                        )

fahrenheit_entry = Entry(root,
                         borderwidth=1,
                         relief="solid",
                         width=20,
                         textvariable=fahrenheit,               
                         )
fahrenheit_entry.focus()

tocelcius_button = Button(root,
                          width=10,
                          text="Convert",
                          command=convert,
                          )
                        
celsius_label = Label(root,
                      text="Celsius temperatur:"
                      )
result_label = Label(root,
                     textvariable=celsius
                     )

fahrenheit_label.grid(row=0, column=0)
fahrenheit_entry.grid(row=0, column=1)
celsius_label.grid(row=1, column=0)
result_label.grid(row=1, column=1)
tocelcius_button.grid(row=2, column=0)



root.mainloop()




