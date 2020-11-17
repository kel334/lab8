# Kendra Ludwig (kel334@nau.edu)
# Dann Gonzalez (deg266@nau.edu)


import json
import random


def main():
    print("----------------------------------------------")
    print()
    print("Welcome to our CS126 Trivia Game")
    print("Win MILLIONS!!?!\n")
    print("----------------------------------------------")
    menu()


def menu():
    print("Main Menu")
    print("\t(p)lay game")
    print("\t(c)redits")
    print("\t(q)uit\n")
    print("Make your selection and then hit enter!\n")
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
        random.shuffle(contents)
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
            while answer not in possible:
                try:
                    print("\tThat's not an option! Try again, think harder!\n")
                    answer = input("\tYour answer: ")
                    if answer == questions["correct"]:
                        break
                except:
                    pass #come back to this
            if answer == questions["correct"]:
                print("\tGood job! *Confetti falls in the background*")
                score += 1
                index += 1
            else:
                print("\tNot correct. *The audience boos*")
                index += 1
            print(str(score), "points out of 10!")
            
        print()
        print("----------------------------------------------")
        print("\tGood job!\n")
        print("\tFinal Score: ", str(score))
        print("\tThanks for Playing!\n")
        print("----------------------------------------------")
        print()
        menu()


def count_lines():
    with open('questions.json', 'r') as question_file:
        number_lines = 0
        for line in question_file:

            number_lines += 1


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


def quit():
    print()
    print("------------------------------------------------")
    print("\tThank you for playing!")
    print("\tQuitting in 3... 2... 1...")
    print("------------------------------------------------")

if __name__ == '__main__':
    main()
