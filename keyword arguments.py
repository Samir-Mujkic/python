# keyworkd arguments = argumenet proceded  by an identifier when we pass them to a function
#                      The order of the arguments doesnt matter, unlike positional arguments
#                      Python knows the names of the arguments that our function receives

#example

def hello(last,first,middle):
    print("Helo"+ " " +last + " "+ first+ " "+ middle)

hello("samir","mujkic","kraljina")
hello(last="mujkic",middle="kraljina",first="samir")