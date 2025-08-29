#Assignment 1
import sqlite3
conn=sqlite3.connect("library.db")

cursor=conn.cursor()
print("Database connected successfully...")

cursor.execute("""CREATE TABLE IF NOT EXISTS books(id INTEGER PRIMARY KEY AUTOINCREMENT,title TEXT NOT NULL,author TEXT,year INTEGER)""")
print("Table created successfully")


#Assignment 2
cursor.execute("""INSERT INTO books (title,author,year)VALUES("agnipankh","APJ abdul kalam",1996),
               ("Python programming","john smith",2014),
               ("Data science","Jane doe",2020),
               ("AI basics","Mark lee",1767),
               ("Databse system","Alan turing",1767)""")
conn.commit()
print("record inserted successfully")



#Assignment 3
cursor.execute("SELECT * FROM books")
rows=cursor.fetchall()
for row in rows:
    print(row)


#Assignment 4
cursor.execute("SELECT * from books where year>2015")
rows=cursor.fetchall()
for row in rows:
    print(row)


#Assignment 5
cursor.execute("UPDATE books set title=? where id=?",("Data science advanced",114))
conn.commit()


#Assignment 6
cursor.execute("DELETE from books where id=?",(101,))
conn.commit()


#Assignment 7
def addBook():
    title=input("Enter book name:")
    author=input("Enter author name:")
    year=int(input("Enter year:"))
    cursor.execute("insert into books(title,author,year)values(?,?,?)",(title,author,year))
    conn.commit()
    print("Books added successfully")

def viewBook():
    cursor.execute("select * from books")
    for row in cursor.fetchall():
        print(row)

def searchByAuthor():
    name=input("Enter author name:")
    cursor.execute("select * from books where author like ?",('%'+name+'%',))
    result=cursor.fetchall()
    if result:
        for row in result:
            print(row)
    else:
        print("no books found")

while True:
    print("******LIBRARY MENU******")
    print("1.Add book")
    print("2.view all books")
    print("3.Search book by author")
    print("4.exit")

    choice=input("Enter choice:")
    if choice=="1":
        addBook()
    elif choice=="2":
        viewBook()
    elif choice=="3":
        searchByAuthor()
    elif choice=="4":
        print("Exiting...")
        break
    else:
        print("Enter valid choice")
        
conn.close()