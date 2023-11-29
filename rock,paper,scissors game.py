import random # dodali random 
while True:
 choices = ["rock","paper","scissors"] # choices za iganje

 computer = random.choice(choices) # da kompjuter sam izabere jedno od dodatih u choices
 player = None # dali vrednost playeru none
 while player not in choices: # napravili while petlju da mora izabrati nesto od ponudjenog u choices
             player = input("rock,paper,scissors: ").lower() # case sensetive

 if player == computer:
        print("computer: ",computer)

        print("player:", player )
        print("tie")
 elif player == "rock":
     if computer == "paper":
        print("computer: ",computer)

        print("player:", player )
        print("lose")

     if computer == "scissors":
        print("computer: ",computer)

        print("player:", player )
        print("win") # tako jos do kraja samo izmenimo paper i rock i snicessers
 elif player == "paper":
      if computer == "rock":
        print("computer: ",computer)

        print("player:", player )
        print("win")

      if computer == "scissors":
        print("computer: ",computer)

        print("player:", player )
        print("lose")
 elif player == "scissors":
      if computer == "paper":
        print("computer: ",computer)

        print("player:", player )
        print("win")

      if computer == "rock":
        print("computer: ",computer)

        print("player:", player )
        print("lose")

 play_again = input("play again (yes/no)").lower()
 
 if play_again != "yes":
          break
     
 print("bye")