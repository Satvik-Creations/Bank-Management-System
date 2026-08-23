import amsql
balance = 0
inaccname = None

def Account():
    global inaccname
    decorator = "-"
    print(decorator.center(105,'-'))
    print("Welcome!")
    print(decorator.center(105,'-'))        
    accask = input("If You Have An Existing Account, Press(1), If Not, Press(2) To Create One: ")
    if accask == "1":
        inaccname = input("Enter Your Account Name: ")
        inpass = input("Enter Your Account Password: ")
        amsql.accaccess(inaccname,inpass)
        while True:
            AccTask()
            sp = input("To Open Task Menu Again Press(1), Else To Exit Press(2) : ")
            if sp == "1":
                pass
            if sp == "2":
                break
    if accask == "2":
        decorator = "-"
        print(decorator.center(105,'-'))
        print("Creating New Account")
        print(decorator.center(105,'-'))
        print()
        print("Make Sure Your Account Name Should Follow The Format: '{YOURNAME_DOB}' ")
        newaccname = input("Create New Account Name: ")
        newpass = input("Create New Password To Keep Your Account Secure: ")
        amsql.acccreate(newaccname,newpass)
        inaccname = input("Enter Your Account Name: ")
        inpass = input("Enter Your Account Password: ")
        amsql.accaccess(inaccname,inpass)
        amsql.acctable(inaccname)
        while True:
            AccTask()
            sp = input("To Open Task Menu Again Press(1), Else To Exit Press(2) : ")
            if sp == "1":
                pass
            if sp == "2":
                break
        
def Deposit():
    global balance
    global inaccname
    deposits = int(input("Enter the amount to be deposited: "))
    if deposits < 0:
            print("Cannot deposit a negative amount!")
    elif deposits > 100000:
        print("The Transaction Limit is up to ₹1,00,000/-")
    else:
        balance += deposits
        print(f"Balance: {balance}")
        amsql.Deposited(inaccname,deposits,balance,withdrawals=0)

def Withdraw():
    global balance
    global inaccname
    withdrawals = int(input("Enter the amount to be withdrawn: "))
    if withdrawals < 0:
            print("Cannot withdraw a negative amount.")
    elif balance <= 0:
        print("Balance = 0 , Zero Balance, Account is empty!")
    elif withdrawals > balance:
        print(f"Insufficient Balance!")
    elif withdrawals > 100000:
        print("The Transaction Limit is up to ₹1,00,000/-")
    else:
        balance -= withdrawals
        print(f"Balance: {balance}")
        amsql.Withdrawn(inaccname,withdrawals,balance,deposits=0)
        
def Balance():
    print(f"Your Account Balance is: {balance}")

def AccTask():
    acc_task = input("""What would you like to do?
          1. Check Balance
          2. Deposits
          3. Withdrawals
          """)
    if acc_task == "1":
        Balance()
    if acc_task == "2":
        Deposit()
    if acc_task == "3":
        Withdraw()

Account()