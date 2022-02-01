print("First variant:")
a = 1
b = 2
print("a:", a)
print("b:", b)
b -= a
a += a
print("a:", a)
print("b:", b)
print("Second variant:")
a = 1
b = 2
print("a:", a, "\n", "b:", b)
b = a
a += b
print("a:", a, "\n", "b:", b)
