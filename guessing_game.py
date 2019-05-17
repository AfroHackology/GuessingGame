import random

"""
 Errors that need to be fixed

- Run Script

 Program crashes at any point due to an uncaught exception.

Reviewer Comments:

Putting in a nonnumber crashes the program.

- User input

 The player was not prompted for their number choice.

- Displaying Tries

 The player was not shown how many attempts they made at the end of each game.

Reviewer Comments:

You do show the number of tries but you are not resetting that number to 0 
in between games. So, after playing the game, the next game I start at whatever 
number of tries I ended the last game on. 
 """
def start_game():
    # Welcome player
    print("--------------------------------\n"
          "Welcome to the Number Guessing Game\n"
          "--------------------------------\n")
    # Variables for while loop
    atmpts = 0
    answer = int(4)
    # answer = int(random.randrange(1, 10))
    # continuously prompt player for a guess
    while True:
        # Try block for user error
        try:
            # Body of while loop
            guess = int(input("Pick a number between 1-10: "))

            atmpts += 1
            if guess > answer:
                    print("It's lower")
            elif guess < answer:
                    print("It's Higher")
            else:
                print("You did it!!")
                print("It took you {} attempts".format(atmpts))
                game_replay = input("Would you like to play again [y]es/[n]o?")
                if game_replay == 'y':
                    # show lowest number for score
                    score = []
                    score += [atmpts]
                    # make HIGHSCORE static number that show the lowest number
                    print("\n\nThe HIGHSCORE is {}".format(score))
                    continue
                else:
                    break
        except ValueError:
            print("Please enter a number between 1-10.")
        else:
            continue

# store highscroe in list
# print highest number


if __name__ == '__main__':
    # Kick off the program by calling the start_game function.
    start_game()

