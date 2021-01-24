from graphics import *

height = 800
width = 1000
anchorpoint = Point(width / 2, height / 2)

win = GraphWin("map_display_window", width, height)
image = Image(anchorpoint, height, width)

vs=10
rs=10
l=.01
c=5*pow(10,-6)
step=1*pow(10,-9)
t=0
on=True

vouts=[]

while(True):
    time.sleep(2)
