#custom string representation
class book:
    def __init__(self,title,author):
        self.title=title
        self.author=author
    def __str__(self):
        return f"{self.title} by {self.author}"
    def __repr__(self):
        return f"({self.title} by {self.author})"
b1=book("Agnipankh","APJ abdul kalam")
print(str(b1))
print(repr(b1))
b2=book("Basics of python","John doe")
print(str(b2))
print(repr(b2))


#vector addition using operator oevrloading
class vector:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __add__(self,other):
        return vector(self.x+other.x,self.y+other.y)
    def __str__(self):
        return f"vector ({self.x} {self.y})"
v1=vector(3,5)
v2=vector(7,9)
v3=v1+v2
print(str(v3))


#employee comparison
class employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def __gt__(self,other):
        return self.salary>other.salary
    def __lt__(self,other):
        return self.salary<other.salary
    def __str__(self):
        return f"({self.name} has salary {self.salary})"
e1=employee("abc",30000)
e2=employee("pqr",80000)
print(str(e1))
print(str(e2))
print("Is employee1 salary greater than employee2 ?",e1>e2)
print("Is employee1 salary less than employee2 ?",e1<e2)


#shopping cart with operator overloading
class item:
    def __init__(self,name,price):
        self.name=name
        self.price=price
    def __str__(self):
        return f"{self.name} has price {self.price}"
class cart:
    def __init__(self):
        self.items=[]
    def __add__(self,item):
        self.items.append(item)
        return self
    def __len__(self):
        return len(self.items)
    def __str__(self):
        contents="\n".join(str(item) for item in self.items)
        return f"cart has {len(self)} items:\n{contents}"
c=cart()
item1=item("apple",50)
item2=item("banana",60)
c=c+item1
c=c+item2
print(c)


#students grade display
class student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def __str__(self):
        return f"student{self.name} has marks {self.marks}"
    def __repr__(self):
        return f"student({self.name} has marks {self.marks})"
students=[
    student("renuka",{"Math":90,"sci":85}),
    student("Pragati",{"Math":88,"sci":35}),
    student("Meena",{"Math":20,"sci":70})
]
for student in students:
    print(students)