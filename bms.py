import mysql.connector as sql
from getpass import getpass
import random

print("Welcome To Bank Management System")
print("This Is A Simple Bank Management System Project Using Python And MySQL")
print("="*105)
password = getpass("Enter Your MySQL Password To Connect With Database: ")
print("="*105)

def CreateDatabase():
    conn = sql.connect(host='localhost', user='root', password=password)
    cur = conn.cursor()
    cur.execute("CREATE DATABASE IF NOT EXISTS bank_management_system;")
    cur.close()
    conn.close()

def CreateTable():
    conn = sql.connect(host='localhost', user='root', password=password, database='bank_management_system')
    cur = conn.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS accinfo (
                ACCOUNT_NUMBER BIGINT(12) PRIMARY KEY,
                ACCOUNT_PIN BIGINT(4),
                NAME_OF_ACCOUNT_HOLDER VARCHAR(50),
                DOB BIGINT(8),
                PHONE_NUMBER BIGINT(10),
                EMAIL_ID VARCHAR(100),
                TYPE_OF_ACCOUNT VARCHAR(50)
                );
                """)
    cur.close()
    conn.close()

CreateDatabase()
CreateTable()

def accaccess(inaccno,inpin):
    conn = sql.connect(host='localhost',user='root',password=password,database='BANK_MANAGEMENT_SYSTEM')
    cur = conn.cursor()
    query = "SELECT * FROM accinfo WHERE ACCOUNT_NUMBER = %s and ACCOUNT_PIN = %s;"
    cur.execute(query, (inaccno, inpin))
    result = cur.fetchone()
    if result:
            if result[0] == inaccno and result[1] == inpin:
                decorator = "-"
                print(decorator.center(105,'-'))
                print("Access Granted...!")
                print(decorator.center(105,'-'))
            else:
                decorator = "-"
                print(decorator.center(105,'-'))
                print("Invalid Account Name Or Password!")
                print(decorator.center(105,'-'))
                exit()   
    else:
        decorator = "-"
        print(decorator.center(105,'-'))
        print("Account Doesn't Exist! Create One!")
        print(decorator.center(105,'-'))
        conn.commit()
        cur.close()
        conn.close()
        exit()

def acccreate(newaccno,newpin,holdername,dob,phno,email,typeofacc): 
    conn = sql.connect(host='localhost',user='root',password=password,database='BANK_MANAGEMENT_SYSTEM')
    cur = conn.cursor()
    query1 = "SELECT * FROM accinfo WHERE ACCOUNT_NUMBER = %s and ACCOUNT_PIN = %s;"
    cur.execute(query1, (newaccno, newpin))
    result = cur.fetchone()
    if result:
         decorator = "-"
         print(decorator.center(105,'-'))
         print("Account Already Exists!")
         print(decorator.center(105,'-'))
    else:
        query2 = "INSERT INTO accinfo (ACCOUNT_NUMBER, ACCOUNT_PIN, NAME_OF_ACCOUNT_HOLDER, DOB, Phone_Number, EMAIL_ID, TYPE_OF_ACCOUNT) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        cur.execute(query2, (newaccno, newpin, holdername, dob, phno, email, typeofacc))
        decorator = "-"
        print(decorator.center(105,'-'))
        print("Account Created Successfully")
        print(decorator.center(105,'-'))   
    conn.commit()
    cur.close()
    conn.close()

def acctable(inaccno):
    conn = sql.connect(host='localhost',user='root',password=password,database='BANK_MANAGEMENT_SYSTEM')
    cur = conn.cursor()
    try:
        cur.execute(f"CREATE TABLE `{inaccno}` (DATE_TIME DATETIME DEFAULT CURRENT_TIMESTAMP, DEPOSITS INT, WITHDRAWALS INT, BALANCE INT DEFAULT 0);")
    except sql.Error as e:
        print(f"Error creating table: {e}")
    finally:
        cur.close()
        conn.close()

def Deposited(inaccno,deposits,balance,withdrawals=0):
    conn = sql.connect(host='localhost',user='root',password=password,database='BANK_MANAGEMENT_SYSTEM')
    cur = conn.cursor()
    cur.execute(f"INSERT INTO `{inaccno}` (DEPOSITS,WITHDRAWALS,BALANCE) VALUES ({deposits},{withdrawals},{balance})")
    conn.commit()
    cur.close()
    conn.close()

def Withdrawn(inaccno,withdrawals,balance,deposits=0):
    conn = sql.connect(host='localhost',user='root',password=password,database='BANK_MANAGEMENT_SYSTEM')
    cur = conn.cursor()
    cur.execute(f"INSERT INTO `{inaccno}` (DEPOSITS,WITHDRAWALS,BALANCE) VALUES ({deposits},{withdrawals},{balance})")
    conn.commit()
    cur.close()
    conn.close()

def AvailBalance(inaccno):
    if inaccno is None:
        print("Account number is not set.")
        return 0
    conn = sql.connect(host='localhost',user='root',password=password,database='BANK_MANAGEMENT_SYSTEM')
    cur = conn.cursor()
    cur.execute(f"SELECT * FROM `{inaccno}` ORDER BY DATE_TIME DESC LIMIT 1;")
    row = cur.fetchone()
    
    if row:
        return int(row[3])
    else:
        return 0
        
balance = 0
inaccno = None

def Account():
    global inaccno
    decorator = "-"
    print(decorator.center(105,'-'))
    print("Welcome!")
    print(decorator.center(105,'-'))        
    accask = input("If You Have An Existing Account, Press(1), If Not, Press(2) To Create One: ")
    if accask == "1":
        inaccno = int(input('Enter Your Account Number: '))
        inpin = int(input("Enter Your 4 Digit MPin : "))
        accaccess(inaccno,inpin)
        global balance
        balance = AvailBalance(inaccno) 
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
    
        holdername = input('Enter Name of the Holder: ')
        dob = int(input('Enter Your Date Of Birth: '))
        phno = int(input('Enter Your Phone Number: '))
        email = input('Enter Your Email ID: ')
        typeofacc = input('What Type Of Account Do You Want "SAVINGS" OR "DEMAT"?: ')
        print(decorator.center(105,'-'))
        print()
        n = '1234567890'
        accno = ''
        for i in range(12):
            accno += random.choice(n)
        
        print("Generating A New Account Number...")
        
        newaccno = int(accno)
        decorator = "-"
        print(decorator.center(105,'-'))    
        print('Your Account Number Has Been Successfully Generated...')
        print(decorator.center(105,'-'))    
        print('Your Account Number Is:',newaccno)
        newpin = int(input("Create New 4 Digit MPin To Keep Your Account Secure: "))
        if len(str(newpin))!=4:
            print('Enter 4 Digit Pin Only...')
            exit()
        acccreate(newaccno,newpin,holdername,dob,phno,email,typeofacc)
        acctable(newaccno)
        
        inaccno = newaccno
        balance = 0
        while True:
            AccTask()
            sp = input("To Open Task Menu Again Press(1), Else To Exit Press(2) : ")
            if sp == "1":
                pass
            if sp == "2":
                break
        
        
def Deposit():
    global balance
    global inaccno
    deposits = int(input("Enter the amount to be deposited: "))
    if deposits < 0:
            print("Cannot deposit a negative amount!")
    elif deposits > 10000000:
        print("The Transaction Limit is up to ₹1,00,00,000/-")
    else:
        balance += deposits
        print(f"Balance: {balance}")
        Deposited(inaccno,deposits,balance,withdrawals=0)

def Withdraw():
    global balance
    global inaccno
    withdrawals = int(input("Enter the amount to be withdrawn: "))
    if withdrawals < 0:
            print("Cannot withdraw a negative amount.")
    elif balance <= 0:
        print("Balance = 0 , Zero Balance, Account is empty!")
    elif withdrawals > balance:
        print(f"Insufficient Balance!")
    elif withdrawals > 10000000:
        print("The Transaction Limit is up to ₹1,00,00,000/-")
    else:
        balance -= withdrawals
        print(f"Balance: {balance}")
        Withdrawn(inaccno,withdrawals,balance,deposits=0)
        
def Balance():
    
    print(f"Your Account Balance is: {AvailBalance(inaccno)}")

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