import sys

def b(str):
    print("in b")
    str = removeWhiteSpace(str)
    boolVal, str = it(str)
    if (str[0] == '.'):
        print(boolVal)
        return boolVal

def it(str):
    print("in it")
    str = removeWhiteSpace(str)
    boolVal, str = ot(str)
    return itTail(boolVal, str)

def itTail(boolValLeft, str):
    print("in ittail")
    print("this is the str in itTail " + str)
    str = removeWhiteSpace(str)
    print("string in itTail is " + str)
    if (str[0] in ".)"):
        return boolValLeft, str
    elif (str[0] == '-'):
        if (str[1].isspace()):
            printError("Space between - and > not allowed")
        if (str[1] == '>'):
            boolValRight, str = ot(str[2:])
            if ((boolValLeft and (not boolValRight)) or
                ((not boolValLeft) and boolValRight) or
                (not boolValLeft) and (not boolValRight)):
                boolValLeft = True
                return boolValLeft, str
            elif (boolValLeft and (not boolValRight)):
                boolValLeft = False
                return boolValLeft, str
            # else:
            #     printError("Extraneous symbol after >")
            return itTail(boolValLeft, str)
        else:
            printError("Extraneous symbol after -")
    else:
        printError("Expected a closing character such as . or )")

def ot(str):
    print("in ot")
    str = removeWhiteSpace(str)
    boolVal, str = at(str)
    return otTail(boolVal, str)

def otTail(boolValLeft, str):
    print("in otTail")
    str = removeWhiteSpace(str)
    print("str in otTail is " + str[0])
    if ((str[0] in ".)") or (str[:2] == "->")):
        return boolValLeft, str
    # else:
    #     printError("Expected closing character . or ) or implication ->")
    if (str[0] == 'v'):
        boolValRight, str = at(str[1:])
        boolValLeft = boolValLeft or boolValRight
        return otTail(boolValLeft, str)
    else:
        printError("Expected a 'v'")

def at(str):
    print("in at")
    str = removeWhiteSpace(str)
    boolVal, str = l(str)
    return atTail(boolVal, str)

def atTail(boolValLeft, str):
    print("in atTail")
    str = removeWhiteSpace(str)
    print("str in atTail is " + str)
    if ((str[0] in "v.)") or (str[:2] == "->")):
        return boolValLeft, str
    # else:
    #     printError("Expected v, ., ), or ->")
    if(str[0] == '^'):
        boolValRight, str = l(str[1:])
        boolValLeft = boolValLeft and boolValRight
        return atTail(boolValLeft, str)
    else:
        printError("Expected a '^'")

def l(str):
    print("in l")
    str = removeWhiteSpace(str)
    if (str[0] == '~'):
        boolVal, str = a(str[1:])
        boolVal = not boolVal
    else:
        boolVal, str = a(str)
    return boolVal, str

def a(str):
    print("in a")
    str = removeWhiteSpace(str)
    if (str[0] == '('):
        boolVal, str = it(str[1:])
        if (str[0] == ')'):
            return boolVal, str[1:]
        else:
            printError("Missing ) to close statement")
    print(str)
    if (str[0] == 'T'):
        return True, str[1:]
    elif (str[0] == 'F'):
        return False, str[1:]
    else:
        printError("Unknown character")

def printError(strError):
    print(strError)
    sys.exit()

def removeWhiteSpace(str):
    if (not (str[0].isspace())):
        return str
    else:
        return removeWhiteSpace(str[1:])

strUserIn = raw_input("Enter a T/F expression: \n")

b(strUserIn)
