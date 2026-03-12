THEME_COLOR = "#375362"
from tkinter import *

class QuizInterface():
    def __init__(self,quiz_brain):
        self.quiz=quiz_brain
        q_text=self.quiz.next_question()
        self.score=self.quiz.score
        self.window=Tk()
        self.window.title('Quiz')
        self.window.config(bg=THEME_COLOR,padx=20,pady=20)
        self.plate=Canvas(width=300,height=250,highlightthickness=0)
        self.plate.create_text(150,125,text=q_text,font=('Arial',20,'italic'),width=280)
        self.plate.grid(row=1,column=0,columnspan=2,pady=20)

        self.score_label=Label(text=f'Score:{self.score} ', font=('Arial',12,'normal'),bg=THEME_COLOR)
        self.score_label.grid(row=0,column=1)
        
        self.true_image=PhotoImage(file='day34/images/true.png')
        self.false_image=PhotoImage(file='day34/images/false.png')
        self.button_true=Button(image=self.true_image,borderwidth=0,highlightthickness=0,command=self.true_button)
        self.button_true.grid(row=2,column=0)
        self.false_button=Button(image=self.false_image,borderwidth=0,highlightthickness=0,command=self.false_button)
        self.false_button.grid(row=2,column=1)

        self.window.mainloop()

    def true_button(self):
        is_right = self.quiz.check_answer('True')
        self.give_feedback(is_right)

    def false_button(self):
        is_right = self.quiz.check_answer('False')
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.plate.config(bg='green')
        else:
            self.plate.config(bg='red')
        self.window.after(1000, self.load_next_question)

    def load_next_question(self):
        self.plate.config(bg='white')
        q_text = self.quiz.next_question()
        self.plate.itemconfig(1, text=q_text)
        self.score_label.config(text=f'Score:{self.quiz.score}/{self.quiz.question_number}')
    
    def reset_color(self):
        self.plate.config(bg='white')