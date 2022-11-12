def FormatUserInput(userInput):
    import re
    """
    The function takes an array of strings representing the input taken and **validated** from a jupyter user.
    The function returns a matrix.
    PS: The function take care of a maximum of 3 variables(x, y, z) in a system i.e. R3.
    Arguments:
        userInput : array of string
    Returns:
        Matrix : array of array of int
    """
    def formatVars(s):
        s = re.sub(' +', '', s.lower()) # remove spaces
        s = re.sub('x', 'x ', s)
        s = re.sub('y', 'y ', s)
        s = re.sub('z', 'z ', s)
        s = re.sub('\+', '', s)
        return s
    
    def formatConstraints(s):
        s = re.sub('>', '', s)
        s = re.sub('<', '', s)
        s = re.sub('=', '', s)
        return s
    
    def castNumbers(inp):
        """
        The function takes a string representing a constraint or objective function
        and returns an array of int.
        Arguments:
            inp : List[str]
        Returns:
            res : List[int]
        """
        res = [0 for _ in range(nbVar + 2)] # variables coefficients + constraint + function
        for var in inp[:-2]:
            idx = 0
            if 'y' in var:
                idx = 1
            if 'z' in var:
                idx = 2
            var = var[:-1]
            if var == '-':
                res[idx] = -1
            elif var == '':
                res[idx] = 1
            else:
                res[idx] = int(var)     
        res[-2] = int(inp[-2]) # constraint row
        res[-1] = int(inp[-1]) # function row
        return res

    def countNumberOfVariables():
        """
        The function counts the number of variables in the provided system.
        PS: Maximum number of variables is 3.
        Parameters:
            None
        Returns:
            nbVar : int
        """
        nbVar = 0
        found = [False for _ in range(3)]
        for i in range(1, len(userInput)):
            if 'x' in userInput[i].lower() and not found[0]:
                nbVar += 1
                found[0] = True
            if 'y' in userInput[i].lower() and not found[1]:
                nbVar += 1
                found[1] = True
            if 'z' in userInput[i].lower() and not found[2]:
                nbVar += 1
                found[2] = True
            if nbVar == 3: # we have all the variables
                return nbVar
        if 'z' in userInput[0].split('=')[1].lower() and not found[2]:
            nbVar += 1
        return nbVar
    
    # sanitize the input by removing all the extra spaces
    for i in range(len(userInput)):
        userInput[i] = re.sub(' +', ' ', userInput[i].strip())

    # get the number of variables
    nbVar = countNumberOfVariables()
    
    # create the matrix
    matrix = [[0 for _ in range(len(userInput))] for _ in range(nbVar + 2)]

    for i in range(1, len(userInput)): # skip the first line for now
        constraint = formatVars(userInput[i]).split(' ')
        if constraint[-1][0] == '>':
            constraint.append('1') # 1 means greater than
        elif constraint[-1][0] == '=':
            constraint.append('0') # 0 means equal to
        else:
            constraint.append('-1') # -1 means less than
        constraint[-2] = formatConstraints(constraint[-2])
        res = castNumbers(constraint)
        for j in range(len(res)):
            matrix[j][i-1] = res[j]
        
    objectiveFunction = userInput[0].lower()
    op = '-1' # minimize by default
    if 'max' in objectiveFunction:
        op = '1' # 1 means maximize
    objectiveFunction = formatVars(objectiveFunction.split('=')[-1])
    objectiveFunction = [*objectiveFunction.split(' ')[:-1], '0', op]

    res = castNumbers(objectiveFunction)
    for i in range(len(res)):
        matrix[i][-1] = res[i] # add the objective function to the matrix
    return matrix


userInput = ["Max Z = 3x+y","x-2y<=2","3x+5y=8"]
matrix = FormatUserInput(userInput)
print(matrix)
