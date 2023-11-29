#dictionary = a changeable, unorder collection of unique key:valuepairs
# fast because they use hashing ,allow us to access a value quickly

# key:value

#example
capitals = {"USA": "washington",
            "India": "New dehli",
            "China": "Beijing",
            "Russia": "Moscow"}

capitals.update({'German:berlin'}) # dodali novi u capitals
capitals.update({"USA":"los vegas"}) # izmjenili postojeci
capitals.pop("china") #remove china from capitals
capitals.clear # izbrisali sve


#print(capitals["Russia"])

#print(capitals.get("germany"))

#print(capitals.keys())

#print(capitals.values())

for key,value in capitals.items():
    print(key,value)

