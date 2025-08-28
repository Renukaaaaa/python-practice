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