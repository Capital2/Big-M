import numpy as np
import pandas as pd
from abc import ABC, abstractmethod
from aliases import Iterations, Variables

class Simplex(ABC):
    
    @abstractmethod
    def simplex_matrix_preparation(self):
        pass


    def select_vars(self, init_simplex_df: pd.DataFrame) -> Variables:
        variables = {"bv": [], "nbv": []}
        return variables


    def verify_solution_existene():
        pass
    

    def run_simplex(self, init_simplex_df: pd.DataFrame) -> Iterations:
        iterations: Iterations = []
        print("Going to run simplex")
        return iterations