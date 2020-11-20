from random import choice
from string import ascii_lowercase

with open("words", "r") as words:
    word_list = [_ for _ in words]
end = False
max_guesses = 10
symbol = "-"
greeting = "Welcome to \n\n" \
           "|-------------|\n" \
           "|H A N G M A N|\n" \
           "|-------------|\n\n" \
           "Enter \"q\" to quit\n" \
           "or press enter to \n" \
           "start a new game"
input_error_message = 'Please enter'
starting_message= f'The secret word has {num} letters. Good Luck!'


class Game:
    def __init__(self):
        self.tries = max_guesses
        self.secret_word = choice(word_list)
        self.word_label = symbol * len(self.secret_word)
        print(f'The secret word has {len(self.secret_word)} letters. Good Luck!')
        self.logic()

    def logic(self):
        while self.word_label != self.secret_word and self.tries > 0:
            self.showOutput()
            self.guess()
            self.handleOutput()
        self.finishGame()

    def showOutput(self):
        #TODO: add and display list for already entered letters.
        print(self.word_label)

    def guess(self):
        print()
        guess = input("Guess a letter! ").lower()
        if guess in ascii_lowercase and len(guess) == 1:
            if guess in self.secret_word:
                self.word_label = [s if s == guess else symbol for s in self.secret_word]
        else:
            print("Please ")

    def handleOutput(self):
        pass

    def finishGame(self):
        pass


def main():
    while not end:
        guesses = max_guesses
        print(greeting)
        if input().lower() == "q":
            break
        game = Game()


main()
