#login attempt tracker
attempt=0
def login():
    global attempt
    attempt=attempt+1
    print("login attempt",attempt)
login()
login()

#global counter
count=0
def counterIncrement():
    global count
    count=count+1
print("count=",count)
counterIncrement()
print("After function call ",count)
counterIncrement()
print("After function call ",count)

#update nested variable
def outer():
    msg="hi...how are you?"
    print(msg)
    def inner():
        nonlocal msg
        print(msg)
    inner()
outer()

#wheather logger
weather="sunny"
def calculateWeather(new_weather):
    global weather
    weather=new_weather
    print("updated wheather:",weather)
calculateWeather("Rainy")
calculateWeather("sunny")

#toggle dark/light theme
theme="light"
def toggle_theme():
    global theme
    theme="dark" if theme=="light" else "light"
    print("current theme",theme)
toggle_theme()
toggle_theme()

#session timer
def start_timer():
    minute=0
    def tick():
        nonlocal minute
        minute=minute+1
        print("minutes passed:",minute)
    tick()
    tick()
start_timer()

#task tracker
task_done=0
def taskTracker():
    global task_done
    task_done=task_done+1
    print("total task done:",task_done)
taskTracker()
taskTracker()
taskTracker()

#wallet system
balance=1000
def deposit(amount):
    global balance
    balance=balance+amount
    print("Total balance:",balance)
def withdraw(amount):
    global balance
    if(balance>amount):
        print("balance withdraw successfully",balance)
    else:
        print("not sufficient balance")
deposit(400)
withdraw(800)

#scoreboard tracker
score=0
def add_score(points):
    global score
    score=score+points
    print("total score",score)
add_score(4)
add_score(9)

#event logger with nonlocal count
def event_logger():
    count=0
    def log():
        nonlocal count
        count=count+1
        print("number of times event logged:",count)
    log()
    log()
event_logger()

#stock quantity manager
stock={"apple":10,"banana":20}
def add_stock(item,qty):
    global stock
    stock[item] = stock.get(item, 0) + qty
    print("Stock after adding:", stock)

def sell_item(item, qty):
    global stock
    if stock.get(item, 0) >= qty:
        stock[item] -= qty
        print("Stock after selling:", stock)
    else:
        print("Not enough stock.")

add_stock("apple", 5)
sell_item("banana", 3)