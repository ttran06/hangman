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
                print(" ", end=" ")  # put space if character is space
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

        if (letter_guess is True):
            print("\nYou guess on letter " + guess_letter + " is right!")
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


# This function Prints the categories.
def CategoryScreen():
    # Create window
    win = GraphWin("Hangman", 1640, 800)

    # creating the graphics
    PickCategory = Image(Point(800, 100), "pickcategory.gif")
    food = Image(Point(134, 500), "food.gif")
    animal = Image(Point(455.5, 500), "animal2.gif")
    countries = Image(Point(838, 500), "animal.gif")
    Popculture = Image(Point(1243, 500), "Pop culture.gif")
    questionmark = Image(Point(1545.5, 500), "questionmark.gif")

    # Returns the width of the image
    Width_food = food.getWidth()
    Width_animal = animal.getWidth()
    Width_countries = countries.getWidth()
    Width_Popculture = Popculture.getWidth()
    Width_questionmark = questionmark.getWidth()

    # Returns the height of the image
    Height_food = food.getHeight()
    Height_animal = animal.getHeight()
    Height_countries = countries.getHeight()
    Height_Popculture = Popculture.getHeight()
    Height_questionmark = questionmark.getHeight()

    # Returns the center of the image
    Center_food = food.getAnchor()
    Center_animal = animal.getAnchor()
    Center_countries = countries.getAnchor()
    Center_Questionmark = questionmark.getAnchor()
    Center_Popculture = Popculture.getAnchor()

    # Returns the X Coord of the center of the image
    X_Center_food = Center_food.getX()
    X_Center_animal = Center_animal.getX()
    X_Center_countries = Center_countries.getX()
    X_Center_Questionmark = Center_Questionmark.getX()
    X_Center_Popculture = Center_Popculture.getX()

    # returns the Y cordinate of the center of the image
    Y_Center_food = Center_food.getY()
    Y_Center_animal = Center_animal.getY()
    Y_Center_countries = Center_countries.getY()
    Y_Center_Questionmark = Center_Questionmark.getY()
    Y_Center_Popculture = Center_Popculture.getY()

    # to get the max (X and Y) and min (X and Y) for the food
    X_cordinate2_food = (Width_food/2) + X_Center_food
    X_cordinate1_food = X_Center_food - (Width_food/2)
    Y_cordinate2_food = (Height_food/2) + Y_Center_food
    Y_cordinate1_food = Y_Center_food - (Height_food/2)

    # to get the max (X and Y) and min (X and Y) for the animal
    X_cordinate2_animal = (Width_animal/2) + X_Center_animal
    X_cordinate1_animal = X_Center_animal - (Width_animal/2)
    Y_cordinate2_animal = (Height_animal/2) + Y_Center_animal
    Y_cordinate1_animal = Y_Center_animal - (Height_animal/2)

    # to get the max (X and Y) and min (X and Y) for the countries
    X_cordinate2_country = (Width_countries/2) + X_Center_countries
    X_cordinate1_country = X_Center_countries - (Width_countries/2)
    Y_cordinate2_country = (Height_countries/2) + Y_Center_countries
    Y_cordinate1_country = Y_Center_countries - (Height_countries/2)

    # to get the max (X and Y) and min (X and Y) for the PopCulture
    X_cordinate2_PopCulture = (Width_Popculture/2) + X_Center_Popculture
    X_cordinate1_PopCulture = X_Center_Popculture - (Width_Popculture/2)
    Y_cordinate2_PopCulture = (Height_Popculture/2) + Y_Center_Popculture
    Y_cordinate1_PopCulture = Y_Center_Popculture - (Height_Popculture/2)

    # to get the max (X and Y) and min (X and Y) for the Question mark
    X_cordinate2_questionmark = (Width_questionmark/2) + X_Center_Questionmark
    X_cordinate1_questionmark = X_Center_Questionmark - (Width_questionmark/2)
    Y_cordinate2_questionmark = (Height_questionmark/2) + Y_Center_Questionmark
    Y_cordinate1_questionmark = Y_Center_Questionmark - (Height_questionmark/2)

    # Drawing the window and all the images onto the window
    PickCategory.draw(win)
    food.draw(win)
    animal.draw(win)
    countries.draw(win)
    Popculture.draw(win)
    questionmark.draw(win)

    # Returns the point where the mouse is clicked
    Pos_mouse_clicked = win.getMouse()

    # X-Position of the point clicked
    X_point_mouse_clicked = Pos_mouse_clicked.getX()

    # Y-Position of the point clicked
    Y_point_mouse_clicked = Pos_mouse_clicked.getY()

    # finds where the mouse has been clicked
    # Food category
    if X_point_mouse_clicked <  X_cordinate2_food and Y_cordinate1_PopCulture < Y_point_mouse_clicked < Y_cordinate2_PopCulture:
        file = open("food.txt". "r")
        word_list = file.readlines()
        file.close()
        word_to_guess = random.choice(word_list)

        if ("\n" in word_to_guess):
            word = word_to_guess
        else:
            word = word_to_guess

        return word
    # Animal category
    elif X_cordinate1_animal < X_point_mouse_clicked < X_cordinate2_animal and Y_cordinate1_PopCulture < Y_point_mouse_clicked < Y_cordinate2_PopCulture:
        file = open("animal.txt". "r")
        word_list = file.readlines()
        file.close()
        word_to_guess = random.choice(word_list)

        if ("\n" in word_to_guess):
            word = word_to_guess
        else:
            word = word_to_guess

        return word
    # Geography category
    elif X_cordinate1_country < X_point_mouse_clicked < X_cordinate2_country and Y_cordinate1_PopCulture < Y_point_mouse_clicked < Y_cordinate2_PopCulture:
        file = open("geography.txt". "r")
        word_list = file.readlines()
        file.close()
        word_to_guess = random.choice(word_list)

        if ("\n" in word_to_guess):
            word = word_to_guess
        else:
            word = word_to_guess

        return word
    # Pop culture
    elif X_cordinate1_PopCulture < X_point_mouse_clicked < X_cordinate2_PopCulture and Y_cordinate1_PopCulture < Y_point_mouse_clicked < Y_cordinate2_PopCulture:
        file = open("popculture.txt". "r")
        word_list = file.readlines()
        file.close()
        word_to_guess = random.choice(word_list)

        if ("\n" in word_to_guess):
            word = word_to_guess
        else:
            word = word_to_guess

        return word
    # Random
    elif X_cordinate1_questionmark < X_point_mouse_clicked < X_cordinate2_questionmark and Y_cordinate1_PopCulture < Y_point_mouse_clicked < Y_cordinate2_PopCulture:
        categ_list = ['food.txt',
                      'animal.txt',
                      'geography.txt',
                      'popculture.txt']
        categ = random.choice(categ_list)

        file = open(categ, 'r')
        word_list = file.readlines()
        file.close()

        if ("\n" in word_to_guess):
            word = word_to_guess.strip("\n")
        else:
            word = word_to_guess

        return word
    # The Y coordinate of the centers of the images is the same. I will use the
    # height of the popculture image as my boundary for the click point because
    # it has the greatest height "333" compared to the other images.
    elif Y_cordinate1_PopCulture > Y_point_mouse_clicked or Y_point_mouse_clicked > Y_cordinate2_PopCulture:
        print("invalid input, try clicking on the image.")


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


# Main game window
def gameWin(word):
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

    # Draw dashes

    # Create user input box
    user_guess_box = Entry(Point(250, 400), 5)
    user_guess_box.draw(guessWin)

    game_won = False

    # While user has 8 or less incorrect guess or word has not been guessed
    while ((user_word.chance_count <= 8) or (user_word.word_guess is not True)):
        user_word.choose_guess()
        # If word has not been guess
        if (user_word.word_guess is False):
            continue
        else:
            winnerScreen()  # Congratulations you won screen

    loserScreen()


gameWin()


def main():
    # Print welcome splash screen
    welcomeScreen()

    # Category screen
    word = CategoryScreen()
    user_word = Hangman(word)

    # Game screen
    gameWin(user_word)
