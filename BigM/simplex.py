
class Simplex():
    
    def __select_vars(self, init_simplex_df: pd.DataFrame) -> tuple[Variables, Variables]:
        """
        Selects the basic and non-basic variables from the initial simplex dataframe.
        """
        # TODO: what if 2 variables have the only non-zero value in the same row? which one to select?
        ret_vars = ([], [])
        for col in init_simplex_df.columns:
            if col in ['condition', 'p']: # skip the condition and p columns
                continue
            column = init_simplex_df.loc[:, col]
            if column[column != 0].count() == 1: # basic variable (i.e. have only 1 non zero value)
                nonZeroRow = column[column != 0].index[0] # get the row index of the non-zero value
                ret_vars[0].append((col, init_simplex_df.loc[nonZeroRow]['condition'], nonZeroRow))
            else: # non basic variable
                ret_vars[1].append((col, 0, -1))
        return ret_vars


    def __verify_solution_existence(self, variables: Variables) -> bool:
        """
        Verifies if the solution exists.
        checks if all the basic variables are positive.
        """
        for _, value, _ in variables[0]:
            if value < 0:
                return False
        return True
    