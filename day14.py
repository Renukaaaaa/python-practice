#inheritance
class vehicle:
    def start_engine(self):
        print("engine starts...")
class bike(vehicle):
    def start_engine(self):
        print("bike rides")
class car(vehicle):
    def start_engine(self):
        print("car drives")
c=car()
c.start_engine()
b=bike()
b.start_engine()


#inheritance
class shape:
    def area(self):
        print("Area calculation")
class circle(shape):
    def area(self,radius):
        self.radius=radius
        print("area of circle:",radius*radius)
class rectangle(shape):
    def area(self,length,breadth):
        self.length=length
        self.breadth=breadth
        print("Area of rectangle:",length*breadth)
c=circle()
r=rectangle()
print(c.area(5))
print(r.area(10,5))


#encapsulation 
class bankaccount:
    def __init__(self):
        self.balance=0
    def depositAmount(self,amount):
        self.balance+=amount
        print("deposited:",amount,"balance:",self.balance)
    def withdrawAmount(self,amount):
        if(amount<self.balance):
            self.balance-=amount
            print("withdraw:",amount,"balance:",self.balance)
        else:
            print("Insufficent balance")
acc=bankaccount()
acc.depositAmount(500)
acc.withdrawAmount(300)
acc.withdrawAmount(2000)


#abstraction
from abc import ABC,abstractmethod
class Appliance(ABC):
    @abstractmethod
    def turn_on(self):
        pass
    def turn_off(self):
        pass
class fan(Appliance):
    def turn_on(self):
        print("fan started...")
    def turn_off(self):
        print("fan stops...")
class light(Appliance):
    def turn_on(self):
        print("light gets on...")
    def turn_off(self):
        print("light gets off...")
f=fan()
l=light()
print("FAN:",f.turn_on(),f.turn_off())
print("LIGHT:",l.turn_on(),l.turn_off())


#polymorphism
class principal:
    def speak(self):
        print("Principal speaks about college,teachers and students all...")
class teacher(principal):
    def speak(self):
        print("Teacher speaks about subject and students...")    
class student(principal):
    def speak(self):
        print("Sutdents speaks about justice...")
t=teacher()
print("Teacher:",t.speak())
s=student()
print("student",s.speak())    


#inheritance
class employee:
    def work(self):
        print("employee is working...")
class manager(employee):
    def work(self):
        print("Manager is managing the team")
class director(employee):
    def work(self):
        print("Director is setting company goal")
e=employee()
print(e.work())
m=manager()
print(m.work())
d=director()
print(d.work())


#getter & setter method
class person:
    def __init__(self,age):
        self.age=age
    def getAge(self):
        return self.age
    def setAge(self,age):
        if(age>0):
            self.age=age
        else:
            print("Invalid age")
p=person(25)
print("Age:",p.getAge())
p.setAge(30)
print("Updated age:",p.getAge())