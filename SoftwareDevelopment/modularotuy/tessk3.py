# Gas Bill Calculator

def GetReadings():
    pr = int(input('Previous Reading: '))
    cr = int(input('Current Reading:  '))
    return pr, cr

def CalculateIUAndMU(preading, creading):
    iu = cr - pr
    print(f'\nYou have used {iu} units.')
    mu = iu * 1.022604
    mu = mu * 2.83
    return mu

def CalculatekWh(muunits):
    kWh = muunits * 39.3
    kWh = kWh / 3.6
    print(f'This is {kWh} kilowatt hours')
    return kWh

def CalculateFinalBill(totalkWh, currentVATRate, currentkWhRate):
    finalPrice = totalkWh * currentkWhRate
    finalPriceH = finalPrice * 0.05
    finalPrice = finalPrice + finalPriceH
    print(f'Your bill is £{finalPriceH}')

pr, cr = GetReadings()
totalkWh = CalculateIUAndMU(pr, cr)
CalculateFinalBill(totalkWh, 5, 3.74)