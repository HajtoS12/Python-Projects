from tkinter import *
import random
import pandas

BACKGROUND_COLOR = "#B1DDC6"

try:
 data =  pandas.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
 data = pandas.read_csv("./data/french_words.csv")


to_learn = data.to_dict(orient="records")
current_card = {}


def next_card():
     global current_card,flip_timer
     window.after_cancel(flip_timer)
     current_card = random.choice(to_learn)
     card.itemconfig(language, text="French",fill="black")
     card.itemconfig(word, text=current_card["French"],fill="black")
     card.itemconfig(card_side, image=front_card)
     flip_timer = window.after(3000,flip_card)

def flip_card():
     card.itemconfig(card_side,image=back_card)
     card.itemconfig(language, text="English",fill="white")
     card.itemconfig(word, text=current_card["English"],fill="white")

def is_known():
     to_learn.remove(current_card)
     data = pandas.DataFrame(to_learn)
     data.to_csv("data/words_to_learn.csv", index=False)
     next_card()



window = Tk()
window.title("Flashy")
buttonClicked=False
flip_timer = window.after(3000,flip_card)

window.config(bg=BACKGROUND_COLOR, padx=50 ,pady=50)

front_card = PhotoImage(file="./images/card_front.png")
back_card = PhotoImage(file="./images/card_back.png")

card = Canvas(height=526,width=800,bg=BACKGROUND_COLOR, highlightthickness=0)
card_side = card.create_image(400,263, image= front_card)
language = card.create_text(400,150, text="Title", font=("Ariel",40,"italic"))
word = card.create_text(400,263, text="Word", font=("Ariel",60,"bold"))
card.grid(column=0,row=0,columnspan=2)

right_image = PhotoImage(file="./images/right.png")
right = Button( image=right_image, highlightthickness=0,command=is_known)
right.grid(column=1,row=1,)

wrong_image = PhotoImage(file="./images/wrong.png")
wrong = Button( image=wrong_image, highlightthickness=0, command=next_card)
wrong.grid(column=0,row=1,)

next_card()



window.mainloop()

