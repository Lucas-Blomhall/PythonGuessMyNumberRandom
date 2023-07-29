import random

class GuessMyNumber:
    def __init__(self):
        self.number = random.randint(1, 100)
        self.attempts = 0

    def play(self):
        while True:
            guess = int(input("Enter your guess: "))
            self.attempts += 1

            if guess < self.number:
                print("Too low!")
            elif guess > self.number:
                print("Too high!")
            else:
                print("Congratulations! You guessed the number in", self.attempts, "attempts.")
                break

game = GuessMyNumber()
game.play()