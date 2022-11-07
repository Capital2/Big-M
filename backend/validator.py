import re
def validateInput(input):

    #remove white spaces from the input string
    strippedInput =""
    for i in input:
        if(i !=" "):
            strippedInput = strippedInput + i
    
    #match regEx for constraints
    matchConstraint = re.findall("^[-]{0,1}[0-9]+[x|X][+|-][0-9]+[y|Y]([+][0-9]+[z|Z]){0,1}[<|>]{0,1}[=]{0,1}[0-9]+$",strippedInput)
    if(len(matchConstraint)!=0):
        return True
    
     #match regEx for gain
    matchGain = re.findall("^(Max|max|Min|min)[Z|z|W|w][=][-]{0,1}[0-9]+[x|X][+|-][0-9]+[y|Y]([+|-][0-9]+[z|Z]){0,1}",strippedInput)
    if(len(matchGain)!=0):
        return True
   
    return False