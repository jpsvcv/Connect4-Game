from termcolor import colored
import random

# Variables definition
red, blue = colored('X', 'red', attrs=['bold']), colored('O', 'blue', attrs=['bold'])  # u'\u2B24'
balls = [colored(u'\u2B24', 'red'), colored(u'\u2B24', 'blue')]
player_1, player_2 = 'red', 'blue'
row, col = 6, 7


def generate_board():
    return [[] for i in range(col)]  # each nested list represents a column of the game board


board = generate_board().copy()


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
            board[item][cell] = 'blue'


def print_color():
    for column_index in board:
        for cell in column_index:
            if cell == 'red':
                print(red + ' ', end='')
            else:
                print(blue + ' ', end='')
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


def draw_board():
    print_header()
    for i in range(row):
        print_line()
        print_row(i)  # is the columns content (think in that in reverse mode)
    print_line()
    print_header()


# Fill each cell on the screen with the respective column content in reverse order
# Math is beautiful
def print_row(cell_position):
    max_index, max_len = 5, 6
    for column in board:
        print('|' + ' ', end='')
        current_len = len(column)
        current_index = current_len - 1
        total_empty_cells = max_index - current_index
        if cell_position >= total_empty_cells:
            print_index = - 1 * (cell_position + 1)  # this is like reversing the order
            real_index = max_len + print_index  # the right index is targeted in reverse order
            color_ball = column[real_index]
            if color_ball == 'red':
                print(red + ' ', end='')  # print the red ball
            else:
                print(blue + ' ', end='')
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
    players.append(input('- Enter the ' + s + ' Player name: ').strip().capitalize())
    p += 1

print()
draw_board()

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


# check for horizontal victory
def check_horizontal():
    for column in board:
        for cell in column:
            current_column = board.index(column)
            current_cell = column.index(cell)
            try:
                if column[current_cell] == board[current_column + 1][current_cell] \
                        == board[current_column + 2][current_cell] \
                        == board[current_column + 3][current_cell]:
                    address = [column[current_cell], board[current_column + 1][current_cell],
                               board[current_column + 2][current_cell], board[current_column + 3][current_cell]]
                    draw_winner_board(address, 'horizontal')
                    return True
            except IndexError:
                continue
    return False


# check for vertical victory
def check_vertical():
    for column in board:
        for cell in column:
            current_cell = column.index(cell)
            try:
                if column[current_cell] == column[current_cell + 1] == column[current_cell + 2] \
                        == column[current_cell + 3]:
                    address = [column[current_cell], column[current_cell + 1], column[current_cell + 2],
                               column[current_cell + 3]]
                    draw_winner_board(address, 'vertical')
                    return True
            except IndexError:
                continue
    return False


# case - positive_slope or negative_slope
def analyse_slope(case, tmp_board, column, cell):
    current_column = tmp_board.index(column)
    current_cell = column.index(cell)
    status = False
    try:
        if case == 'positive_slope':
            if tmp_board[current_column][current_cell] == tmp_board[current_column + 1][current_cell + 1] \
                    == tmp_board[current_column + 2][current_cell + 2] \
                    == tmp_board[current_column + 3][current_cell + 3]:
                address = [tmp_board[current_column][current_cell], tmp_board[current_column + 1][current_cell + 1],
                           tmp_board[current_column + 2][current_cell + 2],
                           tmp_board[current_column + 3][current_cell + 3]]
                status = True
        else:  # negative_slope
            if tmp_board[current_column][current_cell] == tmp_board[current_column + 1][current_cell - 1] \
                    == tmp_board[current_column + 2][current_cell - 2] \
                    == tmp_board[current_column + 3][current_cell - 3]:
                address = [tmp_board[current_column][current_cell], tmp_board[current_column + 1][current_cell - 1],
                           tmp_board[current_column + 2][current_cell - 2],
                           tmp_board[current_column + 3][current_cell - 3]]
                status = True
        if status:
            draw_winner_board(address, 'slope')
            return status
    except IndexError:
        return False
    return False


# print the winner move with different color on the screen
# case - can be slope (for positive or negative), vertical or horizontal
def draw_winner_board(cells, case):
    # To-do
    # ... implemented on the next version

    return False


# tmp_board = board.copy() or tmp_board = board[::] are not working for me
# so, I'm implementing my own, ... that's working very well
def clone_board():
    tmp = []
    for i in board:
        tmp.append(i.copy())
    return tmp


# to check all possible combination on diagonal, you need analyse only a half (21 cells) of the board (2 cells)
def check_diagonal():
    tmp_board = clone_board()
    status = False
    for column in tmp_board:
        if len(column) > 0:  # must have at least one element
            if color in column:  # the current color must be available in that cell
                if board.index(column) < 4:  # analyze only a half of the board. 21 in 42
                    for cell in column:
                        if column.index(cell) < 3:  # 1st half of the column
                            status = analyse_slope('positive_slope', tmp_board, column, cell)  #
                        elif column.index(cell) > 2:  # 2nd half of the column
                            status = analyse_slope('negative_slope', tmp_board, column, cell)
                        if status:
                            return True
                        tmp_board[tmp_board.index(column)][column.index(cell)] = ''
    return False


def check_winner():

    # check for vertical victory
    if check_vertical():  # difficulty level: very easy
        return True

    # check for horizontal victory
    if check_horizontal():  # difficulty level: easy
        return True

    # check for diagonal victory
    if check_diagonal():  # difficulty level: I'm going to make it to be as medium-easy as possible
        return True

    return False


def set_move():
    col_num = 0
    while col_num < 1 or col_num > 7:
        try:
            col_num = int(input(colored(player.upper(), color, attrs=['bold']) + '\'s move.: '))
            while col_num < 1 or col_num > 7:
                print('\n-- ' + colored('WARNING.:', 'magenta', attrs=['bold']) +
                      ' Please enter a number between [1, 7]')
                col_num = int(input(colored(player.upper(), color, attrs=['bold']) + '\'s move.: '))
        except ValueError:
            print('\n-- ' + colored('WARNING.:', 'magenta', attrs=['bold']) + ' Please enter a number between [1, 7]')
    return col_num


player = start_play
colors = ['red', 'blue']
total_move = 0
while True:
    color = colors[tmp_player]

    move = set_move()

    column_is_full = save_move()  # move option can failed - list bound error

    while column_is_full:
        move = set_move()
        column_is_full = save_move()

    total_move += 1

    # printing the current board on the screen
    print()
    draw_board()
    print()

    if total_move > 6:
        if check_winner():  # check if we have a WINNER
            print(colored('--- BOARD RESULT.: ', 'green', attrs=['bold']) +
                  colored(player.upper() + ' WON the GAME ', color, attrs=['bold']))
            break
        else:  # check for a TIE
            count_full = 0
            for item in board:
                if len(item) == 6:
                    count_full += 1
            if count_full == col:  # col is equals to the total of board inner list
                print(colored('--- BOARD RESULT.: ', 'green', attrs=['bold']) +
                      colored('TIE', attrs=['bold']))
                break

    if tmp_player == 0:
        tmp_player = 1
    else:
        tmp_player = 0
    player = players[tmp_player]