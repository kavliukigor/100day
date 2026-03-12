from tkinter import *

window = Tk()
window.title('MIles to kilopmeters')
window.minsize(width=500,height=300)
label1 = Label(text =f'Convert miles to kilometers', font=('Arial',12,'normal'))
label1.pack(pady=10)
entry = Entry(width=5)
entry.pack(pady=5)
label2 = Label(text ='Yout answer will be here', font=('Arial',12,'normal'))
label2.pack(pady=10)

def calculate():
    res = round(((float(entry.get()))*1.6),2)
    label2.config(text=f'{float(entry.get())} miles is {res} kilometers')

button = Button(text='Calculate', command=calculate)
button.pack(pady=10)

window.mainloop()