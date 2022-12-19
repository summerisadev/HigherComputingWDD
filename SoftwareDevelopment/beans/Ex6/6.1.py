import random

def GeneratePositions(memWord):
    maxLen = len(memWord)
    num1 = random.randint(0, maxLen)
    num2 = random.randint(0, maxLen)
    while num1 == num2:
        num2 = random.randint(0, maxLen)

    return num1,num2,maxLen

def GatherUserInput(num1,num2,maxLen,memWord):
    uInt1 = input(f'Enter charachter at position {num1+1}: ')
    uInt2 = input(f'Enter charachter at position {num2+1}: ')

    return uInt1,uInt2

def ValidateUserInput(num1,num2,uInt1,uInt2,memWord):
    check1 = False
    check2 = False

    if memWord[num1] == uInt1:
        check1 = True
    if memWord[num2] == uInt2:
        check2 = True

    if check1 == True and check2 == True:
        print('User authenticated!')
    else:
        print('Error. Unable to authenticate - please retry.')

memWord = 'doorjamb'
num1,num2,maxLen = GeneratePositions(memWord)
uInt1,uInt2 = GatherUserInput(num1, num2, maxLen, memWord)
ValidateUserInput(num1, num2, uInt1, uInt2, memWord)