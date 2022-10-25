'''This program represent the plot in matplotlib of the live data from the bot.'''

import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style


# import socket
# import time


# ip1 = "192.168.137.106"
# ip2 = "172.20.10.4"
# ip_port = 4210
# mess1 = "1"
# mess2 = "11"
# mess3 = "111"
# mess4 = "1111"
# print("message: %s" % mess1)
# print("message: %s" % mess2)
# print("message: %s" % mess3)
# print("message: %s" % mess4)
# while True:
#     sock = socket.socket(socket.AF_INET,  # Internet
#                      socket.SOCK_DGRAM)  # UDP
#     sock.sendto(mess1.encode(), (ip1, ip_port))
#     data, addr = sock.recvfrom(1024)
#     print("received message: %s" % data)

style.use('fivethirtyeight')

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

def animate(i):
    graph_data=open("example.txt").read()
    lines = graph_data.split('\n')
    xs = []
    ys = []
    for line in lines:
        if len(line) > 1:
            x, y = line.split(',')
            xs.append(float(x))
            ys.append(float(y))
    ax1.clear()
    ax1.plot(xs, ys,color='r')

ani = animation.FuncAnimation(fig, animate, interval=1000)
plt.show()