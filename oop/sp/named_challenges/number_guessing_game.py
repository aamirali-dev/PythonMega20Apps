import datetime
import random
import string
import time


class LetterException(Exception):
    pass


class BeforeLetter(LetterException):
    pass


class AfterLetter(LetterException):
    pass


class NotALetter(LetterException):
    pass


class Game:

    def start(self):
        letter = random.choice(list(string.ascii_lowercase))
        noag = 0
        nobg = 0
        nonal = 0
        print(f'guess a letter game started{letter}')
        start_time = time.time()
        try:
            while True:
                try:
                    guess = input('Input a letter and hit enter: ')
                    if 'z' < guess < 'a':
                        raise NotALetter()
                    if guess == letter:
                        break
                    elif guess > letter:
                        raise AfterLetter()
                    else:
                        raise BeforeLetter()
                except AfterLetter:
                    print('letter you selected is after the actual letter')
                    noag += 1
                except BeforeLetter:
                    print('letter you selected is before the actual letter')
                    nobg += 1
                except NotALetter:
                    print('input is not a valid letter')
                    nonal += 1
        except KeyboardInterrupt:
            print('Interrupted by keyboard')
        finally:
            print(f'total time taken: {time.time() - start_time:.2f}s')
            print(f'total letters guessed before the actual letter: {nobg}')
            print(f'total letters guessed after the actual letter: {noag}')


g = Game()
g.start()
