class Bank(object):
    def __init__(self,cardnumber,pinnumber):
        self.cardnumber = cardnumber
        self.pinnumber = pinnumber

    def cash_balance(self):
        print('You have 20,000 in your bank account , you are rich !!')

    def cash_withdraw(self,withdrawmoney):
        print('You have withdrawn', withdrawmoney,'from your account')
        print('You have',20000-withdrawmoney,'in your account')
        if withdrawmoney>20000:
            print('sorry but you dont have that much money')

print('Welcome to your personal bank , lets  see how rich you are !! (you have more than 15,000)')
cardnumber = input("insert your card number:- ")
pinnumber  = input("enter your pin number:- ")

atmuser =  Bank(cardnumber ,pinnumber)

print("Choose your Bank activity choice ")
print("1.Balance Enquriy or  2.withdrawl")
choice = int(input("Enter choice number :- "))

if (choice == 1):
    atmuser.cash_balance()
elif (choice == 2):
     withdrawl = int(input("Enter the withdrawal money:- "))
     atmuser.cash_withdraw(withdrawl)
else:
    print("Enter a valid number")