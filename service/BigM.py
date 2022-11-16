import numpy as np
from utilities import Utilities
import pandas as pd
from simplex import Simplex
from aliases import Variables, Iterations
from math import pow

class BigM(Simplex):

    def __init__(self) -> None:
        self.m = pow(10, 9)

    def __clean_preconditioned_df(self, preconditioned_df: pd.DataFrame, rows: list[int], columns: list[str]) -> pd.DataFrame:
        # Dropping rows
        preconditioned_df.drop(rows, inplace=True)

        # Droping columns
        preconditioned_df.drop(columns, axis=1, inplace=True)

        return preconditioned_df


    def __determine_coefs(self, preconditioned_matrix: np.matrix):
        coefs = []
        x = 0
        flag = True

        for i in range(0, preconditioned_matrix.shape[0]):
            if (preconditioned_matrix.item(i, preconditioned_matrix.shape[1] - 1)) != -1 and flag:
                flag = False

            if (preconditioned_matrix.item(i, preconditioned_matrix.shape[1] - 1)) == -1 and flag:
                x += 1
                coefs.append(f'x{x}')
            elif (preconditioned_matrix.item(i, preconditioned_matrix.shape[1] - 1)) == 0:
                si = Utilities.get_col_index(preconditioned_matrix, i)
                coefs.append(f's{si +1}')
            elif (preconditioned_matrix.item(i, preconditioned_matrix.shape[1] - 1)) == 1:
                ai = Utilities.get_col_index(preconditioned_matrix, i)
                coefs.append(f'a{ai +1}')
            elif (preconditioned_matrix.item(i, preconditioned_matrix.shape[1] - 1)) == 2:
                coefs.append("p")

        return coefs


    def __transform_equation(self, preconditioned_matrix: np.matrix) -> np.matrix:
        # Multiply all the coefs of the equations by -1
        for i in range(0, preconditioned_matrix.shape[0]):
            preconditioned_matrix.itemset(
                (i, preconditioned_matrix.shape[1]-2), preconditioned_matrix.item((i, preconditioned_matrix.shape[1]-2)) * -1)

        # Add the P coef
        p_row = [0] * (preconditioned_matrix.shape[1])
        

        p_row[len(p_row) - 2] = 1
        p_row[len(p_row) - 1] = 2  # Flag hat stands a p coef
        preconditioned_matrix = np.insert(
                    preconditioned_matrix, preconditioned_matrix.shape[0] - 2, p_row, axis=0)

        return preconditioned_matrix


    def __preconditioner(self, formattedInput: np.matrix) -> pd.DataFrame:
        # Adding the artificial and slack variables to the formattedInput matrix
        artificial_variables = []
        slack_variables = []
        for j in range(0, formattedInput.shape[1] - 1):
            item = formattedInput.item((formattedInput.shape[0] - 1, j))
            if item >= 0:
                artificial_variables.append(1)
            else:
                artificial_variables.append(0)

            if item == 0:
                slack_variables.append(0)
            elif item > 0:
                slack_variables.append(-1)
            else:
                slack_variables.append(+1)

        # print("Slack variables:" + str(slack_variables))
        # print("Artificial variables:" + str(artificial_variables))

        # Copy the formattedInput to the preconditioned_matrix (data is backuped in the formattedInput + avoid refrence access)
        preconditioned_matrix = formattedInput.copy()
        
        # Initialize a new column with -1 values (by default) to determine later on
        # if a variable is a slack or artificial variable
        variable_flag_col = []
        for i in range(0, formattedInput.shape[0]):
            variable_flag_col.append([-1])
        preconditioned_matrix = np.append(
            preconditioned_matrix, variable_flag_col, axis=1)

        # print("1st version of the preconditioned matrix:")
        # print(preconditioned_matrix)

        # Initilize default row that is going to modified based on the
        # the slack and artificial variables positions in the system
        new_row = []
        for j in range(0, preconditioned_matrix.shape[1]):
            new_row.append(0)

        # Handling slack variables
        for k in range(0, len(slack_variables)):
            slack_variable_existence = False
            if slack_variables[k] != 0:
                slack_variable_existence = True
                new_row[k] = slack_variables[k]

            if k != 0:
                new_row[k - 1] = 0

            if slack_variable_existence:
                preconditioned_matrix = np.insert(
                    preconditioned_matrix, preconditioned_matrix.shape[0] - 2, new_row, axis=0)
                preconditioned_matrix.itemset(
                    (preconditioned_matrix.shape[0] - 1, k), 0)
        new_row[k] = 0

        # Handling artificial variables
        new_row[len(new_row) - 1] = 1
        for k in range(0, len(artificial_variables)):
            artificial_variable_existence = False
            if artificial_variables[k] != 0:
                artificial_variable_existence = True
                new_row[k] = artificial_variables[k]

            if k != 0:
                new_row[k - 1] = 0

            if artificial_variable_existence:
                preconditioned_matrix = np.insert(
                    preconditioned_matrix, preconditioned_matrix.shape[0] - 2, new_row, axis=0)

        # print("2sec version of the preconditioned matrix:")
        # print(preconditioned_matrix)

        # Adding the P coef + making modifications to max / min equation
        preconditioned_matrix = self.__transform_equation(preconditioned_matrix)
        
        # print("Equation modifications")
        # print(preconditioned_matrix)
       
        # Determining the coefs within our system after adding
        # the slack and artificial variables
        coefs = self.__determine_coefs(preconditioned_matrix)
        # print(coefs)

        # Converting to pandas df for ease of manipulation 
        # and pretty display in jupiter notebook
        preconditioned_matrix_t = preconditioned_matrix.transpose()
        
        # print("The transposed matrix")
        # print(preconditioned_matrix_t)

        preconditioned_df = pd.DataFrame(preconditioned_matrix_t, columns = [*coefs, "condition", "flags"])
        
        # print("The dataframe")
        # print(preconditioned_df)
        
        filtred_cols = preconditioned_df.filter(regex="a\d").columns
        
        # print("Filtered cols")
        # print(filtred_cols)

        for col in filtred_cols:
            preconditioned_df.loc[preconditioned_df.shape[0] -2, [col]] = self.m

        # Drop columns and delete rows that are unnecessary
        preconditioned_df = self.__clean_preconditioned_df(preconditioned_df, [preconditioned_df.shape[0] -1], ["flags"])

        # print("The dataframe after cleaning")
        # print(preconditioned_df)

        return preconditioned_df


    # This method will perform operations between rows to get
    # rid of the Ms in the artificial variables columns
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
        pass


    def runBigM(self, formattedInput: np.matrix) -> Iterations:
        """
        This function solves linear optimisation problems with the Big M method and returns each iteration
        in a seperate matrix.
        Arguments:
            formattedInput: A description matrix generated by BigM.formatUserInput().
        Returns:
            A list of matrices that corresponds to simplex iterations (+ the Big M initial phase of course)
        """       
        try:
            # Formatted input preconditioning 
            preconditioned_df = self.__preconditioner(formattedInput)
            print("Preconditioned DataFrame")
            print(preconditioned_df)
            # preconditioned_df.to_csv("data.csv", index=False)

            # Preparing the matrix for the simplex algorithm
            init_simplex_df = self.__prepare_matrix(preconditioned_df)

            # Running the normal simplex algorithm on the matrix
            iterations: Iterations = super()._perform_simplex(init_simplex_df)

            return iterations
        except:
            print("oops")
            return []