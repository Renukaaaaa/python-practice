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



