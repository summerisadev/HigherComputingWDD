from time import sleep


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
            # print(f'Car "{items[0]}" Read In')
            line = f.readline().rstrip('\n')

            CarRegArray.append(items[0])
            DatesArray.append(items[1])
            EntryTimeArray.append(items[2])
            ExitTimeArray.append(items[3])

            loopCounter += 1

        items = line.split(',')

    return (CarRegArray, DatesArray, EntryTimeArray, ExitTimeArray)


def CalculatePricing(CarRegArray, EntryTimeArray, ExitTimeArray, PriceTable):
    ChargesArray = []

    print('Processing car entry/exit times...')
    print(f'\n----- Current Parking Charges -----\nUp to 1hr: {PriceTable.get("1hr")}\nUp to 2hrs: {PriceTable.get("2hrs")}\n2hrs to 3hrs: {PriceTable.get("2hrs-3hrs")}\n3hrs to 4hrs: {PriceTable.get("3hrs-4hrs")}\nUp to 12hrs: {PriceTable.get("12hrs")}\nOver 12hrs: {PriceTable.get("ovr12hrs")}\n----- Current Parking Charges -----\n')

    sleep(3)

    counter = 0
    for i in CarRegArray:
        EntryTime = float(EntryTimeArray[counter])
        ExitTime = float(ExitTimeArray[counter])
        Difference = round(ExitTime-EntryTime, 1)

        print(f'Car Reg: {CarRegArray[counter]}\nEntry Time: {EntryTimeArray[counter]}\nDifferent (E2E): {Difference}\n')

        if Difference <= 1:
            # print(f'{CarRegArray[counter]} less than an hour')
            ChargesArray.append(PriceTable.get('1hr'))
        elif Difference <=2:
            # print(f'{CarRegArray[counter]} less than two hour')
            ChargesArray.append(PriceTable.get('2hrs'))
        elif Difference >=2 and Difference <=3:
            # print(f'{CarRegArray[counter]} less than tree hour, but kore than two')
            ChargesArray.append(PriceTable.get('2hrs-3hrs'))
        elif Difference >=3 and Difference <=4:
            # print(f'{CarRegArray[counter]} less than for hour, but kore than three')
            ChargesArray.append(PriceTable.get('3hrs-4hrs'))
        elif Difference <=12:
            # print(f'{CarRegArray[counter]} less than 12 hour')
            ChargesArray.append(PriceTable.get('12hrs'))
        elif Difference > 12:
            # print(f'{CarRegArray[counter]} more than 12 hour')
            ChargesArray.append(PriceTable.get('ovr12hrs'))

        sleep(0.15)
        counter += 1

    return ChargesArray

def WriteCharges(CarRegArray, EntryTimeArray, ExitTimeArray, DatesArray, ChargesArray):
    counter = 0
    with open('SoftwareDevelopment/datafiles/CarParkingCharges.csv', "w") as f:
        for i in range(len(CarRegArray)):
            line = f'{CarRegArray[counter]},{EntryTimeArray[counter]},{ExitTimeArray[counter]},{DatesArray[counter]},{ChargesArray[counter]}\n'
            f.write(line)
            counter += 1

        print('\nCharges Outputted in file CarParkingCharges.csv')


CRA, DA, EntryTA, ExitTA = ReadFile()

PriceTable = {
    "1hr": "1.00",
    "2hrs": "2.20",
    "2hrs-3hrs": "3.30",
    "3hrs-4hrs": "4.40",
    "12hrs": "12.00",
    "ovr12hrs": "20.00",
}

Charges = CalculatePricing(CRA, EntryTA, ExitTA, PriceTable)
WriteCharges(CRA, EntryTA, ExitTA, DA, Charges)
