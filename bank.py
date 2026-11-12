from abc import ABC,abstractmethod
from random import randint

class Account(ABC):
    @abstractmethod
    def createAccount():
        return 0
    @abstractmethod
    def authenticate():
        return 0
    @abstractmethod
    def withdraw():
        return 0
    @abstractmethod
    def deposit():
        return 0
    @abstractmethod
    def displayBalance():
        return 0


class SavingsAccount(Account):
    def __init__(self):
        self.savingsAccount = {}
    def createAccount(self,name,intialDeposite):
        print()
        self.accountNumber = randint(10000,99999)
        self.savingsAccount[self.accountNumber] = [name,intialDeposite]
        print("Account creation has been succuessful.Your accountnumber is :",self.accountNumber)
        print()
        
    def authenticate(self,name,accountNumber):
        print()
        if accountNumber in self.savingsAccount.keys():
            if self.savingsAccount[accountNumber][0] == name:
                print("Authentication is succussful")
                self.accountNumber = accountNumber
                print()
                return True
            else:
                print("authentication Failed")
                print()
                return False
        else:
            print("Authentication Failed")
            print()
            return False


    def withdraw(self,withdrawalAmount):
        print()
        if withdrawalAmount > self.savingsAccount[self.accountNumber][1]:
            print("Insufficient balance")

        else:
            self.savingsAccount[self.accountNumber][1] -= withdrawalAmount
            print("Withdrawal was successfull")
            self.displayBalance()
        print()



    def deposit(self,depositAmount):
        print()
        self.savingsAccount[self.accountNumber][1] += depositAmount
        print("Amount deposited Succussfully..")
        self.displayBalance()
        print()

    def displayBalance(self):
                  print("Available Balance :",self.savingsAccount[self.accountNumber][1])
        

savingsAccount = SavingsAccount()
while True:
    print()
    print("Enter 1 to create a new account")
    print("Enter 2 to access an existing account")
    print("Enter 3 to exit")

    userChoice = int(input())
    print()
    if userChoice ==  1:
        print()
        print("Enter your name :")
        name = input()
        print("Enter a initial deposit :")
        deposit = int(input())
        savingsAccount.createAccount(name,deposit)
        print()
    elif userChoice == 2:
        print()
        print("Enter your name :")
        name = input()
        print("Enter your Account number :")
        accountNumber = int(input())
        authenticationStatus = savingsAccount.authenticate(name,accountNumber)
        print()
        if authenticationStatus is True:
            while True :
                print()
                print("Enter 1 to withdraw")
                print("Enter 2 to deposite")
                print("Enter 3 to display available balance")
                print("Enter 4 to go back to previous menu")
                userChoice = int(input())
                print()
                if userChoice == 1 :
                    print("Enter the withdrawal amount")
                    withdrawalAmount = int(input())
                    savingsAccount.withdraw(withdrawalAmount)
                    print()
                elif userChoice == 2:
                    print("Enter an amount to  be deposited")
                    depositAmount = int(input())
                    savingsAccount.deposit(depositAmount)
                    print()
                elif userChoice == 3:
                    print()
                    savingsAccount.displayBalance()
                    print()

                elif userChoice == 4:
                    break
    elif userChoice == 3:
             quit()


           




