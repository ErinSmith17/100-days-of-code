import random

max_guesses = 5
START, END = 1,20

def get_random_num():
    # gets a random num between start and end, returns int
    return random.randint(START, END)

class Game:
    # Number guess class, make it callable to inititate game

    def __init__(self):
        # init _guesses, _answer, _win to set(), get_random_num(), False
        self._guesses = set()
        self._answer = get_random_num()
        self._win = False

    def guess(self):
        # asks user for input, converts to int, rasies ValueError outputting the following errors when applicable:
        # 'Please enter a num', 'Should be a num', 'Num not in range', 'Already guessed'
        # If all good, return int
        guess = input(f'Guess a number between {START} and {END}: ')
        if not guess:
            raise ValueError('Please enter a number')
        try:
            guess = int(guess)
        except ValueError:
            raise ValueError('Should be a number')

        if guess not in range(START, END+1):
            raise ValueError('Number not in range')

        if guess in self._guesses:
            raise ValueError('Already guessed')

        self._guesses.add(guess)
        return guess

    def _validate_guess(selfself, guess):
        # verify if the guess is correcy, prints the following
        # {guess} is correct, {guess} is too low, {guess} is too high, returns a Boolean
        if guess == self._answer:
            print(f'{guess} is correct!')
            return True
        else:
            high_or_low = 'low' if guess < self._answer else 'high'
            print(f'{guess} is too {high_or_low}')
            return False

    @property
    def num_guesses(self):
        return len(self._guesses)

    def __call__(self):
        # entry points, game loop, sees the tests for the win/lose message
        while len(self._guesses) < MAX_GUESSES:
            try:
                guess = self.guess()
            except ValueError as ve:
                print(ve)
                continue

            win = self._validate_guess(guess)
            if win:
                guess_str = self.num_guesses == 1 and "guess" or "guesses"
                print(f'It took you {self.num_guesses} {guess_str}')
                self._win = True
                break
        else:
            # else on while/for = anti-pattern? do find it useful in this case!
            print(f'Guessed {MAX_GUESSES} times, answer was {self._answer}')

    if __name__ == '__main__':
        game = Game()
        game()
