# str.format() = optinal method that gives users
#                more control when displazing output

#example

animal = "cow"
item = "moon"


print("the {} jumped over the {}".format(animal,item))
print("the {1} jumped over the {3}".format(animal,item,"samir","mujkic")) #positional argument

text = "The {} jumped over the {}"
print(text.format(animal,item))


number = 1000

print("The broj je {:,}".format(number))
print("The broj je {:b}".format(number))
print("The broj je {:o}".format(number))
print("The broj je {:x}".format(number))
print("The broj je {:e}".format(number))