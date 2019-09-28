#игра "угадай число"
import random

play_again = 'да'
print("Привет! Как тебя зовут?")
name = input()

def guessNumber ():
    print("Что ж, "+name+" я загадаваю число от 1 до 20")

    number = random.randint(1,20)

    counter = 0
    for counter in range (6):
        if counter == 0:
            print("Попробуй угадать число")
        else:
            print("Попробуй угадать число еще раз")

        guess_number = int(input())
        if guess_number > number:
            print("Ваше число слишком большое")
        if guess_number < number:
            print("Ваше число слишком маленькое")
        if guess_number == number:
            break

    if guess_number== number:
        counter =str(counter+1)
        print("Вы угадали за " +counter+ " попыток")
    else:
        number = str(number)
        print("Я загадала число "+number)

    print('Сыграем ещё? (\'да\', \'нет\')')


while play_again == 'да':
    guessNumber()
    play_again = input()

print('Спасибо за игру '+name+'!')