import tkinter as tk
import time as tm

root = tk.Tk()
root.title('Digital clock')
root.iconbitmap('./assets/digital_clock .ico')
main_frame = tk.Frame(root)
main_frame.grid(row=0, column=0)


def display_clock():
    current_time = tm.strftime('%H:%M:%S')
    clock_label.config(text=current_time)
    root.after(1000, display_clock)

def clock_exit():
    root.destroy()
    
def bg_blue():
    clock_label.config(bg='blue')
def bg_green():
    clock_label.config(bg='green')
def bg_gray():
    clock_label.config(bg='gray')
def bg_white():
    clock_label.config(bg='white')

def fg_blue():
    clock_label.config(fg='blue')
def fg_green():
    clock_label.config(fg='green')
def fg_gray():
    clock_label.config(fg='gray')
def fg_white():
    clock_label.config(fg='white')
    
def fs_20():
    clock_label.config(font='Arial 20 italic')
def fs_40():
    clock_label.config(font='Arial 40 italic')
def fs_80():
    clock_label.config(font='Arial 80 italic')
def fs_100():
    clock_label.config(font='Arial 100 italic')

clock_label = tk.Label(main_frame, bg='black', fg='red', font=f'Arial 60 italic', padx=15, pady=10)
clock_label.grid(row=0, column=0)

menu = tk.Menu(root)
menu.add_command(label='exit', command=clock_exit)
sub_menu_background = tk.Menu(menu, tearoff=0)
sub_menu_foreground = tk.Menu(menu, tearoff=0)
sub_menu_fontsize = tk.Menu(menu, tearoff=0)

menu.add_cascade(label='background', menu=sub_menu_background)
menu.add_cascade(label='foreground', menu=sub_menu_foreground)
menu.add_cascade(label='fontsize', menu=sub_menu_fontsize)

sub_menu_background.add_command(label='blue', command=bg_blue)
sub_menu_background.add_command(label='green', command=bg_green)
sub_menu_background.add_command(label='gray', command=bg_gray)
sub_menu_background.add_command(label='white', command=bg_white)

sub_menu_foreground.add_command(label='blue', command=fg_blue)
sub_menu_foreground.add_command(label='green', command=fg_green)
sub_menu_foreground.add_command(label='gray', command=fg_gray)
sub_menu_foreground.add_command(label='white', command=fg_white)

sub_menu_fontsize.add_command(label='20', command=fs_20)
sub_menu_fontsize.add_command(label='40', command=fs_40)
sub_menu_fontsize.add_command(label='80', command=fs_80)
sub_menu_fontsize.add_command(label='100', command=fs_100)

root.config(menu=menu)


display_clock()





root.mainloop()