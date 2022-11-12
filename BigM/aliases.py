import pandas as pd

Variable = tuple[str, int | float, int]
# example: ("x1", "5.0", 2) x1 with value of 5.0 belongs to the second equation

Variables = list[Variable]
# example: [("x1", "5.0", 2), ("x1", "5.0", 2)]

Iteration = tuple[pd.DataFrame, Variables, Variables]
# example: (DataFrame, [("x1", "5.0", 2), ("x1", "5.0", 2)], [("s1", "0", 1), ("s2", "5.0", 4)])

Iterations = list[Iteration]
# example: [
# (DataFrame, [("x1", "5.0", 2), ("x1", "5.0", 2)], [("s1", "0", 1), ("s2", "5.0", 4)]),
# (DataFrame, [("x1", "5.0", 2), ("x1", "5.0", 2)], [("s1", "0", 1), ("s2", "5.0", 4)]),
# ...
# ]
