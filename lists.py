# list = used to sotre multile items in single variable

food = ["pizza", "hambas", "hotdog", "spagete", "puding"]



food[0]= "susi" # replace 0 tj prvi po redu sa susi

food.append("ice cream") # dodali ice cream u listu
food.remove("hotdog") # izbrisali hotdog
food.pop() # izbrisali zadnji u redu
food.insert(0, "cake") 
food.sort() #sortiraj
food.clear() # clear all from food 

for i in food:
    print(i)