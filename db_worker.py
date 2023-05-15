import sqlite3
from sqlite3 import Error

from statistics import Statistics


class Database:
    def __init__(self, name):
        self.__name = name
        self.__connection = self.create_connection()

    def create_connection(self):
        connection = None
        try:
            connection = sqlite3.connect(self.__name)
        except Error:
            raise Error('Неккоректное имя базы данных')
        return connection

    def insert_data(self, user):
        cursor = self.__connection.cursor()
        cursor.execute('''
            INSERT INTO users(user_name, password) VALUES(?, ?)
        ''', user)
        self.__connection.commit()

    def get_value(self, user_name):
        cursor = self.__connection.cursor()
        cursor.execute('''
            Select * from users where "user_name" = ?
        ''', (user_name, ))
        result = cursor.fetchone()
        return result

    def update_value(self, user_name, statistics: Statistics):
        cursor = self.__connection.cursor()
        cursor.execute('''
            UPDATE users SET wrong_answers=?, right_answers=? WHERE user_name=?
        ''', (statistics.wrong_answers, statistics.right_answers, user_name))
        self.__connection.commit()

    def get_all_values(self):
        cursor = self.__connection.cursor()
        cursor.execute('''
            Select "id", "user_name", "wrong_answers", "right_answers"  from users
        ''')
        return cursor.fetchall()


