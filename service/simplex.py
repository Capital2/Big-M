import numpy as np
import pandas as pd
from aliases import Iterations, Variables
from utilities import Utilities


class Simplex():

    def __select_vars(self, init_simplex_df: pd.DataFrame) -> Variables:
        pass

    def __verify_solution_existence(self, variables: Variables) -> bool:
        exist: bool = True
        return exist

    def __find_equation_coef(self, iteration: pd.DataFrame) -> dict:
        equation: pd.Series = iteration.iloc[-1]
        equation = equation.drop(
            labels=["condition", "p", "ratio", "operations"])

        # equation = equation.apply(abs)
        equation = equation.astype('float64')
        print("equation")
        print(equation)
        min_coef_index = equation.argmin()

        return {
            "row": iteration.shape[0] - 1,
            "col": min_coef_index,
            "col_name": iteration.columns[min_coef_index]
        }

    def __find_min_ratio(self, iteration: pd.DataFrame) -> int:
        ratio = iteration["ratio"]
        ratio = ratio.drop(ratio.size - 1)
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
                                ["row"]] = f'LP <- (1/{pivot["value"]})*LP'
        for j in range(0, iteration.shape[1] - 2):
            iteration.iloc[pivot["position"]["row"],
                           j] = iteration.iloc[pivot["position"]["row"], j] / pivot["value"]

        return iteration

    def __transform_pivot_columns(self, iteration: pd.DataFrame, pivot: dict) -> pd.DataFrame:
        for i in range(0, iteration.shape[0]):
            if i != pivot["position"]["row"] and iteration.iloc[i, pivot["position"]["col"]] != 0:
                pivot_row_coef = iteration.iloc[i,
                                                pivot["position"]["col"]] / pivot["value"]
                tmp_pivot_row = iteration.iloc[pivot["position"]["row"]]
                tmp_pivot_row = tmp_pivot_row.drop(
                    labels=["ratio", "operations"])
                tmp_pivot_row = tmp_pivot_row.apply(
                    lambda item: item * pivot_row_coef * -1)
                for j in range(0, tmp_pivot_row.size):
                    iteration.iloc[i, j] = iteration.iloc[i,
                                                          j] + tmp_pivot_row[j]

                iteration["operations"][i] = f'L{i} <- L{i} + ({pivot_row_coef *-1}*LP)'

        print("===============================")
        print(iteration)
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

    def _perform_simplex(self, init_simplex_df: pd.DataFrame) -> Iterations:
        # variables: Variables = self.__select_vars(init_simplex_df)
        # exist = self.__verify_solution_existence(variables)
        # if not exist:
        #     raise ValueError('SIMPLEX_SOLULTION_DOES_NOT_EXIST,')

        # init_iteration = {
        #     "matrix": DataFrame, "variables": {"bv": [{"name": "x1": "value": 3.0}, {"name": "x2": "value": 2.0}], "nbv": [{"name": "s1": "value": 0}, {"name": "s2": "value": 0}]}
        #     }

        # Test
        init_simplex_df = pd.read_csv("simplex_data.csv")

        iteration = init_simplex_df.copy()
        ratio = [0] * iteration.shape[0]
        operations = ["DEFAULT"] * iteration.shape[0]
        iteration['ratio'] = ratio
        iteration['operations'] = operations
        iterations: Iterations = []
        done = False
        while not done:
            # Determine the max coef position
            coef_position = self.__find_equation_coef(iteration)

            # Calculating ratio
            # iteration["ratio"] = iteration.apply(lambda row: row["condition"] / row[coef_position["col_name"]] if row.name != coef_position["row"] else 0,
            #                                      axis=1 )
            iteration["ratio"] = iteration.apply(
                self.__calculate_ratio, axis=1, args=[coef_position])

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

            # Perform a transformation of the pivot row to make the pivot value equals to one
            iteration = self.__transform_pivot_row(iteration, pivot)

            # Perform transformations on the other rows to make all the values of the pivot column
            # except the pivot equal to zero
            iteration = self.__transform_pivot_columns(iteration, pivot)

            # Verify if we hit the final iteration of the simplex algorithm
            done = self.__verify(iteration)

            # Update basic and non basic variables and the iterations list
            # ...

            iteration = self.__reset_operations(iteration)
            input('type something to coninue ...')

        return iterations
