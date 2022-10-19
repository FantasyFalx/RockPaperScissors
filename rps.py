from random import randint


# This is a function for the human player

def HumanPlayer():
    """Takes in human input from user"""

    # Containers for humans and computers 

    comp_con = []
    
    hum_con = []

    # counter for game rounds, counter is set to zero

    counter = 0

    # Variables that keep score

    hum_wins = 0

    comp_wins = 0
    
    # Flag variable for the while loop 

    on = True

    # While loop

    while on:
    
    # Game menu variable. It is here if user wants to call and see valid 
    # commands

        menu = ["\nMenu Commands", "Enter either rock, paper, or scissor to play",
                "To access the game menu again enter m",
                "To see a record of the game enter g", 
                "If you want to quit enter q"]

    # Variable for human input 

        hum_input = input("\nPlease make your choice: ")

    # Variable the generates random number 

        num_getter = randint(1,3)

    # Conditionals that determine if user input is valid for game 

        if (hum_input == 'rock' or hum_input == 'paper' 
            or hum_input == 'scissor'):
        
        # Function call that judges and prints outcome of round
        
            PrintOutome(Judge(hum_input, ComputerPlayer(num_getter)), 
                            hum_input, ComputerPlayer(num_getter))

        # Conditionals that update computer and human score for game 

            if (Judge(hum_input, ComputerPlayer(num_getter)) == 1 or 
                Judge(hum_input, ComputerPlayer(num_getter)) == 2 or
                Judge(hum_input, ComputerPlayer(num_getter)) == 3):

                # Updates hum score each round if hum wins round

                    hum_wins += 1

            elif (Judge(hum_input, ComputerPlayer(num_getter)) == 4 or
                 Judge(hum_input, ComputerPlayer(num_getter)) == 5 or 
                 Judge(hum_input, ComputerPlayer(num_getter)) == 6):

                # Updates comp score each round of comp wins

                    comp_wins += 1
        
        # Appends items to lists

            hum_con.append(hum_input)
            comp_con.append(num_getter)

        # Counter

            counter += 1

        # Second part of conditionals 
        
        elif hum_input == 'm':
            for items in menu:
                print(f"{items}")
            hum_input
        elif hum_input == 'g':
            GameRecord(counter, hum_wins, comp_wins, hum_con, comp_con,)
        elif hum_input == 'q':
            return hum_input
        else: 
            print("\nComputer does not understand input")
            hum_input
    
    
# This is a function were the computer player chooses a random option 
# for the game: rock, paper, or scissors

def ComputerPlayer(comp_choice):
    """Function where the computer chooses a game options"""

    # list of options for computer

    choices = ['rock', 'paper', 'scissor']

    # conditionals that return computer selection from number input

    if comp_choice == 1:
        return choices[0]
    elif comp_choice == 2:
        return choices[1]
    elif comp_choice == 3:
        return choices[2]
    

# Function that judges who won the round of game

def Judge(hum_choice, comp_choice):
    """Function that determines who won the round based each players choice"""
    
    # Var that holds a number. This var will determine who wins based off
    # updated number once conditionals are run. 

    number = None
    
    # Conditionals that check to see who won round of game based off
    # computer and user choices

    if hum_choice == comp_choice:
        number = 0
        return number
    elif hum_choice == 'rock' and comp_choice == 'scissor':
        number = 1
        return number
    elif hum_choice == 'paper' and comp_choice == 'rock':
        number = 2
        return number
    elif hum_choice == 'scissor' and comp_choice == 'paper':
        number = 3 
        return number
    elif hum_choice == 'rock' and comp_choice == 'paper':
        number = 4
        return number
    elif hum_choice == 'paper' and comp_choice == 'scissor':
        number = 5
        return number
    elif hum_choice == 'scissor' and comp_choice == 'rock':
        number = 6
        return number

    


# Function that prints the results of the round

def PrintOutome(Outcome, hum_choice, comp_choice):
    """Prints the outcome of who won the round"""

    # Outcome var that takes return numbers from judge 

    result = Outcome

    # Conditionals that print certain results based off number input 

    if result == 0:
        print(f"\nHuman chose {hum_choice}, computer chose {comp_choice} " +
        "result is a TIE!")
        return 0
    elif result == 1 or result == 2 or result == 3:
        print(f"\nHuman chose {hum_choice}, computer chose {comp_choice} " + 
        ", human player won this round!")
        return 1
    else:
        print(f"\nHuman chose {hum_choice}, computer chose {comp_choice} " + 
        "the computer won this round")


# Function that updates each data point of both players 

def GameRecord(round, hum_stnd, comp_stnd, human, computer):
    """Updates the game record, a list of three lists"""

    # Container for human 

    hum_container = human[:]

    # Container for computer

    comp_container = computer[:]

    # Conditionals that change the items of the computer list to choice 
    # selection...

    for items in range(len(comp_container)):
        if comp_container[items] == 1:
            comp_container[items] = 'rock'
        elif comp_container[items] == 2:
            comp_container[items] = 'paper'
        elif comp_container[items] == 3:
            comp_container[items] ='scissor' 

    # Variable that holds the round counter

    round_counter = round

    # Variables that hold standings of comp and human 

    hum_wins = hum_stnd

    comp_wins = comp_stnd

    # Line of code that merges both hum and computer into a list of tuples

    merger = [[str(hum_container[i] + ',' + ' ' + comp_container[i])] 
            for i in range(0, len(hum_container))]

    # Puts in Human and computer for header, this is for formatting 
    
    merger.insert(0, ['Human, Computer'])

    # Strings that will be outputte for scored board

    round_str = f"\nRound {round_counter}"

    hum_score = f"Human has {hum_wins} wins"

    comp_score = f"Computer has {comp_wins} wins"

    # Print call for these strings 

    print(round_str)
    print(hum_score)
    print(comp_score)
    
    # For loop that iterates through merger list and outputs in format required

    for items in merger:
        for things in items:
            print(things)


# Main function that runs the game

def PlayGame():
    """Function that runs the main game until human player decides to quit"""

    # Print message that tells user they are playing rock, paper, and scissors.

    print("Welcome to rock, paper, scissors!")

    # list that holds menu options

    menu = ["You will be playing a computer!", 
            "Enter rock, paper, or scissor to play the game",
            "If you want to see the game menu enter m",
            "If you want to see a record of the game enter g", 
            "If you want to quit the game enter q"]

    # For loop that prints the menu when game first starts

    for items in menu:
        print(items)

    # Flag variable for while loop

    on = True

    # While loop that runs main game

    while on: 

    # conditionals that run or stop the game based off user input

        if HumanPlayer() == 'q':
            print("\nGame is now over!")
            on == False
            break
        else:
            on


# If name = main portion of code

if __name__ == '__main__':
    PlayGame()
else:
    pass
