number_float_namber = int(input("Введите количество чисел последовательности: "))
iteration_limiter = 1
float_namber = float(input("Введите число: "))
min_float_namber = float_namber
max_float_namber = float_namber
sum_float_namber = float_namber
while iteration_limiter < number_float_namber:
    float_namber = float(input("Введите число: "))
    sum_float_namber += float_namber
    if float_namber < min_float_namber:
        min_float_namber = float_namber
    if float_namber > max_float_namber:
        max_float_namber = float_namber
    iteration_limiter += 1
average_float_namber = sum_float_namber / number_float_namber
print("Количество введенных чисел последовательности", number_float_namber)
print("Минимальное число, из чисел введенной последовательности: ", min_float_namber)
print("Максимальное число, из чисел введенной последовательности: ", max_float_namber)
print("Среднее арифметическое, из чисел введенной последовательности", average_float_namber)