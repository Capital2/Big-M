class BigM(Simplex):

    def __prepare_matrix(self, preconditioned_df: pd.DataFrame) -> pd.DataFrame:
        """
        This method performs operations between rows of the preconditioned DataFrame
        to get rid of every M that resides in one of the artificial variables columns.
        Arguments:
            preconditioned_df: A pandas DataFrame that holds the linear program
            after adding slack and artificial variables, performing transformations on the 
            eqution of maximisation and cleaning the DataFrame from unnecessary data
        Returns:
            A pandas DataFrame that allows the execution of the simplex algorithm
        """
        objectiveFunctionRow = preconditioned_df.shape[0] - 1
        newChange = True
        while newChange: # idk if that's necessary but meh
            newChange = False
            for col in preconditioned_df.filter(regex="a\d").columns: # loop through the artificial variables columns
                if preconditioned_df.loc[objectiveFunctionRow][col] != 0: # if last rows column of artificial variable contains M
                    for row in range(0, preconditioned_df.shape[0] - 1):
                        if preconditioned_df.loc[row][col] != 0:
                            # we can perform operations between this row and the last row
                            # to get rid of the M
                            preconditioned_df = self.__perform_operations(preconditioned_df, row, objectiveFunctionRow, col)
                            newChange = True
        
        return preconditioned_df


    def __perform_operations(self, preconditioned_df: pd.DataFrame, row: int, objectiveFunctionRow: int, col: str) -> pd.DataFrame:
        """
        This method performs operations between row and the objective function row
        to get rid of the M in the artificial variable column that resides in the column col.
        Arguments:
            preconditioned_df: A pandas DataFrame that holds the linear program.
            row: The row that we can use to perform operations with the objective function row.
            objectiveFunctionRow: The row that contains the objective function
            col: The column that contains the M
        Returns:
            A pandas DataFrame after performing the operations.
        """
        operation = -preconditioned_df.loc[objectiveFunctionRow][col] / preconditioned_df.loc[row][col] # quick meth, trivial
        for column in preconditioned_df.columns: # loop through the columns to do chaka laka boom boom between the rows
            preconditioned_df.loc[objectiveFunctionRow][column] += operation * preconditioned_df.loc[row][column]
        return preconditioned_df

