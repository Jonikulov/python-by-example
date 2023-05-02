# Challenge 134

from tkinter import *
import random

def check_answer():
    num1 = int(question_box['text'].split()[0])
    num2 = int(question_box['text'].split()[2])
    if int(answer_box.get()) == num1+num2:
        answer_img['image'] = photo1
    else:
        answer_img['image'] = photo2

def next_question():
    num1 = random.randint(10, 50)
    num2 = random.randint(10, 50)
    question_box['text'] = f"{num1} + {num2}"
    answer_box.delete(0, END)

    answer_img['image'] = ""

root = Tk()
root.geometry("300x330")
root.title("Quizzes")

qlabel = Label(text="Question:")
qlabel.place(x=30, y=30)

num1 = random.randint(10, 50)
num2 = random.randint(10, 50)
question_box = Label(text=f"{num1} + {num2}", bg='white', width=17)
question_box.place(x=100, y=30)

alabel = Label(text="Answer:")
alabel.place(x=30, y=60)

answer_box = Entry(justify='center', width=20)
answer_box.place(x=100, y=60)
answer_box.focus()

check_btn = Button(text="Check❓", command=check_answer, bg='orange')
check_btn.place(x=80, y=100)

next_btn = Button(text="Next➡️", command=next_question, bg='light blue')
next_btn.place(x=160, y=100)

photo1 = PhotoImage(file="correct.png")
photo2 = PhotoImage(file="incorrect.png")
answer_img = Label()
answer_img.place(x=67, y=140)

root.mainloop()