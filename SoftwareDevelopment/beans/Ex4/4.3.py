def ReadFile(filename):
    counter = 0
    names = [""] * 50
    scores = [""] * 50

    with open(filename, "r") as f:
        line = f.readline().rstrip('\n')
        while line:
            items = line.split(',')
            names[counter] = items[0]
            scores[counter] = items[1]
            line = f.readline().rstrip('\n')
            counter += 1

    return names,scores

def findMax(theList):
    last = len(theList)
    position = 0
    max = theList[0]
    for counter in range(1, last):
        if theList[counter] > max:
            max = theList[counter]
            macPnt = counter
    return max, macPnt

def findMin(theList):
    last = len(theList)
    position = 0
    max = theList[0]
    for counter in range(1, last):
        if theList[counter] < max:
            max = theList[counter]
            macPnt = counter
    return max, macPnt

names,scores = ReadFile('SoftwareDevelopment/datafiles/Scores.csv')
min,minpnt = findMin(scores)
max,maxpnt = findMax(scores)
print(f'Highest score {max} belongs {names[maxpnt]}\nLowest score {min} belongs {names[minpnt]}')