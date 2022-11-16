import numpy as np
from BigM import BigM


fake_data = np.matrix([[1, 1, 0, 1], [1, 0, 1, -1], [0, 1, 1, 3],[20, 5, 10, 0], [-2, 0, 2, 0]]) 
big_m = BigM()

if __name__ == "__main__":
    big_m.runBigM(fake_data)