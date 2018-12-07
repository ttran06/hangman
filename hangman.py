import random
from graphics import *
from time import sleep


# Width of window
WIDTH = 500
# Height of window
HEIGHT = 600


class Hangman:
    """Functions and characteristics of the hangman game."""

    def __init__(self, word):
        """Initialize the attributes."""
        self.word = word
        self.chance_count = 0
        self.found_position = []
        self.letter_list = []
        self.guessed_letters = []
        self.word_guess = False

    # Create dashes
    def word_process(self):
        """Create dashes from len(word)."""
        # break the word into letters to make a list
        for i in range(len(self.word)):
            self.letter_list.append(self.word[i])
        for letter in self.word:
            if letter == " ":
                print(" ", end=" ") # put space if character is space
            print("_", end=" ")

    def take_guess_by_letter(self, guess_letter):
        guess = guess_letter.upper()
        self.guessed_letters.append(guess)
        letter_guess = False

        # test if the user's guessed letter is in the word

        for i in range(len(self.letter_list)):
            if (guess == self.letter_list[i]):
                self.found_position.append(i)
                letter_guess = True

        # test if the whole word has been guessed

        answer = len(self.letter_list)
        if (len(self.found_position) == answer):
            self.word_guess = True

        # print out the dashes + guesses

        for i in range(len(self.letter_list)):
            if (i in self.found_position):
                if self.letter_list[i] == " ":
                    print(" ", end=" ")
                print(self.letter_list[i], end=" ")
            else:
                if self.letter_list[i] == " ":
                    print(" ", end=" ")
                print('_', end=" ")

        # print out comments on user's guesses

        if (letter_guess == True):
            print("\nYou guess on letter " + guess_letter + " is right!" )
        else:
            print("\nSorry ;/ The letter " + guess_letter + "doesn't occur in this word...")
    def take_guess_by_word(self, guess_word):
        guess = guess_word.upper()
        self.guessed_letters.append(guess)

        # test if the user's guessed word is the right word

        if (guess == self.word):
            print("Your guess is right! The answer is " + self.word + ".")
            self.word_guess = True
        else:
            print("Sorry ;/ Your guess is wrong...")


class Button(Rectangle):
    """Create a button."""

    def onClick(self):
        """Check if the button was clicked."""
        print("Button was clicked!")


class enterButton(Button):
    """Create a Enter button."""

    def onClick(self):
        """Check if the button was clicked."""
        self.guess = user_guess_box.getText()
        if len(guess) > 1:
            Hangman.take_guess_by_word()
        else:
            Hangman.take_guess_by_letter()

def welcomeScreen():
    """Create the welcome screen and display it for 3 seconds."""
    welcomeScreen = GraphWin("Welcome", 800, 400)
    welcomeImage = Image(Point(350, 200), "welcome_image.PPM")
    welcomeImage.draw(welcomeScreen)
    sleep(3)    # Open window for 3 seconds
    welcomeScreen.close()


# Create winner splash screen
def winnerScreen():
    """Screen if user wins the game and displays for 2 seconds."""
    winnerScreen = GraphWin("Congratulations!", 600, 300)
    winnerImage = Image(Point(300, 150), "winner.gif")
    winnerImage.draw(winnerScreen)
    sleep(2)
    winnerScreen.close()


def loserScreen():
    """Screen if user lose the game and displays for 2 seconds."""
    loserScreen = GraphWin("Sorry, You Lost.", 600, 300)
    loserImage = Image(Point(300, 150), "lost.PPM")
    loserImage.draw(loserScreen)
    sleep(2)
    loserScreen.close()


def choose_category():
    """Screen where user choose the topic of the word."""
    categoryWin = GraphWin("Hangman", WIDTH, HEIGHT)
    food_image = Image(Point(100, 100), "food.PPM")
    food_image.draw(categoryWin)


# Main game window
def gameWin():
    """Main game window."""
    guessWin = GraphWin("Hangman", WIDTH, HEIGHT)

    # Draw gallow
    line1 = Line(Point(120, 50), Point(120, 200))   # Long vertical line
    line2 = Line(Point(45, 50), Point(120, 50))  # Top horizontal line
    line3 = Line(Point(45, 50), Point(45, 80))   # Short vertical line
    line4 = Line(Point(85, 200), Point(155, 200))    # Bottom horizontal line

    line1.draw(guessWin)
    line2.draw(guessWin)
    line3.draw(guessWin)
    line4.draw(guessWin)

    # Select from category file
    # food = open('food.txt', 'r').readlines()
    # word = random.choice(food)

    # Create user input box
    user_guess_box = Entry(Point(250, 400), 5)
    user_guess_box.draw(guessWin)
    while True:
        continue
    while (user_word.chance_count < 7 and user_word.word_guess is not True):
        user_word.choose_guess()
        if (user_word.word_guess is False):
            # If user has 0 wrong guess, print the head
            if user_word.chance_count == 0:
                user_word.chance_count += 1
                head = Circle(Point(45,95),15)
                head.draw(guessWin)
            # If user has 1 wrong guess, print the body
            elif user_word.chance_count == 1:
                user_word.chance_count += 1
                body = Line(Point(45, 110), Point(45, 150))
                body.draw(guessWin)
            # If user has 2 wrong guess, print the left leg
            elif user_word.chance_count == 2:
                    l_leg = Line(Point(45, 150), Point(25, 180))
                    l_leg.draw(guessWin)
            # If user has 3 wrong guess, print the right leg.
            elif user_word.chance_count == 3:
                    r_leg = Line(Point(45, 150), Point(65, 180))
                    r_leg.draw(guessWin)
            # If user has 4 wrong guess, print the left arm.
            elif user_word.chance_count == 4:
                    l_arm = Line(Point(45, 120), Point(25, 140))
                    l_arm.draw(guessWin)
            # If user has 5 wrong guess, print the right arm.
            elif user_word.chance_count == 5:
                r_arm = Line(Point(45, 120), Point(64, 140))
                r_arm.draw(guessWin)
            # If user has 6 wrong guess, print the left l_eye.
            elif user_word.chance_count == 6:
                l_eye_x = Line(Point(38, 90), Point(42, 94))
                l_eye_x2 = Line(Point(42, 90), Point(38, 94))
                l_eye_x.draw(guessWin)
                l_eye_x2.draw(guessWin)
            # If user has 7 wrong guess, print the right eye.
            elif user_word.chance_count == 7:
                r_eye_x = Line(Point(48, 90), Point(52, 94))
                r_eye_x2 = Line(Point(52,90), Point(48, 94))
                r_eye_x.draw(guessWin)
                r_eye_x2.draw(guessWin)
            # If the user has 8 wrong guess, print the mouth.
            elif user_word.chance_count == 8:
                mouth = Line(Point(42, 100), Point(47, 100))
                mouth.draw(guessWin)
           for i in range(len(user_word.guessed_letters)):
               print(user_word.guessed_letters[i], end = " ")
        else:
            print("Congratulations! You won the game!")

    print("Game over! The answer is " + word)

gameWin()
def test():
    # Print welcome splash screen
    welcomeScreen()

    # Category screen

    # Game screen

    # Win or lose screen
