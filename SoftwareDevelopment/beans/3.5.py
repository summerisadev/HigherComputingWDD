def ReadFile():
    counter = 0
    loopCounter = 0
    CarRegArray = []
    DatesArray = []
    EntryTimeArray = []
    ExitTimeArray = []

    with open('SoftwareDevelopment/datafiles/Times.csv', "r") as f:
        line = f.readline().rstrip('\n')
        while line:
            items = line.split(',')
            print(f'Car "{items[0]}" Read In')
            line = f.readline().rstrip('\n')

            CarRegArray.append(items[0])
            DatesArray.append(items[1])
            EntryTimeArray.append(items[2])
            ExitTimeArray.append(items[3])
            
            loopCounter += 1

            

        items = line.split(',')
                
        

    return(CarRegArray,DatesArray,EntryTimeArray,ExitTimeArray)

def CalculatePricing(CarRegArray, EntryTimeArray, ExitTimeArray):
    print('Starting Calculations...')
    counter = 0
    for i in CarRegArray:
        print(f'Car Reg: {CarRegArray[counter]}\nEntry Time: {EntryTimeArray[counter]}\n')
        counter += 1

CRA,DA,EntryTA,ExitTA = ReadFile()
CalculatePricing(CRA, EntryTA, ExitTA)