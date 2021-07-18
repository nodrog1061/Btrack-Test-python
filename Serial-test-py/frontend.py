import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time
import datetime as dt

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

def animate(i):
    pullData = open("dataDump.txt","r").read()
    dataArray = pullData.split('\n')
    xar = []
    yar = []
    for eachLine in dataArray:
        if len(eachLine)>1:
            x,y = eachLine.split(',')
            xar.append(x)
            yar.append(int(y))
    ax1.clear()
    ax1.plot(xar,yar)

    # Format plot
    plt.xticks(rotation=45, ha='right')
    plt.subplots_adjust(bottom=0.30)
    plt.title('Bin Fullness over time')
    plt.ylabel('Remaining percentage (%)')
    plt.xlabel('Time')

ani = animation.FuncAnimation(fig, animate, interval=1000)
plt.show()