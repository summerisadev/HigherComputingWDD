def ReadFile(filename):
    counter = 0
    names = [""] * 100
    genders = [""] * 100
    trips = [""] * 100

    with open(filename, "r") as f:
        line = f.readline().rstrip('\n')
        while line:
            items = line.split(',')
            names[counter] = items[0]
            genders[counter] = items[1]
            trips[counter] = items[2]
            line = f.readline().rstrip('\n')
            counter += 1

    return names,genders,trips

# count the number of pupils going on a certain trip
def CountPupils(trips,names):
    counter = 0
    tripCountDict = {
        "london":0,
        "paris":0,
        "mountainbiking":0,
        "gorgewalking":0
    }

    for count in range(1,len(trips)):
        if trips[count].upper() == "LONDON":
            newCount = tripCountDict.get('london') + 1
            holdDict = {"london":newCount}
            tripCountDict.update(holdDict)
        if trips[count].upper() == "PARIS":
            newCount = tripCountDict.get('paris') + 1
            holdDict = {"paris":newCount}
            tripCountDict.update(holdDict)
        if trips[count].lower() == "mountain biking":
            newCount = tripCountDict.get('mountainbiking') + 1
            holdDict = {"mountainbiking":newCount}
            tripCountDict.update(holdDict)
        if trips[count].lower() == "gorge walking":
            newCount = tripCountDict.get('gorgewalking') + 1
            holdDict = {"gorgewalking":newCount}
            tripCountDict.update(holdDict)

    london = tripCountDict.get('london')
    paris = tripCountDict.get('paris')
    biking = tripCountDict.get('mountainbiking')
    gorge = tripCountDict.get('gorgewalking')

    print(f'\nLondon Trip: {london} pupils\nParis Trip: {paris} pupils\nMountain Biking Trip: {biking} pupils\nGorge Walking Trip: {gorge} pupils\n')
    return tripCountDict
    
    
# def WriteFile(tripCountDict):
#     for i in range(1,len(tripCountDict)):
    #     # print(tripCountDict.keys())
    #     print(tripCountDict.pop(key))

names,genders,trips = ReadFile("SoftwareDevelopment/datafiles/SchoolTrips.csv")
tripdict = CountPupils(trips, names)
# WriteFile(tripdict)