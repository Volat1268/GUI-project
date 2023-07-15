import tkinter as tk
import time as tm

root = tk.Tk()
root.title('digital clock class')
main_frame = tk.Frame(root)
main_frame.grid(row=0, column=0)

class DigitalClock():
    def __init__(self, master, clock_backround, clock_foreground, clock_row, clock_column):
        self.master = master
        self.clock_Label = tk.Label(self.master, bg=clock_backround, fg=clock_foreground, font='Arial 80 italic', padx=20, pady=10)
        self.clock_Label.grid(row=clock_row, column=clock_column)
        self.display_time()
        
    def display_time(self):
        self.current_time = tm.strftime('%H:%M:%S')
        self.clock_Label.config(text=self.current_time)
        self.master.after(2000, self.display_time)

my_clock_one = DigitalClock(main_frame, clock_backround='black', clock_foreground='red', clock_row=0, clock_column=0)
my_clock_two = DigitalClock(main_frame, clock_backround='red', clock_foreground='black', clock_row=0, clock_column=1)
my_clock_three = DigitalClock(main_frame, clock_backround='blue', clock_foreground='yellow', clock_row=1, clock_column=0)
my_clock_four = DigitalClock(main_frame, clock_backround='yellow', clock_foreground='blue', clock_row=1, clock_column=1)


root.mainloop()