import numpy as np
from IPython.display import clear_output
from BigM import BigM
from BigM import graph
from BigM import InputHandling
import random
mem = [
    ["Max Z = x+5y","6x+5y<=60","x+2y<=14", "x<=9"]
]

#graph.drawGraph(mem[1])
class N1(Exception):
    pass
class N2(Exception):
    pass
class StopExec(Exception):
    def _render_traceback_(self):
        pass

def display_iteration(iteration):
    # courtesy of amine
    print("==============================================================================================================")
    print(iteration[0])
    print()
    print("basic variables")
    print(iteration[1])
    print("non basic variables")
    print(iteration[2])
    print()
    print("==============================================================================================================")

def handle_display_graph(prob : np.ndarray):
    while True:
        c = input("Voulez vous afficher un représentation graphique? (o/n)\n")
        if c in ['o', 'n']:
            break
    if c == 'o' :
        graph.drawGraph(prob) # TODO ipynb magik

def validate_with_msgs(expr: str, obj=None) -> bool:
    if InputHandling.validateUserInput(expr):
        #if not obj:
        return True
        # if InputHandling.validateUserInputSemantic(expr, obj):
        #     return True
        # else:
        #     print("l\'expression semble etre correcte mais n\'a pas de sens\n")
        #     return False
    else:
        print("expression fausse\n")
        return False

def handle_problem_input() -> np.ndarray:
    # fonction objectif
    while True:
        obj = input("Donner votre fct objective sous la forme: (max/min) z = ax +/- by ...\n")
        if validate_with_msgs(obj):
            break
    
    # Contraintes
    ctr = []
    print("Donner vos contraintes sous la forme ax +/- by ... ( <= / < / = / >= / > ) d \n")
    c = "go"
    while c :
        c = input(f"Donner la contrainte no {len(ctr)+1}, envoyer une chaine vide pour terminer\n")
        if c :
            if validate_with_msgs(c, obj):
                ctr.append(c)
    
    return np.array(InputHandling.formatUserInput([obj] + ctr))

def appliquer_bigm(prob : np.ndarray , is_R2: bool):
    # niveau 3 (4)
    bm = BigM.BigM()
    iterations = bm.runBigM(prob)
    while True:
        print(f"""1- Afficher le resultat final
                2- Afficher la resolution a travers le tableaux
                3-Afficher la resolution graphique
                4- revenir
                5- menu\n""")
        match input("votre choix ... ") :
            case '1':
                # solution is the last iteration basic variables
                print(iterations[-1][1], end="\n")
                
            case '2':
                for iteration in iterations:
                    display_iteration(iteration)
                
            case '3':
                if is_R2:
                    pass
                # TODO
                
            case '4':
                raise N2()
            
            case '5':
                raise N1()
            case _:
                print("Choisir de 1 a 5\n")

def do_job(prob : np.ndarray , is_R2: bool) :
    # niveau 2
    
    while True:
        print("""1- Tracer l\'encemble des contraintes
            2- Appliquer Big M
            3- menu""")
        match input("Votre choix ... "):
            case '1':
                if is_R2:
                    handle_display_graph(prob)
                else :
                    print("le probleme n\'est pas R2")
            case '2':
                try:
                    appliquer_bigm(prob, is_R2)
                except N2:
                    pass
            case '3':
                raise N1()
            case _:
                print("choisir de 1 a 3\n")

def handle_choice():
    match input("votre choix ... ") :
        case '1':
            # assuming that all problems are R2
            probchoisit = random.choice(mem)
            print(f"probleme pioche est {probchoisit}\n")
            prob = np.array(InputHandling.formatUserInput(probchoisit))
            do_job(prob, True)
            
        case '2':
            prob = handle_problem_input()
            do_job(prob, True)
            
        case '3':
            prob = handle_problem_input()
            do_job(prob, False)
            
        case '4':
            print("Bye!")
            raise StopExec
            
        case _:
            print("Choisir de 1 a 4\n")
            raise N1()

            
while True :
    clear_output(wait=True)
    print("""1- choisir programme de la memoire
            2- saisir programme dans R2
            3- saisir programme dans R3
            4- quitter\n""")
    try :
        handle_choice()
    except N1:
        continue