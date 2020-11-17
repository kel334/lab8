# Kendra Ludwig (kel334@nau.edu)
# Dann Gonzalez (deg266@nau.edu)


import json
import random


# creates welcome screen and starts main menu
def main():
    print("----------------------------------------------")
    print()
    print("Welcome to our CS126 Trivia Game")
    print("Win MILLIONS!!?!\n")
    print("----------------------------------------------")
    menu()


# asks user for selection and moves to option functions
def menu():
    print("Main Menu")
    print("\t(p)lay game")
    print("\t(c)redits")
    print("\t(q)uit\n")
    print("Make your selection and then hit enter!\n")
    selection = input().lower()
    execution(selection)


# takes input and calls proper function or asks again
def execution(selection):
    only_select = ['p', 'c', 'q']
    while selection not in only_select:
        try:
            print("Please select one of the options.\n")
            selection = input().lower
            if selection in only_select:
                break
        except:
            pass  # INTENTIONAL
    if selection == 'p':
        game()
    if selection == 'c':
        show_credits()
    if selection == 'q':
        quit()


# starts the game
def game():
    with open('questions.json', 'r') as qs:
        contents = json.load(qs)
        score = 0
        index = 0
        # shuffles the questions around
        random.shuffle(contents)
        # asks the question
        while index < len(contents):
            questions = contents[index]
            print()
            print("----------------------------------------------")
            choice = questions["prompt"]
            print(choice)
            options = questions["answers"]
            options = "".join(options)
            print(options)
            print()
            answer = input("\tYour Answer: ")
            possible = questions["choices"]
            # keeps asking question in case of invalid input
            while answer not in possible:
                try:
                    print("\tThat's not an option! Try again, think harder!\n")
                    answer = input("\tYour answer: ")
                    if answer == questions["correct"]:
                        break
                except:
                    pass  # INTENTIONAL
            # gives response based on input and keeps score and Q count
            if answer == questions["correct"]:
                print("\tGood job! *Confetti falls in the background*")
                score += 1
                index += 1
            else:
                print("\tNot correct. *The audience boos*")
                index += 1
            print("\tYour score is: ", str(score), "points out of 10!")
        # called at the end of the game, returns to menu
        print()
        print("----------------------------------------------")
        print("\tGood job!\n")
        print("\tFinal Score: ", str(score))
        print("\tThanks for Playing!\n")
        print("----------------------------------------------")
        print()
        menu()


# prints the credits, returns to menu
def show_credits():
    print()
    print("----------------------------------------------")
    print("Credits:")
    print("\tthe CS126 Trivia Show\n")
    print("\tCreated by\n")
    print("\tKendra Ludwig")
    print("\t&")
    print("\tDann Gonzalez")
    print("----------------------------------------------\n")
    menu()


# quits the game politely
def quit():
    print()
    print("------------------------------------------------")
    print("\tThank you for playing!")
    print("\tQuitting in 3... 2... 1...")
    print("------------------------------------------------")


if __name__ == '__main__':
    main()
