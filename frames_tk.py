from tkinter import *

root = Tk()
name_frame = Frame(root)
address_frame = Frame(root)

name_label = Label(name_frame, text="First Name: ")
middle_label = Label(name_frame, text="Middle Name: ")
surname_label = Label(name_frame, text="Surname: ")

name_entry = Entry(name_frame)
middle_entry = Entry(name_frame)
surname_entry = Entry(name_frame)

name_button = Button(name_frame, text="   Submit   ")

street_label = Label(address_frame, text="Street: ")
town_label = Label(address_frame, text="Town: ")
country_label = Label(address_frame, text="Country: ")

street_entry = Entry(address_frame)
town_entry = Entry(address_frame)
country_entry = Entry(address_frame)

address_button = Button(address_frame, text="   Submit   ")


name_frame.grid(row=0, column=0)
address_frame.grid(row=0, column=1)

name_label.grid(row=0, column=0)
middle_label.grid(row=1, column=0)
surname_label.grid(row=2, column=0)

name_entry.grid(row=0, column=1)
middle_entry.grid(row=1, column=1)
surname_entry.grid(row=2, column=1)

name_button.grid(row=3, columnspan=2)

street_label.grid(row=0, column=0)
town_label.grid(row=1, column=0)
country_label.grid(row=2, column=0)

street_entry.grid(row=0, column=1)
town_entry.grid(row=1, column=1)
country_entry.grid(row=2, column=1)

address_button.grid(row=3, columnspan=2)








root.mainloop()