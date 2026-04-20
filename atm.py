pin = 4569
balance = 10000
user_pin = int(input("Enter Pin = "))
if user_pin == pin:
    amount = int(input("Enter Amount = "))
    if amount <= balance:
        balance = balance - amount
        print("Cash given")
        print("Available balance = " ,balance)
    else:
        print("Insuffient Balance")
else:
    print("Invalid Pin")
