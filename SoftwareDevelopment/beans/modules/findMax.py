def findMax(theList):
    last = len(theList)
    position = 0
    max = theList[0]
    for counter in range(1, last):
        if theList[counter] > max:
            max = theList[counter]
            macPnt = counter+1
    return max, macPnt
    
theList=[0,1,3,-2,4,5,121,6,7,9,8,4,3,758,4,2,3,1,-4,99,99,99]
max,mapnt=findMax(theList)
print(f'Max Number: {max}\nPos: {maxpnt}')