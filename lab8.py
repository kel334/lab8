# Kendra Ludwig (kel334@nau.edu)
# Dann Gonzalez (deg266@nau.edu)

import json
import random


def main():
    print("Welcome to our CS126 Trivia Game")
    print("Win MILLIONS!!?!\n")
    menu()


def menu():
    print("Main Menu")
    print("\t(p)lay game")
    print("\t(c)redits")
    print("\t(q)uit\n")
    print("Make your selection, just type a letter in the parentheses," +
            "then hit enter!\n")
    selection = input().lower()
    execution(selection)


def execution(selection):
    if selection not in ['p', 'c', 'q']:
        print("Please select one of the options.\n")
    if selection == 'p':
        game()
    if selection == 'c':
        show_credits()
    if selection == 'q':
        quit()


def game():
    with open('questions.json', 'r') as qs:
        contents = json.load(qs)
        score = 0
        index = 0
        while index < len(contents):
            questions = contents[index]
            print()
            choice = questions["prompt"]
            #choice = list(choice)
            #choice = random.shuffle(choice)
            #choice = "".join(choice)
            print()
            print(choice)
            options = questions["answers"]
            options = "".join(options)
            print(options)
            print()
            answer = int(input())
            if answer == questions["correct"]:
                print("Good job! *Confetti falls in the background*\n")
                score += 1
                index += 1
            else:
                print("Not correct. *The audience boos*\n")
                index += 1
            print(0 + score, "points out of 10!")
            #while attempted_input != questions["prompt"]["correct"]:
                #try:
                    #print("\tThat's not an option! Try again, think harder!\n")
                    #answer = int(input())
            

    

def show_credits():
    print()
    print("----------------------------------------------")
    print("Credits:")
    print("CS126 Game Show\n")
    print("\tCreated by\n")
    print("\tKendra Ludwig")
    print("\t&")
    print("\tDann Gonzalez")
    print("----------------------------------------------\n")
    menu()


def quit():
    print()
    print("------------------------------------------------")
    print("\tThank you for playing!")
    print("\tQuitting in 3... 2... 1...")
    print("------------------------------------------------")

if __name__ == '__main__':
    main()
