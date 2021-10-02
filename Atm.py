class Atm(object):

    def __init__(self, cardNumber, pinNumber):
        self.cardNumber = cardNumber
        self.pinNumber = pinNumber
    
    def cashWithDrawl(self, howmuch):
        print("$"+ str(howmuch) +" has been withdrawed from your account")

    def balanceEnquiry(self, totalamount):
        print("You have $" + str(totalamount) + " remaining in your account")

def main():
    cnumber = input("Card Number: -")
    pnumber = input("Pin Number: -")
    
    newUser = Atm(cnumber, pnumber)
    totalamount = 60000000

    print("1. Balance Enquiry")
    print("2. Withdrawl")
    activity = int(input("enter activity number -"))
    if (activity == 1):
        newUser.balanceEnquiry(totalamount)
    elif(activity==2):
        howmuch = int(input("How much money do you want to withdraw? -"))
        newUser.cashWithDrawl(howmuch)
    else:
        print("enter the valid number")

main()


