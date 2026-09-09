n = int(input("Enter number: "))
k = int(input("Enter K: "))

if n & (1 << k):
    print("Bit is set")
else:
    print("Bit is not set")