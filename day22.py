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


