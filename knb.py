from tkinter import *

root = Tk()
root.title("Камень, ножницы, бумага.")
root.iconbitmap("./assets/knb_image.ico")
ROOT_WIGHT = 600
ROOT_HIGHT = 400
ROOT_XCOR = 200
ROOT_YCOR = 200
FONT_LABEL = ("Helvetica", 14, "bold italic")
FONT_BUTTON = ("Helvetica", 12, "normal")
player_score = 0
comp_score = 0


# -----root (window of game)----------------------
root.geometry("{}x{}+{}+{}".format(ROOT_WIGHT, ROOT_HIGHT, ROOT_XCOR, ROOT_YCOR))


# --------------labels:---------------------------
title_Label = Label(root,
                    text="🤞 Давай поиграем в\nКамень, Ножницы, Бумага!",
                    font=FONT_LABEL,                    
                    )
title_Label.pack()


score_label = Label(root,
                    text=f"СЧЕТ: компьютер {comp_score} : игрок {player_score},"
                    )
score_label.pack()

# TOFIX:
# img = PhotoImage(True, file="./assets/knb_image.jpg")
# image_label = Label(root, image=img,                    
#                     )
# image_label.pack()

# --------------buttons:---------------------------
stone_button = Button(text="камень")
stone_button.pack()

scissors_button = Button(text="ножницы")
scissors_button.pack()

paper_button = Button(text="бумага")
paper_button.pack()


root.mainloop()