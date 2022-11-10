def UserInputSemanticValidation(objectiveFunction, constraint):
    import re
    """
    Checks whether the input provided by the user is semantically correct or not
    Arguments:
        objectiveFunction : String
        constraint : String
    Returns:
        Boolean
    """
    constraint = constraint.lower()
    objectiveFunction = objectiveFunction.lower().split("=")[-1]
    constraintVariables = ['x' in constraint, 'y' in constraint, 'z' in constraint]
    objectiveFunctionVariables = ['x' in objectiveFunction, 'y' in objectiveFunction, 'z' in objectiveFunction]
    for i in range(len(constraintVariables)):
        if constraintVariables[i] and not objectiveFunctionVariables[i]: # If a variable is present in the constraint but not in the objective function
            return False
    return True

objF = "Max Z = 3x+y"
constraint = "3x+y-z <= 3"
print(UserInputSemanticValidation(objF, constraint)) # False
