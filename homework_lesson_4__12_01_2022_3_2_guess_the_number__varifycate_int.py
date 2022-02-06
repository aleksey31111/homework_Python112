import random
namber_that_guess = round(random.random() * 100)
print(namber_that_guess)
attempt_number = 1
while True:
    nam = input("Введите число от 1 до 100: ")
    while type(nam) != int:
        try:
            nam = int(nam)
        except ValueError:
            print("Число не целое!")
            nam = input("Введите целое число: ")
    if nam == 0:
        break
    elif nam < namber_that_guess:
        print("Загаданное число больше")
    elif nam > namber_that_guess:
        print("Загаданное число меньше")
    else:
        print("Вы угадали загаданное число с %d раза" % attempt_number)
        break
    attempt_number += 1
