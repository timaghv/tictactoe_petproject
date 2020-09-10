XO_mat = [[' ' for i in range(3)] for j in range(0, 9, 3)]  # Initiating empty field
xo_flag = 1  # 1 - X, -1 - O
game_status = 0  # 0 not finished, 1 finished
cell_entry = -1  # 1 - entered , -1 not entered


def cell_display(mtrx):
    print('---------')
    for i in range(0, 3):
        print("| ", end='')
        for j in range(0, 3):
            print(mtrx[i][j], end=' ')
        print("|")
    print('---------')


cell_display(XO_mat)  # displaying empty field
x_ij = []  # list of X positions
o_ij = []  # list of O positions
Xwin = False
Owin = False


def enter_cell(x, y):
    global xo_flag
    global cell_entry
    if x.isalpha() or y.isalpha():
        print('You should enter numbers!')
    elif int(x) > 3 or int(y) > 3:
        print("Coordinates should be from 1 to 3! ")
    elif XO_mat[3 - int(y)][int(x) - 1] == ' ':
        if xo_flag == 1:
            XO_mat[3 - int(y)][int(x) - 1] = 'X'
            cell_entry *= -1
        else:
            XO_mat[3 - int(y)][int(x) - 1] = 'O'
            cell_entry *= -1
        return True
    else:
        print("This cell is occupied! Choose another one!")
    return False


def status_check():
    global x_ij
    global o_ij
    global Xwin
    global Owin
    global game_status
    x_i = list(a[0] for a in x_ij)
    x_j = list(a[1] for a in x_ij)
    x_i_dict = {x: x_i.count(x) for x in x_i}
    x_j_dict = {x: x_j.count(x) for x in x_j}

    o_i = list(a[0] for a in o_ij)
    o_j = list(a[1] for a in o_ij)
    o_i_dict = {o: o_i.count(o) for o in o_i}
    o_j_dict = {o: o_j.count(o) for o in o_j}

    if 3 in x_i_dict.values() or 3 in x_j_dict.values():
        Xwin = True
    if 3 in o_i_dict.values() or 3 in o_j_dict.values():
        Owin = True
    # diag1
    if sum(a[0] == a[1] for a in x_ij) == 3:
        Xwin = True
    if sum(a[0] == a[1] for a in o_ij) == 3:
        Owin = True
    # diag2
    if set(x_ij).intersection(((0, 2), (1, 1), (2, 0))) == {(0, 2), (1, 1), (2, 0)}:
        Xwin = True
    if set(o_ij).intersection(((0, 2), (1, 1), (2, 0))) == {(0, 2), (1, 1), (2, 0)}:
        Owin = True

    if abs(len(x_ij) - len(o_ij)) > 1 or (Xwin and Owin):
        print("Impossible")
        game_status = 1
    # elif len(x_ij) + len(o_ij) < 9 and not Xwin and not Owin:
    #     print("Game not finished")
    #     game_status = 0
    elif len(x_ij) + len(o_ij) == 9 and not Xwin and not Owin:
        print("Draw")
        game_status = 1
    elif Xwin:
        print("X wins")
        game_status = 1
    elif Owin:
        print("O wins")
        game_status = 1


while not game_status:
    while cell_entry == -1:
        x, y = input("Enter the coordinates: ").split(" ")
        enter_cell(x, y)
    else:
        cell_entry *= -1

    cell_display(XO_mat)
    if xo_flag == 1:
        x_ij.append((3-int(y), int(x)-1))
        xo_flag *= -1
    else:
        o_ij.append((3-int(y), int(x)-1))
        xo_flag *= -1
    if len(x_ij) >= 3 or len(o_ij) >= 3:
        status_check()


