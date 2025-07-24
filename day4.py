#arithmetic operators
a=int(input("enter 1 no="))
b=int(input("enter 2 no="))
print("a+b=",a+b)
print("a-b=",a-b)
print("a*b=",a*b)
print("a/b=",a/b)
print("a//b=",a//b)    #nearest rounded number
print("a%b=",a%b)
print("a**b=",a**b)     #raise to

#comparison operators
print("a==b=",a==b)
print("a>b=",a>b)
print("a<b=",a<b)
print("a>=b=",a>=b)
print("a<=b=",a<=b)
print("a!=b=",a!=b)

#assignment operators
p=7
print(p,"After assign")
p+=1                             
print(p,"afetr p+=1")
p-=1                             
print(p,"afetr p-=1")
p*=1                             
print(p,"afetr p*=1")
p/=1                             
print(p,"afetr p/=1")
p//=3                            
print(p,"afetr p//=1")
p**=2                            
print(p,"afetr p**=1")

#logical operators
print(6>4 and 4<2)           #false
age=20
nationality='Indian'
isIndian=True
print(age>18 and nationality =='Indian')         #true
print(age>10 or isIndian)                         #true
print(not isIndian)                               #false

#bitwise operators
q=5
r=3
print(q & r)
print(q | r)
print(q^r)
print(~q)
print(q<<r)
print(q>>r)

#membership operators
str='python'
print('y' in str)               #true
print('m' not in str)           #true

#identity operators
m=34
n=5
print(m is n)                  #false
print(m is not n)               #true