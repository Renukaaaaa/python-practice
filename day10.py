#capitalize user names
username=['john','alice','bob']
capital=list(map(lambda u:u.capitalize(),username))
print("original usernames:",username)
print("Usernames in capital:",capital)

#filter valid email address
emails=['abc@gmail.com','xyz@yahoo.com','admin@gmail.com']
output=list(filter(lambda e:e.endswith('@gmail.com'),emails))
print("Original emails:",emails)
print("Valid email address:",output)

#calculate final price after discount
prices=[100,200,300]
output=list(map(lambda p:p*0.9,prices))
print("Original prices:",prices)
print("prices after 10% discount:",output)

#get full names of employees
employees=[('john','doe'),('alice','smith')]
output=list(map(lambda emp:emp[0]+'  '+emp[1],employees))
print("Original employee names:",employees)
print("full names of employees:",output)

#find product above rs1000
price=[850,1000,999,1600]
output=list(filter(lambda p:p>1000,price))
print("original prices:",price)
print("Price >1000",output)

#Total marks of students
from functools import reduce
marks=[78,85,90,88]
total_marks=reduce(lambda a,b:a+b,marks)
print("original marks:",marks)
print("sum of marks:",total_marks)

#sort list of student by age
students=[{'name':"Meera",'age':30},{'name':"Radha",'age':22}]
output=sorted(students,key=lambda key:key['age'])
print("original students:",students)
print("student sorted by age:",output)