#number iz positive,negative or zero
num=int(input("enter the number:"))
if(num>0):
    print("positive")
elif(num<0):
    print("negative")
else:
    print("zero")

#driving eligibility
age=76
if(age>=18):
    print("Eligible to drive")
else:
    print("you are not eligible to drive")

#grading system
marks=int(input("Enter the marks:"))
if(marks>90):
    print("Grade A")
elif(marks>75 and marks<=89):
    print("Grade B")
elif(marks>60 and marks<=74):
    print("Grade C")
elif(marks<60):
    print("failed")

#nested login check
is_logged_in=True
is_admin=False
if(is_logged_in==True and is_admin==True):
    print("Welcome admin")
elif(is_logged_in==True and not is_admin==False):
    print("Welcome user")
else:
    print("please log in")

#largest of 3 numbers
num1=int(input("Enter the first number:"))
num2=int(input("Enter the second number:"))
num3=int(input("Enter the third number:"))
if(num1>num2 and num1>num3):
    print("num1 is greater")
elif(num2>num3 and num2>num3):
    print("num2 is greater")
else:
    print("Num3 is greater")

#number is even or odd
number=int(input("enter the number:"))
if(number%2==0):
    print("number is even")
else:
    print("number is odd")       

#password validator
password='admin123'
new_password=(input("Enter the passowrd:"))
if(new_password==password):
    print("Access granted")
else:
    print("Access deined")

#leap year checker
year=int(input("Enter the year:"))
if(year%4==0 and year%100!=0) or (year%400==0):
    print(year,"is leap year")
else:
    print(year,"is not leap year")

#temprature convertor
temp=float(input("Enter temprature:"))
u=input("Enter unit:(C/F)")
if(u=='C'):
    print(temp*9/5+32,"F")
elif(u=='F'):
    print((temp-32)*5/9,"C")
else:
    print("invalid")
