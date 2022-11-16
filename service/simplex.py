import numpy as np
import pandas as pd
from aliases import Iterations, Variables

class Simplex():
    
    def __select_vars(self, init_simplex_df: pd.DataFrame) -> Variables:
        pass


    def __verify_solution_existence(self, variables: Variables) -> bool:
        exist: bool = True
        return exist
    

    def _perform_simplex(self, init_simplex_df: pd.DataFrame) -> Iterations:
        variables: Variables = self.__select_vars(init_simplex_df)
        exist = self.__verify_solution_existence(variables)
        if not exist:
            raise ValueError('SIMPLEX_SOLULTION_DOES_NOT_EXIST,')
        iterations: Iterations = []
        print("Going to run simplex")
        return iterations