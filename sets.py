# set = colelctio which is inordered,unindexed. no duplicate values

#example

utensils = {"fork", "spoon", "knife"}
dishes = {"bowl", "plate", "cup"}

#utensils.add("napkin")

#utensils.remove("fork")

#utensils.update(dishes)

dinnet = utensils.union(dishes)

print(utensils.difference(dishes))

print(dinnet)
for x in utensils:
    print(x)