#Cette fonction s'execute pour analyser les donner qui provient de chaque itération du big M
#bien sur à l'excution de la fontion les valeurs de retours ne vont pas s'afficher car il faut avoir des input correcte (qui sont en commentaires si vous voulez testez)

#RQ : cette fonction recoie en input une iteration ( de la fonction de Med Amine) qui contient les variables de bases , hors bases et une matrice du big M
# Pour les variables de bases et hors bases , ils seront tout simplement afficher et pour la matrice de l'iteration on affiche le z max


def AnalyseData(variablesdebases , variableshorsbases , mat):
    """
    Not Tested
    """
    print("les variables de bases dans cette iteration sont")
    for var in enumerate(variablesdebases):
        nomvariable=var[1].get('name')
        valeurvariable=var[1].get('value')
        print(nomvariable+'='+str(valeurvariable))
    print("les variables hors bases dans cette iteration sont")
    for var in enumerate(variableshorsbases):
        nomvariable=var[1].get('name')
        valeurvariable=var[1].get('value')
        print(nomvariable+'='+str(valeurvariable))
    print(-mat[[n-1],[m-1]])
    return 0

# Une variable correspond au couple (nom , valeur) , exemple: {"name": "x1": "value": 3.0}
#declaration de "Variable"
Variable = dict[str, float]                         

#des exmples de Variables(juste pour le test)
#Variable1={"name": "x", "value": 3.0}
#Variable2={"name": "y", "value": 4.0}
#Variable3={"name": "e1", "value": 0.0}
#Variable4={"name": "e2", "value": 0.0}
#Variable5={"name": "e3", "value": 0.0}

#les variables de bases sont une liste de variables , et ceci est leur déclaration
variablesdebases=list[Variable]

#les variables hors bases sont une liste de variables , et ceci est leur déclaration
variableshorsbases=list[Variable]

#initialisation de variables de bases (test)
#variablesdebases= [Variable1 , Variable2]

#initialisation de variables hors bases 
#variableshorsbases= [Variable3 , Variable4, Variable5]

#La matrice provenant de l'itération est de cette forme : n lignes , m colones 
import numpy as np

n=4
m=5

mat= np.zeros((n,m))
AnalyseData(variablesdebases , variableshorsbases , mat)