marks = int(input("Enter marks: "))
attendance = int(input("Enter attendance: "))
income = int(input("Enter family income: "))

if marks >= 80 and attendance >= 75 and income <= 300000:
    print("Eligible for scholarship")
else:
    print("Not eligible")