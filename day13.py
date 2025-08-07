#person class with name and age
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def displayData(self):
        print("person name:",self.name)
        print("person age:",self.age)
p1=Person("Renuka",20)
print("details of person1:",p1.displayData())
p2=Person("Pragati",25)
print("details of person2:",p2.displayData())

#car details
class Car:
    def __init__(self,brand,model,year):
        self.brand=brand
        self.model=model
        self.year=year
    def carDetails(self):
        print("Car brand:",self.brand)
        print("Car model:",self.model)
        print("Car year:",self.year)
c=Car('Thar','Tata',2001)
print("car details:",c.carDetails())
 
#product details
class Product:
    def __init__(self,name,price):
        self.name=name
        self.price=price
    def getDetails(self):
        print("Product name:",self.name)
        print("Product price:",self.price)
p1=Product("T-shirt",500)
print("Product1:",p1.getDetails())
p2=Product("Jeans",1000)
print("Product2:",p2.getDetails())

#calculate area of circle
class Circle:
    def __init__(self,radius):
        self.radius=radius
    def calculateArea(self):
        print("Area of circle:",self.radius*self.radius)
c=Circle(24)
print(c.calculateArea())

#fruits category


#movies details
class Movie:
    def __init__(self,title,rating,genre):
        self.title=title
        self.rating=rating
        self.genre=genre
    def movieDetails(self):
        print("movie title:",self.title)
        print("movie rating:",self.rating)
        print("movie genre:",self.genre)
m=Movie('12th fail','5star','Drama')
print("Movie details:",m.movieDetails())

#laptop price comparison
class Laptop:
    def __init__(self,brand,ram,price):
        self.brand=brand
        self.ram=ram
        self.price=price
    def laptopDetails(self):
        print("Lpatop brand:",self.brand)
        print("Lpatop Ram:",self.ram)
        print("Lpatop Price:",self.price)
l1=Laptop("HP",8,70000)
print("Laptop1:",l1.laptopDetails())
l2=Laptop("Dell",16,80000)
print("Laptop2:",l2.laptopDetails())
if(l1.price<l2.price):
    print("Laptop1 is cheaper")
else:
    print("Laptop2 is cheapar")

#employee details
class Employee:
    def __init__(self,name,position,salary):
        self.name=name
        self.position=position
        self.salary=salary
    def give_raise(self,amount):
        self.salary+=amount
    def EmployeeDetails(self):
        print("Employee name:",self.name)
        print("Employee position:",self.position)
        print("Employee salary:",self.salary)
e=Employee("renuka","project manager",50000)
print("Employee details:",e.EmployeeDetails())
e.give_raise(5000)
print("after raise:",e.EmployeeDetails())

#bank details
class BankAccount:
    def __init__(self,balance):
        self.balance=balance
    def deposit(self,amount):
        self.balance+=amount
        print("Deposited amount",self.balance)
    def withdraw(self,amount):
        if(amount>self.balance):
            print("insufficient balance")
        else:
            self.balance-=amount
            print("remaining balance",self.balance)
    def display(self):
        print("Account balance:",self.balance)
b=BankAccount(10000)
b.deposit(2000)
b.withdraw(5000)
b.withdraw(9000)