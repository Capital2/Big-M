import matplotlib.pyplot as plt
import numpy as np


def drawGraph(formattedUserInput):
    def drawConstraint(constraint):
        # ax + by = c
        a = constraint[0]
        b = constraint[1]
        c = constraint[2]

        if(a == 0):# x = 0 draw horizontal line
            plt.axhline(y=c/b, color='b', linestyle='-',label=f"{b}y={c}")
            
        elif(b == 0):# y = 0 draw vertical line
                plt.axvline(x=c/a, color='g', linestyle='-',label=f"{a}x={c}")
        else:# both x and y !=0 
            x = np.linspace(0,10,2)#generate 2 values for x between 1 and 10
            y=(-a*x + c)/b
            plt.plot(x, y, '-r',label=f"{a}x+{b}y={c}")   

    d = np.linspace(0,16,300)
    x,y = np.meshgrid(d,d)
    x = np.linspace(0, 16, 300)

    plt.xlim(0,16)
    plt.ylim(0,11)
    plt.xlabel(r'$x$')
    plt.ylabel(r'$y$')


    listConstraints=[]

    for i in range(len(formattedUserInput[0])): 
        listConstraints.append([row[i] for row in formattedUserInput]) 


    for i in listConstraints:
        drawConstraint(i)

    filledArea = [] 
    for i in listConstraints:
        a = i[0]
        b = i[1]
        c = i[2]
        operator = i[3]
        if(a == 0):
            if(operator == 0):
                filledArea.append(b*y==c)
            elif(operator == 1):
                filledArea.append(b*y>c)
            elif(operator == -1):
                filledArea.append(b*y<c)
            elif(operator == 2):
                filledArea.append(b*y>=c)
            elif(operator == -2):
                filledArea.append(b*y<=c)
        if(b == 0):
            if(operator == 0):
                filledArea.append(a*x==c)
            elif(operator == 1):
                filledArea.append(a*x>c)
            elif(operator == -1):
                filledArea.append(a*x<c)
            elif(operator == 2):
                filledArea.append(a*x>=c)
            elif(operator == -2):
               filledArea.append(a*x<=c)
        else:
            if(operator == 0):
                filledArea.append(b*y==c-a*x)
            elif(operator == 1):
                filledArea.append(b*y>c-a*x)
            elif(operator == -1):
                filledArea.append(b*y<c-a*x)
            elif(operator == 2):
                filledArea.append(b*y>=c-a*x)
            elif(operator == -2):
                filledArea.append(b*y<=c-a*x)

    calculate = filledArea[0]
    
    for i in range(1,len(filledArea)):
        calculate = calculate & filledArea[i]

    plt.imshow((calculate).astype(int),extent=(x.min(),x.max(),y.min(),y.max()),origin="lower", cmap="Greys", alpha = 0.3)
    plt.grid()
    plt.legend()
    plt.show()