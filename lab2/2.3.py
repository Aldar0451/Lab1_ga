 
for m in range(2, 1000, 2):
    for n in range(1, 1001, 2):
        if 200000000<2**m * 3**n<400000000:
            print(2**m * 3**n)
