from tkinter import ttk
from tkinter import *

from db_worker import Database
from statistics import Statistics
from tabs import StatisticsTab, QuestionTab, LeadersBoard


class App(Tk):

    def __init__(self, user: str):
        super().__init__()

        self.user = user

        self.protocol("WM_DELETE_WINDOW", self.destroy)
        self.tab_control = ttk.Notebook(self)

        self.db = Database('users.db')

        self.statistics = Statistics(self.db.get_value(user)[3], self.db.get_value(user)[4])
        self.user_label = Label(self, text=f'Текущий пользователь: {user}')

        self.question_tab = QuestionTab(self.tab_control, self.statistics)
        self.statistics_tab = StatisticsTab(self.tab_control, self.statistics)
        self.leaders_tab = LeadersBoard(self.tab_control)

        self.tab_control.add(self.question_tab, text="Вопросы")
        self.tab_control.add(self.statistics_tab, text="Статистика")
        self.tab_control.add(self.leaders_tab, text="Таблица лидеров")

        self.tab_control.pack(expand=1, fill="both")

        self.question_tab.next_question()

    def destroy(self):
        self.db.update_value(self.user, self.statistics)
        super().destroy()
