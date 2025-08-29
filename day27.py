#Assignment 1
import sqlite3
conn=sqlite3.connect("student.db")

cursor=conn.cursor()
print("Database connected successfully...")

cursor.execute("""CREATE TABLE IF NOT EXISTS student(id INTEGER PRIMARY KEY AUTOINCREMENT,name TEXT NOT NULL,age integer,grade text)""")
print("Table created successfully")

cursor.execute("""INSERT INTO student (name,age,grade)VALUES("renu",20,"A+"),
               ("Payal",23,"B+"),
               ("Divya",22,"C"),
               ("Aryan",30,"B"),
               ("Pragati",24,"A")""")
conn.commit()
print("record inserted successfully")



#Assignment 2
cursor.execute("SELECT name,grade FROM student")
rows=cursor.fetchall()
for row in rows:
    print(row)



#Assignment 3
cursor.execute("update student set grade=? where id=?",("A+",2))
conn.commit()



#Assignment 4
cursor.execute("delete from student where age>25")
conn.commit()


#Assignment 5
try:
    cursor.execute("insert into student(name,age)values(?,?)",("Renuka",25))
    conn.commit()
except Exception as e:
    print("Error",e)


#Assignment 6
def getStudentByGrade(grade):
    conn=sqlite3.connect("student.db")
    cursor=conn.cursor()
    cursor.execute("Select * from student where grade=?",(grade,))
    rows=cursor.fetchall()
    conn.close()
    return rows

print("students with grade A:")
for student in getStudentByGrade("A"):
    print(student)


#Assignment 7
conn=sqlite3.connect("bank.db")
cursor=conn.cursor()
cursor.execute("""create table if not exists accounts(
               account_no integer primary key autoincrement,name text not null,balance integer)
""")
def insertAccount(name,balance):
    cursor.execute("insert into accounts(name,balance)values(?,?)",(name,balance))
    conn.commit()
    print("Account created successfully")

def deposit(account_no,amount):
    cursor.execute("Update accounts set balance=balance + ? where account_no=?",(amount,account_no))
    conn.commit()
    print("Deposit successfully")

def withdraw(account_no,amount):
    cursor.execute("select balance from accounts where account_no=?",(account_no,))
    bal=cursor.fetchone()
    if bal and bal[0]>=amount:
        cursor.execute("update accounts set balance=balance-? where account_no=?",(amount,account_no))
        conn.commit()
        print("Withdraw successfully")
    else:
        print("Insufficient balance")

def deleteAccount(account_no):
    cursor.execute("delete from accounts where account_no=?",(account_no,))
    conn.commit()
    print("Account deleted")

insertAccount("Renuka",1000)
insertAccount("Riya",2000)
deposit(1,200)
withdraw(2,100)
deleteAccount(2)
conn.close()