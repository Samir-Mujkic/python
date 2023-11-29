
text = 'have a nice \ndaz\nasdassda'

#with open('text.txt', 'w') as file: #overwritefile
 #   file.write(text)

with open('text.txt', 'a') as file: #append to file
    file.write(text)