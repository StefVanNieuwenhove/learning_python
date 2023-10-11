import random
import sys

if len(sys.argv) <3: 
    print(f'Required lminimum and max values \nCommand: python {sys.argv[0]} 1 1000')
    exit()


try: 
    _min = int(sys.argv[1])
    _max = int(sys.argv[2])
except Exception as E:
    print('Args must be numbers')
    print(f'Command: python {sys.argv[0]} 1 1000')
    exit()



nbr = random.randint(int(_min), int(_max))

def check_number(usernbr):
    # Check if number is INTEGER
    try:
        usernbr = int(usernbr)
    except Exception as E:
        print('Guess must be number, not a string\n')
        return False

    # check if number is the same
    if usernbr == nbr:
        print("Congrats you found the number")
        return True

    #check if number is <
    if usernbr < nbr:
        print('The number to guess is Bigger')
        return False
     #check if number is >
    if usernbr > nbr:
        print('The number to guess is Smaller')
        return False

    return False

user_input = False

while (user_input == False):
    user_input = check_number(input('Guess the number?\n'))
    


