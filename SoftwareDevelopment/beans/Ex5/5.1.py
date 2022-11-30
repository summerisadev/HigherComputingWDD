def ReadFile(filename):
    titles =  []
    authors = []
    ISBN =    []
    prices =  []
    counter = 0

    with open(filename, "r") as f:
        line = f.readline().rstrip('\n')
        while line:
            items = line.split(',')
            titles.append(items[0])
            authors.append(items[1])
            ISBN.append(items[2])
            prices.append(items[3])
            line = f.readline().rstrip('\n')

    return titles,authors,ISBN,prices

def SearchBookDetails(titles,authors,ISBN,prices):
    found = False
    selection = input("Please enter ISBN to search: ")
    for counter in range(0,len(ISBN)):
        if ISBN[counter] == selection:
            found = True
            position = counter

    if found == False:
        print('Unable to find book.')
    else:
        print('Book Found: ')
        print(f'Title: {titles[position]}')
        print(f'Author: {authors[position]}')
        print(f'Price: {prices[counter]}')

titles,authors,ISBN,prices = ReadFile("SoftwareDevelopment/datafiles/books.txt")
SearchBookDetails(titles, authors, ISBN, prices)