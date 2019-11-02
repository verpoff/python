from time import sleep
print("Введите команду")
command = input()
engine = False
was_started = False
car_go = False

while command:
    while command not in {"on", "off", "help", "exit","go","stop"}:
        print('''Команда не найдена
введи help для списка команд''')
        command = input()
    if command == 'help':
        print("     on = вкл двигатель")
        sleep(1)
        print("     off = откл двигатель")
        sleep(1)
        print("     exit = выйти")
        sleep(1)
        print("     go = поехать на машине")
        sleep(1)
        print("     stop = остановить машину")

    if command == 'on':

        if engine:
            print('Двигатель уже включён')
        else:
            print("Завожу двигатель")
            sleep(2)
            print("Двигатель включен")
            engine = True
            was_started = True

    if command == "off":
        if engine:
            print("Выключаю двигатель")
            sleep(2)
            print("Двигатель выключен")
            engine = False
        else:
            if was_started:
                print("Двигатель уже выключен")
            else:
                print("Двигатель еще не включен")
    if command == "exit":
        print("Выхожу из автомобиля")
        break
    if command == "go":

        if car_go:
            print("Машина уже едет")
        else:
            print("Машина поехала")
            car_go = True
    if command == "stop":

        if car_go:
            if
    print("Введите команду")
    command = input()
