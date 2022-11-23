import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import Slider


def drawGraph(formattedUserInput):

    def update(val):
        idx = int(freq_slider.val)
        ax.lines.remove(objectif[0])
        a = objectifCoeff[0]
        b = objectifCoeff[1]
        c = idx
        x = np.linspace(-15,15,2)#generate 2 values for x between 1 and 10
        y=(-a*x + c)/b
        objectif[:] =ax.plot(x, y, '-g',label=f"{a}x+{b}y={c}",lw=2)
        fig.canvas.draw_idle()   

    
    def drawObjectif():
        a = objectifCoeff[0]
        b = objectifCoeff[1]
        c = 0
        x = np.linspace(-5,5,2)#generate 2 values for x between 1 and 10
        y=(-a*x + c)/b
        return ax.plot(x, y, '-r',label=f"{a}x+{b}y={c}",lw=2)   
    
        
    def drawConstraint(constraint):
        colors =["#F44336","#E91E63","#9C27B0","#673AB7","#3F51B5","#2196F3","#4CAF50","#FF9800","#795548","#607D8B", ]
        # ax + by = c
        a = constraint[0]
        b = constraint[1]
        c = constraint[2]
        operator = constraint[3]

        if(a == 0):# x = 0 draw horizontal line
            plt.axhline(y=c/b, color=colors[np.random.randint(0,len(colors))], linestyle='-',label=f"{b}y={c}")
            
        elif(b == 0):# y = 0 draw vertical line
                plt.axvline(x=c/a, color= colors[np.random.randint(0,len(colors))], linestyle='-',label=f"{a}x={c}")
        else:# both x and y !=0 
            x = np.linspace(0,10,2)#generate 2 values for x between 1 and 10
            y=(-a*x + c)/b
            plt.plot(x, y, colors[np.random.randint(0,len(colors))],label=f"{a}x+{b}y={c}")   

   
    d = np.linspace(0,16,300)
    x,y = np.meshgrid(d,d)
    x = np.linspace(0, 16, 300)
    
    fig,ax = plt.subplots()
 
    plt.xlim(0,16)
    plt.ylim(0,11)
    plt.xlabel(r'$x$')
    plt.ylabel(r'$y$')

    listConstraints=[]
    #get objectif function (the objectif funtion SHOULD ALWAYS be the last int the formatted user input!)
    objectifCoeff = [row[-1] for row in formattedUserInput]
   
    #get constraint functions
    for i in range(len(formattedUserInput[0])-1):
        listConstraints.append([row[i] for row in formattedUserInput]) 

    #draw constraint
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
    
    #calculate feasable area
    for i in range(1,len(filledArea)):
        calculate = calculate & filledArea[i]

    plt.imshow((calculate).astype(int),extent=(x.min(),x.max(),y.min(),y.max()),origin="lower", cmap="Greys", alpha = 0.3)
    
    #draw objectif function (move the graph to see it at (0,0))
    objectif = drawObjectif()
    
    plt.grid()
    plt.legend()
    
    #setup slider
    fig.subplots_adjust(left=0.25, bottom=0.25)
    axfreq = fig.add_axes([0.25, 0.1, 0.65, 0.03])
    freq_slider = Slider(ax=axfreq,label='move objectif function',valmin=0,valmax=50,valinit=0,)
    
    #listener for changes
    freq_slider.on_changed(update)  
    
    #open graph window
    plt.show()