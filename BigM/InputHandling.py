import re

def validateUserInputSemantic(objectiveFunction, constraint):
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

def formatUserInput(userInput):
    """
    The function takes an array of strings representing the input taken and **validated** from a jupyter user.
    PS: The function take care of a maximum of 3 variables(x, y, z) in a system i.e. R3.
    Arguments:
        userInput : List[str]
    Returns:
        Matrix : List[List[int]]
    """
    def formatVars(s):
        s = re.sub(' +', '', s.lower()) # remove white spacess
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
        The function takes a string representing a constraint or objective function.
        Arguments:
            inp : str
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
        constraints = "".join(userInput[1:]).lower()
        return ('x' in constraints) + ('y' in constraints) + ('z' in constraints)
    
    # sanitize the input by removing all the extra spaces
    for i in range(len(userInput)):
        userInput[i] = re.sub(' +', ' ', userInput[i].strip())

    # get the number of variables
    nbVar = countNumberOfVariables()
    
    # create the matrix
    matrix = [[0 for _ in range(len(userInput))] for _ in range(nbVar + 2)]

    for i in range(1, len(userInput)): # skip the first line for now
        constraint = formatVars(userInput[i]).split(' ')
        flag = '0' # 0 means equal to
        if constraint[-1][0] == '>':
            # 2 means >= and 1 means >
            flag = '2' if constraint[-1][1] == '=' else '1'
        elif constraint[-1][0] == '<':
            # -2 means <= and -1 means <
            flag = '-2' if constraint[-1][1] == '=' else '-1'
        constraint.append(flag)
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

def validateUserInput(input):
    '''
    Validate user input, check if the objectif or the constraint is valid 
    '''
    #remove white spaces from the input string
    strippedInput = re.sub(' ','', input.lower())

    #get occurence of each variable
    occurenceOfX =re.sub('(max|min)[a-z]','',strippedInput).count("x")
    occurenceOfY=re.sub('(max|min)[a-z]','',strippedInput).count("y")
    occurenceOfZ =re.sub('(max|min)[a-z]','',strippedInput).count("z")

    #check if each variable exist once at most
    if(occurenceOfX > 1 or occurenceOfY > 1 or occurenceOfZ > 1):
        return False
   
    #match regEx for constraints
    matchConstraint = re.findall("^[-]{0,1}[0-9]*[x|y|z|]([+|-][0-9]*[x|y|z])*(<|>|<=|>=|=)[-]{0,1}[0-9]+$",strippedInput)
    if(len(matchConstraint)!=0):
        return True
    
     #match regEx for gain
    matchGain = re.findall("^(max|min)[a-zA-Z][=][-]{0,1}[0-9]*[x|y|z][+|-][0-9]*[x|z|y]([+|-][0-9]*[x|y|z]){0,1}$",strippedInput)
    if(len(matchGain)!=0):
        return True
   
    return False
