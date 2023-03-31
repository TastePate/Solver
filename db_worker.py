import sqlite3
from sqlite3 import Error

class Database:
    def __init__(self, name):
        self.__name = name
        self.__connection = self.create_connection()

    def create_connection(self):
        connection = None
        try:
            connection = sqlite3.connect(self.__name)
            print('Успешно подключено!')
        except Error as e:
            print(f'Произошла ошибка подключения: \'{e}\'')
        return connection

    def insert_data(self, user):
        cursor = self.__connection.cursor()
        cursor.execute('''
            INSERT INTO users(user_name, password, wrong_answers, right_answers) VALUES(?, ?, ?, ?)
        ''', user)
        self.__connection.commit()
