#shopping cart
cart={
    "apple":3,
    "banana":7,
    "pineapple":4,
    "milk":9
}
price={
    "apple":20,
    "banana":45,
    "pineapple":46,
    "milk":90
}
total=0
for index,value in cart.items():
   print(index,"***",value) 
   print(price[index])
   total=total+price[index]*value
print("total:",total)

#students names with grades
students={
   "renuka":'A',
   "bhakti":'B',
   "seema":'c'
}
for name,grade in students.items():
   print(name,"has grade",grade)

#numbered survey result
response=['yes','no','maybe','not fixed yet']
for index,response in enumerate(response):
   print(index,"***",response)

#attendence checker
present=['meena','seema','renuka','renu','ankita']
for student in present:
   print(student,"is present")

#unique cities visited
cities={"nagpur","pune","mumbai","delhi","pune"}
for c in cities:
   print("India has",c,"city")

print("***PRACTICE ASSIGNMENT***")

#loop through tuple
movies=("Vivegam","Raid 2","genius","12th fail","chaava")
for m in movies:
   print("movie name:",m)

#enumerate with list
fruits=['apple','banana','pineapple','orange']
for index,value in enumerate(fruits):
   print(index,"fruit is",value)

#use items() on dictionary
student={
   "renuka":'A',
   "bhakti":'B',
   "sai":'C'
}
for key,value in student.items():
   print(key,"has grade",value)

#use values() on dictionary
countries={
   "Australia":'Canberra',
   "Egypt":'Cairo',
   "Japan":'Tokyo',
   "Bangladesh":'Dhaka'
}
for c in countries.values():
   print("Capitals are:",c)

#loop through set
animals={'fox','tiger','lion','elephant','fox'}
for a in animals:
   print("Animal is:",a)

#loop through dictionary keys only
products={
   "pen":'20',
   "notebook":'40',
   "Eraser":'10'
}
for p in products.keys():
   print("product names are:",p)

#loop thorugh range to generate even numbers
for i in range(0,20,2):
   print("Even number is:",i)

#loop through nested dictionary
student={
   "Renuka":{"age":20,"grade":'A'},
   "Nikita":{"age":23,"grade":'B'},
   "Pavan":{"age":24,"grade":'C'}
}
for name,details in student.items():
   print("student",name,"has grade",details['grade'])




#loop through string
language=input("Enter your favourite language:")
for l in language:
   print("character from string is:",l)

#use enumerate() to build menu
menu=['pizza','burger','pasta','salad']
for index,value in enumerate(menu):
   print(index,"number has menu",value)