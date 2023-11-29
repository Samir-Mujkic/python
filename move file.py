import os

source = 'text.txt'
destination = "/home/samir/Desktop/nyca.txt"

try:
    if os.path.exists(destination):
       print("There is that file")
    else:
        os.replace(source,destination)
        print(source+ "was moved")
except FileNotFoundError:
    print(source+ "was not found")

