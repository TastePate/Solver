import tkinter
from tkinter import *
from tkinter import ttk

from question import Question
from statistics import Statistics

import matplotlib

matplotlib.use('TkAgg')

from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk


class StatisticsTab(ttk.Frame):

    def __init__(self, master: ttk.Notebook, statistics: Statistics):
        super().__init__(master)

        self.statistics = statistics
        self.data = {
            'Правильные ответы': statistics.right_answers,
            'Неправильные ответы': statistics.wrong_answers,
        }

        x_data = self.data.keys()
        y_data = self.data.values()

        self.figure = Figure(figsize=(6, 4), dpi=100)
        self.figure_canvas = FigureCanvasTkAgg(self.figure, self)

        NavigationToolbar2Tk(self.figure_canvas, self)

        self.axes = self.figure.add_subplot()

        self.axes.bar(x_data, y_data)
        self.axes.set_title('Статистика правильных ответов')
        self.axes.set_ylabel('Кол-во')

        self.figure_canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

        # self.right_answers_label = Label(self, font=("Times New Roman", 10),
        #                                  text=f'Правильных ответов: {self.statistics.right_answers}')
        # self.wrong_answers_label = Label(self, font=("Times New Roman", 10),
        #                                  text=f'Неправильных ответов: {self.statistics.wrong_answers}')
        #
        # self.right_answers_label.pack()
        # self.wrong_answers_label.pack()

        self.update()

    def update(self):
        # self.right_answers_label.config(font=("Times New Roman", 10),
        #                                 text=f'Правильных ответов: {self.statistics.right_answers}')
        # self.wrong_answers_label.config(font=("Times New Roman", 10),
        #                                 text=f'Неправильных ответов: {self.statistics.wrong_answers}')
        self.data['Правильные ответы'] = self.statistics.right_answers
        self.data['Неправильные ответы'] = self.statistics.wrong_answers
        self.figure.canvas.draw()
        self.figure.canvas.flush_events()
        self.after(100, self.update)


class QuestionTab(ttk.Frame):
    
    def __init__(self, master: ttk.Notebook, statistics: Statistics):
        super().__init__(master)

        self.statistics = statistics
        self.question_label = Label(self, font=("Times New Roman", 30))
        self.question = None

        self.check = StringVar()
        self.check.trace("w", self.deactivate_button_on_empty_entry)
        self.answer_entry = Entry(self, width=5,
                                  font=("Times New Roman", 30),
                                  textvariable=self.check)

        self.accept_button = Button(self, font=("Times New Roman", 20),
                                    text='Принять ответ',
                                    state=DISABLED,
                                    command=lambda: [self.after(1000, self.next_question), self.accept_answer()])

        self.right_or_not_label = Label(self, font=("Times New Roman", 20))


    def deactivate_button_on_empty_entry(self, *args):
        result = self.check.get()
        self.accept_button.config(state=DISABLED if result == "" else ACTIVE)
        
    def accept_answer(self):
        self.accept_button.config(state=DISABLED)
        if self.answer_entry.get() == str(self.question.right_answer):
            self.statistics.right_answers += 1
        else:
            self.statistics.wrong_answers += 1
        self.right_or_not_label.config(text="Правильно!" if self.answer_entry.get() == str(self.question.right_answer)
                                                         else "Неверно!")

    def next_question(self):
        self.right_or_not_label.config(text="")
        self.answer_entry.delete(0, END)
        self.question = Question(1, 100)
        self.question_label.config(text=self.question.__str__())

        self.question_label.pack()
        self.answer_entry.pack()
        self.accept_button.pack()
        self.right_or_not_label.pack()
