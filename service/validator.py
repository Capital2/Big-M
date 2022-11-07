import re
input = "MaX Z = 3X+Y+80z"
def ValidateUserInput(input):
    '''
    Validate user input, check if the objectif or the constraint is valid 
    '''
    #remove white spaces from the input string
    strippedInput =""
    for i in input:
        if(i !=" "):
            strippedInput = strippedInput + i
    
    strippedInput = strippedInput.lower()
    
    #get occurence of each variable
    occurenceOfX =len(re.findall("[^a-zA-Z]x",strippedInput))
    occurenceOfY = len(re.findall("y",strippedInput))
    occurenceOfZ = len(re.findall("[^a-zA-Z]z",strippedInput))

    #check if each variable exist once at most
    if(occurenceOfX > 1 or occurenceOfY > 1 or occurenceOfZ > 1):
        return False
   
    #match regEx for constraints
    matchConstraint = re.findall("^[-]{0,1}[0-9]*[x|y|z|]([+|-][0-9]*[x|y|z])*[<|>]{0,1}[=]{0,1}[0-9]+$",strippedInput)
    if(len(matchConstraint)!=0):
        return True
    
     #match regEx for gain
    matchGain = re.findall("^(max|min)[a-zA-Z][=][-]{0,1}[0-9]*[x][+|-][0-9]*[y]([+|-][0-9]*[z]){0,1}$",strippedInput)
    if(len(matchGain)!=0):
        return True
   
    return False
