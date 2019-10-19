from time import sleep
command1 = input()
if command1 == 'on':
    print("Двигатель включён")
if command1 == 'help':
    print("on = вкл двигатель")
    sleep(1)
    print("off = откл двигатель")
    sleep(1)
    print("exit = выйти")
if command1 == "off":
    print("Двигатель выключен")
