import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import Slider


def drawGraph(formattedUserInput,slider=False):

    def update_annot(ind):
        pos = points.get_offsets()[ind["ind"][0]]
        annot.xy = pos
        text = f" {pos[0],pos[1]}"
        annot.set_text(text)
    
    def onIntersectionHover(event):
        vis = annot.get_visible()
        if event.inaxes == ax:
            cont, ind = points.contains(event)
            if cont:
                update_annot(ind)
                annot.set_visible(True)
                fig.canvas.draw_idle()
            else:
                if vis:
                    annot.set_visible(False)
                    fig.canvas.draw_idle()

    def updateObjectif(val):
        idx = float(freq_slider.val)
        ax.lines.remove(objectif[0])
        a = objectifCoeff[0]
        b = objectifCoeff[1]
        c = idx
        x = np.linspace(-1000, 3000, 2)
        y=(-a*x + c)/b
        objectif[:] = ax.plot(x, y, '-g', lw=2)
        fig.canvas.draw_idle()   

    def drawObjectif():
        a = objectifCoeff[0]
        b = objectifCoeff[1]
        op = "Max" if objectifCoeff[3] == 1 else "Min"
        c = 0
        x = np.linspace(-1000, 3000, 2)
        y=(-a*x + c)/b
        return ax.plot(x, y, '-g',label=f"{op} Z = {a}x+{b}y",lw=2)   
            
    def drawConstraint(constraint):
        # ax + by = c
        a = constraint[0]
        b = constraint[1]
        c = constraint[2]
        operator = '='
        if constraint[3] == 1:
            operator = '>'
        elif constraint[3] == 2:
            operator = '>='
        elif constraint[3] == -1:
            operator = '<'
        elif constraint[3] == -2:
            operator = '<='

        colors =["#F44336","#E91E63","#9C27B0","#673AB7","#3F51B5","#2196F3","#4CAF50","#FF9800","#795548","#607D8B", ]
        randomColor = colors[np.random.randint(0, len(colors))]
        if(a == 0):# x = 0 draw horizontal line
            plt.axhline(y=c/b, color=randomColor, linestyle='-',label=f"{b}y{operator}{c}")
        elif(b == 0):# y = 0 draw vertical line
                plt.axvline(x=c/a, color=randomColor, linestyle='-',label=f"{a}x{operator}{c}")
        else:# both x and y !=0 
            x = np.linspace(0, 3000, 2)#generate 2 values for x between 1 and 10
            y=(-a*x + c)/b
            plt.plot(x, y, randomColor,label=f"{a}x+{b}y{operator}{c}")   

    def inFeasibleRegion(constraints, point):
        """
        Checks if a given point is in the feasible region.
        i.e. if the point satisfies all the constraints.
        Input:
            constraints: list of constraints
            point: tuple of the point coordinates (x, y)
        Output:
            True if the point is in the feasible region, False otherwise.
        """
        for constraint in constraints:
            a = constraint[0]
            b = constraint[1]
            c = constraint[2]
            operation = a*point[0] + b*point[1]
            if constraint[3] == 1 and operation <= c: # >
                return False
            elif constraint[3] == 2 and operation < c: # >=
                return False
            elif constraint[3] == -1 and operation >= c: # <
                return False
            elif constraint[3] == -2 and operation > c: # <=
                return False
            elif constraint[3] == 0 and operation != c: # =
                return False
        return True

    def drawIntersectionPoints(constraints):
        """
        Draws the feasible intersection points of the constraints
        """
        intersections = set()
        for i in range(len(constraints)):
            a1 = constraints[i][0]
            b1 = constraints[i][1]
            c1 = constraints[i][2]
            # draw intersection points with x axis
            if(a1 != 0):
                x = c1/a1
                intersections.add((x,0))
            # draw intersection points with y axis
            if(b1 != 0):
                y = c1/b1
                intersections.add((0,y))
                          
            for j in range(i+1,len(constraints)):
                a2 = constraints[j][0]
                b2 = constraints[j][1]
                c2 = constraints[j][2]
                try:
                    x = (b2*c1 - b1*c2)/(a1*b2 - a2*b1) 
                    y = (a1*c2 - a2*c1)/(a1*b2 - a2*b1)
                    if x >= 0 and y >= 0:
                        intersections.add((x,y))
                except ZeroDivisionError: # parallel lines
                    pass
        xList=[]
        ylist=[]

        for intersection in intersections:
            # check if intersection is in the feasible region            
            if not inFeasibleRegion(constraints, intersection):
                continue
            #save x and y of each valid intersection point 
            xList.append(intersection[0])
            ylist.append(intersection[1])
            
        #pass the list of x and y to scatter them
        points=plt.scatter(xList,ylist)
        
        return intersections,points

    def getBestAxisScaling(intersections):
        """
        Returns the best scaling for the x and y axis
        """
        maxX = 0
        maxY = 0
        for intersection in intersections:
            maxX = max(maxX, intersection[0])
            maxY = max(maxY, intersection[1])
        maxX = max(maxX, 10)
        maxY = max(maxY, 10)
        return (maxX * 1.1, maxY * 1.1)
    
    def DrawObjectifStaticly():
        a = objectifCoeff[0]
        b = objectifCoeff[1]
        x = np.linspace(0, 3000, 2)
        cRange=np.linspace(0,valmax/2,5)
        for i in range(0,len(cRange)):
            y=(-a*x + cRange[i])/b
            plt.plot(x, y, 'black',linestyle='--')  

    def fillingGrid(listConstraints,y):  
        grid = []
        for i in listConstraints:
            a = i[0]
            b = i[1]
            c = i[2]
            operator = i[3]
            if(a == 0):
                match operator:
                    case 0:
                        grid.append(b*y==c)  
                    case 1 :
                        grid.append(b*y>c)
                    case -1 :
                        grid.append(b*y<c)
                    case 2 :
                        grid.append(b*y>=c)
                    case -2 :
                        grid.append(b*y<=c)
                    case _:
                        raise ValueError(f"received {operator} which is not in [0, 1, -1, 2, -2]")
            elif(b == 0):
                match operator:
                    case 0 :
                        grid.append(a*x==c)
                    case 1 :
                        grid.append(a*x>c)
                    case -1 :
                        grid.append(a*x<c)
                    case 2 :
                        grid.append(a*x>=c)
                    case -2 :
                        grid.append(a*x<=c)
                    case _:
                        raise ValueError(f"received {operator} which is not in [0, 1, -1, 2, -2]")
            else:
                match operator:
                    case 0 :
                        grid.append(b*y==c-a*x)
                    case 1 :
                        grid.append(b*y>c-a*x)
                    case -1 :
                        grid.append(b*y<c-a*x)
                    case 2 :
                        grid.append(b*y>=c-a*x)
                    case -2 :
                        grid.append(b*y<=c-a*x)
                    case _:
                        raise ValueError(f"received {operator} which is not in [0, 1, -1, 2, -2]")
        return grid

    if(len(formattedUserInput) != 4):
        raise ValueError("You need to pass exactly two variables")

    fig,ax = plt.subplots()

    #get objectif function (the objectif funtion SHOULD ALWAYS be the last int the formatted user input!)
    objectifCoeff = [row[-1] for row in formattedUserInput]
   
    listConstraints = []
    
    #get constraint functions
    for i in range(len(formattedUserInput[0])-1):
        listConstraints.append([row[i] for row in formattedUserInput]) 

    #draw constraint
    for constraint in listConstraints:
        drawConstraint(constraint)

    # draw intersection points
    intersections, points = drawIntersectionPoints(listConstraints)

    bestX, bestY = getBestAxisScaling(intersections)
   
    #initialze annotation
    annot = ax.annotate("", xy=(0,0), xytext=(20,20),textcoords="offset points",bbox=dict(boxstyle="round", fc="w"),arrowprops=dict(arrowstyle="->"))
    annot.set_visible(False)

    d = np.linspace(0, bestY, 300)
    x,y = np.meshgrid(d,d)
    x = np.linspace(0, bestX, 300)

    plt.xlim(0, bestX)
    plt.ylim(0, bestY)
    plt.xlabel(r'$x$')
    plt.ylabel(r'$y$')
 
    grid = fillingGrid(listConstraints,y)

    feasableArea = grid[0]
    
    #calculate feasable area
    for i in range(1, len(grid)):
        feasableArea = feasableArea & grid[i]

    #color the feasible area
    plt.imshow(feasableArea.astype(int), extent=(x.min(),x.max(),y.min(),y.max()), origin="lower", cmap="Greys", alpha=0.3)
    
    #draw objectif function (move the graph to see it at (0,0))
    objectif = drawObjectif()
    
    plt.grid()
    plt.legend()
    
    if(slider):
        #setup slider
        fig.subplots_adjust(left=0.25, bottom=0.25)
        axfreq = fig.add_axes([0.25, 0.1, 0.65, 0.03])
        
        # choose the best valmax for the slider
        valmax = objectifCoeff[0] * bestX + objectifCoeff[1] * bestY
        freq_slider = Slider(ax=axfreq, label='Z=', valmin=0, valmax=valmax, valinit=0,valstep=0.2,)
        
        #listener for changes
        freq_slider.on_changed(updateObjectif) 
    else:
        #draw objectif line staticly
        valmax = objectifCoeff[0] * bestX + objectifCoeff[1] * bestY
        DrawObjectifStaticly() 
    
    #set event listener
    fig.canvas.mpl_connect("motion_notify_event", onIntersectionHover)
    
    #open graph window
    plt.show()


#exemple in case of testing 
#drawGraph([[0,1,2,3],[1,0,3,2],[6,4,18,0],[-2,-2,-2,-2]],slider=True)