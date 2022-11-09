def ReadPupilDetails():
    namesarray = [""] * 20
    housesarray = [""] * 20
    counter = 0

    with open('SoftwareDevelopment/datafiles/PupilDetails.csv', 'r') as f:
        line = f.readline().rstrip('\n')
        while line:
            items = line.split(',')
            namesarray[counter] = (items[0])
            housesarray[counter] = (items[1])
            line = f.readline().rstrip('\n')
            counter += 1
        
    input('File read successful... Press enter to continue')
    return namesarray, housesarray

def DisplayContents(names, houses):
    print("{0:<10s}".format("Name"), "{0:<10}".format("House"))
    for counter in range(len(names)):
        print("{0:<10}".format(names[counter]), "{0:<10}".format(houses[counter]))

names, houses = ReadPupilDetails()
DisplayContents(names, houses)
