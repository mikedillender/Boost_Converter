from graphics import *
import numpy as np

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
rl=10000
on=True
maxtime=.1
f=10000
D=.5

v1=0
v2=0
v3=0
il=0
il0=0
ic=0
ic0=0
vc=0
vc0=0
vl=0
vl0=0
t0=0

for tstep in range(np.floor(maxtime/step)):
    t=tstep*step
    if (t%(1/f)>(1/f)*.5):
        if(not on):
            t0=t
            ic0=ic
            il0=il
            vc0=vc
            vl0=vl
            on = True
        ''' Switch activated '''
        il_approaches=vs/rs

    else:
        if (not on):
            t0 = t
            ic0 = ic
            il0 = il
            vc0 = vc
            vl0 = vl

        ''' Switch Off '''

        on=False



vouts=[]

while(True):
    time.sleep(2)
