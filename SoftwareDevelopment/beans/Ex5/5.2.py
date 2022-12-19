# Redone with records:
#Ex 5.1 ISBN No
#Mrs Gillespie
#Run then add internal commentary

class Book():
  Title:str
  Author:str
  ISBN:str
  Price:float

def readBooks(filename):
  books = [Book() for x in range(20)]
  counter = 0

  with open(filename,'r') as readfile:
    line = readfile.readline().rstrip('\n')
    while line:
      items = line.split(",")
      books[counter].Title = items[0]
      books[counter].Author = items[1]
      books[counter].ISBN = items[2]
      books[counter].Price = items[3]

      line = readfile.readline().rstrip('\n')
      counter +=1

  input("File read....Press any key to continue")
  
  return books


def searchBooks(books):
  found = False
  choice = input("Please enter the ISBN to search for: ")
  for counter in range(0, len(books)):
    if books[counter].ISBN==choice:
      found = True
      position = counter
  if found ==False:
    print("No book found in the list")
  else:
    print("\nBook found: \n")
    print("Title: ",books[position].Title)
    print("Author: ", books[position].Author)
    print("Price: ", books[position].Price)


#main Program
filename="books.txt"
books = readBooks(filename)
searchBooks(books)