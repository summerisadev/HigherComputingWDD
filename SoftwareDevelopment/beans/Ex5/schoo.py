class TripDataObject():
    Name:str
    Gender:str
    Trip:str

def readTripInfo(fn):
    trips = [TripDataObject() for x in range(100)]
    i = 0

    with open(fn,"r") as f:
        line = f.readline().rstrip("\n")
        while line:
            items = line.split(',')
            trips[i].Name   = items[0]
            trips[i].Gender = items[1]
            trips[i].Trip   = items[2]

            line = f.readline().rstrip("\n")
            i+=1

    input("file read... press enter to continue")
    return trips

def countTrips(tripData):
    paris  = 0
    gorge  = 0
    bike   = 0
    bmx    = 0
    london = 0

    for x in range(0, len(tripData)):
        if tripData[x].Trip == "Paris":
            paris += 1
        if tripData[x].Trip == "Gorge Walking":
            gorge += 1
        if tripData[x].Trip == "Mountain Biking":
            bike += 1
        if tripData[x].Trip == "BMX":
            bmx += 1
        if tripData[x].Trip == "London":
            london += 1

tripData = readTripInfo("./SoftwareDevelopment/datafiles/SchoolTrips.csv")
countTrips(tripData)