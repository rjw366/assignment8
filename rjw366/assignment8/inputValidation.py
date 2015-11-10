'''
Created on Nov 10, 2015

@author: rjw366

Validates input for the investment assignment
'''

def positionValidation(positionInput):
    positionInput.replace(" ","")
    if(not positionInput[0] == "["):
        raise ValueError("First character must be [")
    if(not positionInput[-1] == "]"):
        raise ValueError("Last character must be ]")
    positionsList = list(map(int, positionInput[1:-1].split(',')))
    for i in positionsList:
        if(not isNumber(i)):
            raise ValueError("Not all values in positions are numbers")
    return positionsList
        
        
def numTrialValidation(numTrialsInput):
    if(not isNumber(numTrialsInput)):
        raise ValueError("This is not a number")
    if(int(numTrialsInput) < 1):
        raise ValueError("Number of trials must be positive")
    return numTrialsInput
    
def isNumber(testingNumber):
    try:
        int(testingNumber)
        return True
    except:
        return False