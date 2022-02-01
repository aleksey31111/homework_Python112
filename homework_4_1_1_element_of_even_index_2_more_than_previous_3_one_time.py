### ELEMENT OF EVEN INDEX
# a = [i for i in range(21, 42)]
# print(a[1::2])
### MORE THAN PREVENT ELEMENT OF TUPLE ###
a = [input("-->") for i in range(3)]
# ar = range(a)
for i in range(len(a)):
    for j in range(len(a)):
        if(a[i]<a[j]):
            print(a[j])
