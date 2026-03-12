from tkinter import *
from tkinter import messagebox
import random
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def pass_function():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for letter in range(nr_letters)]
    password_symbols = [random.choice(symbols) for sym in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for num in range(nr_numbers)]

    password_list = password_letters+password_symbols+password_numbers

    random.shuffle(password_list)

    pass_generated=''.join(password_list)
    
    pass_enter.delete(0,END)
    pass_enter.insert(0,str(pass_generated))
# ---------------------------- SAVE PASSWORD ------------------------------- #
def write_password():
    web_text=web_enter.get()
    mail_text=mail_enter.get()
    password=pass_enter.get()
    new_data = {
        web_text: {
            'mail': mail_text,
            'password': password
        }
    }

    if len(web_text)==0 or len(password)==0:
        messagebox.showinfo(message="Don't left empty fields")
    else:
        try:
            with open('passwords.json', 'r') as file:
                data=json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            with open('passwords.json', 'w') as file:
                json.dump(new_data, file,indent=4)
        else:
            with open('passwords.json', 'w') as file:    
                data.update(new_data)
                json.dump(data,file,indent=4)
        finally:
            web_enter.delete(0, END)
            pass_enter.delete(0,END)

def search():
    web_text=web_enter.get()
    mail_text=mail_enter.get()
    
    try:
        with open('passwords.json', 'r') as file:
            data=json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(message="Nothing to search, create passwords at first")
    else:
        try:
            data[web_text]
        except KeyError:
            messagebox.showinfo(message="No password for this website")
        else:
            messagebox.showinfo(message=f"For {web_text}\n Email: {mail_text}\n Passwors is:{data[web_text]['password']}")
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Password Manager')
window.config(padx=20,pady=20)

canvas=Canvas(width=200,height=200,highlightthickness=0)
logo=PhotoImage(file='logo.png')
canvas.create_image(100,100,image=logo)
canvas.grid(row=0,column=1)

web=Label(text='Website: ', font=('Arial',12,'normal'))
web.grid(row=1,column=0)
web_enter=Entry(width=21)
web_enter.grid(row=1,column=1,sticky='ew')
web_button=Button(text='Search', command=search)
web_button.grid(row=1,column=2,sticky='ew')

mail=Label(text='Email/Username: ', font=('Arial',12,'normal'))
mail.grid(row=2,column=0)
mail_enter=Entry(width=35)
mail_enter.grid(row=2,column=1,columnspan=2,sticky='ew')
mail_enter.insert(0, 'igor2018kavl@gmail.com')

pas_label=Label(text='Password: ', font=('Arial',12,'normal'))
pas_label.grid(row=3,column=0)
pass_enter=Entry(width=21)
pass_enter.grid(row=3,column=1,sticky='ew')
pass_gen=Button(text='Generate Password',command=pass_function)
pass_gen.grid(row=3,column=2)

add_pass=Button(text='Add Password',width=36,command=write_password)
add_pass.grid(row=4,column=1, columnspan=2,sticky='ew')

window.mainloop()