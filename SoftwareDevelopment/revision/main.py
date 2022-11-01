import os
import time
from tabulate import tabulate

bookName = "Software Development for Beginners"
bookCost = 15.99
activeDiscount = 0
currentVoucherCode = "Z2VuZXJhdG9y"
isVoucherActive = False

quantity = 0

os.system('clear')

# Functions
def getQuantity():
    return int(input('How many books are you ordering?: '))

print(f'"{bookName}" Ordering System')
quantity = getQuantity()

while quantity > 80 or quantity < 1:
    os.system('clear')
    print('Quantity cannot be more than 80 or less than 1.')
    quantity = getQuantity()

os.system('clear')
print('Submitting order to system...')
time.sleep(5)
os.system('clear')

if quantity >= 51:
  activeDiscount = activeDiscount + 10
  print(f'Applied {activeDiscount}% discount!')
elif quantity >= 11 & quantity <= 50 :
    activeDiscount = activeDiscount + 7.5
    print(f'Applied {activeDiscount}% discount!')
elif quantity <= 10 & quantity >= 5:
    activeDiscount = activeDiscount + 5
    print(f'Applied {activeDiscount}% discount!')
elif quantity <= 5:
    activeDiscount = activeDiscount + 0
else:
    print('Something happened... And that should\'t be possible...')

time.sleep(2.3)
os.system('clear')

inputtedCode = input("If you have one, please enter a voucher code NOW: ")

if inputtedCode != "":
    os.system('clear')
    print('Checking voucher...')
    time.sleep(5)
    if inputtedCode == currentVoucherCode:
        isVoucherActive = True
        print('Valid code! Applied £25 discount!')
    else:
        print('Invalid code. Skipping...')
    time.sleep(5)
    os.system('clear')

total = quantity * bookCost
temptotal = total / activeDiscount
total = total - temptotal
if isVoucherActive == True:
    total = total - 25
total = round(total, 2)

mydata = [ [bookName, bookCost, total] ]
header = ["Book Name", "Book Price (x1 Units)","Final Price"]
print(tabulate(mydata, headers=header, tablefmt="grid"))