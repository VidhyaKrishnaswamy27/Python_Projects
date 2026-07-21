from tkinter import *
import pandas as pd
import random


BACKGROUND_COLOR = "#B1DDC6"
random_word={}


def generate_word():
    global random_word, waiting_time
    window.after_cancel(waiting_time)
    random_word = random.choice(data_dict)
    french_word = random_word["French"]
    canvas.itemconfig(card, image=flash_card_front)
    canvas.itemconfig(title_text,text="French", fill="black")
    canvas.itemconfig(word_text, text=french_word, fill="black")
    waiting_time=window.after(1000,flip_card)

def update_list():
    data_dict.remove(random_word)
    new_data=pd.DataFrame(data_dict)
    new_data.to_csv("../flash-card-project-start/data/words_to_learn.csv",index=False)
    generate_word()


def flip_card():
    english_word=random_word["English"]
    canvas.itemconfig(card,image=flash_card_back)
    canvas.itemconfig(title_text,text="English",fill="white")
    canvas.itemconfig(word_text,text=english_word,fill="white")

#Data
try:
    updated_data = pd.read_csv("../flash-card-project-start/data//words_to_learn.csv")
except FileNotFoundError:
    original_data = pd.read_csv("../flash-card-project-start/data/french_words.csv")
    data_dict=original_data.to_dict(orient="records")
else:
    data_dict=updated_data.to_dict(orient="records")

window = Tk()
window.title("Flash Card")
window.config(padx=50, pady=50, width=1000, height=700, bg=BACKGROUND_COLOR)

waiting_time=window.after(1000,flip_card)

#Canvas Image
canvas=Canvas(width=800, height=526,bg=BACKGROUND_COLOR, highlightthickness=0)
flash_card_front=PhotoImage(file="../flash-card-project-start/images/card_front.png")
flash_card_back=PhotoImage(file="../flash-card-project-start/images/card_back.png")
right_button_image=PhotoImage(file="../flash-card-project-start/images/right.png")
wrong_button_image=PhotoImage(file="../flash-card-project-start/images/wrong.png")
card=canvas.create_image(400,263,image=flash_card_front)
title_text=canvas.create_text(400,150,text="",font=("Ariel",40,"italic"))
word_text=canvas.create_text(400,263,text="",font=("Ariel",60,"bold"))
canvas.grid(row=0,column=0,columnspan=2)


#Button
right_button=Button(image=right_button_image,bg=BACKGROUND_COLOR, highlightthickness=0,command=update_list)
right_button.grid(row=1, column=0)
wrong_button=Button(image=wrong_button_image, bg=BACKGROUND_COLOR, highlightthickness=0,command=generate_word)
wrong_button.grid(row=1, column=1)

generate_word()

window.mainloop()
