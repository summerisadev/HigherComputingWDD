def GetPhoneNumber():
    number = input("Enter mobile phone number: ")
    number = number.replace(" ","")
    while len(number) != 11:
        print("Invalid phone number | Format: 07840 235678")
        number = input("Enter mobile phone number: ")
        number = number.replace(" ","")

    return number

def InternationalNumberFormatter(fNum):
    num = fNum[1:]
    numleft, numright = num[:4], num[4:]
    print(f'+44 {numleft} {numright}')

num = GetPhoneNumber()
InternationalNumberFormatter(num)