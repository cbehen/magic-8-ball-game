#magic 8 ball
#chloe behen
#1.22.24

#initialize
import random

#functions

#welcomes the user to the program
print("Welcome to Magic 8 Ball! Enter any yes-or-no question that's on your mind to recieve a response.")

#function that prompts the user to enter their question and generates a random response
def fortune():
    question = input("What's your question? ")
#checks that the question includes a question mark. if it does not, the user is asked to re-enter their question
    validation = question
    x = "?" in validation
    if x == False:
        print("End your question with a question mark")
        fortune()
        
#list of possible responses
    responses = ["absolutely not", "that's laughable", "if you're lucky", "I hope not", "I guess you'll have to see", "I guess so", "Only if you want to", "Never in a million years", "Don't get too hopeful", "Of course!", "In your wildest dreams", "Maybe, maybe not", "Nahhh", "Yes!"]
    print(random.choice(responses))
    
#asks the user if they would like to ask another question or end the game
    ans = input("Would you like to ask another question? Enter yes or no. ")
    if ans == "yes":
        fortune()
    elif ans == "no":
        print("Goodbye, thanks for playing!")
        quit()
    
#main
fortune()