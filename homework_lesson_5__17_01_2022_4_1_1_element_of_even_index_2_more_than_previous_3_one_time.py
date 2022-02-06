print("### Term_1 ELEMENT OF EVEN INDEX ###")
a = [int(input("--> ")) for i in range(int(input("n: ")))]
print(a[::2])

print("### Term_2 MORE THAN PREVIOUS ###")
a = [int(input("--> ")) for i in range(int(input("n: ")))]
# a = [3, 1, 3, 1, 5, 9, 11, 6, 12, 11]
for i in range(1, len(a)):
    if a[i] > a[i - 1]:
        print(a[i], end=" ")
print()

s = [1, 3, 5, 6, 2, 4, 6, 1, 2, 7]
print(s)
for i in s:
    if s.count(i) == 1:
        print(i, end=" ")

print("### Term_3 UNIQUE ELEMENT OF LIST ###")
# b = [ int(input("--> ")) for i in range(int(input("n: ")))]
b = [1, 3, 5, 6, 2, 4, 6, 1, 2, 7]
unique = list()
for namber in b:
    if namber in unique:
        continue
    else:
        unique.append(namber)
print(b)
print(unique)

lst = [1, 3, 5, 6, 2, 4, 6, 1, 2, 7]
print(lst)
for j in range(len(lst)):
    for i in range(len(lst)):
        if lst[j] == lst[i] and j != i:
            break
    else:
        print(lst[j], end=" ")

b = []
for i in range(len(s)):
    if s[i] not in b:
        b.append(s[i])
print(b)
