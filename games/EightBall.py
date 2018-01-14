from random import choice

###
# Things to try
# - More answers to questions would be cool.
# - What if I asked the same question again? Should it remind me I already got an answer? 
###

class EightBall:
    def __init__(self, playerName, callback):
        self.playerName = playerName
        self.callback = callback
        self.name = "Magic Eightball"

    def play(self):
        print(f"Welcome to the magic eightball, {self.playerName} ... Type your question below.")
        answers = ["Yes","No","Maybe"]
        playing = True
        while playing:
            question = input("> ")
            if(question == "q"):
                playing = False
                self.callback(self.name)
            else:
                answer = choice(answers)
                print(f"{answer}")
