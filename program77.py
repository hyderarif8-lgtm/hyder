def print_numbers(n):
    if n == 0:
        return

    print_numbers(n - 1)
    print(n)


n = int(input("Enter N: "))

print("Increasing:")
print_numbers(n)

print("Decreasing:")

def decreasing(n):
    if n == 0:
        return

    print(n)
    decreasing(n - 1)

decreasing(n)