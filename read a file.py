
try:
   with open('text.txt') as file:
     print(file.read())
except FileNotFoundError:
   print("_that file was not found")
