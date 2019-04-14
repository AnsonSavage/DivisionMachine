def badInput():
    print("Input must be a valid real number, expressed as a decimal")

def isValidInput(string):
    print(string)
    periodCount = 0
    for s in string:
        if not(s.isdigit()):
            if s == ".":
                periodCount += 1
            else:
                print(s + "is not a digit!")
                return False
    if periodCount > 1:
        print("Too many decimal points!")
        return False
    return True

def getLocationOfDecimal(string):
    for i in range(0, len(string)):
        if string[i] == ".":
            if i == len(string) - 1: #if the decimal is the last character
                return len(string)
            else:
                return i
    return len(string)

def moveDecimalRight(string, numPlaces):
    currentDecimalLocation = getLocationOfDecimal(string)
    newString = ""
    if currentDecimalLocation == len(string): #If the decimal place is at the end of the string, just add zeros
        newString = string[0:currentDecimalLocation] + ("0" * numPlaces)
        return newString
    else:
        newString = string[0:currentDecimalLocation] + string[currentDecimalLocation + 1: currentDecimalLocation + 1 + numPlaces] + "." + string[currentDecimalLocation + numPlaces + 1: len(string)]
    currentDecimalLocation = getLocationOfDecimal(newString) #To increase efficiency, you should be able to do if newString[len(newString) - 1] == ".":
    if currentDecimalLocation == len(newString):#After shifting the decimal place, if it's not at the end
        newString = newString[0:len(newString) - 1] #Chop off the decimal place at the end
    return newString

def divisionAlgorithm(numeratorS, denominatorS, numberOfDigits):
    print("Location of " + numeratorS + " decimal place is " + str(getLocationOfDecimal(numeratorS)))
    print("Moving the decimal place over, we have: " + moveDecimalRight(numeratorS, len(numeratorS) - 1 - getLocationOfDecimal(numeratorS)))
    if "." in numeratorS or "." in denominatorS:
        while "." in numeratorS or "." in denominatorS: #getLocationOfDecimal(numeratorS) != len(numeratorS) and getLocationOfDecimal(denominatorS) != len(denominatorS):
            #print(numeratorS, denominatorS)
            numeratorS = moveDecimalRight(numeratorS, 1)
            denominatorS = moveDecimalRight(denominatorS, 1)
            #print(numeratorS, denominatorS)
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
    badInput()
while (True):
    denominator = input("Enter the denominator: ")
    if (isValidInput(denominator)):
        break
    badInput()
numDigits = int(input("How many digits would you like to calcuate this division to?"))

print(divisionAlgorithm(numerator, denominator, numDigits))
