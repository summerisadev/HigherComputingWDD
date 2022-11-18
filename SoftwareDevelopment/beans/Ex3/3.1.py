import os

def WriteFile(content):
    with open(f'SoftwareDevelopment/datafiles/newfile.txt', 'a') as f:
        f.write(f'{content} \n')
        print('file updated successfully')

message = input("Please enter your message >> ")
WriteFile(message)
