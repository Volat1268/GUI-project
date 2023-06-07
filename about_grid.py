import tkinter as tk

window = tk.Tk()
window.title("About method grid in Tkinter")
window.geometry(f"800x400+200+100")
window.config(padx=30, pady=30)



################# размещение кнопок в желаемом порядке, растягивание кнопки на неск.рядов или неск строк:#######
# btn1 = tk.Button(window, text="Button1")
# btn2 = tk.Button(window, text="Button2")
# btn3 = tk.Button(window, text="Button3")
# btn4 = tk.Button(window, text="Button4 Button4") # увеличинная кнопка, чтобы показать как можно подвинуть кн.2 влево и кн6 вправо(см.ниже)
# btn5 = tk.Button(window, text="Button5")
# btn6 = tk.Button(window, text="Button6")
# btn7 = tk.Button(window, text="Button7")
# btn8 = tk.Button(window, text="Button8")

# btn1.grid(row=0, column=0)
# btn2.grid(row=0, column=1, sticky="w") #подвинул кнопку 2 влево
# btn3.grid(row=1, column=0)
# btn4.grid(row=1, column=1)
# btn5.grid(row=2, column=0)
# btn6.grid(row=2, column=1, sticky="e") #подвинул кнопку 6 вправо
# btn7.grid(row=3, column=0, columnspan=2, sticky="we") #растянул кнопку на 2 столбца
# btn8.grid(row=0, column=3, rowspan=4, sticky="ns") #раснянул кнопку на 4 ряда



############ установка ширины колонок ################
window.grid_columnconfigure(0,minsize=200)
window.grid_columnconfigure(1, minsize=100)
window.grid_columnconfigure(2, minsize=50)



# btn1 = tk.Button(window, text="Button1")
# btn2 = tk.Button(window, text="Button2")
# btn3 = tk.Button(window, text="Button3")
# btn4 = tk.Button(window, text="Button4 Button4") # увеличинная кнопка, чтобы показать как можно подвинуть кн.2 влево и кн6 вправо(см.ниже)
# btn5 = tk.Button(window, text="Button5")
# btn6 = tk.Button(window, text="Button6")
# btn7 = tk.Button(window, text="Button7")
# btn8 = tk.Button(window, text="Button8")

# btn1.grid(row=0, column=0)
# btn2.grid(row=0, column=1, sticky="w") #подвинул кнопку 2 влево
# btn3.grid(row=1, column=0, sticky="we") #растянул кнопку на всю ширину колонки, установл. в window.grid_columnconfigure
# btn4.grid(row=1, column=1)
# btn5.grid(row=2, column=0)
# btn6.grid(row=2, column=1, sticky="we")
# btn7.grid(row=3, column=0, columnspan=2, sticky="we") #растянул кнопку на 2 столбца
# btn8.grid(row=0, column=3, rowspan=4, sticky="ns") #раснянул кнопку на 4 ряда


############ установка ширины колонок ################
for i in range(5):
    for j in range(3):
        tk.Button(text=f"Button {i}{j}").grid(row=i, column=j, sticky="we")

window.mainloop()