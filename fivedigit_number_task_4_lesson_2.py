# fivedigit_number = int(input("Введите пятизначное число"))
# num = 12345
# mul5 = (num % 10)
# num = num // 10
# mul4 = (num % 10)
# num = num // 10
# mul3 = num % 10
# num = num // 10
# mul2 = num % 10
# num = num // 10
# mul1 = num
# print(mul1, mul2, mul3, mul4, mul5)
# print(mul1 * mul2 * mul3 * mul4 * mul5)

num = int(input("Введите пятизначное число"))
mul = (num % 10)
num = num // 10
mul *= (num % 10)
num = num // 10
mul *= num % 10
num = num // 10
mul *= num % 10
num = num // 10
mul *= num
print(mul)
