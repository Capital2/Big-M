
import matplotlib.pyplot as plt
import numpy as np
def graph(linProg):

    def draw2dGraph(equation, constraintNum):
        if(equation[0] == 0):#x=0 draw horizontal line
            ax.hlines(y=equation[2]/equation[1], xmin=0, xmax=10, linewidth=2, color='g',label=f"C{constraintNum}")
        elif(equation[1] == 0):# y=0 draw vertical line 
            ax.vlines(x=equation[2]/equation[0], ymin=0, ymax=10, linewidth=2, color='b',label=f"C{constraintNum}")
        else:# both x and y !=0 
            x = np.linspace(0,10,100)
            y=(-equation[0]*x + equation[2])/equation[1]
            plt.plot(x, y, '-r',label=f"C{constraintNum}")


    
    
    if(len(linProg)==5): #3d graph      
        pass
        #coming soon

    
    
    else:#2d graph
    
        fig, ax = plt.subplots()
   
        for i in range(len(linProg[0])): 
        draw2dGraph([row[i] for row in linProg],i)
        
        plt.ylim(0, None)
        ax.set(xlabel='x axe', ylabel='y axe',title='linear program graph')
        ax.grid()
        plt.legend()
        plt.show() 
        
graph([[ 1, 0,3], [ 0, 2, 2], [ 4, 12, 18], [ 0, 1, 1]])
