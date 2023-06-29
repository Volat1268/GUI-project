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

nambe_Label = Label(root,
                    text="🤞 Давай поиграем в\nКамень, Ножницы, Бумага!",
                    font=FONT_LABEL,
                    
                    )
nambe_Label.pack()





root.mainloop()