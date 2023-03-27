import random


class Question:

    def __init__(self, start, stop):
        self.__random = random.Random()
        self.__first_number = self.__random.randint(start, stop)
        self.__second_number = self.__random.randint(start, stop)
        self.__sign_number = self.__random.randint(1, 4)
        self.__sign = self.__generate_sign()
        self.__right_answer = self.__get_right_answer()


    @property
    def right_answer(self):
        return self.__right_answer


    def __generate_sign(self):
        match self.__sign_number:
            case 1:
                return "+"
            case 2:
                return "-"
            case 3:
                return "/"
            case 4:
                return "*"


    def __get_right_answer(self):
        match self.__sign:
            case "+":
                return self.__first_number + self.__second_number
            case "-":
                return self.__first_number - self.__second_number
            case "/":
                temp_answer = round(self.__first_number / self.__second_number, 2)
                return int(temp_answer) if temp_answer == int(temp_answer) else temp_answer
            case "*":
                return self.__first_number * self.__second_number

    def __str__(self):
        return f"{self.__first_number} {self.__sign} {self.__second_number}"
