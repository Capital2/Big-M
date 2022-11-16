import pandas as pd

Variable = dict[str, float]                         
# example: {"name": "x1": "value": 3.0}

Variables = dict[list[Variable], list[Variable]]    
# example: {"bv": [{"name": "x1": "value": 3.0}, {"name": "x2": "value": 2.0}], "nbv": [{"name": "s1": "value": 0}, {"name": "s2": "value": 0}]}

Iteration = dict[pd.DataFrame, Variables] 
# example: {"matrix": DataFrame, "variables": {"bv": [{"name": "x1": "value": 3.0}, {"name": "x2": "value": 2.0}], "nbv": [{"name": "s1": "value": 0}, {"name": "s2": "value": 0}]}}

Iterations = list[Iteration]              
# example: [
# {"matrix": DataFrame, "variables": {"bv": [{"name": "x1": "value": 3.0}, {"name": "x2": "value": 2.0}], "nbv": [{"name": "s1": "value": 0}, {"name": "s2": "value": 0}]}},
# {"matrix": DataFrame, "variables": {"bv": [{"name": "x1": "value": 3.0}, {"name": "x2": "value": 2.0}], "nbv": [{"name": "s1": "value": 0}, {"name": "s2": "value": 0}]}},
# ...
# ]
