# Kendra Ludwig (kel334@nau.edu)
# Dann Gonzalez (deg266@nau.edu)


def main():
    print("Welcome to our CS126 Trivia Game")
    print("Win MILLIONS!!?!\n")
    menu()
    execution()


def menu():
    print("Main Menu")
    print("\t(p)lay game")
    print("\t(c)redits")
    print("\t(q)uit\n")
    print("Make your selection, just type a letter in the parentheses," +
            "then hit enter!\n")
    selection = input().lower()
    return selection


def execution(selection):
    if selection not in ['p', 'c', 'q']:
        print("Please select one of the options.\n") 

    options = {
            'p': start_game(),
            'c': show_credits(),
            'q': quit()
            }
    # call from dictionary here -- start here a demain


def start_game():
    with open('questions.json', 'r') as questions:
        #FINISH!!!

# def show_credits():
# def quit():


if __name__ == '__main__':
    main()
