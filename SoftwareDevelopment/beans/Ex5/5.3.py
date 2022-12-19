class Secondary():
    Name:str
    Score:str
    School:str
    Type:str

class Primary():
    Name:str
    Score:str
    School:str
    Type:str

def findMax(theList):
        last = len(theList)
        position = 0
        max = theList[0]
        for counter in range(1, last):
            if theList[counter] > max:
                max = theList[counter]
                macPnt = counter+1
        return max, macPnt

def ReadFile(fn):
    primaryPupils = [Primary() for x in range(40)]
    secondaryPupils = [Secondary() for x in range(60)]

    primaryCounter = 0
    secondaryCounter = 0

    with open(fn) as f:
        line = f.readline().rstrip("\n")
        while line:
            items = line.split(",")
            if items[3] == "Primary":
                primaryPupils[primaryCounter].Name = items[0]
                primaryPupils[primaryCounter].Score = items[1]
                primaryPupils[primaryCounter].School = items[2]
                primaryPupils[primaryCounter].Type = items[3]
                primaryCounter += 1
            elif items[3] == "Secondary":
                secondaryPupils[secondaryCounter].Name = items[0]
                secondaryPupils[secondaryCounter].Score = items[1]
                secondaryPupils[secondaryCounter].School = items[2]
                secondaryPupils[secondaryCounter].Type = items[3]
                secondaryCounter += 1

            line = f.readline().rstrip("\n")

    return primaryPupils,secondaryPupils

def CalcBestSchool(primary,secondary):
    maxPrimary = 0
    maxSecondary = 0
    pC = 0
    sC = 0

    maxPrimary = findMax(primary.Score)
    print(maxPrimary)


pPupils,sPupils = ReadFile("SoftwareDevelopment/datafiles/baking.csv")
            