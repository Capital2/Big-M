import pandas as pd

Variables = dict[list[str], list[str]]    # example: {"bv": ["x1", "x2"], "nbv": ["s1", "s2"]}
Iteration = dict[pd.DataFrame, Variables] # example: {"matrix": DataFrame, "variables": {"bv": ["x1", "x2"], "nbv": ["s1", "s2"]}}
Iterations = list[Iteration]              # example: [{"matrix": DataFrame, "variables": {"bv": ["x1", "x2"], "nbv": ["s1", "s2"]}}, {"matrix": DataFrame, "variables": {"bv": ["x1", "x2"], "nbv": ["s1", "s2"]}}, {"matrix": DataFrame, "variables": {"bv": ["x1", "x2"], "nbv": ["s1", "s2"]}}]