from random import randint

###
# Things to try:
# - how many times has the player won? How many times has the CPU won?
# - what if I could quit by hitting the ESC key instead of typing Q?
# - if I type Q, it won't quit. How can we fix that?
###

class RPS:
    def __init__(self, playerName, callback):
        self.playerName = playerName
        self.callback = callback
        self.name = "Rock, Paper, Scissors"

    def play(self):
        playing = True
        weapons = ["Rock", "Paper", "Scissors"]
        beats = [2, 0, 1]
        print(f"Ok, {self.playerName} ... lets play!")
        while playing:
            playerWeapon = input("0: Rock, 1: Paper, 2: Scissors > ")
            cpuWeapon = randint(0,2)

            if(playerWeapon == "q"):
                playing = False
                self.callback(self.name)

            try:
                playerWeapon = int(playerWeapon)
            except ValueError:
                playerWeapon = 0;

            if(playerWeapon > 2):
                playerWeapon = 0

            print(f"You chose {weapons[playerWeapon]}.")
            print(f"I chose {weapons[cpuWeapon]}.")

            if(beats[playerWeapon] == cpuWeapon):
                print("You win!")
            elif(beats[cpuWeapon] == playerWeapon):
                print("I win!")
            else:
                print("It's a tie!")
