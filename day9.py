#contact form with optional fields
def submit_form(name,email,phone=None):
    print(name,"have email",email,"has phone number",phone)
submit_form("renuka",'renupatil@gmail.com')

#shopping cart with *args
def calculate_total(*prices):
    return sum(prices)
print(calculate_total(45,778,90))

#Bok information with **kwargs
def book_info(**kwargs):
    for key,value in kwargs.items():
        print("Book",key,"is",value)
book_info(Title="Agnipankh",author="APJ abdul kalam",price=500)

#multi item billing
def print_bill(*items):
    for i in items:
        sum=0
        total_price=sum+i
    print(total_price)
print_bill(32,44,78)

#User settings handler
def save_settings(**options):
    print("user settings:")
    for key,value in options.items():
        print(key,value)
save_settings(theme="black",language="hindi")
