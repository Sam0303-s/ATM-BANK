import time
# __________________Global variables_______________
o1 = 1
o2 = 2
o3 = 3
o4 = 4
password = 1234
Balance = 10000

print("Please insert your card__ ")
time.sleep(3)

while True:
    try:
        Account_Pin = int(input("Enter your pin:  "))
    except ValueError:
        print("Please enter valid data type..........\n")
        continue

    if Account_Pin == password:
        print("Hello, Samuel!! \n Welcome, to International bank ! \n")
        while True:

            print("How can we help you? \n ")
            print("1: Check Balance.")
            print("2 Money Withdraw.")
            print("3: Money Deposit.")
            print("4: Exit")
            # print("4: New Account.")

            try:
                purpose = int(input("Enter any one option:  \n"))
            except:
                print("Please enter valid answer  >>> \n \n")
                continue

            if purpose == 1:
                print("Balance amount in your account is {} \n".format(Balance))
                print("=================||================")
                print("=================||================\n")
            elif purpose == 2:
                try:
                    cash_debit = int(input("Enter Amount:  "))
                except ValueError:
                    print("Please enter valid data type..........\n")
                    continue
                if cash_debit > Balance:
                    print(f"You do not have enough money in your account...\n You have Rs {Balance}")
                elif Balance - cash_debit < 2000:
                    print("There must be min of Rs 2000 in your account")
                else:
                    Balance = Balance - cash_debit
                    print("Rs {} is successfully debited from your account".format(cash_debit))
                    print("your current Bal in your account is {} \n".format(Balance))
                print("=================||================")
                print("=================||================\n")
            elif purpose == 3:
                cash_credit = int(input("Enter Amount:  "))
                Balance = Balance + cash_credit
                print("Rs {} is successfully credited to your account!!".format(cash_credit))
                print("your current Bal in your account is {} \n".format(Balance))
                print("=================||================")
                print("=================||================\n")
            elif purpose == 4:
                print("Thank You for coming!!!")
                print("Visit again..........")
                break
            else:
                print("Please enter the correct option ........")
    else:
        print("OOps entered Incorrect pin........ \n Try again \n")
        continue
