import numpy as np
import pandas as pd
from aliases import Iterations, Variables, Variable
from utilities import Utilities
# from sympy import solve, Eq, symbols

pd.options.mode.chained_assignment = None


class Simplex():

    def __select_vars(self, init_simplex_df: pd.DataFrame) -> tuple[Variables, Variables]:
        """
        Selects the basic and non-basic variables from the initial simplex dataframe.
        """
        # TODO: what if 2 variables have the only non-zero value in the same row? which one to select?
        ret_vars = ([], [])
        for col in init_simplex_df.columns:
            if col in ['condition', 'p']:  # skip the condition and p columns
                continue
            column = init_simplex_df.loc[:, col]
            # basic variable (i.e. have only 1 non zero value)
            if column[column != 0].count() == 1:
                # get the row index of the non-zero value
                nonZeroRow = column[column != 0].index[0]
                ret_vars[0].append(
                    (col, init_simplex_df.loc[nonZeroRow]['condition'], nonZeroRow))
            else:  # non basic variable
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

    def __find_equation_coef(self, iteration: pd.DataFrame) -> dict:
        equation: pd.Series = iteration.iloc[-1]
        equation = equation.drop(
            labels=["condition", "p", "ratio", "operations"])

        # equation = equation.apply(abs)
        equation = equation.astype('float64')
        min_coef_index = equation.argmin()

        return {
            "row": iteration.shape[0] - 1,
            "col": min_coef_index,
            "col_name": iteration.columns[min_coef_index]
        }

    def __find_min_ratio(self, iteration: pd.DataFrame) -> int:
        ratio = iteration["ratio"]
        ratio = ratio.drop(ratio.size - 1)  # potential pb at this line
        min_index = ratio.argmin()
        return min_index

    def __calculate_ratio(self, row: pd.Series, coef_position: dict) -> pd.Series:
        try:
            if row.name != coef_position["row"]:
                return (row["condition"] / row[coef_position["col_name"]])
            else:
                return (0)
        except ZeroDivisionError:
            return (float('inf'))

    def __transform_pivot_row(self, iteration: pd.DataFrame, pivot: dict) -> pd.DataFrame:
        iteration["operations"][pivot["position"]
                                ["row"]] = f'LP<-(1/{pivot["value"]})*LP'
        for j in range(0, iteration.shape[1] - 2):
            iteration.iloc[pivot["position"]["row"],
                           j] = iteration.iloc[pivot["position"]["row"], j] / pivot["value"]

        return iteration

    def __transform_pivot_columns(self, iteration: pd.DataFrame, pivot: dict) -> pd.DataFrame:
        for i in range(0, iteration.shape[0]):
            if i != pivot["position"]["row"] and iteration.iloc[i, pivot["position"]["col"]] != 0:
                pivot_row_coef = iteration.iloc[i, pivot["position"]["col"]]

                tmp_pivot_row = iteration.iloc[pivot["position"]["row"]]
                tmp_pivot_row = tmp_pivot_row.drop(
                    labels=["ratio", "operations"])
                tmp_pivot_row = tmp_pivot_row.apply(
                    lambda item: item * pivot_row_coef * -1)
                for j in range(0, tmp_pivot_row.size):
                    iteration.iloc[i, j] = iteration.iloc[i,
                                                          j] + tmp_pivot_row[j]

                iteration["operations"][i] = f'L{i}<-L{i}+({pivot_row_coef *-1}*LP)'

        return iteration

    def __reset_operations(self, iteration: pd.DataFrame) -> pd.DataFrame:
        iteration["operations"] = "DEFAULT"
        return iteration

    def __verify(self, iteration: pd.DataFrame) -> bool:
        done = True
        equation_row = iteration.shape[0] - 1
        cols = iteration.shape[1]
        for j in range(0, cols - 2):
            if iteration.iloc[equation_row, j] < 0:
                done = False
                break

        return done

    def __find_variable_by_equation_index(self, associated_equation: int, variables: Variables) -> Variable | None:
        target_variable: Variable = None
        for variable in variables:
            if variable[2] == associated_equation:
                target_variable = variable
                break

        return target_variable

    def __find_variable_by_name(self, name: str, variables: Variables) -> Variable:
        target_variable: Variable = None
        for variable in variables:
            if variable[0] == name:
                target_variable = variable
                break

        return target_variable

    def __update(self, iteration: pd.DataFrame, basic_variables: Variables) -> Variables:
        updated_basic_variables = []
        for variable in basic_variables:
            updated_basic_variables.append(
                (variable[0], iteration['condition'][variable[2]], variable[2]))
        return updated_basic_variables

    def _perform_simplex(self, init_simplex_df: pd.DataFrame) -> Iterations:
        variables = self.__select_vars(init_simplex_df)
        exist = self.__verify_solution_existence(variables)
        if not exist:
            raise ValueError('SIMPLEX_SOLULTION_DOES_NOT_EXIST,')

        bv = variables[0]
        nbv = variables[1]

        iteration = init_simplex_df.copy()
        ratio = [0] * iteration.shape[0]
        operations = ["DEFAULT"] * iteration.shape[0]
        iteration['ratio'] = ratio
        iteration['operations'] = operations
        iterations: Iterations = []
        iterations.append((iteration.copy(), bv, nbv))
        
        iterations_nbr = 0
        done = False
        while not done:

            # Utilities.debug(iteration, "Iteration at the start")

            iterations_nbr+= 1
            if iterations_nbr == 100 and not done:
                raise ValueError('Le programme linéaire ne converge pas.')
            # Utilities.debug(iteration, "Iteration at the start")


            # Determine the max coef position
            coef_position = self.__find_equation_coef(iteration)
            # Utilities.debug(coef_position, "The coef position")

            # Calculating ratio
            iteration["ratio"] = iteration.apply(
                self.__calculate_ratio, axis=1, args=[coef_position])
            iteration = iteration.round(5)
            # Utilities.debug(iteration, "After calculating the ratio")

            # Determine the min ratio position
            min_ratio_position = {
                "col_name": "ratio",
                "col": iteration.shape[1] - 1,
                "row": self.__find_min_ratio(iteration)
            }

            pivot_position = {
                "col": coef_position["col"],
                "row": min_ratio_position["row"]
            }

            pivot = {
                "value": iteration.iloc[pivot_position["row"], pivot_position["col"]],
                "position": pivot_position
            }
            # Utilities.debug(pivot, "calculating pivot + position")

            # Perform a transformation of the pivot row to make the pivot value equals to one
            iteration = self.__transform_pivot_row(iteration, pivot)
            iteration = iteration.round(5)
            # Utilities.debug(iteration, "Making the pivot row to 1")

            # Updating the pivot value
            pivot = {
                **pivot,
                "value": 1
            }

            # Perform transformations on the other rows to make all the values of the pivot column
            # except the pivot equal to zero
            iteration = self.__transform_pivot_columns(iteration, pivot)
            # Utilities.debug(iteration, "making the pivot to zeros")

            # Verify if we hit the final iteration of the simplex algorithm
            done = self.__verify(iteration)
            # Utilities.debug(done, "simplex stop flag")

            # Update basic and non basic variables and the iterations list
            bv = self.__update(iteration, bv)

            # Finding the variable that is going to leave the basic variables
            out_variable = self.__find_variable_by_equation_index(
                pivot["position"]["row"], bv)

            # Creation of the variable that is going to be added to the basic variables
            in_variable = (iteration.columns[pivot["position"]["col"]],
                           iteration["condition"][out_variable[2]], out_variable[2])

            bv.remove(out_variable)
            nbv.append((out_variable[0], 0, -1))

            nbv.remove(self.__find_variable_by_name(in_variable[0], nbv))
            bv.append(in_variable)

            # Utilities.debug(iteration, "Iteration at the end")
            iterations.append((iteration.copy(), bv, nbv))

            iteration = self.__reset_operations(iteration)

        return iterations