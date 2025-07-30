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



