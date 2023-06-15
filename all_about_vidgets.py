import random
import tkinter as tk

# ----------------window---------------
window = tk.Tk()
width_screen = 800
heigth_screen = 600
horiz_shift = 200
vert_shift = 100
my_icon = tk.PhotoImage(file="./python.png")
window.iconphoto(False, my_icon)
window.title("My first GUI project")
window.geometry(f"{width_screen}x{heigth_screen}+{horiz_shift}+{vert_shift}")
window.resizable(True, True)
window.minsize(300, 200)
window.config(background="#FFFBF5")


# -----------------label-----------------
# название виджета:
label_label = tk.Label(window, text="LABEL:", bg="#FFFBF5", font=("Arial", 18, "bold"), fg="#884A39", pady=3).grid(row=0, column=1)

# сам виджет:
label = tk.Label(window, text='''Hello!
I'm a vidget Label!''',  # window - это где размащается виджет
                 bg="#FFF8D6",  # цвет фона виджета
                 fg="#D25380",  # цвет шрифта
                 font=("Arial", 18, "bold"),
                 padx=10,  # отступ от краев по гориз
                 pady=5,  # отступ от краев по вертик
                 width=15,
                 height=3,
                 anchor="center",  # размещение надписи на виджет
                 #  # отрисовка границы (разные виды 3д границ)
                 #  relief="raised",
                 #  bd=5,  # ширина 3D границы
                 justify="center"  # выравнивание текста, который имеет несколько строк
                 )
label.grid(row=1, column=1)



# название виджета:
buttons_label = tk.Label(window, text="BUTTONS:", bg="#FFFBF5", font=("Arial", 18, "bold"), fg="#884A39", pady=3).grid(row=2, column=1)

# -----------------Button 1 при нажатии на кнопку (изменяет label)-----------------

def change_label():  # функция при нажатии на кнопку (изменяет label)
    label.config(text='''Click on button 
change 
the text''', fg="blue", font=("Courier New", 16, "normal"), justify="left")


button = tk.Button(
    							 window, text="Klick me!",
                   relief="groove", bd=10,
                   command=change_label
                   )
button.grid(row=3, column=0)

# -----------------Button 2 button - counter -----------------
count = 0  # для command btn_counter


def btn_counter():
    global count
    count += 1
    button_counter.config(text=f"Счетчик {count}")


button_counter = tk.Button(window, text=f"Счетчик {count}", bg="#6096B4",
                           relief="sunken", bd=10,
                           fg="white", activebackground="red",
                           command=btn_counter)
button_counter.grid(row=3, column=1)

# ------------------ Button 3: random change background color of window:

bg_colors = ["#F5F0BB", "#DBDFAA", "#B3C890", "#73A9AD",
             "#FFF2CC", "#FFD966", "#F4B183", "#DFA67B"]


def change_bg_color():
    new_bg_color = random.choice(bg_colors)
    window.config(background=new_bg_color)


button_change_color = tk.Button(window, text="Change the color of window!",
                                bg="#1B9C85", activebackground="#E8F6EF", relief="raised", bd=10, fg="white", padx=5, pady=5, command=change_bg_color
                                )
button_change_color.grid(row=3, column=2)


# ----------------ENTRY-----------------------
# название виджета:
entry_label = tk.Label(window, text="ENTRY:", bg="#FFFBF5", font=("Arial", 18, "bold"), fg="#884A39", pady=3).grid(row=4, column=1)

#  entry1 - enter name:
def get_entry():
    name_value = name_entry.get()
    password_value = password_entry.get()
    if name_value and password_value:
        print(f"name: {name_value}")
        print(f"password: {password_value}")
    else:
        print("Empty Values")
        
def reset_entry(): # функция удаления внесенной в форму записи (с 0 позиции до конца)
    name_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)
    
name_label = tk.Label(window, text="Name").grid(row=5, column=0, sticky="we")
name_entry = tk.Entry(window) 
name_entry.grid(row=5, column=1)
name_button = tk.Button(window, text="Enter", command=get_entry).grid(row=5, column=2, rowspan=2, sticky="w")

#  entry2 - enter password:
password_label = tk.Label(window, text="Password").grid(row=6, column=0, sticky="we")
password_entry = tk.Entry(window, show="*")
password_entry.grid(row=6, column=1)

# button to reset entered value
reset_button = tk.Button(window, text="Reset", width=10, command=reset_entry).grid(row=5, column=3)

# button to insert ("hello!") in to entry "name"
def insert_entry():
    name_entry.delete(0, tk.END)
    name_entry.insert(0, "hello!")
insert_button = tk.Button(window, text="Insert", width=10, command=insert_entry).grid(row=6, column=3)



window.mainloop()
