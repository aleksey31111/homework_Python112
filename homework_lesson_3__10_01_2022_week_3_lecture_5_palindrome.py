# palindrom = int(input("Введите число: "))
# while palindrom > 0:
# if palindrom // 10 > 0:
#     print(palindrom % 10)
# if palindrom // 100 > 0:
#     print(((palindrom % 10) // 10) % 10)
# if palindrom // 1000 > 0:
#     print(((((palindrom % 10) // 10) % 10) // 10) % 10)
# if palindrom // 10000 > 0:
#     print(((((((palindrom % 10) // 10) % 10) // 10) % 10) // 10) % 10)
# if palindrom // 100000 > 0:
#     print(((((((((palindrom % 10) // 10) % 10) // 10) % 10) // 10) % 10) // 10) % 10)
palindrom = int(input("Введите число: "))
temp_1 = 0
temp_2 = 0
palindrom_copy = palindrom
while palindrom > 0:
    temp_1 = palindrom % 10
    temp_2 = temp_2 * 10 + temp_1
    palindrom = palindrom // 10
# if palindrom_copy == temp_2:
#     print("temp_2 = %d" % temp_2)
#     print("Число {0} является палиндромом".format(palindrom_copy))
# else:
#     print("temp_2 = %d" % temp_2)
#     print("Число {0} не является полиндромом".format(palindrom_copy))
print("Число -", palindrom_copy, "" if palindrom_copy == temp_2 else "не", "палиндром")

# palindrom = input(" Заведите число или слово -->")
# temp_1 = list(palindrom)
# temp_2 = len(palindrom)
# i = 1
# while i <= (temp_2/2):
#     if temp_1[i-1] == temp_1[-1]:
#         print("Ok")
#     else:
#         print("Not Ok")
#         break
#     i += 1
# print("Число", palindrom,"Является Палиндромом")
# print(palindrom, temp_1, temp_2)
# print(palindrom[-1:])
# print(palindrom[:1])
