# VAT Calculator

# Imports
from time import sleep
from os import system

def GetPrice():
    print('UK 2022 VAT Calculator')
    return float(input("Enter the price exclusing VAT: £"))

def CalulateVAT(price):
    system('clear')
    print('Calculating VAT...')
    sleep(1.75)

    priceHOLD = price * 0.2
    priceWithVAT = price + priceHOLD
    priceWithVAT = round(priceWithVAT, 2)
    system('clear')

    return priceWithVAT

def DisplayTotals(priceWOUTVAT, priceWVAT):
    print(f'Enter the price excluding VAT: £{priceWOUTVAT}')
    print(f'The price including VAT: £{priceWVAT}')

# main function
price = GetPrice()
priceWVAT = CalulateVAT(price)
DisplayTotals(price, priceWVAT)
