class atm(object):
    def __init__(self, cardNumber, pin):
        self.cardNumber = cardNumber
        self.pin = pin

    def balanceEnquiry(self):
        print("You have a balance of Rs.10,00,000.")

    def cashWithdrawal(self):
        money = int(input("Enter the amount you want to withdraw(in multiples of 100): "))
        withdrawalAmount = 1000000 - money
        print("You have withdrawed Rs.", money )
        print("Your balance has reduced to, Rs.", withdrawalAmount)

def main():
    print("Welcome to this ATM!")
    cardNumber = int(input("Enter Your Card Number: "))
    pin = int(input("Enter the pin: "))
    user1 = atm(cardNumber, pin)
    user1.balanceEnquiry()
    user1.cashWithdrawal()

main()
    