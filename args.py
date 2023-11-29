#  *args = parameter that will pack all arguments into a tuple
#         useful to that a function can accept a varying amout of arguments

#example



def add(*args):
    sum = 0
    for i in args:
        sum += i
    return sum

print(add(1,2,3,4,5,6))