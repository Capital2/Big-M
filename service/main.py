import numpy as np
from BigM import BigM

def display_iteration(iteration):
    print("==============================================================================================================")
    print(iteration[0])
    print()
    print("basic variables")
    print(iteration[1])
    print("non basic variables")
    print(iteration[2])
    print()
    print("==============================================================================================================")



def main():
    fake_data = np.matrix([[1, 1, 0, 1], [1, 0, 1, -1], [0, 1, 1, 3],[20, 5, 10, 0], [-2, 0, 2, 0]]) 
    big_m = BigM()
    iterations = big_m.runBigM(fake_data)
    for iteration in iterations:
        display_iteration(iteration)


if __name__ == "__main__":
    main()