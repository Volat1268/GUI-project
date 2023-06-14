from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Arial"
FONT_WATCH = ("Arial", 34, "bold")
FONT_LABEL = ("Times New Roman", 30, "bold")
COLOR_WATCH = "white"
CHECKMARK = "✓"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_breack_sec = LONG_BREAK_MIN * 60
    if reps == 8:
        count_down(long_breack_sec)
    elif reps % 2 == 0:
        count_down(short_break_sec)
    else:
        count_down(work_sec) 
        

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    time_min = math.floor(count / 60)
    time_sec = count % 60
    if time_sec < 10:
        time_sec = f"0{time_sec}"
    canvas.itemconfig(timer_count, text=f"{time_min}:{time_sec}")
    if count > 0:
    	window.after(1000, count_down, count - 1)
    else:
        start_timer()
# ---------------------------- UI SETUP ------------------------------- #

# --------window-----------
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)
icon = PhotoImage(file="./tomato_icon.png")
window.iconphoto(False, icon)


canvas = Canvas(width=200, height=223, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="./tomato.png")
canvas.create_image(100, 110, image=tomato_img)
timer_count = canvas.create_text(100, 130, text="00:00", fill=COLOR_WATCH, font=FONT_WATCH)
canvas.grid(row=1, column=1)

# -------------TIMER label--------------
timer_label = Label(window, text="Timer", bg=YELLOW, font=FONT_LABEL, fg=GREEN)
timer_label.grid(row=0, column=1)

# -----------START button -------------
start_button = Button(window, command=start_timer, text="Start", bg="white",activebackground=YELLOW, highlightthickness=0)
start_button.grid(row=2, column=0)

# -----------RESET button -------------
reset_button = Button(window, text="Reset", bg="white",activebackground=YELLOW, highlightthickness=0)
reset_button.grid(row=2, column=2)

# -----------CHECKMARK button -------------
check_label = Label(window, text=CHECKMARK, bg=YELLOW, foreground=GREEN)
check_label.grid(row=3, column=1)









window.mainloop()