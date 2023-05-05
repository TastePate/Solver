from tkinter import ttk
from tkinter import *

from db_worker import Database
from statistics import Statistics
from tabs import StatisticsTab, QuestionTab


class App(Tk):

    def __init__(self):
        super().__init__()

        self.protocol("WM_DELETE_WINDOW", self.destroy)
        self.tab_control = ttk.Notebook(self)

        self.db = Database('users.db')

        self.statistics = Statistics()

        self.question_tab = QuestionTab(self.tab_control, self.statistics)
        self.statistics_tab = StatisticsTab(self.tab_control, self.statistics)

        self.tab_control.add(self.question_tab, text="Вопросы")
        self.tab_control.add(self.statistics_tab, text="Статистика")

        self.tab_control.pack(expand=1, fill="both")

        self.question_tab.next_question()

    def destroy(self):
        pass
