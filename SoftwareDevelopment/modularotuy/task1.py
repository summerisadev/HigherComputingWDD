# make number do thing

# funct to ask user to input two numbers
def GetInput():
    value1 = int(input('Please enter value 1: '))
    value2 = int(input('Please enter value 2: '))
    return value1, value2

# subrtn to display the answer
def DisplayAnswer(v1,v2):
    total = v1+v2
    print(f'{v1} + {v2} = {total}')

# main program
number1,number2 = GetInput()
DisplayAnswer(number1,number2)