import random

show_table = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
winning_combinations = {1: ['X', 'X', 'X']}
moves_list = {1: {}, 2: {}, 3: {}, 4: {}, 5: {}, 6: {}, 7: {}, 8: {}, 9: {}, 10: {}}
winning_list = []
player_choice_list = []
score_list = [0, 0]
match_number = 1
round_number = 1


def print_table(x):
    for i in range(0, len(x), 3):
        print(x[i + 0] + ' | ' + x[i + 1] + ' | ' + x[i + 2])
        if i != 6:
            print("----------")


def check_round():
    n = ""
    while n.isdigit() is False:
        n = input("Enter the number of rounds (1-10) : ")
        if n.isdigit() is False:
            print("Please enter a valid number")
    return int(n)


def round_range(n):
    if 1 <= n <= 10:
        return True
    else:
        return False


def get_round():
    boo = False
    while boo is False:
        num = check_round()
        if round_range(num) is True:
            boo = True
        elif round_range(num) is False:
            print("Value out of range!!!")
    return num


def position(player):
    index = ' '
    acceptable_values = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    while index.isdigit() is False or index not in acceptable_values:
        index = input("Enter the position to input {} (1-9)  : ".format(player))
        if index.isdigit() is False:
            print("Please enter a valid number")
        elif index not in acceptable_values:
            print("Please enter a value within range")
    return int(index) - 1


def choose_player():
    p1 = " "
    while p1 not in ['X', 'O', 'x', 'o']:
        p1 = input("Enter choice of player (X or O) : ")
        if p1 not in ['X', 'O', 'x', 'o']:
            print("Invalid choice!!!")
    p1 = p1.upper()
    if p1 == 'X':
        p2 = 'O'
    elif p1 == 'O':
        p2 = 'X'
    return p1, p2


def insert(pos, player):
    table[pos] = player


def check_position(pos1, table1):
    if pos1 in table1:
        table1.pop(pos1)
        return True
    elif pos1 not in table1:
        print("Move already made")
        return False


def get_position(player):
    position_check = False
    while position_check is False:
        p = position(player)
        position_check = check_position(p, check_list)
    return p


def cpu_position():
    position_check1 = False
    while position_check1 is False:
        p = random.randint(0, 8)
        position_check1 = check_position(p, check_list)
    return p


def check_win(t, p1, p2):
    stat = winner = 'tie'
    sublist = [[t[0], t[1], t[2]], [t[3], t[4], t[5]], [t[6], t[7], t[8]], [t[0], t[3], t[6]], [t[1], t[4], t[7]],
               [t[2], t[5], t[8]], [t[0], t[4], t[8]], [t[2], t[4], t[6]]]
    for item in sublist:
        if item == [p1, p1, p1]:
            winner = p1
            stat = 'won'
        elif item == [p2, p2, p2]:
            winner = p2
            stat = 'won'
    return stat, winner


def check_history(h):
    if winning_list[h - 1] == 0:
        print("Round Winner : Player")
    elif winning_list[h - 1] == 1:
        print("Round Winner : CPU")
    elif winning_list[h - 1] == -1:
        print("Round Winner : Tied")
    print("Player Choice : {}".format(player_choice_list[h - 1]))
    if player_choice_list[h - 1] == 'X':
        print("CPU Choice : O")
    elif player_choice_list[h - 1] == 'O':
        print("CPU Choice : X")
    print("Move History")
    print("------------------------")
    for j in moves_list[h]:
        print_table(moves_list[h][j])
        print("------------------------")


number_of_rounds = get_round()
for k in range(number_of_rounds):
    table = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    check_list = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 0: 0}
    player = ['', '']
    pos = [0, 0]
    status = winning_player = ''
    print("Round {}\n------------------------".format(k + 1))
    player[0], player[1] = choose_player()
    print("Player is {} and CPU is {}".format(player[0], player[1]))
    player_choice_list.append(player[0])
    print_table(show_table)
    index = 0
    while status != 'won' and index != 9:
        if index % 2 == 0:
            i = 0
            pos[i] = get_position(player[i])
        else:
            i = 1
            pos[i] = cpu_position()
        insert(pos[i], player[i])
        moves_list[round_number][index + 1] = table.copy()
        if i == 0:
            print("Player Move")
        elif i == 1:
            print("CPU Move")
        print_table(table)
        status, winning_player = check_win(table, player[0], player[1])
        index += 1
    if status == 'won':
        if winning_player == player[0]:
            print("Winner of round {} is Player".format(round_number))
            winning_list.append(0)
            score_list[0] += 1
        elif winning_player == player[1]:
            print("Winner of round {} is CPU".format(round_number))
            winning_list.append(1)
            score_list[1] += 1
    elif status == 'tie':
        print("The Match is Tied")
        winning_list.append(-1)
    round_number += 1
if score_list[0] > score_list[1]:
    print("Winner of the series is Player")
elif score_list[0] < score_list[1]:
    print("Winner of the series is CPU")
else:
    print("The Series is Tied")
print("Player Score : {}\nCPU Score    : {}".format(score_list[0], score_list[1]))
history = input("Enter the round whose information is required (0 to exit) : ")
while history != '0':
    if history.isdigit() is False:
        print("Invalid Value!!!")
    else:
        history = int(history)
        if history > number_of_rounds:
            print("Value cannot be greater than total number of rounds!!!")
        else:
            check_history(int(history))
    history = input("Enter the round whose information is required (0 to exit) : ")
