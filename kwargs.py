#**kwargs = parametar that will pack all arguments into a dictionary
#           useful so that a function can accept a varying amout of keyword arguments

#example



def hello (**kwargs):
    for key,value in kwargs.items():
        print(value,end=" ")

hello(title="mr.",first="bro",middle="dude",last="code")