n = 6

for i in range(3):
    for j in range(7):
        if (i == 0 and (j == 1 or j == 5)) or \
           (i == 1 and (j != 0 and j != 6)) or \
           i == 2:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

for i in range(4):
    print("  " * i + "* " * (7 - 2 * i))