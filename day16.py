#bank account withdrawal
class Bank:
    def __init__(self,balance):
        self.balance=balance
    def withdraw(self,amount):
        if(amount>self.balance):
            raise ValueError("Insufficient balance")
        self.balance-=amount
        return self.balance
    def deposit(self,amount):
        if(amount<0):
            raise ValueError("Invalid amount")
        self.balance=self.balance+amount
        return self.balance
acc=Bank(5000)
print(acc.withdraw(1000))
try:
    acc.deposit(20000)
    acc.withdraw(6000)
    acc.deposit(-547)
except ValueError as e:
    print("transaction failed",e)
finally:
    print("Thank you...!")


#Age validator in class
class person:
    def __init__(self,name):
        self.name=name
    def setAge(self,age):
        if(0>age<100):
            raise ValueError("Please enter correct age")
        self.age=age
    def getInfo(self):
        return f"your name is {self.name}, age is {self.age}"
p=person("renuka")
try:
    p.setAge(9)
    print(p.getInfo())
except ValueError as e:
    print("error",e)


#student grade input
class student:
    def __init__(self,name,grade):
        for sub,marks in grade.items():
            if not(0<=marks<=100):
                raise ValueError(f"Invalid mark for {sub}:{marks}")
        self.name=name
        self.grade=grade
try:
    s=student("Renuka",{"math":56,"sci":90})
except ValueError as e:
    print("Error",e)


#file reader class with exception handling
class FileReader:
    def readFile(self,filename):
        try:
            with open(filename,'r')as file:
                print(file.read())
        except FileNotFoundError:
            print("File doesnt found...")
reader=FileReader()
reader.readFile('1.py')


#password validator
class user:
    def set_password(self,pwd):
        if len(pwd)<8 or not any(ch.isdigit()for ch in pwd):
            raise ValueError("password must be of 8 letters and contain at least one digit")
        return "valid password"
try:
    password=input("Enter password:")
    u=user()
    print(u.set_password(password))
except ValueError as e:
    print("error",e)
            

#temprature convertor
class temprature:
    def __init__(self,c):
        if(c<-273.15):
            raise ValueError("Below absolute zero")
        self.c=c
    def conversion(self):
        return(self.c*9/5)+32
try:
    t=temprature(float(input("Enter temp in c:")))
    print("Fahreneit:",t.conversion())
except ValueError as e:
    print("error",e)
    

#shopping cart
class shoppingCart:
    def __init__(self,stock):
        self.stock=stock
    def add(self,qty):
        if(qty>self.stock):
            raise ValueError("Exceeds quantity")
        return "quantity added"
try:
    print(shoppingCart(10).add(int(input("enter qty:"))))
except ValueError as e:
    print("error",e)


#exam hall
class examHall:
    def __init__(self,cap):
        self.cap=cap
    def allocate(self,n):
        if(n>self.cap):
            raise ValueError("Limit exceeds...")
        return "students added"
try:
    print(examHall(40).allocate(int(input("Enter students no:"))))
except ValueError as e:
    print("Error",e)


#flight booking
class flightBooking:
    def __init__(self,name,age):
        if(age<0 or age>100):
            raise ValueError("invalid age")
        self.name=name
        self.age=age
    def info(self):
        return f"name:{self.name},age:{self.age}"
try:
    b=flightBooking(input("Name:"),int(input("age:")))
    print(b.info())
except ValueError as e:
    print("error",e)