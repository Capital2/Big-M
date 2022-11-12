import re
def ValidateUserInput(input):
    '''
    Validate user input, check if the objectif or the constraint is valid 
    '''
    #remove white spaces from the input string
    strippedInput = re.sub(' ','', input.lower())

    print(strippedInput)
    #get occurence of each variable
    occurenceOfX =re.sub('(max|min)[a-z]','',strippedInput).count("x")
    occurenceOfY=re.sub('(max|min)[a-z]','',strippedInput).count("y")
    occurenceOfZ =re.sub('(max|min)[a-z]','',strippedInput).count("z")

    #check if each variable exist once at most
    if(occurenceOfX > 1 or occurenceOfY > 1 or occurenceOfZ > 1):
        return False
   
    #match regEx for constraints
    matchConstraint = re.findall("^[-]{0,1}[0-9]*[x|y|z|]([+|-][0-9]*[x|y|z])*(<|>|<=|>=|=)[0-9]+$",strippedInput)
    if(len(matchConstraint)!=0):
        return True
    
     #match regEx for gain
    matchGain = re.findall("^(max|min)[a-zA-Z][=][-]{0,1}[0-9]*[x|y|z][+|-][0-9]*[x|z|y]([+|-][0-9]*[x|y|z]){0,1}$",strippedInput)
    if(len(matchGain)!=0):
        return True
   
    return False