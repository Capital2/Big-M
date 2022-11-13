import numpy as np
#fonction qui recoit un dictionnaire sous la forme par exemple Max=2x+3y : 3x+1y<2 ; 1x-1y>3; et renvoie une matrice
def FormatUserInputR2(dictionnaire):
    #tableau qui va contenir par exemple Max=2x+3y
    maximisation=''
    #tableau qui va contenir les contraintes par exemple 3x+1y<2 ; 1x-1y>3;
    contraintes=''
    #variable de parcour du dictionnaire pour detecter par exemple Max=2x+3y
    z=0
    #variable qui va contenir le nombre de contraintes
    contr=0
    #parcourir le disctionnaire jusqu'a trouver :, ensuite la variable e prend la position du ":"+1 et le tableau maximisation sera rempli de par exemple Max=2x+3y
    for i, c in enumerate(dictionnaire):
        if(c==':'): 
            e=i+1
            for j in range (z,i,1) :
                maximisation=maximisation + dictionnaire[j]
                z=z+1
    #parcourir le dictionnaire jusqu'a touver ; , et si on trouve alors on ajoute +1 au nombres de contraintes , et on parcour le dictionnaire de e jusqu'a la fin de la contrainte en avancant e  
    for i, c in enumerate(dictionnaire):
        if(c==';'): 
            contr=contr+1
            for j in range (e,i+1,1) :
                contraintes=contraintes + dictionnaire[j]
                e=e+1
    #creation de notre matrice résultat : numpy matrix initialement rempli de zeros
    mat= np.zeros((4,contr+1))
    #deux variables x et y pour contenir les - en cas de besoins
    x=''
    y=''
    #traitement de la partie maximisation par exemple Max=2x+3y
    #parcourir le tableau maximisation qui contient Max=2x+3y, si on arrive au deuxième x de la chaine , on ajoute à x le chiffre derriere le x avec le signe - s'il ya
    for i,c in enumerate(maximisation):
         if(c=='x' and maximisation[i-2]!='M'):
                if(maximisation[i-2]=='-'):
                    x=x+'-'
                x=x+maximisation[i-1]
    #si on trouve le y , on ajoute a la variable y le chifffre derriere le y avec le signe - s'il ya
         if(c=='y'): 
                if(maximisation[i-2]=='-'):
                    y=y+'-'
                y=y+maximisation[i-1]
    #on rempli la derniere colone de la matrice identifié par -1 , par x , y , 0 et 1 dans la dernière ligne puisque c'est une maximisation
    mat[[0],[-1]]=x
    mat[[1],[-1]]=y
    mat[[2],[-1]]=0
    #pour detecter s'il ya le i du mot "Min" , mais par defaut c'est max
    mat[[3],[-1]]=1
    for i,c in enumerate(maximisation):
        if(c=="i"):
         mat[[3],[-1]]=-1
    #traitement de la partie contrainte
    #r est un indice pour parcourir une seul contrainte
    r=0
    p=0
    #parcours du tableau contraintes
    for i,c in enumerate(contraintes):
        con=''
        #si on arrive au ; alors la contrainte est terminée
        if(c==';'):           
            p=p+1
            for j in range(r,i,1):
                con=con+contraintes[j+1];
                r=r+1
        #initialisation des nombres des moins dans la contrainte
        nbmoins=0
        #Dans le cas de nombre de moins egale à 1 , il faut detecter si c'est derriere le x ou derriere le y
        derrierey=0
        derrierex=0
        #detection de nombre de moins dans la contrainte
        for p,c in enumerate(con):
            if(c=='-'):
                nbmoins=nbmoins+1
        #parcours de la contrainte et remplissage de la matrice suivant chaque cas
        for m,c in enumerate(con):
            contr2=contr
            #si le nombre des moins dans la contrainte egale à 0
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
            #si le nombre des moins dans la contrainte egale à 1
            if(nbmoins==1 ):
                if(c=='x'):
                    if(con[m-2]=='-'):
                        derrierex=1
                        mat[[0],[-contr-3+m]]=-int(con[m-1])
                    else: mat[[0],[-contr-2+m]]=con[m-1]
                if(c=='y'):
                    if(con[m-2]=='-'):
                        derrierey=derrierey+1
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
            #si le nombre des moins dans la contrainte egale à 0
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


dictionnairetest = 'Max=2x+3y : 3x+1y<2 ; 1x-1y>3;'
FormatUserInputR2(dictionnairetest)





