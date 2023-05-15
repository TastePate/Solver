from tkinter import *
from tkinter.messagebox import showinfo, showerror

from app import App
from db_worker import Database


class EnterWindow(Tk):

    def __init__(self):
        super().__init__()
        self.geometry("800x600")
        self.db = Database('users.db')

        self.check_user_name_entry = StringVar()
        self.check_password_entry = StringVar()

        self.user_name_entry = Entry(self, textvariable=self.check_user_name_entry)
        self.password_entry = Entry(self, textvariable=self.check_password_entry)

        self.entry_button = Button(self,
                                   text='Войти',
                                   command=self.enter_to_account)
        self.registration_button = Button(self,
                                          text='Зарегистрироваться',
                                          command=self.open_registration_window)

        self.user_name_entry.pack()
        self.password_entry.pack()
        self.entry_button.pack()
        self.registration_button.pack()

    def enter_to_account(self):
        user_name = self.user_name_entry.get()
        password = self.password_entry.get()
        user = self.db.get_value(user_name)
        if user is None:
            showerror('Ошибка', 'Неверный логин или пароль!')
        elif user[1] == user_name and user[2] == password:
            self.open_main_app(user_name)


    def open_registration_window(self):
        self.destroy()
        registration_window = RegistrationWindow()
        registration_window.mainloop()
        registration_window.protocol("WM_DELETE_WINDOW", lambda: self.destroy())

    def open_main_app(self, user: str):
        self.destroy()
        main_app = App(user)
        main_app.mainloop()
        main_app.protocol("WM_DELETE_WINDOW", lambda: self.destroy())


class RegistrationWindow(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("800x600")
        self.db = Database('users.db')

        self.check_user_name_entry = StringVar()
        self.check_password_entry = StringVar()

        self.user_name_entry = Entry(self, textvariable=self.check_user_name_entry)
        self.password_entry = Entry(self, textvariable=self.check_password_entry)

        self.entry_button = Button(self,
                                   text='Зарегистрироваться',
                                   command=self.register_user)

        self.user_name_entry.pack()
        self.password_entry.pack()
        self.entry_button.pack()

    def register_user(self):
        user_name = self.user_name_entry.get()
        password = self.password_entry.get()
        user = self.db.get_value(user_name)
        if user is None:
            self.db.insert_data((user_name, password))
            self.open_main_app(user_name)
        else:
            showinfo('Предпреждение', 'Пользователь с таким именем уже существует!')

    def open_main_app(self, user: str):
        self.destroy()
        main_app = App(user)
        main_app.mainloop()
        main_app.protocol("WM_DELETE_WINDOW", lambda: self.destroy())
