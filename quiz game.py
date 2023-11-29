
#-------------------------------
def new_game():
    guesses = []
    correct_guesses = 0
    question_num = 1
    for key in questions:
        print("--------")
        print(key)
        for i in options[question_num-1]:
            print(i)
        guess = input("Enter(A,B,C OR D)")
        guess = guess.upper()
        guesses.append(guess)

        correct_guesses += check_answer(questions.get(key),guess)
        question_num += 1

        display_score(correct_guesses, guesses)
    pass

#--------------------------

def check_answer(answer, guess):
    if answer == guess:
        print("Correct")
        return 1
    else:
        print("Wrong")
        return 0
    pass

#---------------------------

def display_score(correct_guesses, guesses):
    print("-----")
    print("Results")
    print("-------")
    print("Answers: ", end="")
    for i in questions:
        print(questions.get(i), end="")
    print()

    print("Guesses: ", end="")
    for i in guesses:
        print(i, end="")
    print()

    score = int((correct_guesses/len(questions)) * 100)
    print("your score is "  + str(score)+ "%")

    pass

#--------------------------

def play_again():

    resposnse = input("Do you wont to play again: (yes or no)")
    resposnse = resposnse.upper()

    if resposnse == "YES":
        return True
    else:
        return False
        
    pass
#-------------------------------
questions = {
    "Who created python: " : "A",
    "What year was python cerated: " : "B",
    "Python is tributed to which comedy group: " : "C",
    "Is the Earth round: " : "A"
}

options = [["A. Gudio van Rossum", "B. Elon Musk", "C. Bill Gates", "D. Mark Zuckerburg"],
          ["A. 1989", "B. 1991", "C. 2000", "D. 2016"],
          ["A. Lonely Island", "B. Smosh", "C. Monty Python", "D. SNL"],
          ["A. True","B. False","C. sometimes", "D. Whats Earth"]]

new_game()

while play_again():
    new_game()

print("Byeee")