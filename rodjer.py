# Программа для автоматизации навыков счёта
from timeit import default_timer
from time import sleep
from random import randint, choice

print('Привет! Меня зовут Роджер. А как тебя?')
name = input()
name = name.title()

print('Приятно познакомиться, ' + name)
sleep(1)
print('Давай проверим твои знания в математике.')
sleep(1)
print('Ты готов? (да или нет)')

ready = input()
while ready not in ('да', 'нет'):
    print("Должно быть да или нет")
    ready = input()
if ready == 'да':
    answers_quantity = ''
    while not answers_quantity.isdigit():
        print(name+", сколько присеров ты готов решить")
        answers_quantity = input()
        print("Должна быть цифра")
        if answers_quantity.isdigit():
            while int(answers_quantity) < 1:
                print('')
        else:
            print("Должна быть цифра")

    print("До скольки будем считать?")
    maximum_answer = int(input())

    while maximum_answer < 2:
        print("введи число больше 1")
        maximum_answer = int(input())

    # случайным образом сгенерируем
    numeric1 = randint(1, maximum_answer)  # левый операнд
    numeric2 = randint(1, maximum_answer)  # правый операнд
    sign = choice('+-')  # арифметический оператор

    # вычислим результат в зависимости от операции
    if sign == '-':
        # исключим отрицательный ответ
        while numeric1 < numeric2:
            numeric1 = randint(1, maximum_answer)
        correct_answer = numeric1 - numeric2

    if sign == '+':
        # исключим превышение максимально допустимого ответа
        while numeric1 + numeric2 > maximum_answer:
            numeric1 = randint(1, maximum_answer)
            numeric2 = randint(1, maximum_answer)
            correct_answer = numeric1 + numeric2


if ready == 'нет':
    print('''Передумал? Хорошо, может как-нибудь в следующий раз...
Пока!''')