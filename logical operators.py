#logical operators (and,or,not) = used to check if two or more conditinal statement is ture

temp = int(input("Koja je temperatura vani ? : "))

#if temp >= 0 and temp<= 30:
    #print("temperatura je dobra danas")
    #print("Moze se neka kafica za kuliranje cvike ovo onoo laga samo")

#elif temp < 0 or temp > 30:
    #print(" hladno je jaro sjedi kuci ili je  ze nekog bazena pa ti vidi")
    #print("Miran budi")

 #example 2 sa not operator

if not(temp >= 0 and temp<= 30):
    print("temperatura je dobra danas")
    print("Moze se neka kafica za kuliranje cvike ovo onoo laga samo")

elif not(temp < 0 or temp > 30):
     print(" hladno je jaro sjedi kuci ili je  ze nekog bazena pa ti vidi")
     print("Miran budi")