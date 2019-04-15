def badInput(reason):
    print("Input must be a valid real number, expressed as a decimal")
    print(reason)

def isValidInput(string):
    print(string)
    periodCount = 0
    for char in string:
        if not(char.isdigit()):
            if char == ".":
                periodCount += 1
            else: #The character is neither a digit or a decimal place
                badInput(char + "is not a digit!")
                return False
    if periodCount > 1:
        badInput("Too many decimal points!")
        return False
    return True

def getLocationOfDecimal(strNumber): #strNumber is a string representation of a number. This function returns the index of the decimal place
    for i in range(0, len(strNumber)):
        if strNumber[i] == ".":
            if i == len(strNumber) - 1: #if the decimal is the last character
                return len(strNumber)
            else:
                return i
    return len(strNumber)

def moveDecimalRight(strNumber, numPlaces): #Input is a string representation of a number and a positive integer representing the number of places the decimal place should be moved. Returns the string with the decimal moved
    result = strNumber.replace(".", "") #Remove the decimal place from the passed in strNumber
    previousDecimalLocation = getLocationOfDecimal(strNumber)
    newDecimalLocation = previousDecimalLocation + numPlaces
    if newDecimalLocation > len(result): #If the new decimal place must go past the length of the string, we append as many zeros as needed onto the end of the result
        result += "0" * (newDecimalLocation - len(result))
    if newDecimalLocation != len(result): #So long as the period won't just be tacked on the end
        result = result[:newDecimalLocation] + "." + result[newDecimalLocation:] #Insert the decimal where it belongs
    return result

def divisionAlgorithm(numeratorS, denominatorS, numberOfDigits):
    if "." in numeratorS or "." in denominatorS:
        normalizingDistance = max(len(numeratorS) - getLocationOfDecimal(numeratorS), len(denominatorS) - getLocationOfDecimal(denominatorS)) - 1 #Find which string needs to have the most decimal places moved
        numeratorS = moveDecimalRight(numeratorS, normalizingDistance) #Multiply both the numerator and denominator until both are a whole number
        denominatorS = moveDecimalRight(denominatorS, normalizingDistance)
    numeratorI = int(numeratorS)
    denominatorI = int(denominatorS)
    decimalInserted = False
    result = "" #This will hold the string that is returned
    endIndex = 1 #Holds the position of how far we've cut into the numerator
    while(int(int(numeratorS[0:endIndex]) / denominatorI) == 0):
        endIndex += 1
        if endIndex > len(numeratorS):
            if not(decimalInserted):
                decimalInserted = True
                result += "0." #Add the decimal place
            numeratorS += "0"
            calculatedDigit = int(int(numeratorS[0:endIndex]) / denominatorI) #This variable will hold the digit that was just calculated\
            result += str(calculatedDigit) #Add first calculated digit to result

    if not(decimalInserted):
        calculatedDigit = int(int(numeratorS[0:endIndex]) / denominatorI) #This variable will hold the digit that was just calculated\
        result += str(calculatedDigit) #Add first calculated digit to result
    #print(result) #This is working, at least. It increments the endIndex until the denominator can go into the numerator

    tempNumerator = numeratorS[0:endIndex]
    while len(result) < numberOfDigits:
        tempNumerator = str(int(tempNumerator[0:endIndex]) - calculatedDigit * denominatorI)
        endIndex += 1
        if endIndex > len(numeratorS):
            if not(decimalInserted):
                decimalInserted = True
                result += "." #Add the decimal place
            tempNumerator += "0"
        else:
            tempNumerator += numeratorS[endIndex - 1:endIndex] #Append the next digit from the numerator on
        calculatedDigit = int(int(tempNumerator) / denominatorI)
        result += str(calculatedDigit)
        #print(result)
    return result


#MAIN
while (True): #The following emulates a do-while loop in Python
    numerator = input("Enter the numerator: ")
    if (isValidInput(numerator)):
        break
    badInput("")
while (True):
    denominator = input("Enter the denominator: ")
    if (isValidInput(denominator)):
        break
    badInput("")
numDigits = int(input("How many digits would you like to calcuate this division to?"))

print(divisionAlgorithm(numerator, denominator, numDigits))
