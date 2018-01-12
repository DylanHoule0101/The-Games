from games.EightBall import EightBall
from games.GuessingGame import GuessingGame
from games.RPS import RPS

###
# Things to try
# - What if the player just hits enter without putting in a name? How can we prevent that?
###

class TheGames:
    def __init__(self):
        self.welcome()

    def welcome(self):
        print("Welcome ... whats your name?")
        self.playerName = input("> ")
        print(f"Ok, welcome to The Games, {self.playerName} ...")
        self.displayGameMenu()

    def quitGame(self, gameName):
        print(f"Thanks for playing {gameName}, {self.playerName}!")
        self.displayGameMenu()

    def displayGameMenu(self):
        print("Please Select a Game....")
        print("1 = Eightball, 2 = Guessing, 3 = Rock Paper Scissors, 4 = Junglemon/Pokemon, 0 = Quit")
        game = None;

        gamechoice = input("> ")
        
        if(gamechoice == "0"):
            print(f"Thanks for playing, {self.playerName}!")
            exit()
        elif(gamechoice == "1"):
            game = EightBall(self.playerName, self.quitGame)
        elif(gamechoice == "2"):
            game = GuessingGame(self.playerName, self.quitGame)
        elif(gamechoice == "3"):
            game = RPS(self.playerName, self.quitGame)
        else:
            print(f"No really, {self.playerName} - pick a game!")
            self.displayGameMenu()

        if(game != None):
            game.play()


app = TheGames()

#
#           if "4" in gamechoice:
#             import random
# from time import sleep
# junglings = ["treehoot","froggitir","charring"]
# names = ["Viola","Grant","Clement","Ramos","Ash","Korina","Ash","Ash","Korina","Carson The Dev of The Game","Dylan The Dev of The Game","Viola","Viola","Clement", "Clement","Ramos","Ramos","Korina","Korina"]
# CPUname = random.choice(names)
# gyms = ["Cyllage City","Saffron City Gym","Fuchsia City Gym","Pewter City Gym","Pallet Town Gym"]
# print("Hello, new challenger, I'm trainer {CPUname}. what is your name?")
# name = input(">")
# sleep(1)
# CPUCity = random.choice(gyms)
#
# print("welcome, trainer {name} to {CPUCity}, choose your jungling.")
# sleep(1)
# print("charring: fire type. abilitys: flamethrower, fire breath, lava spout, and Blaze ")
# sleep(1)
# print("froggitir: water type, abilitys: Water Gun, Tsunami Blast, Shark Sword, Acid Rain")
# sleep(1)
# print("treehoot: plant type, abilitys: Thorn Toss,Root Grab, Overgrow , Sap Spit")
# userjungling = input(">")
# if "charring" in userjungling:
#   print("you have chosen charring!")
# elif "froggitir" in userjungling:
#   print(" you have chosen froggitir!")
#
# elif "treehoot" in userjungling:
#   print("you have chosen treehoot!")
#   userchoice = "treehoot"
# else:
#   print("thats not one, silly!")
#   userchoice = random.choice(junglings)
#   sleep(2)
#   print("the game chose for you. and you have {userchoice}")
# if "Dylan The Dev" in CPUname:
#   print("Dylan The Dev Of The Game has chosen WEMTHREE(Junglemon Mewtwo)")
#
# elif "Carson The Dev" in CPUname:
#   print("Carson The Dev Of The Game has chosen WEMTHREE(Junglemon Mewtwo)")
# else:
#   CPUjungling = random.choice(junglings)
#   print("CPU: I have chosen {CPUjungling}")
