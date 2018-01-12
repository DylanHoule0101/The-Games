import random
from time import sleep

###
# Things to try:
# - keep track of how many guesses the user makes
# - if the user plays again, how could we tell them if they did better or worse than their last game?
# #

class GuessingGame:
    def __init__(self, playerName, callback):
        self.playerName = playerName
        self.name = "The Guessing Game"
        self.callback = callback

    def play(self):
        guess = random.randint(1, 100)
        playing = True
        print(f"Ok, {self.playerName}, I'm thinking of a number 1 through 100")
        sleep (2)
        print("Now start guessing!")
        while playing:
            userguess = input("> ")
            if(userguess == "q"):
                playing = False
                self.callback(self.name)
            try:
                userguess = int(userguess)
            except ValueError:
                print(f"I said I was thinking of a number! \"{userguess}\" isn't a number!")
                userguess = 0

            if userguess < guess:
                print("Too small!")
            elif userguess > guess:
                print("Too large!")
            else:
                print("You win!!!")
                playing = False
                self.playAgain()

    def playAgain(self):
        print("Would you like to play again? y/n")
        response = input("> ")
        self.play() if response == "y" else self.callback(self.name)
