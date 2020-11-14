from termcolor import colored
import random

# Variables definition
red, black = colored('X', 'red', attrs=['bold']), colored('O', attrs=['bold'])  # u'\u2B24'
balls = [colored(u'\u2B24', 'red'), colored(u'\u2B24')]
player_1, player_2 = 'red', 'black'

row, col = 6, 7
# board = [['' for i in range(row)] for i in range(col)]
board = [[] for i in range(col)]  # each nested list represents a column of the game board
tmp_board = board[:]  # clone the main_board


def first_player():
    return random.randint(1, 2)


player = first_player()

'''
for item in range(col):
    for cell in range(row):
        option = first_player()
        if option == 1:
            board[item][cell] = 'red'
        else:
            board[item][cell] = 'black'


def print_color():
    for column_index in board:
        for cell in column_index:
            if cell == 'red':
                print(red + ' ', end='')
            else:
                print(black + ' ', end='')
        print()


# print_color()
'''


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


def draw_board(fill_empty):
    print_header()
    for i in range(row):
        print_line()
        print_row(i)  # is the columns content (think in that in reverse mode)
    print_line()


# Fill each cell on the screen with the respective column content in reverse order
# Math is beautiful
def print_row(cell_position):
    max_index, max_len = 5, 6
    for item in board:
        print('|' + ' ', end='')
        current_len = len(item)
        current_index = current_len - 1
        total_empty_cells = max_index - current_index
        if cell_position >= total_empty_cells:
            print_index = - 1 * (cell_position + 1)  # this is like reversing the order
            real_index = max_len + print_index  # the right index is targeted in reverse order
            color_ball = item[real_index]
            if color_ball == 'red':
                print(red + ' ', end='')  # print the red ball
            else:
                print(black + ' ', end='')
        else:
            print('  ', end='')
    print('|')


def print_title():
    print('\n' + ' ' * 3 + '--- Connect 4 Game ---')


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

print()
draw_board(False)

tmp_player = first_player() - 1

start_play = players[tmp_player]
ball = str(balls[tmp_player])

print('\n--- ' + colored(start_play.upper(), attrs=['bold']) + ' shall start the game with '
      + ball + ' ---\n')  # u'\u2B24'


def save_move():
    column = move - 1
    if len(board[column]) < 6:
        board[column].append(color)
    else:
        print('\n-- ' + colored('WARNING.:', 'blue', attrs=['bold']) +
              ' Invalid move. Please choose new column to play.')
        return True
    return False


def check_winner():
    return 1


def set_move():
    col_num = 0
    try:
        if color == 'red':
            col_num = int(input(colored(player.upper(), color, attrs=['bold']) + '\'s move.: '))
            while col_num < 1 or col_num > 7:
                print('\n-- ' + colored('WARNING.:', 'blue', attrs=['bold']) + ' Please enter a number between [1, 7]')
                col_num = int(input(colored(player.upper(), color, attrs=['bold']) + '\'s move.: '))
        else:
            col_num = int(input(colored(player.upper(), attrs=['bold']) + '\'s move.: '))
            while col_num < 1 or col_num > 7:
                print('\n-- ' + colored('WARNING.:', 'blue', attrs=['bold']) + ' Please enter a number between [1, 7]')
                col_num = int(input(colored(player.upper(), attrs=['bold']) + '\'s move.: '))
    except ValueError:
        print('\n-- ' + colored('WARNING.:', 'blue', attrs=['bold']) + ' Please enter a number between [1, 7]')

    return col_num


def invert_board_columns():
    column_index = move - 1
    column = board[column_index].copy()
    tmp_board.insert(column_index, column[::-1])  # updating -> append the reversed version of a board column
    tmp_board.pop(move)  # { move = column_index + 1 } remove the old version
    return tmp_board


player = start_play
colors = ['red', 'black']
while True:
    color = colors[tmp_player]

    move = set_move()
    column_is_full = save_move()  # move option can failed - list bound error

    while column_is_full:
        move = set_move()
        column_is_full = save_move()

    # printing the current board on the screen
    print()
    draw_board(True)
    print()

    # check if we have a winner
    check_winner()

    if tmp_player == 0:
        tmp_player = 1
    else:
        tmp_player = 0
    player = players[tmp_player]