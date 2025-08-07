#students marks entry system
def enter_marks():
    try:
        marks=int(input("enter the marks:"))
        if(marks<0 or marks>100):
            raise ValueError("Marks must be in between 0 to 100")
        print("Marks eneterd:",marks)
    except ValueError as e:
        print("Invalid input",e)
    finally:
        print("entry process completed")
enter_marks()

#ATM withdraw simulation
try:
    balance=6000
    amount=int(input("Enter the amount:"))
    if(amount<0):
        raise ValueError("amount must be greater than 0")
    if(amount>balance):
        print("insufficient balance")
    balance-=amount
    print("withdraw successfully")
    print("remaining balance",balance)
except ValueError as e:
    print("error",e)
finally:
    print("This is end of transaction")

#safe division calculator
def safe_division():
    try:
        num1=int(input("enter first number:"))
        num2=int(input("Enter second number:"))
        result=num1/num2
        print("Division:",result)
    except ZeroDivisionError:
        print("Number cannot be divide by zero")
    except ValueError:
        print("please provide correct value")
    finally:
        print("This is end of safe division")
safe_division()


#file reader with exception
def open_file():
    try:
        f=open('1.py','r')
        contetnt=f.read()
        print("content of file:",contetnt)
    except FileNotFoundError:
        print("file not found")
    finally:
        print("End of file")
open_file()

#students mark entry
def enter_marks():
    try:
        marks=int(input("enter the marks:"))
        print("Marks:",marks)
    except ValueError:
        print("Invalid marks")
enter_marks()

#login attempt checker
username={'renu':10,'seema':20,'meena':30}
new_user=input("enter the username:")
try:
    print("username has value is:",username[new_user])
except KeyError:
    print("username not present")

#list index access
lst=[2,4,5,9]
try:
    i=int(input("index:"))
    print("value:",lst[i])
except IndexError:
    print("Invalid index")

    
#division with finally block
def division1():
    try:
        num1=int(input("enter first number:"))
        num2=int(input("Enter second number:"))
        result=num1/num2
        print("Division:",result)  
    except ZeroDivisionError:
        print("cant divide by zero")
    finally:
        print("Thank u for using calculator")
division1()
