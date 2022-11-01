# WABR&Co Room Booking Application

import os
import time
import qrcode

pricingTable = {
    "single":"47",
    "double":"90",
    "family":"250"
}
discountReq = 3
currentVATRate = 20

DOA = "1/1/1980"
NoOfNights = 0
BookingName = ""
RoomType = ""

print('WABR&Co Room Booking Portal | v0.1.5')
BookingName = input('Full Name: ')
NoOfNights = int(input('Number Of Nights: (max. 14)'))
DOA = input('Date Of Arrival: (Format 1/1/1980)')
RoomType = input('Type Of Room: (Single/Double/Family)')

os.system('clear')
print('Checking data...')
time.sleep(3.5)


data = f"BN{BookingName}DOA{DOA}RT{RoomType}NON{NoOfNights}DCTyes"
img = qrcode.make(data)
img.save('wabrco-hotel-booking.png')

print('A booking QR code has been saved. Please show this at reception when you arrive on your DOA. Please inform us if this datae changes as the QR code will become invalid.')


# print(pricingTable.get('single'))