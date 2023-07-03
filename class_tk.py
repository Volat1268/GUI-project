from tkinter import *


root = Tk()

class RedFrame(Frame):
    def __init__(self, master):
        super().__init__()
        self["height"] = 150
        self["width"] = 150
        self["bd"] = 8
        self["relief"] = RAISED
        self["bg"] = "red"


class HelloFrame(Frame):
    def __init__(self, master):
        super().__init__()
        self.user_name = StringVar()
        self.greeting_text = StringVar()
        
        self.name_label = Label(self, text="Enter your Name: ")
        self.name_entry = Entry(self, textvariable=self.user_name)
        self.name_entry.focus()
        self.button = Button(self, text="Click Me", command=self.greeting_make)
        self.greeting_label = Label(self, textvariable=self.greeting_text, relief=SOLID)
        
        self.name_label.grid(row=0, column=0)
        self.name_entry.grid(row=0, column=1)
        self.button.grid(row=1, column=0)
        self.greeting_label.grid(row=1, column=1)
        
    def greeting_make(self):
        self.greeting_text.set(f"Hello {self.user_name.get()}")

my_frame = HelloFrame(root)
my_frame.grid(row=0, column=0)


# frame_a = RedFrame(root)
# frame_b = RedFrame(root)
# frame_c = RedFrame(root)
# frame_c["background"] = "blue"
# frame_a.grid(row=0, column=0)
# frame_b.grid(row=1, column=1)
# frame_c.grid(row=3, column=0)



root.mainloop()
                