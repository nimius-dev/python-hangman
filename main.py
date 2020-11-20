from random import choice
from string import ascii_lowercase

with open("words", "r") as words:
    word_list = [_.rstrip() for _ in words]
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
input_error_message = "Please enter a single letter"
starting_message = 'The secret word has {num} letters. Good Luck!'
win_message = 'Congratulations, you won! The secret word was {secret}. You had {num} wrong guesses.'
loss_message = 'Sorry, no more tries left. You lost! The secret word was {secret}.'
guess_message = "Guess a letter! You have {num} wrong guesses so far.\n"
right_message = "Good job, \"{letter}\" is in the secret word"

class Game:
    def __init__(self):
        self.tries = max_guesses
        self.secret_word = choice(word_list)
        self.word_label = symbol * len(self.secret_word)
        print(starting_message.format(num=len(self.secret_word)))
        self.logic()

    def logic(self):
        while self.word_label != self.secret_word and self.tries > 0:
            self.showOutput()
            self.guess()
        self.finishGame()

    def showOutput(self):
        # TODO: add and display list for already entered letters.
        print(self.word_label.upper())

    def guess(self):
        print()
        guess = input(guess_message.format(num=max_guesses-self.tries)).lower()  # TODO: Let user guess whole word
        if guess in ascii_lowercase and len(guess) == 1:
            if guess in self.secret_word:
                print(right_message.format(letter=guess))
                self.word_label = ''.join([s if s == guess else self.word_label[self.secret_word.index(s)] for s in self.secret_word])
            else:
                self.tries -= 1
        else:
            print(input_error_message)

    def finishGame(self):
        if self.tries > 0:
            print(win_message.format(secret=self.secret_word, num=max_guesses-self.tries))
        else:
            print(loss_message.format(secret=self.secret_word))


def main():
    while not end:
        guesses = max_guesses
        print(greeting)
        if input().lower() == "q":
            break
        game = Game()


main()
