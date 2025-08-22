#set operations
set1={2,4,6,8,3,5}
set2={2,8,9,7}
print("Student in set1:",set1)
print("Student in set2:",set2)
print("student only in set1",set1.difference(set2))
print("unique students:",set1.union(set2))


#dictionary phonebook
phonebook={
    'renu':1928736363,
    'pragati':5283829192,
    'seema':6542313131
}
for key,value in phonebook.items():
    print(f"student {key} has mobile number {value}")
phonebook['neeta']=7654325343
print("After add new item:")
for key,value in phonebook.items():
    print(f"student {key} has mobile number {value}")
phonebook['seema']=9898767654
print("After update for seema item:")
for key,value in phonebook.items():
    print(f"student {key} has mobile number {value}")
phonebook.pop('seema')
for key in phonebook.keys():
    print(key)
name='neeta'
if name in phonebook:
    print("neeta:",phonebook[name])
else:
    print("name not found in dictionary")


#calculator with dictionary
n1=int(input("First number:"))
n2=int(input("Second number:"))
op=input("Enter operation:")
calculator={
    'add':n1+n2,
    'sub':n1-n2,
    'mul':n1*n2,
    'div':n1/n2 if n1!=0 else "division by zero"
}
if op in calculator:
    print("Result:",calculator[op])
else:
    print("Invalid operation")


#word frequency
text=input("Enter paragraph:").lower().split()
freq={}
for word in text:
    if word in freq:
        freq[word]+=1
    else:
        freq[word]=1
sorted_freq=sorted(freq.items(),key=lambda x:x[1],reverse=True)
for word,count in sorted_freq:
    print(word,":",count)


#country capitals
capitals={
    'india':'new delhi',
    'USA':'washington D.C',
    'france':'paris',
    'japan':'tokyo',
    'germeny':'berlin'
}
country=input("enter country name:")
if country in capitals:
    print("capital:",capitals[country])
else:
    print("not found")


#set operations on friends
my_friends={'neeta','seema','vanita','sakshi','pragati'}
your_friends={'sunil','atul','sujit','omkar','akash','sakshi','pragati'}
print("My friends:",my_friends)
print("your friends:",your_friends)
print("Friends in both sets:",my_friends.union(your_friends))
print("friends only i have:",my_friends.difference(your_friends))
print("friends only they have:",your_friends.difference(my_friends))


#menu system with dictionary
items=[]
while True:
    print("1-Add item")
    print("2-view item")
    print("3-exit")
    choice=input("enter your choice:")
    menu={
    1:'add',
    2:'view',
    3:'exit'
    }
    if choice=="1":
        item=input("enter items to add:")
        items.append(item)
        print("Item added:",item)
    elif choice=="2":
        print("items in list:",items)
    elif choice=="3":
        print("Exiting...")
        break
    else:
        print("invalid choice")

