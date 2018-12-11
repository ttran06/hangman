import random
from graphics import *
from time import sleep


# Width of window
WIDTH = 500
# Height of window
HEIGHT = 600


class Hangman:
    """Functions and characteristics of the hangman game."""

    def __init__(self, word, win):
        """Initialize the attributes."""
        self.word = word
        self.chance_count = 0
        self.win = win
        self.found_position = []
        self.letter_list = []
        self.guessed_letters = []
        self.trash_bin = []
        self.word_guess = False
        self.dashes = ""
        self.d = Text(Point(240, 290), self.dashes)


    # Create dashes
    def word_process(self):
        """Create dashes from len(word)."""
        # break the word into letters to make a list
        for i in range(len(self.word)):
            self.letter_list.append(self.word[i])

        # Create dashes
        for letter in self.word:
            if letter != " ":
                self.dashes = self.dashes + '_'
                self.dashes = self.dashes + ' '
            else:
                self.dashes = self.dashes + ' '

        # Remove last ' '
        self.dashes = self.dashes[0:len(self.dashes)-1]
        self.d = Text(Point(240, 290), self.dashes)
        self.d.draw(self.win)

    # If user guess by letter
    def take_guess_by_letter(self, guess_letter):
        guess = guess_letter.upper()
        self.guessed_letters.append(guess)
        letter_guess = False
        letter_list_spaces = []

        # Put a space between every letter in the word
        for letter in self.word:
            if letter != " ":
                letter_list_spaces.append(letter)
                letter_list_spaces.append(" ")
            else:
                letter_list_spaces.append(letter)
        # Remove last element from list, remove " "
        del letter_list_spaces[-1]

        for i in range(len(letter_list_spaces)):
            if (guess == letter_list_spaces[i]):
                self.found_position.append(i)
                letter_guess = True

        list_dashes = list(self.dashes)
        # print(letter_list_spaces)

        # print out the dashes + guesses
        for i in range(len(letter_list_spaces)):
            if (i in self.found_position):
                list_dashes[i] = letter_list_spaces[i]
                dashes_guess = "".join(list_dashes)
                self.d.setText(dashes_guess)

        # test if the whole word has been guessed
        new_list = self.letter_list.copy()
        if " " in new_list:
            new_list.remove(" ")
        answer = len(new_list)
        if (len(self.found_position) == answer):
            self.word_guess = True
            winnerScreen()

        # print out comments on user's guesses

        if (letter_guess is True):
            m = Text(Point(270, 480), "Your guess is correct!")
            m.draw(self.win)
            sleep(1)
            m.undraw()
            return letter_guess
        else:
            self.trash_bin.append(guess)
            m = Text(Point(270, 500), "Sorry. Your guess doesn't occur in this word")
            m.draw(self.win)
            sleep(1)
            m.undraw()
            return letter_guess

    def take_guess_by_word(self, guess_word):
        guess = guess_word.upper()
        self.guessed_letters.append(guess)

        # test if the user's guessed word is the right word

        if (guess == self.word):
            s = "Your guess is right! The answer is " + self.word + "."
            m = Text(Point(270, 470), s)
            m.draw(self.win)
            sleep(0.5)
            self.word_guess = True
        else:
            self.trash_bin.append(guess)
            print("Sorry ;/ Your guess is wrong...")
            self.word_guess = False

# print out the wrong guesses in the trash bin
def trashBin(user_word, guessWin):

    title = Text(Point(100, 230), "List of wrong guesses:")
    wrong_guesses = Text(Point(270, 230), user_word.trash_bin)

    if (len(user_word.trash_bin) < 8):
        trashBox = Rectangle(Point(245, 220), Point(350, 240))
    else:
        n = len(user_word.trash_bin) - 4
        trashBox = Rectangle(Point((245 - 10*n), 220), Point((295 + 10*n), 240))

    trashBox.draw(guessWin)
    trashBox.setFill(color_rgb(0, 255, 255))
    trashBox.setWidth(2)
    title.draw(guessWin)
    wrong_guesses.draw(guessWin)


def welcomeScreen():
    """Create the welcome screen and display it for 2 seconds."""
    welcomeScreen = GraphWin("Welcome", 800, 400)
    welcomeImage = Image(Point(350, 200), "welcome_image.PPM")
    welcomeImage.draw(welcomeScreen)
    sleep(2)    # Open window for 2 seconds
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
        file = open("food.txt", "r")
        word_list = file.readlines()
        file.close()
        word_to_guess = random.choice(word_list)

        if ("\n" in word_to_guess):
            word = word_to_guess.strip("\n")
        else:
            word = word_to_guess

        win.close()
        return word

    # Animal category
    elif X_cordinate1_animal < X_point_mouse_clicked < X_cordinate2_animal and Y_cordinate1_PopCulture < Y_point_mouse_clicked < Y_cordinate2_PopCulture:
        file = open("animal.txt", "r")
        word_list = file.readlines()
        file.close()
        word_to_guess = random.choice(word_list)

        if ("\n" in word_to_guess):
            word = word_to_guess.strip("\n")
        else:
            word = word_to_guess

        win.close()
        return word

    # Geography category
    elif X_cordinate1_country < X_point_mouse_clicked < X_cordinate2_country and Y_cordinate1_PopCulture < Y_point_mouse_clicked < Y_cordinate2_PopCulture:
        file = open("geography.txt", "r")
        word_list = file.readlines()
        file.close()
        word_to_guess = random.choice(word_list)

        if ("\n" in word_to_guess):
            word = word_to_guess.strip("\n")
        else:
            word = word_to_guess

        win.close()
        return word

    # Pop culture
    elif X_cordinate1_PopCulture < X_point_mouse_clicked < X_cordinate2_PopCulture and Y_cordinate1_PopCulture < Y_point_mouse_clicked < Y_cordinate2_PopCulture:
        file = open("popculture.txt", "r")
        word_list = file.readlines()
        file.close()
        word_to_guess = random.choice(word_list)

        if ("\n" in word_to_guess):
            word = word_to_guess.strip("\n")
        else:
            word = word_to_guess

        win.close()
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
        word_to_guess = random.choice(word_list)


        if ("\n" in word_to_guess):
            word = word_to_guess.strip("\n")
        else:
            word = word_to_guess

        win.close()
        return word

    # The Y coordinate of the centers of the images is the same. I will use the
    # height of the popculture image as my boundary for the click point because
    # it has the greatest height "333" compared to the other images.
    elif Y_cordinate1_PopCulture > Y_point_mouse_clicked or Y_point_mouse_clicked > Y_cordinate2_PopCulture:
        message = Text(Point(900, 200), "Not a valid choice.")
        message.draw(win)

# Create winner splash screen
def winnerScreen():
    """Screen if user wins the game and displays for 2 seconds."""
    winnerScreen = GraphWin("Congratulations!", 600, 300)
    winnerImage = Image(Point(300, 150), "winner.gif")
    winnerImage.draw(winnerScreen)
    sleep(2)
    winnerScreen.close()


# Create lose splash screen
def loserScreen():
    """Screen if user lose the game and displays for 2 seconds."""
    loserScreen = GraphWin("Sorry, You Lost.", 600, 300)
    loserImage = Image(Point(300, 150), "lost.PPM")
    loserImage.draw(loserScreen)
    sleep(2)
    loserScreen.close()


def continueScreen():
    win = GraphWin("Continue screen", WIDTH, HEIGHT)
    continue_message = Text(Point(240, 100), "Do you want to play again?")
    continue_message.setSize(28)
    yesBtn = Rectangle(Point(50, 150), Point(150, 250))
    noBtn = Rectangle(Point(350, 150), Point(450, 250))
    yes_message = Text(Point(100, 200), "YES")
    no_message = Text(Point(400, 200), "NO")
    yesBtn.setFill("green")
    noBtn.setFill("red")
    continue_message.draw(win)
    yesBtn.draw(win)
    noBtn.draw(win)
    yes_message.draw(win)
    no_message.draw(win)

    mousePt = win.getMouse()

    # If user click within yes button
    # Check if user click within x range of yes button
    if (yesBtn.getP1().getX() < mousePt.getX() < yesBtn.getP2().getX()):
        # Check if user click within y range of yes button
        if (yesBtn.getP1().getY() < mousePt.getY() < yesBtn.getP2().getY()):
            game = True
            win.close()
            return game
    # If user click within no button
    # Check if user click within x range of no button
    if (noBtn.getP1().getX() < mousePt.getX() < noBtn.getP2().getX()):
        # Check if user click within y range of no button
        if (noBtn.getP1().getY() < mousePt.getY() < noBtn.getP2().getY()):
            game = False
            win.close()
            return game

def goodbyeScreen():
    win = GraphWin("Goodbye!", WIDTH, HEIGHT)

    goodbye = Text(Point(250, 300), "GOODBYE!")
    goodbye.setSize(28)
    goodbye.draw(win)
    sleep(2)
    win.close()


# Main game window
def gameWin(guessWin, user_word):
    """Main game window."""

    # Draw gallow
    line1 = Line(Point(120, 50), Point(120, 200))   # Long vertical line
    line2 = Line(Point(45, 50), Point(120, 50))  # Top horizontal line
    line3 = Line(Point(45, 50), Point(45, 80))   # Short vertical line
    line4 = Line(Point(85, 200), Point(155, 200))    # Bottom horizontal line

    line1.draw(guessWin)
    line2.draw(guessWin)
    line3.draw(guessWin)
    line4.draw(guessWin)


    user_word.word_process()  # Create dashes

    # Draw enter Button
    enterBtn = Rectangle(Point(250, 390), Point(300, 410))
    p1 = Point(250, 390)
    p2 = Point(300, 410)
    enter_message = Text(Point(270, 400), "Enter")
    enterBtn.setFill("yellow")
    enterBtn.setWidth(2)
    enterBtn.draw(guessWin)
    enter_message.draw(guessWin)


    # Create user input box
    user_guess_box = Entry(Point(200, 400), 5)
    user_guess_box.draw(guessWin)


    # While user has 8 or less incorrect guess or word has not been guessed
    while ((user_word.chance_count <= 8) and (user_word.word_guess is not True)):
        mousePt = guessWin.getMouse()
        if (enterBtn.getP1().getX() < mousePt.getX() < enterBtn.getP2().getX()):
                # Check if their click was within the y range of the button
                if (enterBtn.getP1().getY() < mousePt.getY() < enterBtn.getP2().getY()):
                    guess = user_guess_box.getText()
                    user_guess_box.setText("")
                    if (len(guess) == 1):
                        answer = user_word.take_guess_by_letter(guess)
                        if answer is True:
                            continue
                        else:
                            # If user has 0 wrong guess, print the head
                            if user_word.chance_count == 0:
                                user_word.chance_count += 1
                                head = Circle(Point(45,95),15)
                                head.draw(guessWin)
                                trashBin(user_word, guessWin)
                            # If user has 1 wrong guess, print the body
                            elif user_word.chance_count == 1:
                                user_word.chance_count += 1
                                body = Line(Point(45, 110), Point(45, 150))
                                body.draw(guessWin)
                                trashBin(user_word, guessWin)
                            # If user has 2 wrong guess, print the left leg
                            elif user_word.chance_count == 2:
                                user_word.chance_count += 1
                                l_leg = Line(Point(45, 150), Point(25, 180))
                                l_leg.draw(guessWin)
                                trashBin(user_word, guessWin)
                            # If user has 3 wrong guess, print the right leg.
                            elif user_word.chance_count == 3:
                                user_word.chance_count += 1
                                r_leg = Line(Point(45, 150), Point(65, 180))
                                r_leg.draw(guessWin)
                                trashBin(user_word, guessWin)
                            # If user has 4 wrong guess, print the left arm.
                            elif user_word.chance_count == 4:
                                user_word.chance_count += 1
                                l_arm = Line(Point(45, 120), Point(25, 140))
                                l_arm.draw(guessWin)
                                trashBin(user_word, guessWin)
                            # If user has 5 wrong guess, print the right arm.
                            elif user_word.chance_count == 5:
                                user_word.chance_count += 1
                                r_arm = Line(Point(45, 120), Point(64, 140))
                                r_arm.draw(guessWin)
                                trashBin(user_word, guessWin)
                            # If user has 6 wrong guess, print the left l_eye.
                            elif user_word.chance_count == 6:
                                user_word.chance_count += 1
                                l_eye_x = Line(Point(38, 90), Point(42, 94))
                                l_eye_x2 = Line(Point(42, 90), Point(38, 94))
                                l_eye_x.draw(guessWin)
                                l_eye_x2.draw(guessWin)
                                trashBin(user_word, guessWin)
                            # If user has 7 wrong guess, print the right eye.
                            elif user_word.chance_count == 7:
                                user_word.chance_count += 1
                                r_eye_x = Line(Point(48, 90), Point(52, 94))
                                r_eye_x2 = Line(Point(52,90), Point(48, 94))
                                r_eye_x.draw(guessWin)
                                r_eye_x2.draw(guessWin)
                                trashBin(user_word, guessWin)
                            # If the user has 8 wrong guess, print the mouth.
                            elif user_word.chance_count == 8:
                                user_word.chance_count += 1
                                mouth = Line(Point(42, 100), Point(47, 100))
                                mouth.draw(guessWin)
                                loserScreen()
                                trashBin(user_word, guessWin)
                                guessWin.close()

                    else:
                        answer = user_word.take_guess_by_word(guess)

        # If word has not been guess

        if (user_word.word_guess == True):
            winnerScreen()  # Congratulations you won screen


def main():
    # Print welcome splash screen
    welcomeScreen()


    while True:
        guessWin = GraphWin("Hangman", WIDTH, HEIGHT)
        # Category screen
        word = CategoryScreen()
        user_word = Hangman(word, guessWin)

        # Game screen
        gameWin(guessWin, user_word)

        # Calling the continue screen
        game = continueScreen()
        if game is True:
            continue
        else:
            break

    goodbyeScreen()

main()
