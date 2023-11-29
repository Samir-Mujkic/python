#if statement = a block of code that will execute if it's condition is true

age = int(input( "how old are you"))

if age == 100:
   print("zour are a century old")
elif age >= 18 and age < 100:
   print("your are ok")
elif age  < 0:
   print(" zou are noy born yet")
elif age > 100:
   print("jedva ti jarane")

else:
   print("zour are child")