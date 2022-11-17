import numpy as np
import pandas as pd
from aliases import Iterations, Variables

class Simplex():
    
    def __select_vars(self, init_simplex_df: pd.DataFrame) -> tuple[Variables, Variables]:
        """
        Selects the basic and non-basic variables from the initial simplex dataframe.
        """
        # print the column a1
        ret_vars = (dict(), dict())
        numberOfRows = init_simplex_df.shape[0]
        for col in init_simplex_df.columns:
            if col in ['condition', 'p']: # skip the condition and p columns
                continue
            column = init_simplex_df.loc[:, col]
            if column[column == 0].count() == numberOfRows-1: # basic variable
                nonZeroRow = column[column != 0].index[0] # get the row index of the non-zero value
                ret_vars[0][col] = init_simplex_df.loc[nonZeroRow]['condition']
            else: # non basic variable
                ret_vars[1][col] = 0
        return ret_vars


    def __verify_solution_existence(self, variables: Variables) -> bool:
        """
        Verifies if the solution exists.
        checks if all the basic variables are positive.
        """
        for key, value in variables[1].items():
            if value < 0:
                return False
        return True
    

    def _perform_simplex(self, init_simplex_df: pd.DataFrame) -> Iterations:
        variables: Variables = self.__select_vars(init_simplex_df)
        exist = self.__verify_solution_existence(variables)
        if not exist:
            raise ValueError('SIMPLEX_SOLULTION_DOES_NOT_EXIST,')
        iterations: Iterations = []
        print("Going to run simplex")
        return iterations