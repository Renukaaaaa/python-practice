import json

#assignment 1
with open("demo 25.txt",'r')as f:
    for line in f:
        if 'python' in line:
            print(line.strip())


#Assignment 2
fruits=['apple','banana','mango','pineapple','orange']
with open("fruits.txt",'r')as f1:
    for fruit in fruits:
        print(fruit+"\n")

with open("fruits.txt",'r')as f2:
    print(f2.read())


#Assignment 3
dictEmp={"name":"renu","ID":1001,"dept":"computer"}
with open("employee.json",'w')as f3:
    json.dump(dictEmp,f3)

with open("employee.json",'r')as f4:
    data=json.load(f4)
print(data)


#Assignment 4
with open("story.txt",'r')as f5:
    text=f5.read()
lines=text.splitlines()
words=text.split()
characters=len(text)
print("Lines:",len(lines))
print("Words:",len(words))
print("Characters:",characters)


#Assignment 5
quotes=["Do what you can, with what you have, where you are.",
        "Happiness is not something ready-made. It comes from your own actions.",
        "In the middle of every difficulty lies opportunity.",
        "The best way to predict the future is to create it.",
        "Don’t count the days, make the days count."
        ]
with open("quotes.txt",'a')as f6:
    for q in quotes:
        f6.write(q+"\n")


#Assignment 6
grades={"alice":90,"bob":40,"charlie":79}
with open("grades.txt",'w')as f7:
    for name,grade in grades.items():
        f7.write(f"{name} : {grade}\n")
with open("grades.txt",'r')as f8:
    print(f8.read())



#assignment 7
with open("bigfile.txt",'r')as f9:
    for i in range(10):
        line=f9.readline()
        if not line:
            break
        print(line.strip())