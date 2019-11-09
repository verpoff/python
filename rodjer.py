# Программа для автоматизации навыков счёта
from timeit import default_timer
from time import sleep
from random import randint, choice

print('Hello! My name is Rodjer. And you name?')
name = input()
name = name.title()

print('Welcome ' + name)
sleep(1)
print('Lets check your math knowledge.')
sleep(1)
print('You are ready (yes or no)')

ready = input()

while ready not in {'yes', 'no'}:
    print('''Should be 'yes' or 'no'
Введи заново''')
    ready = input()

if ready == 'yes':

    answers_quantity = ''  # количество примеров
    maximum_answer = ''  # до скольки будет считать
    question = ''
    correct_answers = 0
    fails = 0
    time_in_seconds = 0

    while not answers_quantity.isdigit():
        print(name + "How many mathematical actions are you ready to solve?")
        answers_quantity = input()

        if answers_quantity.isdigit():
            while int(answers_quantity) < 1:
                print("Enter a number greater than 0")
                answers_quantity = input()
                while not answers_quantity.isdigit():
                    print("Must be number")
                    answers_quantity = input()
        else:
            print("Должна быть цифра")

    while not maximum_answer.isdigit():
        print("До скольки будем считать")
        maximum_answer = input()

        if maximum_answer.isdigit():
            while int(maximum_answer) < 2:
                print("Введи число больше 1")
                maximum_answer = input()
                while not maximum_answer.isdigit():
                    print("Должна быть цифра")
                    maximum_answer = input()
        else:
            print("Должна быть цифра")

        for question in range(int(answers_quantity)):
            print("Пример " + str(question + 1))

            # случайным образом сгенерируем
            numeric1 = randint(1, int(maximum_answer))  # левый операнд
            numeric2 = randint(1, int(maximum_answer))  # правый операнд
            sign = choice('+-')  # арифметический оператор

            # вычислим результат в зависимости от операции
            if sign == '-':
                # исключим отрицательный ответ
                while numeric1 < numeric2:
                    numeric1 = randint(1, int(maximum_answer))  # левый операнд
                    numeric2 = randint(1, int(maximum_answer))  # правый операнд

                correct_answer = numeric1 - numeric2
            if sign == '+':
                # исключим превышение максимально допустимого ответа
                while numeric1 + numeric2 > int(maximum_answer):
                    numeric1 = randint(1, int(maximum_answer))
                    numeric2 = randint(1, int(maximum_answer))

                correct_answer = numeric1 + numeric2

            print("сколько будет " + str(numeric1) + str(sign) + str(numeric2))

            start = default_timer()
            student_answer = input()
            stop = default_timer()
            time_in_seconds += round(stop - start)

            while not student_answer.isdigit():
                print("Должна быть цифра")
                student_answer = input()

            if int(student_answer) == correct_answer:
                print("Правильно, молодец!")
                correct_answers += 1
            else:
                print("Неправильно")
                print("Правильный ответ: " + str(correct_answer))
                fails += 1

    if time_in_seconds < 60:
        spend_time = f"Ты справился за {time_in_seconds} секунд"
    else:
        minutes = time_in_seconds // 60
        seconds = time_in_seconds - (minutes * 60)
        if seconds > 0:
        spend_time = f"Ты справился за {minutes} минут и {seconds} секунд"
    if fails == 0:
        print(f'Молодец {name}! Ты правильно ответил на все вопросы ')
    elif correct_answers == 0:
        print("Ты не ответил ни на один вопрос правильно!")
    else:
        print(f"Ты правильно ответил на {correct_answers} вопроса")
        sleep(1)
        print(f"Ошибок {fails}")
if ready == 'нет':
    print('''Передумал? Хорошо, может как-нибудь в следующий раз...
Пока!''')
