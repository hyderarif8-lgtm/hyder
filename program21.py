age = int(input("Enter age: "))

if age < 5:
    price = 0
elif age <= 12:
    price = 50
else:
    price = 100

print("Ticket Price =", price)