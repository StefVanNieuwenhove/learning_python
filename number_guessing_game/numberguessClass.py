import random
import sys

class Player():
    def __init__(self, player):
        self.name = player
        self.max_guess = 20
        self.cnt_guess = 0
        self.level = 0
        self.wins = 0



class Game() :
    def __init__(self, player):
        #Assign variables   
        self.nbr = self.get_random_nbr(self)
        self.player = player
        self.difficulty = 1
        self.levels = {'0': 20, '1': 18, '2': 15}
        print('Game is set! Good Luck')

    def get_random_nbr(self, _min=None, _max=None):
        while (_min == None) or (_max == None):
            try:
                _min = int(input("What's the MIN value: ")) 
                _max = int(input("What's the MAX value: ")) * self.difficulty
                if _max < _min:
                    _min, _max = _max, _min
                    print('You numbners were incerted...')
                nbr = random.randint(_min, _max)
                return nbr
            except Exception as E: 
                print('MIN and MAX must be nubers')
                pass

    def check_number(self, usernbr):
        # Check if number is INTEGER
        try:
            usernbr = int(usernbr)
        except Exception as E:
            print('Guess must be number, not a string\n')
            return False

        # check if number is the same
        if usernbr == self.nbr:
            print("Congrats you found the number")
            self.player.cnt_guess += 1
            self.player.level += 1
            return True

        #check if number is <
        if usernbr < self.nbr:
            print('The number to guess is Bigger')
            self.player.cnt_guess += 1
            return False
        #check if number is >
        if usernbr > self.nbr:
            print('The number to guess is Smaller')
            self.player.cnt_guess += 1
            return False

        return False


if __name__ == "__main__":
    player = Player('Steven')
    print(player.name)
    game = Game(player)
    _success = False
    while not _success:
        guess_left = (game.player.max_guess - game.player.cnt_guess)
        if (guess_left > 0):
            print(f'You have {guess_left} guesses left.')
            _success = game.check_number(input('Guess the number: '))
        else: 
            print('You have 0 guess left. Bye')
            exit()

    print(f'You solved the game in {game.player.cnt_guess} guess!')