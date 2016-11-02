class Account(object):
    accountNumber = 0
    def __init__(self, owner, balance = 0.00):
        Account.accountNumber += 1
        self.owner = owner
        self.balance = balance
        self.accountNumber = Account.accountNumber
    def deposit(self, amount):
        assert type(amount) == float
        assert amount > 0.00
        self.balance = self.balance + amount
        print "You have deposited $" + str(float(amount))
    def withdraw(self, amount):
        assert type(amount) == float
        assert amount > 0.00
        calculation = self.balance - amount
        if calculation < 0.00:
            overdraftChoice = raw_input("Your account will be overdrafted by $" + str(calculation) + ". Are you sure you want to continue?").lower().startswith('y')
            if overdraftChoice:
                self.balance = calculation
                print "Your balance is now $" + str(calculation)
            else:
                print "Please enter another withdrawal amount."
        else:
            self.balance = calculation
            print "Your balance is now $" + str(calculation)
    def getBalance(self):
        return "$" + str(float(self.balance))
    def __str__(self):
        string = "This account belongs to " + self.owner
        return string

inUse = True

while inUse:
    name = raw_input('Please enter your name. ')
    newUser = Account(name)
    print "Hello " + name + "!"
    inLoop = True
    while inLoop:
        action = raw_input("What would you like to do? ").lower()
        if action.startswith('d'):
            amount = float(raw_input("Please enter an amount. "))
            newUser.deposit(amount)
        elif action.startswith('w'):
            amount = float(raw_input("Please enter an amount. "))
            newUser.withdraw(amount)
        elif action.startswith('b'):
            print newUser.getBalance()
        else:
            print "I do not recognize that command"
            exit = raw_input("Are you done with this terminal? ").lower()
            if exit.startswith('y'):
                inLoop = False
                inUse = False
            else:
                continue
