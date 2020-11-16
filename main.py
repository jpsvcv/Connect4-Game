from termcolor import colored
import random

# Variables definition
red, black = colored('X', 'red', attrs=['bold']), colored('O', attrs=['bold'])  # u'\u2B24'
balls = [colored(u'\u2B24', 'red'), colored(u'\u2B24')]
player_1, player_2 = 'red', 'black'

row, col = 6, 7
# board = [['' for i in range(row)] for i in range(col)]
board = [[] for i in range(col)]  # each nested list represents a column of the game board
# tmp_board = board[:]  # clone the main_board


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
    print_header()


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
    players.append(input('- Enter the ' + s + ' Player name: ').strip().capitalize())
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


# check for horizontal victory as the boar is printed on the screen
def check_horizontal():
    # cell_index, counter = 0, 0
    # for list_item in board:
    #     if len(list_item) > 0:
    #         if list_item[cell_index] == color:
    #             counter += 1
    #             if counter == 4:
    #                 return True
    return False


# check for vertical victory as the boar is printed on the screen
def check_vertical():
    # for list_item in board:
    #     if list_item.count(color) == 4:
    #         return True
    return False


def left_2_right():
    this_index = next_index = next_index = list_index = counter = 0
    for list_item in board:
        if len(list_item) > 0:  # list is not empty
            try:
                if list_item.count(color) >= 0:  # exists at least one matched element
                    this_index = list_item.index(color)  # get the right position
                    try:
                        if list_item[next_index] == color:
                            this_index = next_index
                            counter += 1
                            if counter == 4:
                                return True
                        else:
                            counter = 0
                    except IndexError:
                        counter = 0
                        continue
                    next_index = this_index + 1
            except ValueError:
                counter = 0
                continue
    return False


def positive_slope(column, cell):
    current_column = board.index(column)
    current_cell = column.index(cell)
    try:
        if board[column][cell] == board[current_column + 1][current_cell + 1] \
                == board[current_column + 2][current_cell + 2] \
                == board[current_column + 3][current_cell + 3]:
            return True
    except:
        return False
    return False


def negative_slope(column, cell):
    current_column = board.index(column)
    current_cell = column.index(cell)
    try:
        if board[column][cell] == board[current_column + 1][current_cell - 1] \
                == board[current_column + 2][current_cell - 2] \
                == board[current_column + 3][current_cell - 3]:
            return True
    except:
        return False
    return False


def check_diagonal():
    tmp_board = board
    status = False
    for column in tmp_board:
        if len(column) > 0:  # must have at least one element
            if color in column:  # the current color must be available in that cell
                if board.index(column) < 4:  # analyze only a half of the board. 21 in 42
                    for cell in column:
                        if column.index(cell) < 3:  # 1st half of the column
                            status = positive_slope(column, cell)  #
                            tmp_board[tmp_board.index(column)][column.index(cell)] = ''
                            status = True
                        elif column.index(cell) > 2:  # 2nd half of the column
                            status = negative_slope(column, cell)
    return status


def check_winner():
    progressive_index = 0

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
    draw_board(True)
    print()

    if total_move > 6:
        if check_winner():  # check if we have a WINNER
            print(colored('--- BOARD RESULT.: ', attrs=['bold']) +
                  colored(player.upper() + ' WIN the GAME ', attrs=['bold']))
            break
        else:  # check for a TIE
            count_full = 0
            for item in board:
                if len(item) == 6:
                    count_full += 1
            if count_full == col:  # col is equals to the total of board inner list
                print(colored('--- BOARD RESULT.: ', attrs=['bold']) +
                      colored('TIE', attrs=['bold']))
                break

    if tmp_player == 0:
        tmp_player = 1
    else:
        tmp_player = 0
    player = players[tmp_player]
