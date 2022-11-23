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
    # fake_data = np.matrix([ [3, 1, 1, 200], [2, 2, 1, 300], [600, 400, 225, 0], [0, -2, -2, 0] ])
    # fake_data = np.matrix([ [4, 1, 0, 3], [1, 1, 1, 2], [1, 0, 1, 6], [100, 40, 30, 0], [-2, 2, -2, 0] ])
    # fake_data = np.matrix([ [3, 4, 1, -4], [-1, 20, -1, 3], [1, -1, 1, 1], [40, 1, 5, 0], [-2, 0, 2, 0] ])
    # fake_data = np.matrix([[5, 7, 1, -4], [-2, 200, -3, -9],
    #                       [2, -1, -2, -2], [40, 1, 5, 0], [-2, 0, 0, 0]])

    big_m = BigM()
    iterations = big_m.runBigM(fake_data)
    for iteration in iterations:
        display_iteration(iteration)

    print("sensibilty analysis")
    big_m.sensibility_analysis(iterations)
    print("sss")
    


if __name__ == "__main__":
    main()
