from termcolor import colored
import random

# Variables definition
red, black = colored('O', 'red', attrs=['bold']), colored('O', attrs=['bold'])  # u'\u2B24'
balls = [colored(u'\u2B24', 'red'), colored(u'\u2B24')]
player_1, player_2 = 'red', 'black'

row, col = 6, 7
board = [['' for i in range(row)] for i in range(col)]
# board = [[] for i in range(col)]  # each nested list represents a column of the game board


def first_player():
    return random.randint(1, 2)


def draw_board():
    print_header()
    for i in range(row):
        print_line()
        print_row()
    print_line()


player = first_player()

'''
for item in range(col):
    for cell in range(row):
        option = first_player()
        if option == 1:
            board[item][cell] = 'red'
        else:
            board[item][cell] = 'black'
'''


def print_color():
    for col in board:
        temp = []
        for cell in col:
            if cell == 'red':
                print(red + ' ', end='')
            else:
                print(black + ' ', end='')
        print()


print_color()


def print_header():
    for i in range(col):
        if i == 0:
            print(' ' * 2 + str(i+1), end='')
        else:
            print(' ' * 3 + str(i+1), end='')
    print()


# board line
def print_line():
    for i in range(col):
        print('+', end='')
        for j in range(3):
            print('-', end='')
    print('+')


def print_row():
    for c in range(col):
        print('|' + ' ', end='')
        # print columns in reverse mode
        for r in range(row):
            item = board[c][-(1 + r)]  # get reverse items
            print(item)
        item = get_item()
        print(' ' + ' ', end='')  # print the item on the screen
    print('|')


def get_item():
    return 1


def print_title():
    print('\n' + ' ' * 3 + '--- Connect 4 Game ---\n')


print_title()
print()

p = 1
players = []

while p < 3:
    if p == 1:
        s = '1st'
    else:
        s = '2nd'
    players.append(input('- Enter the ' + s + ' Player name: ').capitalize())
    p += 1

tmp_player = first_player() - 1
tmp_player = 0

start_play = players[tmp_player]
ball = str(balls[tmp_player])

print('\n--- ' + colored(start_play.upper(), attrs=['bold']) + ' shall start the game with '
      + ball + ' ---')  # u'\u2B24'


def save_move():
    column = move - 1
    board[column].append(color)
    # reverse = []
    # reverse.append(board[column][::-1])
    return 1


def check_winner():
    return 1


player = start_play
colors = ['red', 'black']
while True:
    color = colors[tmp_player]
    try:
        if color == 'red':
            move = int(input(colored(player.upper(), color, attrs=['bold']) + '\'s move.: '))
            while move < 1 or move > 7:
                print('--- Please enter a number between [1, 7]')
                move = int(input(colored(player.upper(), color, attrs=['bold']) + '\'s move.: '))

        else:
            move = int(input(colored(player.upper(), attrs=['bold']) + '\'s move.: '))
            while move < 1 or move > 7:
                print('--- Please enter a number between [1, 7]')
                move = int(input(colored(player.upper(), attrs=['bold']) + '\'s move.: '))

        save_move()
        # draw_board()
        # check_winner()

        if tmp_player == 0:
            tmp_player = 1
        else:
            tmp_player = 0
        player = players[tmp_player]
    except ValueError:
        print('--- Please enter a number between [1, 7]')