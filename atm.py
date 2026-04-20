pin = 4569
balance = 10000
attempts = 0

while attempts < 3:
    user_pin = int(input("Enter Pin = "))

    if user_pin == pin:
        amount = int(input("Enter Amount = "))

        if amount <= balance:
            balance -= amount
            print("Cash given")
            print("Available balance = ", balance)
        else:
            print("Insufficient Balance")
        break   # important

    else:
        attempts += 1
        print("Wrong Pin")

if attempts == 3:
    print("Your Card Has Been Blocked"
