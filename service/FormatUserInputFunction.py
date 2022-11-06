#!/usr/bin/env python
# coding: utf-8

# In[1317]:


import os
print('Donner votre systeme sous cette forme : Max=...x+...y : ...x+/-...y</>...; ...')
dict=input("le systeme :")
print("Votre dictionnaire est : "+dict)
os. system("pause")


# In[1316]:


import numpy as np
dictionnaire = 'Max=2x+3y : 3x+1y<2 ; 1x-1y>3;'
dictionnaireMax = ''
dictionnaireMin = ''
maximisation=''
contraintes=''
if(dictionnaire.find('Max')==0):dictionnaireMax=dictionnaireMax+dictionnaire
if(dictionnaire.find('Min')==0):dictionnaireMin=dictionnaireMin+dictionnaire
def FormatUserInputR2(dictionnaireMax , maximisation , contraintes):
    z=0
    for i,c in enumerate(dictionnaire):
        if(c==':'):
            e=i+1
    contr=0
    for i, c in enumerate(dictionnaireMax):
        if(c==':'): 
            for j in range (z,i,1) :
                print(dictionnaireMax[j] , j)
                maximisation=maximisation + dictionnaireMax[j]
                z=z+1
    for i, c in enumerate(dictionnaire):
        if(c==';'): 
            contr=contr+1
            for j in range (e,i+1,1) :
                print(dictionnaire[j] , j)
                contraintes=contraintes + dictionnaire[j]
                e=e+1
    print('equation de maximisation est : ',maximisation)
    print('On a',contr,'contraintes, qui sont sont :',contraintes)
    mat= np.zeros((4,contr+1))
    print(mat)
    x=''
    y=''
    for i,c in enumerate(maximisation):
         if(c=='x' and maximisation[i-2]!='M'):
                if(maximisation[i-2]=='-'):
                    print('hiiiiii',maximisation[i-2])
                    x=x+'-'
                x=x+maximisation[i-1]
         if(c=='y'): 
                if(maximisation[i-2]=='-'):
                    print('hiiiiii',maximisation[i-2])
                    y=y+'-'
                y=y+maximisation[i-1]
    mat[[0],[-1]]=x
    mat[[1],[-1]]=y
    mat[[2],[-1]]=0
    mat[[3],[-1]]=1

    print(mat)
    r=0
    p=0
    
    for i,c in enumerate(contraintes):
        con=''
        if(c==';'):           
            p=p+1
            print('contrainte',p)
            for j in range(r,i,1):
                con=con+contraintes[j+1];
                r=r+1
        print('')
        print('avant boucle',con)
        nbmoins=0
        derrierey=0
        derrierex=0
        for p,c in enumerate(con):
            if(c=='-'):
                nbmoins=nbmoins+1
                print('le nombre des moins est',nbmoins)
        for m,c in enumerate(con):
            
            print('je suis le caractere ',c)
            contr2=contr
            if(nbmoins==0):    
                if(c=='x'):
                    mat[[0],[-contr-2+m]]=con[m-1]
                if(c=='y'):
                    mat[[1],[-contr-2+m]]=con[m-1]
                if(c=='<'):
                    mat[[2],[-contr-3+m]]=con[m+1]
                    mat[[3],[-contr-3+m]]=-1
                if(c=='>'):
                    mat[[2],[-contr-3+m]]=con[m+1]
                    mat[[3],[-contr-3+m]]=1
            if(nbmoins==1 ):
                if(c=='x'):
                    if(con[m-2]=='-'):
                        print('le moins est deriere le x')
                        derrierex=1
                        mat[[0],[-contr-3+m]]=-int(con[m-1])
                    else: mat[[0],[-contr-2+m]]=con[m-1]
                if(c=='y'):
                    if(con[m-2]=='-'):
                        derrierey=derrierey+1
                        print('le moins est deriere le y',derrierey)
                        mat[[1],[-contr-2+m]]=-int(con[m-1])
                    else: mat[[1],[-contr-3+m]]=con[m-1]
                if(c=='<' and derrierey==1):
                    mat[[2],[-contr-3+m]]=con[m+1]
                    mat[[3],[-contr-3+m]]=-1
                if(c=='<' and derrierex==1):
                    mat[[2],[-contr-4+m]]=con[m+1]
                    mat[[3],[-contr-4+m]]=-1
                if(c=='>'and derrierey==1):
                    mat[[2],[-contr-3+m]]=con[m+1]
                    mat[[3],[-contr-3+m]]=1
                if(c=='>'and derrierex==1):
                    mat[[2],[-contr-4+m]]=con[m+1]
                    mat[[3],[-contr-4+m]]=1
            if(nbmoins==2):
                if(c=='x'):
                    mat[[0],[-contr-3+m]]=-int(con[m-1])
                if(c=='y'):
                    mat[[1],[-contr-3+m]]=-int(con[m-1])
                if(c=='<'):
                    mat[[2],[-contr-4+m]]=con[m+1]
                    mat[[3],[-contr-4+m]]=-1
                if(c=='>'):
                    mat[[2],[-contr-4+m]]=con[m+1]
                    mat[[3],[-contr-4+m]]=1
    
    print(mat)
    return(mat)


# In[1302]:


FormatUserInputR2(dictionnaire , maximisation , contraintes)


# In[ ]:





# In[ ]:




