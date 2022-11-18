def ReadFile(filename):
    counter = 0
    flowers = [""] * 200
    price = [""] * 200

    with open(filename, "r") as f:
        line = f.readline().rstrip('\n')
        while line:
            items = line.split(',')
            flowers[counter] = items[0]
            price[counter] = items[1]
            line = f.readline().rstrip('\n')
            counter += 1

    return flowers,price


def SearchFile(names):
    counter = 0
    found = False
    foundPos = 0
    searchItem = input("Item to be searched: ")

    while (counter < len(names) and found == False):
        if names[counter] == searchItem:
            found = True
            foundPos = counter
            counter += 1

    print(f"Item found in isle {str(foundPos+1)}")

    # for i in range(len(names)):
    #     if names[i] == searchItem:
    #         print(f"Item found in aisle {str(i+1)}")
    #     else:
    #         return print('Item not found! Are you sure you spelled it correctly?')

items,prices = ReadFile('SoftwareDevelopment/datafiles/PlantStockFile.csv')
SearchFile(items)