# loop control statemnets = change a loops execution from its normal sequence

#break = used to terminate the loop
#continue = skips to next iteration of loop
# pass = does nothing ,acts as a placeholder

#while True:
 #   name= input("dodaj ime") # Dodaj ime ako ne dodoas ponovo ce odradit se loop
  #  if name != "":
   #     break


#phone= "123-456-789"

#for i in phone:
    #if i == "-":
    #    continue
    #print(i, end="") # ispisi brojeve  u phone i nastavi ako doodjes do znaka -

for i in range(1,21):
    if i == 13:
        pass
    else:
        print(i)  # ispisi brojeve od 1 do 21 ali kada je broj 13 na redu njega preskoci i nastavi
