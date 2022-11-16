from string import ascii_lowercase
import matplotlib.pyplot as plt
import numpy as np


def graph(linProg):
  
    def removeDuplicate(intersectionPoints):
        l = []
        intersectionPoints.sort(key=lambda k:(k[0],k[1]))
        for i in range(0,len(intersectionPoints)-1):
          if intersectionPoints[i][0] != intersectionPoints[i+1][0]:
            l.append(intersectionPoints[i])
            if(i+1 == len(intersectionPoints)-1):
                l.append(intersectionPoints[i+1])
                break
          elif i+1 == len(intersectionPoints)-1:
            l.append(intersectionPoints[i+1])
            break
        return l

    def offsetPoints(intersectionPoints,listOfConstraints):
        for constraint in listOfConstraints:
            if(constraint[3] == -1):
                a = constraint[0]
                b = constraint[1]
                c = constraint[2]
                for intersectionPoint in intersectionPoints:
                    x = intersectionPoint[0]
                    y = intersectionPoint[1]
                    if(round(a*x+b*y,4)==c or x < 0 ):
                        offset.append(intersectionPoint)
        
    def paintPoints(intersectionPoints,listOfConstraints):
            for constraint in listOfConstraints:
                if(constraint[3] == 1 or constraint[3] ==0):
                    a = constraint[0]
                    b = constraint[1]
                    c = constraint[2]
                    for intersectionPoint in intersectionPoints:
                        x = intersectionPoint[0]
                        y = intersectionPoint[1]
                        if(round(a*x+b*y,4)==c or x < 0 ):
                            color.append(intersectionPoint)
            

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

    def findIntersections(equation1,equation2):
        a1= equation1[0]
        b1=equation1[1]
        c1 = equation1[2]
        
        a2= equation2[0]
        b2=equation2[1]
        c2 = equation2[2]

        linearSystem = np.array([[a1,b1],[a2,b2]])
        sol = np.array([c1,c2])
        coord = np.linalg.solve(linearSystem,sol)
        return coord.tolist()
    
    def validIntersection(intersectionPoints,listOfConstraints):
        """
            remove inersection points that are out of the definition domain
        """
        constraintsToRemove = []
        for intersectionPoint in intersectionPoints:
            for constraint in listOfConstraints:
                a = constraint[0]
                b = constraint[1]
                c = constraint[2]
                upper = constraint[3] 
                x = intersectionPoint[0]
                y = intersectionPoint[1]
                if(upper == 1 or upper == 0):
                    if(round(a*x+b*y,4)>c or x < 0 ):
                        constraintsToRemove.append(intersectionPoint)
                        break
                else:
                     if(round(a*x+b*y,4)<c or x < 0 ):
                        constraintsToRemove.append(intersectionPoint)
                        break

        for constraint in constraintsToRemove:
            intersectionPoints.remove(constraint)

    def highlightArea():
        #draw color
        color.sort(key=lambda k:(k[0],k[1]))
        xColor=[row[0] for row in color]
        yColor=[row[1] for row in color]
        print("color list =",color )
        ax.fill_between(xColor,yColor,color='C1',hatch="\\\\", alpha=0.3)
        
        #paint offset with white
        offset.sort(key=lambda k:(k[0],k[1]))
        xOffset = [row[0] for row in offset]
        yOffset= [row[1] for row in offset]
        print("offset = ",offset)
        ax.fill_between(xOffset,yOffset,color='white', alpha=1,zorder=1)

    def highlightIntersectionPoints(intersectionPoints):
        
        for intersectionPoint,letter in zip(intersectionPoints,ascii_lowercase):
            x = intersectionPoint[0]
            y = intersectionPoint[1]
            plt.scatter(x, y, color="black",zorder=2) 
            ax.annotate(letter,[x,y])
    
    def findIntersectionWithOrigin(listOfConstraints):
        for constraint in listOfConstraints:
            a = constraint[0]
            b= constraint[1]
            c =constraint[2]
            if a==0:
                intersectionPoints.append([0,c/b])
            elif b==0:
                intersectionPoints.append([c/a,0])
            else:
                intersectionPoints.append([0,c/b])
                intersectionPoints.append([c/a,0])

    
    if(len(linProg)==5): #3d graph      
        pass
        #coming soon
    

    else:#2d graph
        offset=[]
        color=[]
        listOfConstraints=[] 
       
       #extract constraints from the formatted user input
        for i in range(len(linProg[0])): 
             listOfConstraints.append([row[i] for row in linProg]) #get column of the matrix
            
        fig, ax = plt.subplots()    
       
       #draw constaints
        for constraint in listOfConstraints: 
            drawConstraint(constraint)
        
        intersectionPoints =[]
        
        #get intersactionsPoins
        for i in range (0,len(listOfConstraints)):
            for j in range(i+1,len(listOfConstraints)):
                intersectionPoints.append(findIntersections(listOfConstraints[i],listOfConstraints[j]))
        
        #get intersection with the x=0 and y =0
        findIntersectionWithOrigin(listOfConstraints)

        
        
        #remove intersection points that are out of the definition domain
        validIntersection(intersectionPoints,listOfConstraints)

       
        offsetPoints(intersectionPoints,listOfConstraints)
        paintPoints(intersectionPoints,listOfConstraints)
        color = removeDuplicate(color)
       
        #color the area of definition domain
        highlightArea()

        #draw points
        highlightIntersectionPoints(intersectionPoints)

        plt.ylim(0, None)
        plt.xlim(0,10)
        ax.set(xlabel='x axe', ylabel='y axe',title='linear program graph')
        ax.grid()
        plt.legend()
        plt.show() 
        
graph([[ 1, 0,3,-3], [ 0, 2, 2,5], [ 4, 12, 18,16], [ -1, 1,1,1]])
