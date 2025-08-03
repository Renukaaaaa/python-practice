#display teacher name
def greet_teacher(name):
    print("English is teached by",name)
greet_teacher("R.A.Patil")

#multiplication
def multiply(a,b):
    return(a*b)
m=multiply(20,4)
print("multiplication:",m)

#total price after tax
def total_tax(price,tax_rate):
    tax=price*tax_rate/100
    total_price=price+tax
    return total_price
t=total_tax(100,30)
print(t)

#employee details
def employee_details(id,name,salary):
    print("employee Id:",id,"employee name:",name,"employee salary:",salary)
employee_details(1001,"renuka",50000)

#convert celcius to fahrenheit
def conversion():
    temp=float(input("Enter temprature in celcius:"))
    print("temprature in fahrenheit:",temp*9/5+32)
conversion()

#square of number
def square(num):
    return(num*num)
s=square(3)
print("Square of no:",s)

#calculate simple interest
def simple_intrest(p,r,t):
    return(p*r*t)/100
print(simple_intrest(3000,4,9))

#Birthday message
def birthday(name,age):
    print("happy birthday",name,"you have completed journey of ",age,"years")
birthday("renuka",20)

#split bill among friends
def split_bills(total_amount,no_of_friends):
    if no_of_friends==0:
        print("bill cannot be slit in 0 students")
    share=total_amount/no_of_friends
    print("each student have to pay rs",share)
print(split_bills(1000,5))

#convert hours into minute and seconds
def conversion(hours):
    minutes=hours*60
    seconds=hours*3600
    print("hours:",hours,"minutes:",minutes,"seconds:",seconds)
conversion(3)
