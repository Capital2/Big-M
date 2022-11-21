from re import M
#from numpy import *
from sympy import *
import random
allcols=5
itr,rows,cols=(3,3,6)
#bigM = [[[random.randint(0, 5) for i in range(allcols)]for j in range(rows)]for k in range(itr)]
#arr = [[[-99 for i in range(cols)] for j in range(rows)]for k in range(itr)]
bigM=[[[3,2,1,0,0,1800],[1,0,0,1,0,400],[0,1,0,0,1,600]],[[3,0,1,0,-2,600],[1,0,0,1,0,400],[0,1,0,0,1,600]],[[1,0,1/3,0,-2/3,200],[0,0,-1/3,1,2/3,200],[0,1,0,0,1,600]]]
arr = [[[0,0,0,0],[0,0,0,0],[0,0,0,0]],[[0,0,0,0],[0,0,0,0],[0,0,0,0]],[[0,0,0,0],[0,0,0,0],[0,0,0,0]]]
for i in range(itr):  
    for j in range(len(bigM[i])):
        x=0
        for k in range(len(bigM[i][j])):
            if k in [0,1,2,5]:
                arr[i][j][x]=bigM[i][j][k]
                x=x+1
for i in range(itr):
    print("itr bigm",i)
    for j in range(rows):
        print(bigM[i][j])
for i in range(itr):
    print("itr arr",i)
    for j in range(rows):
        print(arr[i][j])
cntr = int(input("taper la contrainte a etudier"))
while (cntr > rows and cntr < 0):
    cntr = int(input("taper la contrainte a etudier"))
dlta = [[0 for i in range(rows)]for k in range(itr)]
dlta[0][cntr] = 1
for i in range(itr):
    print(dlta[i])
x = symbols('x')
"""coef = solve(Eq(x*arr[1][2][0],arr[1][3][0]))
print(coef)
dlta[1][2] = dlta[1][2]+coef[0]
xx = [arr[1][2][2]-arr[1][3][2], "<", dlta[2]-dlta[3]]
res=[]
res.append(xx)
print("resulat ",res)
print(dlta)"""
res=[]
itr=len(arr)
rows=len(arr[i])
cols=len(arr[i][j])
for i in range(itr):
    #for k in range(cols):"""k==clpivot""" 
    if i==0 :
        (rwpivot, clpivot) = (2,1)
    if i==(1):
        (rwpivot, clpivot) = (0,0)

    for j in range(rows): 
        if rwpivot==cntr :
            if j!=cntr :
                xx = [arr[i][rwpivot][cols-1]-arr[i][j][cols-1], "<", dlta[i][j]-dlta[i][rwpivot]]
                res.append(xx)
        elif rwpivot!=cntr :
            if j==cntr :
                xx = [arr[i][rwpivot][cols-1]-arr[i][cntr][cols-1], ">", dlta[i][cntr]-dlta[i][rwpivot]]
                res.append(xx) 
        if i<itr-1 :
            if j!=rwpivot:    
                coef = solve(Eq(x*arr[i][rwpivot][clpivot],arr[i][j][clpivot]))
                print(coef)
                dlta[i+1][j] = dlta[i][j]-coef[0]*dlta[i][rwpivot]  
                #dlta[i+1][j] = dlta[i][j]+1
            else :
                dlta[i+1][j] = dlta[i][j]                
print(res)
for i in range(itr):
    print(dlta[i]) 
min=0
max=0
for x in res:
    if  x[1]=='<' and min<x[0]/x[2]:
        min=x[0]/x[2]
    if  x[1]=='>' and max>x[0]/x[2]:
        max=x[0]/x[2]
if (max-min)>0:
    print("possible si x entre ",max," ",min)
else:
    print("not possible ")