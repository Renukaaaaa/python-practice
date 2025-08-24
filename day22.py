#todays date & time
from datetime import datetime
now=datetime.now()
print(now.strftime("%d/%m/%y %H:%M"))


#print current time every 5 seconds
import time
from datetime import datetime
for i in range(3):
    print(datetime.now().strftime("%H:%M:%S"))
    time.sleep(5)


#convert HELLO world to hello WORLD
text="HELLO world"
print(text.swapcase())


#count occurrence of python in text
text="Python is great. python is fun. I love python "
count=text.lower().count("python")
print("Occurence of python:",count)


#create timestamped filename
from datetime import datetime
filename=datetime.now().strftime("report_%Y-%m-%d_%H-%M-%S.txt")
print("generated filename:",filename)