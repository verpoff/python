# Программа для автоматизации навыков счёта
from timeit import default_timer
from time import sleep
from random import randint, choice
import os

def select_mode():
    if not os.path.exists(f'{name}_errors.txt'):

        print("1 = workout")
        print('2 = settings')
        print("0 = exit")


        mode = input()
        while mode not in  {'0','1','2'}:
            print("Should be '0', '2' or '1' ")
            mode = input()

    elif os.path.exists(f'{name}_errors.txt'):

        print("1 = workout")
        print("2 = error handling")
        print("3 = settings")
        print("0 = exit")

        mode = input()
        while mode not in {'0', '1', '2', '3'}:
            print("Should be '0', '2', '1' or '3' ")
            mode = input()

    return mode


def settings():
    file = 'settings.txt'

    if os.path.exists(file):
        with open(file, 'r') as f:
            pass


def count():

    sleep(1)
    print('Lets check your math knowledge.')
    sleep(1)


    answers_quantity = ''  # количество примеров
    maximum_answer = ''  # до скольки будет считать
    correct_answers = 0
    fails = 0
    time_in_seconds = 0
    example_number = 0
    unique_examples = []


    while not answers_quantity.isdigit():
        print(name + " How many mathematical actions are you ready to solve?")
        answers_quantity = input()

        if answers_quantity.isdigit():
            while int(answers_quantity) < 1:
                print("Enter a number greater than 0")
                answers_quantity = input()
                while not answers_quantity.isdigit():
                    print("Must be number")
                    answers_quantity = input()


    while not maximum_answer.isdigit():
        print("How many will be count")
        maximum_answer = input()

        if maximum_answer.isdigit():
            while int(maximum_answer) < 2:
                print("enter a number more then 1")
                maximum_answer = input()
                while not maximum_answer.isdigit():
                    print("Must be number")
                    maximum_answer = input()
        else:
            print("Must be number")

        my_warnings = ["Wrong","look at the your answer","Wrong digit"]

    col_unique_examples = int(maximum_answer) ** 2

    #Пока не достигним макс количетсва уникальных примеров
    while not len(unique_examples) == col_unique_examples:  

        if not example_number > int(answers_quantity):
    
            for i in range(int(answers_quantity)):

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

                example = f"{numeric1} {sign} {numeric2}"

                while example not in unique_examples:
                    unique_examples.append(example)

                    example_number +=1
                    if example_number > int(answers_quantity):   
                        break
                    print(f"Example {example}")

                    start = default_timer()
                    student_answer = input()
                    stop = default_timer()
                    time_in_seconds += round(stop - start)

                    while not student_answer.isdigit():
                        print("Must be number")
                        student_answer = input()

                    if int(student_answer) == correct_answer:
                        print("Excellent!")
                        correct_answers += 1
                    else:
                        print(my_warnings[randint(0, len(my_warnings)) - 1])
                        print("Correct answer: " + str(correct_answer))
                        fails += 1
                        with open(f'{name}_errors.txt', 'a')as f:
                            f.write(f'{numeric1} {sign} {numeric2} 3\n')
        else:
            break
    else:
        print()
        if not example_number > int(answers_quantity):
            print("Unique examples is over")

    if time_in_seconds < 60:
        spend_time = f"{time_in_seconds} seconds"
    else:
        minutes = time_in_seconds // 60
        seconds = time_in_seconds - (minutes * 60)
        if seconds > 0:
             spend_time = f"{minutes} minutes and {seconds} seconds"
             
    if fails == 0:
        print(f"You got it {spend_time}")
        print(f'Well done, {name}! You answered all the questions correctly ')
    elif correct_answers == 0:
        print("You did not answer all the questions correctly!")
    else:
        print(f"You answered {correct_answers} questions")
        sleep(1)
        print(f"Fails {fails}")


def fix_errors(name):
    file = f'{name}_errors.txt'
    tmp_file = f'tmp_{name}_errors.txt'

    if os.path.exists(file):

        with open(file, 'r') as f, open(tmp_file, 'a') as f2:

            for line in f:
                splited = line.split()

                number1,sign,number2,repeat = splited
                number1 = int(number1)
                number2 = int(number2)

                print(f"{number1} {sign} {number2}")
                if sign == '-' :
                    correct_answer = number1 - number2

                if sign == '+':
                    correct_answer = number1 + number2

                my_warnings = ["Wrong", "look at the your answer", "Wrong digit"]
                my_congratulation = ['Right','Correct','Wonderful']

                answer = int(input())
                if answer == correct_answer:
                    print(my_congratulation[randint(0, len(my_congratulation)) - 1])
                    f2.write(f'{number1} {sign} {number2} {int(repeat)-1}\n')
                else:
                    print(my_warnings[randint(0, len(my_warnings)) - 1])
                    f2.write(f'{number1} {sign} {number2} {repeat}\n')



    os.remove(file)
    if os.path.exists(tmp_file):
        os.rename(tmp_file, file)
        if os.path.getsize(file) <1:
            os.remove(file)

            
#  main program block
print('Hello! My name is Rodjer. And your name?')
name = input()

name = name.title()

  

print('Welcome ' + name)

while True:

    if os.path.exists(f'{name}_errors.txt'):
        pass
    mode = select_mode()

    if mode == "1":
        count()
    elif mode == '0':
        break
    elif mode == '2':
        fix_errors(name)
    elif mode == '3':
        settings()
    else:
        pass
