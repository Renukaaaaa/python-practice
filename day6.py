#1 to 10 number using while
i=1
while(i<=10):
    print("The number is",i)
    i=i+1

#print each character of string
language=input("Enter the language name:")
print("Selected language is:")
for i in language:
    print("char from string is:",i)

#sum of first n number
num=int(input("Enter the number:"))
sum=0
for n in range(1,num+1):
    sum=sum+n
print(sum)

#multiplication table
num=int(input("Enter the number:"))
for i in range(1,11):
    print(num,"*",i,"=",num*i)

#even number skipper
for i in range(1,11):
    if i%2==0:
        continue
    print(i)

#reverse countdown timer
n=int(input("Enter the number:"))
for i in range(n,0,-1):
    print(i)


#break the loop on password match
correct_password="python123"
while True:
    passowrd=input("enter the password:")
    if passowrd==correct_password:
        print("Access granted")
        break
    else:
        print("Access deined")

#count vowels in word
str=input("Enter the word:")
vowels="aeiouAEIOU"
count=0
for w in str:
    if w in vowels:
        count+=1
print("No of vowels are:",count)

#odd number between 1 to 50
for i in range(0,50):
    if(i%2!=0):
        print("odd number",i)
    else:
        continue

#factorial calculator
num=int(input("Enter the number:"))
fact=1
for n in range(1,num+1):
    fact*=n
print("factorial of",num,"is:",fact)




