hours = int(input("Enter hours worked: "))
rate = float(input("Enter rate per hour: "))

if hours <= 40:
    salary = hours * rate
else:
    salary = (40 * rate) + ((hours - 40) * rate * 1.5)

print("Salary =", salary)