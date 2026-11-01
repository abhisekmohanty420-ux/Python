import time
from plyer import notification 
 
while True:
    notification.notify(title="Please Drink Some Water",
                        message="You need to drink some water"
                        )
    time.sleep()