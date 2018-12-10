import random
import time

class Hangman:

    # Initialize the attributes

    def __init__(self, word):
        self.word = word
        self.chance_count = 0
        self.found_position = []
        self.letter_list = []
        self.guessed_letters = []
        self.word_guess = False

    # Ask the user to chosse between guessing by letter or by word

    def choose_guess(self):
        
        user_choice = int(input("Do you want to: 1. guess by letter, or 2. guess by word?"))

        if (user_choice == 1):
            user_guess = input("Guess a letter: ")
            self.take_guess_by_letter(user_guess)
        if (user_choice == 2):
            user_guess = input("Guess the word: ")
            self.take_guess_by_word(user_guess)

    def word_process(self):
        
        # break the word into letters to make a list
        for i in range(len(self.word)):
            self.letter_list.append(self.word[i])
            
        # print the dashes
        print("Here's the word to guess: " + "_ " * len(self.word))
        time.sleep(0.3)

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
                print(self.letter_list[i], end = " ")
            else:
                print('_', end = " ")

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

# Ask the user to choose their preferred category of words

def choose_category():
    
    print("Choose a word from the following categories: 1. Animals; 2. Food; 3. Countries.")
    user_choice = int(input("Make your choice here (in numbers): "))

    # read the file based on user choice and make a list for all the words under that category

    if (user_choice == 1):
        file = open("animals.txt", "r")
        word_list = file.readlines()
    if (user_choice == 2):
        file = open("food.txt", "r")
        word_list = file.readlines()
    if (user_choice == 3):
        file = open("countries.txt", "r")
        word_list = file.readlines()

    # close the file
    file.close()

    # choose a random word from the word list
    word_to_guess = random.choice(word_list)

    if ("\n" in word_to_guess):
        word = word_to_guess.strip("\n")
    else:
        word = word_to_guess

    return word

def main():
    word = choose_category()
    user_word = Hangman(word)
    user_word.word_process()

    # The user is given 7 chances to get the word right.

    while (user_word.chance_count < 7 and user_word.word_guess != True):
        user_word.choose_guess()
        if (user_word.word_guess == False):
           user_word.chance_count += 1
           print("You have already guessed the following: ")
           for i in range(len(user_word.guessed_letters)):
               print(user_word.guessed_letters[i], end = " ")
           print("\nYou have", (7 - user_word.chance_count), "chance(s) left! Way to go!")
        else:
            print("Congratulations! You won the game!")

    print("Game over! The answer is " + word)

if __name__ == "__main__":
    main()

