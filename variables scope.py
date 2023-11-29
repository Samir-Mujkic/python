#scope = the region that a avariable is recognized
#        a variable is only available from inside the regoin it is created.
#        a global and locally scoped versions of a a variable can be created

#example

name = "Faruk" # global scope(available inside i outside functons)

def samir():
    name = "almir"
    print(name)  # local scope availabe only inside this function

samir()

print(name)