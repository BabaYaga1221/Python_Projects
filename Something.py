from ast import Global
from cProfile import label
from pickle import FALSE
import random
from tokenize import Double
from turtle import color
import matplotlib.pyplot as plt
# import matplotlib.animation as animation
from matplotlib import style
import math
plt.ion()
style.use('fivethirtyeight')
# plt.axis([0,10,0,10])
x1=10
y1=10
x2=90
y2=90
a=random.randint(1,50)
b=random.randint(1,50)
c=random.randint(60,100)
d=random.randint(60,100)
check=True

def moveRobotTwo():
        global x1,y1,x2,y2
        slope=int(abs(c-a)/abs(d-b))
        if(x2==500):
                y2+=slope*0.6
        elif(y2==500):
                x2+=0.6
        else:
                if(x2>x1):
                        if(y2>y1):
                                x2+=0.6
                                y2+=slope*0.6
                        else:
                                x2+=0.6
                                y2-=slope*0.6
                else:
                        if(y2>y1):
                                x2-=0.6
                                y2+=slope*0.6
                        else:
                                x2-=0.6
                                y2-=slope*0.6



def moveRobotOne():
        global x1,y1
        slope=int(abs(y2-y1)/abs(x2-x1))
        if(x2==x1):
                y1+=slope*1
        elif(y2==y1):
                x1+=1
        else:
                if(x2>x1):
                        if(y2>y1):
                                x1+=1
                                y1+=slope*1
                        else:
                                x1+=1
                                y1-=slope*1
                else:
                        if(y2>y1):
                                x1-=1
                                y1+=slope*1
                        else:
                                x1-=1
                                y1-=slope*1


while True:
        plt.clf()
        plt.scatter(x1, y1,color='r',label='robot 1')
        plt.scatter(x2,y2,color='b',label='robot 2')
        plt.ylim(0,500)
        plt.xlim(0,500)
        plt.axis('off')
        plt.legend(bbox_to_anchor=(0.75,1.15),ncol=2)
        plt.grid()
        plt.show()
        plt.pause(0.1)
        dist=int(math.sqrt(pow(abs(x2-x1),2)+pow(abs(y2-y1),2)))
        if(dist<=5 ):
                break
        if(dist<50):
                        a=random.randint(1,50)
                        b=random.randint(1,50)
                        c=random.randint(60,100)
                        d=random.randint(60,100)
                        moveRobotTwo()
                        moveRobotOne()
                        # check=False
        else:
                # check=True
                moveRobotOne()
        print(dist)

# ani = animation.FuncAnimation(fig, animate,)