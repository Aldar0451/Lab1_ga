a = list()
for m in range(2, 1000, 2):
    for n in range(1, 1001, 2):
        if 400000000<2**m * 3**n<600000000:
            a.append(2**m * 3**n)
a.sort()
print(a)
