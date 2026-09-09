count = 0
sum = 0

while True:
    n = int(input("Enter number: "))

    if n == -1:
        break

    sum = sum + n
    count = count + 1

if count > 0:
    print("Count =", count)
    print("Average =", sum / count)
else:
    print("No numbers entered")