balance = float(input("Enter balance: "))
amount = float(input("Enter withdrawal amount: "))

if amount <= 0:
    print("Invalid amount")
elif amount > balance:
    print("Insufficient balance")
elif balance - amount < 500:
    print("Minimum balance must be ₹500")
else:
    balance = balance - amount
    print("Withdrawal successful")
    print("Remaining balance =", balance)