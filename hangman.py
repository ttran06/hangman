from graphics import *
from time import sleep
import random

# TODO: Splash Window
def printWelcomeScreen():
    welcomeScreen = GraphWin("Welcome", 800, 400)
    welcomeImage = Image(Point(350, 200), "welcome_image.PPM")
    welcomeImage.draw(welcomeScreen)
    sleep(3)    # Open window for 3 seconds
    welcomeScreen.close()
# TODO: Category symbol graphics

# TODO: Connect category graphics to choice of words in the game


# TODO: Create the guess Window
def test():
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

    # Select random word from food.txt
    food_f = open('food.txt', 'r')
    food = food_f.read().splitlines()
    word = random.choice(food)
#
# main()
# TODO: Create the components that are displayed on the window
# Draw Hangman
def drawMan(n_guess):
    if n_guess == 1:
        pass

# TODO: Randomly select a word from correct file

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
        sleep(0.3)

# TODO: User input window
WIDTH = 500
HEIGHT = 600

guessWin = GraphWin("Hangman", WIDTH, HEIGHT)
userGuess = Entry(Point(200, 200), 5)
userGuess.draw(guessWin)

# TODO: Swinging of man animation

# TODO: Determine if guessed letter is right or wrong
# if userGuess in word:
#     put in right space of dashes
# else:
#     put in trash
# TODO: Put incorrect guess in TRASH

# TODO: Put correct guess in dashes

# TODO: Winner Splash screen
def winnerScreen():
    winnerScreen = GraphWin("Congratulations!", 600, 300)
    winnerImage = Image(Point(300,150), "winner.gif")
    winnerImage.draw(winnerScreen)
    sleep(10)
    winnerScreen.close()
winnerScreen()
# TODO: Loser Splash screen
def loserScreen():
    loserScreen = GraphWin("Sorry, You Lost.", 600, 300)
# TODO: Continue screen
