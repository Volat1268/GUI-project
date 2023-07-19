import tkinter as tk
import time as tm

root = tk.Tk()
root.title('digital clock class')

class DigitalClock:
    def __init__(self, master):
        self.master = master
        self.display_clock()
        self.display_time()
        self.display_menu()
        

    def display_clock(self):
        self.main_frame = tk.Frame(self.master)
        self.main_frame.grid(row=0, column=0)
        self.clock_label = tk.Label(self.main_frame, bg='blue', fg='yellow', font='Arial 60 italic bold', padx=15, pady=5)
        self.clock_label.grid(row=0, column=0)

    def display_time(self):
        self.current_time = tm.strftime('%H:%M:%S')
        self.clock_label.config(text=self.current_time)
        self.main_frame.after(1000, self.display_time)

    def small_font(self):
        self.clock_label.config(font='Arial 20 normal', fg='blue', bg='yellow')

    def big_font(self):
        self.clock_label.config(font='Arial 150 italic bold', fg='red', bg='white')
    
    def display_menu(self):
        self.menu = tk.Menu(self.master)
        self.sub_menu = tk.Menu(self.menu, tearoff=0)
        self.sub_menu.add_command(label='small', command=self.small_font)
        self.sub_menu.add_command(label='big', command=self.big_font)
        self.menu.add_cascade(label='clock size', menu=self.sub_menu)
        self.master.config(menu=self.menu)





my_clock = DigitalClock(root)






















# root = tk.Tk()
# root.title('digital clock class')
# main_frame = tk.Frame(root)
# main_frame.grid(row=0, column=0)

# class DigitalClock():
#     def __init__(self, master):
#         self.master = master
#         self.display_clock()
#         self.add_menu()
#         self.display_time()

#     def display_clock(self):
#         self.clock_Label = tk.Label(self.master, bg='black', fg='red', font='Arial 80 italic', padx=20, pady=10)
#         self.clock_Label.grid(row=0, column=0)

#     def small_font(self):
#         self.clock_Label.config(font='Arial 20 normal')
#     def large_font(self):
#         self.clock_Label.config(font='Arial 120 bold')

#     def add_menu(self):
#         self.menu = tk.Menu(self.master)
#         self.sub_menu = tk.Menu(self.menu, tearoff=0)
#         self.sub_menu.add_command(label='Small Font Size', command=self.small_font)
#         self.sub_menu.add_command(label='Large Font Size', command=self.large_font)
#         self.menu.add_cascade(label='settings', menu=self.sub_menu)
#         self.master.config(menu=self.menu)


#     def display_time(self):
#         self.current_time = tm.strftime('%H:%M:%S')
#         self.clock_Label.config(text=self.current_time)
#         self.master.after(1000, self.display_time)

# my_clock = DigitalClock(root)



root.mainloop()