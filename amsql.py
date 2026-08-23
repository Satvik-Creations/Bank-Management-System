import mysql.connector as sql
from getpass import getpass

print("-" * 45)
sql_password = getpass("Enter your MySQL Password: ")
print("-" * 45)

def accaccess(inaccname,inpass):
    conn = sql.connect(host='localhost',user='root',password=sql_password,database='account_manager')
    cur = conn.cursor()
    query = "SELECT * FROM accinfo WHERE acc_name = %s AND acc_pass = %s;"
    cur.execute(query, (inaccname, inpass))
    result = cur.fetchone()
    if result:
            if result[0] == inaccname and result[1] == inpass:
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

def acccreate(newaccname,newpass): 
    conn = sql.connect(host='localhost',user='root',password=sql_password,database='account_manager')
    cur = conn.cursor()
    query1 = "SELECT * FROM accinfo WHERE acc_name = %s AND acc_pass = %s;"
    cur.execute(query1, (newaccname, newpass))
    result = cur.fetchone()
    if result:
         decorator = "-"
         print(decorator.center(105,'-'))
         print("Account Already Exists!")
         print(decorator.center(105,'-'))
    else:
        query2 = "INSERT INTO accinfo (acc_name, acc_pass) VALUES (%s, %s)"
        cur.execute(query2, (newaccname, newpass))
        decorator = "-"
        print(decorator.center(105,'-'))
        print("Account Created Successfully")
        print(decorator.center(105,'-'))   
    conn.commit()
    cur.close()
    conn.close()

def acctable(inaccname):
    conn = sql.connect(host='localhost',user='root',password=sql_password,database='account_manager')
    cur = conn.cursor()
    cur.execute(f"CREATE TABLE {inaccname} (DATE_TIME DATETIME DEFAULT CURRENT_TIMESTAMP, DEPOSITS INT, WITHDRAWALS INT, BALANCE INT DEFAULT 0);")
    cur.close()
    conn.close()

def Deposited(inaccname,deposits,balance,withdrawals=0):
    conn = sql.connect(host='localhost',user='root',password=sql_password,database='account_manager')
    cur = conn.cursor()
    cur.execute(f"INSERT INTO {inaccname} (DEPOSITS,WITHDRAWALS,BALANCE) VALUES ({deposits},{withdrawals},{balance})")
    conn.commit()
    cur.close()
    conn.close()

def Withdrawn(inaccname,withdrawals,balance,deposits=0):
    conn = sql.connect(host='localhost',user='root',password=sql_password,database='account_manager')
    cur = conn.cursor()
    cur.execute(f"INSERT INTO {inaccname} (DEPOSITS,WITHDRAWALS,BALANCE) VALUES ({deposits},{withdrawals},{balance})")
    conn.commit()
    cur.close()
    conn.close()

# def Balance(inaccname):
#     conn = sql.connect(host='localhost',user='root',password=sql_password,database='account_manager')
#     cur = conn.cursor()
#     cur.execute(f"SELECT * FROM {inaccname} ORDER BY DATE_TIME DESC LIMIT 1;")
#     for row in cur:
#         return int(row[3])
