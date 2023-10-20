import random
import sys
import os
import json

class Player():
    def __init__(self):
        _path = "/Users/stefvannieuwenhove/Desktop/learning_python/number_guessing_game/players/"
        _saved_players = [file for file in os.listdir(_path)]

        _txt = ''
        if (len(_saved_players) > 0):
            _txt = 'Choose a player below, or '
        _txt += 'create a new player:'

        _players = ''
        for i, p in enumerate(_saved_players):
            _players += f'{i+1} {p}\n'

        _option = input(f'{_txt} \n {_players}\n[C]: Create new player\n\n')

        try:
            _option = int(_option)
            print('Loading...', _saved_players[_option-1])
            _name = _saved_players[_option-1]
            self.assign_players_values(f'{_path}{_name}')
        except Exception as E:
            print(E)
            _name = input('Create new player here\n-----------------\nName: ')
            with open(_path+_name, 'a') as f:
                f.writelines('''{"name": "'''+_name+'''",
                                "max_guess": 0,
                                "level": 0,
                                "wins": 0
                                }
                            ''').replace(' ', '')
            self.assign_players_values(f'{_path}{_name}')
            pass



    def assign_players_values(self, path):
        f = open(path, 'r')
        _player = json.load(f)
        self.name = _player['name']
        self.max_guess = _player['max_guess']
        self.cnt_guess = 0
        self.level = _player['level']
        self.wins = _player['wins']
        print(f"Player {_player['name']} loaded")

        



class Game() :
    def __init__(self, player):
        #Assign variables   
        self.player = player
        self.difficulty = 1
        self.nbr = self.get_random_nbr(self)
        self.levels = {'0': 20, '1': 18, '2': 15}
        print('Game is set! Good Luck\n--------------------')

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
            print('Bigger')
            self.player.cnt_guess += 1
            return False
        #check if number is >
        if usernbr > self.nbr:
            print('Smaller')
            self.player.cnt_guess += 1
            return False

        return False


if __name__ == "__main__":
    player = Player() 

    game = Game(player)
    _success = False
    while not _success:
        guess_left = (game.player.max_guess - game.player.cnt_guess)
        if (guess_left > 0):
            _text = ''
            if ((guess_left % 5) == 0):
                print(f'You have {guess_left} guesses left.\n')
            _success = game.check_number(input(f'{_text}\n'))
        else: 
            print('You have 0 guess left. Bye')
            exit()

    print(f'You solved the game in {game.player.cnt_guess} guess!')