def product(n):
    if n < 10:
        return n

    return (n % 10) * product(n // 10)


n = int(input("Enter number: "))

print("Product =", product(n))