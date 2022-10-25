'''This code is for hunting simulation where 4 hunter bots chasing 1
prey bot. We can increase the number of hunters bot and prey bots
then its result differ.'''

from cProfile import label
from cmath import atan
from dis import dis
from lib2to3.pgen2.token import NOTEQUAL
from re import X
import matplotlib.pyplot as plt
from matplotlib import style
import math

lowerBoundX=0
upperBoundX=300
lowerBoundY=0
upperBoundY=300

plt.ion()
style.use('fivethirtyeight')

hunters=[
    [10,10,150,150],
    [10,150,10,150],
]
preyLineY=[]
preyLineX=[]
preys=[
    [90],
    [90]
]
Slope=[1,1,1,1]
distance = [100,100,100,100]
walls=[[0,0,0,0],
       [0,90,180,270]]


def overlapping():
        for i in (0,2):
                for j in (i+1,3):
                        if(hunters[0][i]==hunters[0][j]):
                                if(abs(hunters[1][i]-hunters[1][j])<10):
                                        hunters[1][j]+=1



def moveRobotTwo():
        global hunters,preys,Slope
        # sum=1
        diff=5
        for i in (0,3):
            if(Slope[i]!=0):
                diff+=abs(math.degrees(math.atan(Slope[i])))
        if(preys[0][0]<8 and preys[1][0]<8):
                diff=45
        elif(preys[0][0]<8 and preys[1][0]>285):
                diff=(-45)
        elif(preys[0][0]>285 and preys[1][0]>285):
                diff=135
        elif(preys[0][0]>285 and preys[1][0]<8):
                diff=135
        elif(preys[0][0]<8):
                diff=45
        elif(preys[0][0]>285):
                diff=(-90)
        elif(preys[1][0]<8):
                diff=0
        elif(preys[1][0]>285):
                diff=(-180)

        # diff=diff-sum
        diff=math.tan(diff)
        # slope=int(abs(c-a)/abs(d-b))
        if(preys[0][0]>=10 and preys[0][0]<=290) and (preys[1][0]>10 and preys[1][0]<=290):
                if(preys[0][0]==290):
                        preys[1][0]+=2
                        preys[0][0]-=2
                elif(preys[1][0]==290):
                        preys[0][0]+=2
                        preys[1][0]-=2
                elif(preys[0][0]==10):
                        if(preys[1][0]==10):
                                preys[1][0]+=2
                                preys[0][0]+=2
                        else:
                                preys[1][0]-=2
                                preys[0][0]+=2    
                elif(preys[1][0]==10):
                        if(preys[0][0]==10):
                                preys[0][0]+=2
                                preys[1][0]+=2
                        else:
                                preys[0][0]-=2
                                preys[1][0]+=2  
                else:
                        if(preys[0][0]>hunters[0][0]):
                                if  (preys[1][0]>hunters[1][0]):
                                        preys[0][0]+=2
                                        preys[1][0]+=diff*2
                                else:
                                        preys[0][0]+=2
                                        preys[1][0]-=diff*2
                        else:
                                if  (preys[1][0]>hunters[1][0]):
                                        preys[0][0]-=2
                                        preys[1][0]+=diff*2
                                else:
                                        preys[0][0]-=2
                                        preys[1][0]-=diff*2


def moveRobotOne():
        global hunters,preys,Slope
        i=0
        while i<4:
                if(abs(preys[0][0]-hunters[0][i])!=0):
                        S=int(abs(preys[1][0]-hunters[1][i])/abs(preys[0][0]-hunters[0][i]))
                        if S > 1:
                                Slope[i]=1
                                i+=1
                        elif S < -1:
                                Slope[i]=-1
                                i+=1
                        else:
                                Slope[i]=S
                                i+=1
                else:
                        i+=1
        j=0
        while j<4:
                if(preys[0][0]==hunters[0][j]):
                        if(hunters[1][j]>preys[1][0]):
                                hunters[1][j]-=Slope[j]*1
                                j+=1
                        else:
                                hunters[1][j]+=Slope[j]*1
                                j+=1
                elif(preys[1][0]==hunters[1][j]):
                        if(hunters[0][j]>preys[0][0]):
                                hunters[0][j]-=1
                                j+=1
                        else :
                                hunters[0][j]+=1
                                j+=1

                else:
                        if(preys[0][0]>hunters[0][j]):
                                if(preys[1][0]>hunters[1][j]):
                                    hunters[0][j]+=1
                                    hunters[1][j]+=Slope[j]*1
                                    j+=1
                                else:
                                    hunters[0][j]+=1
                                    hunters[1][j]-=Slope[j]*1
                                    j+=1
                        else:
                                if(preys[1][0]>hunters[1][j]):
                                    hunters[0][j]-=1
                                    hunters[1][j]+=Slope[j]*1
                                    j+=1
                                else:
                                    hunters[0][j]-=1
                                    hunters[1][j]-=Slope[j]*1
                                    j+=1
                                    

def game():
    while True:
                plt.clf()
                plt.box()
                plt.scatter(preys[0][0],preys[1][0],color='b',label='Prey')
                plt.scatter(preys[0][0],preys[1][0],s=5000,facecolors='none',edgecolors='b',linestyle='--')
                preyLineX.append(preys[0][0])
                preyLineY.append(preys[1][0])
                plt.scatter(hunters[0][0],hunters[1][0],color='r',label='hunter1')
                plt.scatter(hunters[0][1],hunters[1][1],color='r',label='hunter2')
                plt.scatter(hunters[0][2],hunters[1][2],color='r',label='hunter3')
                plt.scatter(hunters[0][3],hunters[1][3],color='r',label='hunter4')
                plt.plot(preyLineX,preyLineY)
                plt.ylim(0,300)
                plt.xlim(0,300)
                # some=[10,10,10,10]
                # plt.boxplot(some)
                # plt.axis('off')
                plt.legend(bbox_to_anchor=(0.75,1.15),ncol=2)
                # plt.grid(False)
                plt.show()
                plt.pause(0.1)
        #     distanceFromWalls()
                for i in (0,3):
                    distance[i]=int(math.sqrt(pow(abs(preys[0][0]-hunters[0][i]),2)+pow(abs(preys[1][0]-hunters[1][i]),2)))
                minimum=distance.index(min(distance))
                if(distance[minimum]<5):
                    print("Captured")
                    break
                if(distance[minimum]<50):
                                moveRobotTwo()
                                moveRobotOne()
                else:
                        moveRobotOne()
                overlapping()
                print(distance[minimum])

def main():
        # ax= plt.subplots()
        game()

if __name__=="__main__":
        main()