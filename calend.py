import calendar
from datetime import *
from threading import Timer
from py_imessage import imessage
import turtle
wn = turtle.Screen()

cal = calendar.Calendar()
day = cal.iterweekdays()

x=datetime.today()
y = x.replace(day=x.day, hour=1, minute=0, second=0, microsecond=0) + timedelta(days=1)
delta_t=y-x

#secs=delta_t.total_seconds()
secs = 1

def hello_world():
    print("hi!")

t = Timer(secs, hello_world)

stop = False
while stop != True:
    t.start()

wn.onkey(temp, key="Space")

def temp():
    stop = True