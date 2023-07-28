import random
import time

# define global variables
user_choice = 0
comp_choice = 0
user_score = 0
comp_score = 0

# main function
def main():   
    global user_choice, comp_choice, user_score, comp_score

    # get user input    
    user_choice = getUserInput()   

    # picks a random choice  
    comp_choice = random.randint(1,3)

    showChoices()

    # compare both choices & show result
    if (user_choice == comp_choice):
        print("<: DRAW!")
    elif (comp_choice == 1 and user_choice == 2):
        userWins()
        user_score += 1
    elif (comp_choice == 2 and user_choice == 3):
        userWins()
        user_score += 1
    elif (comp_choice == 3  and user_choice == 1):
        userWins()
        user_score += 1
    else:
        print("<: LOST!")
        comp_score += 1
    print()

    # check whether computer or player wins
    if ((comp_score > 2) or (user_score > 2)):
        showResult()

# get user input and a random choice from computer
def getUserInput():   
    errors = True
    while (errors):
        try:
            choice = int(input("Choice: "))
            errors = False
        except:
            print("\n<: WRONG CHOICE!")
            time.sleep(0.8)
            print("<: TRY AGAIN!\n")
            time.sleep(0.4)
            errors = True
    return choice

# return choice text
def select(choice):
    if (choice == 1):
        return "Rock"
    elif (choice == 2):
        return "Paper"
    elif (choice == 3):
        return "Scissor"

# show both choices
def showChoices():
    if(user_choice > 3 and user_choice < 1):
        print("<: INVALID CHOICE!")
        time.sleep(0.8)
    else:
        print(f"Computer : {select(comp_choice)}")
        print(f"Player   : {select(user_choice)}")  

# show win statement
def userWins():
    print("<: YOU WIN!")

# show final result
def showResult():
    print("\nComputer  :  Player")
    print(f"       {comp_score}  :  {user_score}")   
    if(user_score > comp_score):
        print("~~~ Player Wins ~~~")
    else:
        print("~~~ Computer Wins ~~~\n")  
    time.sleep(0.5)    
    gameOver()

# the game ending
def gameOver():
    global comp_score, user_score
    print("-------------------------")
    print("***** THE GAME OVER *****")
    print("-------------------------\n\n")
    time.sleep(0.8)
    print("If u like to play again type 'y' and press enter.")
    time.sleep(0.5)
    choice  = input("Would u like to play again [y/n]: ")
    if (choice  == "y"):
        # reset both scores
        comp_score = 0
        user_score = 0
        print("\n\n")
    else:
        exit()


# ---- PROGRAM STARTS FROM HERE ----

# show the group info
print("---------------------------------------------------------")
print("* ROCK PAPER SCISSOR GAME created by The Fantastic Five *")
print("---------------------------------------------------------\n")
time.sleep(0.8)

# main loop
while(True):
    time.sleep(0.4)
    print("---------------------------------------------------------")
    print("                  ===== CHOICES =====")
    print("           1.Rock     2.Paper     3.Scissor")
    print("---------------------------------------------------------\n")
    time.sleep(0.5)
    print("* Type a number and press enter [1, 2, 3]\n")
    time.sleep(0.3)
    main()  
