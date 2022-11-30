def ReadFile(filename):
    counter = 0
    names = [""] * 100
    classCode = [""] * 100
    prelims = [""] * 100
    cWork = [""] * 100

    with open(filename, "r") as f:
        line = f.readline().rstrip('\n')
        while line:
            items = line.split(',')
            names[counter] = items[0]
            classCode[counter] = items[1]
            prelims[counter] = items[2]
            cWork[counter] = items[3]
            line = f.readline().rstrip('\n')
            counter += 1

    return names,classCode,prelims,cWork

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

name,cc,p,cw = ReadFile("SoftwareDevelopment/datafiles/ComputingMarks.csv")
# prelim marks
minp,minposp = findMin(p)
maxp,maxposp = findMax(p)
# coursework marks
minc,minposc = findMin(cw)
maxc,maxposc = findMax(cw)
# # combined marks
# maxcomb = maxc+maxp
# mincpmb = minc+minp

print(f'Lowest Prelim Mark: {p[minposp]} from {name[minposp]}\nHighest Prelim Mark: {p[maxposp]} from {name[maxposp]}')
print(f'Lowest Coursework Mark: {p[minposc]} from {name[minposc]}\nHighest Coursework Mark: {p[maxposc]} from {name[maxposc]}')