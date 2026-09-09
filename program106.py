n = int(input("Enter size: "))

for i in range(3):
    for j in range(n):
        if i == 0 or i == 2:
            print("*", end=" ")
        elif j == n // 2:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()