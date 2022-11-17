import pandas as pd

Variables = dict[str, float | int]                         
# example: {"name": "x1": "value": 3.0}

Iteration = tuple[pd.DataFrame, Variables, Variables]
# example: (simplex_df, basic_vars, non_basic_vars)
# example: (DataFrame, {"name": "x1": "value": 3.0}, {"name": "s1": "value": 0})


Iterations = list[Iteration]              
# example: [
# (DataFrame, {"name": "x1": "value": 3.0}, {"name": "s1": "value": 0}),
# (DataFrame, {"name": "x1": "value": 3.0}, {"name": "s1": "value": 0})
# ...
# ]