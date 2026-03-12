from tkinter import *

window = Tk()
window.title('GUI')
window.minsize(width=500,height=300)

input = Entry(width=10)
input.pack()


label = Label(text ='I am Label', font=('Arial',24,'bold'))
label.pack()

def click():
    txt= input.get()
    label.config(text = txt)

button = Button(text='Button', command=click)
button.pack()












window.mainloop()
    