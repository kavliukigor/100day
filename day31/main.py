import random
from tkinter import*
import pandas

BACKGROUND_COLOR = "#B1DDC6"
try:
    data=pandas.read_csv('day31/data/words_to_learn.csv')
except:
    data=pandas.read_csv('day31/data/french_words.csv')
    data.to_csv('day31/data/words_to_learn.csv', index=False)
words ={row.French: row.English for (index, row) in data.iterrows()}
current_word=random.choice(list(words.keys()))

def flip_card():
    card_french.itemconfig(word_french, text=words[current_word])
    card_french.itemconfig(language, text='English')
    card_french.itemconfig(card_image,image=card_back)
    
def show_card():
    global current_word
    current_word=random.choice(list(words.keys()))
    card_french.itemconfig(card_image, image=card_front)
    card_french.itemconfig(language, text='French')
    card_french.itemconfig(word_french, text=current_word)
    window.after(3000, flip_card)

def known_word():
    learned_word=pandas.DataFrame({'French':[current_word],'English':[words[current_word]]})
    words.pop(current_word)
    known=pandas.DataFrame({'French':list(words.keys()),'English':list(words.values())})
    try:
        open('day31/data/words_you_learned.csv')
    except FileNotFoundError:
        learned_word.to_csv('day31/data/words_you_learned.csv', index=False)
    else:
        learned_word.to_csv('day31/data/words_you_learned.csv', mode='a', header=False, index=False)
    finally:
        known.to_csv('day31/data/words_to_learn.csv', index=False)
    show_card()

window = Tk()
window.title('Cards')
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)

card_french=Canvas(width=800,height=526,highlightthickness=0,bg=BACKGROUND_COLOR)
card_front=PhotoImage(file='day31/images/card_front.png')
card_back=PhotoImage(file='day31/images/card_back.png')
card_image=card_french.create_image(400,263,image=card_front)
language=card_french.create_text(400,150 ,text='French', font=('Ariel',40,'italic'))
word_french=card_french.create_text(400,263 ,text=current_word, font=('Ariel',60,'bold'))
card_french.grid(row=0,column=0,columnspan=2,sticky='ew')

wrong=PhotoImage(file='day31/images/wrong.png')
button_wrong=Button(image=wrong,bg=BACKGROUND_COLOR,borderwidth=0,highlightthickness=0,command=show_card)
button_wrong.grid(row=1,column=0)

right=PhotoImage(file='day31/images/right.png')
button_right=Button(image=right,bg=BACKGROUND_COLOR,borderwidth=0,highlightthickness=0, command=known_word)
button_right.grid(row=1,column=1)

show_card()
window.mainloop()