from graphics import *
from time import sleep
import random


class Hangman:

    # Initialize the attributes
    def __init__(self, word):
        self.word = word
        self.chance_count = 0
        self.found_position = []
        self.letter_list = []
        self.guessed_letters = []
        self.word_guess = False

    # Create dashes
    def word_process(self):

        # break the word into letters to make a list
        for i in range(len(self.word)):
            self.letter_list.append(self.word[i])

        # print the dashes
        print("Here's the word to guess: " + "_ " * len(self.word))


class Button(Rectangle):

    def onClick(self):
        print("Button was clicked!")


class guessWord(Button):
    def onClick(self):
        

# Create welcome splash screen
def printWelcomeScreen():
    welcomeScreen = GraphWin("Welcome", 800, 400)
    welcomeImage = Image(Point(350, 200), "welcome_image.PPM")
    welcomeImage.draw(welcomeScreen)
    sleep(3)    # Open window for 3 seconds
    welcomeScreen.close()


# Create winner splash screen
def winnerScreen():
    winnerScreen = GraphWin("Congratulations!", 600, 300)
    winnerImage = Image(Point(300,150), "winner.gif")
    winnerImage.draw(winnerScreen)
    sleep(2)
    winnerScreen.close()


# Create loser splash screen
def loserScreen():
    loserScreen = GraphWin("Sorry, You Lost.", 600, 300)
    loserImage = Image(Point(300,150), "lost.PPM")
    loserImage.draw(loserScreen)
    sleep(2)
    loserScreen.close()


# Main game window
def gameWin():
        WIDTH = 500
        HEIGHT = 600

        guessWin = GraphWin("Hangman", WIDTH, HEIGHT)

        # Draw gallow
        line1 = Line(Point(100, 50), Point(100, 150))   # Long vertical line
        line2 = Line(Point(50, 50), Point(100,50))  # Top horizontal line
        line3 = Line(Point(50,50), Point(50, 70))   # Short vertical line
        line4 = Line(Point(75,150), Point(125, 150))    # Bottom horizontal line
        line1.draw(guessWin)
        line2.draw(guessWin)
        line3.draw(guessWin)
        line4.draw(guessWin)

        # Select from food
        food = open('food.txt', 'r').readlines()
        word = random.choice(food)

        # Create user input box
        user_guess_box = Entry(Point(200, 200), 5)
        user_guess_box.draw(guessWin)


def test():
    # Print welcome splash screen
    welcomeScreen()

    # Category screen

    # Game screen

    # Win or lose screen
