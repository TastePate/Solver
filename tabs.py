import tkinter
from tkinter import *
from tkinter import ttk

from question import Question
from statistics import Statistics

from tkinter.messagebox import showerror

import matplotlib

matplotlib.use('TkAgg')

from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class StatisticsTab(ttk.Frame):

    def __init__(self, master: ttk.Notebook, statistics: Statistics):
        super().__init__(master)

        self.statistics = statistics

        self.figure = Figure(figsize=(6, 4), dpi=100)
        self.canvas = FigureCanvasTkAgg(self.figure, self)

        self.axes = self.figure.add_subplot()

        self.axes.set_yticks(range(0, 1000))
        self.axes.set_title('Статистика правильных ответов')
        self.axes.set_ylabel('Кол-во')

        self.canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
        self.canvas.draw()

        self.update()

    def update(self):
        self.axes.bar(['Правильные ответы', 'Неправильные ответы'],
                      [self.statistics.right_answers, self.statistics.wrong_answers],
                      color='b',
                      width=0.1,
                      align='center')
        self.canvas.draw()
        self.after(1000, self.update)


class QuestionTab(ttk.Frame):
    
    def __init__(self, master: ttk.Notebook, statistics: Statistics):
        super().__init__(master)

        self.first_time_running = True
        self.statistics = statistics
        self.question_label = Label(self, font=("Times New Roman", 30))
        self.question = None

        self.check = StringVar()
        self.check.trace("w", self.deactivate_button_on_empty_entry)
        self.answer_entry = Entry(self, width=5,
                                  font=("Times New Roman", 30),
                                  textvariable=self.check,
                                  )

        self.accept_button = Button(self, font=("Times New Roman", 20),
                                    text='Принять ответ',
                                    state=DISABLED,
                                    command=self.accept_answer)

        self.right_or_not_label = Label(self, font=("Times New Roman", 20))


    def deactivate_button_on_empty_entry(self, *args):
        result = self.check.get()
        self.accept_button.config(state=DISABLED if result == "" else NORMAL)
        
    def accept_answer(self):
        self.accept_button.config(state=DISABLED)
        self.answer_entry.config(state=DISABLED)
        try:
            answer = float(self.answer_entry.get())
            if answer == self.question.right_answer:
                self.statistics.right_answers += 1
            else:
                self.statistics.wrong_answers += 1
            self.right_or_not_label.config(
                text="Правильно!" if answer == self.question.right_answer
                                  else "Неверно!")

            self.after(500, self.next_question)
        except ValueError:
            showerror('Ошибка', 'Введеное значение не является числом!')
            self.accept_button.config(state=NORMAL)
            self.answer_entry.config(state=NORMAL)
            self.answer_entry.delete(0, END)

    def next_question(self):
        self.right_or_not_label.config(text="")
        self.answer_entry.config(state=NORMAL)
        self.answer_entry.delete(0, END)
        self.question = Question(1, 100)
        self.question_label.config(text=self.question.__str__())

        self.question_label.pack()
        self.answer_entry.pack()
        self.accept_button.pack()
        self.right_or_not_label.pack()


