# Задание 1

txt = input("Введите текст через пробел:\n")
print(f"Исходный текст: {txt}")
find_txt = "абв"
lst = [i for i in txt.split() if find_txt not in i]
print(f'Результат: {" ".join(lst)}')

# Задание 2

from random import randint

def input_dat(name):
    x = int(input(f"{name}, введите количество конфет, которое возьмете от 1 до 28: "))
    while x < 1 or x > 28:
        x = int(input(f"{name}, введите корректное количество конфет: "))
    return x


def p_print(name, k, counter, value):
    print(f"Ходил {name}, он взял {k}, теперь у него {counter}. Осталось на столе {value} конфет.")

player1 = input("Введите имя первого игрока: ")
player2 = input("Введите имя второго игрока: ")
value = int(input("Введите количество конфет на столе: "))
flag = randint(0,2)
if flag:
    print(f"Первым делает ход {player1}")
else:
    print(f"Первым делает ход {player2}")

counter1 = 0
counter2 = 0

while value > 28:
    if flag:
        k = input_dat(player1)
        counter1 += k
        value -= k
        flag = False
        p_print(player1, k, counter1, value)
    else:
        k = input_dat(player2)
        counter2 += k
        value -= k
        flag = True
        p_print(player2, k, counter2, value)

if flag:
    print(f"Выиграл игрок {player1}")
else:
    print(f"Выиграл игрок {player2}")

# Задание 2а

    from random import randint


    def input_dat(name):
        x = int(input(f"{name}, введите количество конфет, которое возьмете от 1 до 28: "))
        while x < 1 or x > 28:
            x = int(input(f"{name}, введите корректное количество конфет: "))
        return x


    def p_print(name, k, counter, value):
        print(f"Ходил {name}, он взял {k}, теперь у него {counter}. Осталось на столе {value} конфет.")


    player1 = input("Введите имя первого игрока: ")
    player2 = "Bot"
    value = int(input("Введите количество конфет на столе: "))
    flag = randint(0, 2)  # флаг очередности
    if flag:
        print(f"Первым делает ход {player1}")
    else:
        print(f"Первым делает ход {player2}")

    counter1 = 0
    counter2 = 0

    while value > 28:
        if flag:
            k = input_dat(player1)
            counter1 += k
            value -= k
            flag = False
            p_print(player1, k, counter1, value)
        else:
            k = randint(1, 29)
            counter2 += k
            value -= k
            flag = True
            p_print(player2, k, counter2, value)

    if flag:
        print(f"Выиграл игрок {player1}")
    else:
        print(f"Выиграл игрок {player2}")

# Задание 2б

from random import randint

def input_dat(name):
    x = int(input(f"{name}, введите количество конфет, которое возьмете от 1 до 28: "))
    while x < 1 or x > 28:
        x = int(input(f"{name}, введите корректное количество конфет: "))
    return x


def p_print(name, k, counter, value):
    print(f"Ходил {name}, он взял {k}, теперь у него {counter}. Осталось на столе {value} конфет.")


def bot_calc(value):
    k = randint(1,29)
    while value-k <= 28 and value > 29:
        k = randint(1,29)
    return k

player1 = input("Введите имя первого игрока: ")
player2 = "Bot"
value = int(input("Введите количество конфет на столе: "))
flag = randint(0,2) # флаг очередности
if flag:
    print(f"Первым делает ход {player1}")
else:
    print(f"Первым делает ход {player2}")

counter1 = 0
counter2 = 0

while value > 28:
    if flag:
        k = input_dat(player1)
        counter1 += k
        value -= k
        flag = False
        p_print(player1, k, counter1, value)
    else:
        k = bot_calc(value)
        counter2 += k
        value -= k
        flag = True
        p_print(player2, k, counter2, value)

if flag:
    print(f"Выиграл игрок {player1}")
else:
    print(f"Выиграл игрок {player2}")


# Задание 3

board = range(1,10)

def draw_board(board):
    print "-------------"
    for i in range(3):
        print "|", board[0+i*3], "|", board[1+i*3], "|", board[2+i*3], "|"
        print "-------------"

def take_input(player_token):
    valid = False
    while not valid:
        player_answer = raw_input("Куда поставить " + player_token+"? ")
        try:
            player_answer = int(player_answer)
        except:
            print "Некорректный ввод. Необходимо указать число от 1 до 9"
            continue
        if player_answer >= 1 and player_answer <= 9:
            if (str(board[player_answer-1]) not in "XO"):
                board[player_answer-1] = player_token
                valid = True
            else:
                print "Эта клетка уже занята"
        else:
            print "Некорректный ввод. Введите число от 1 до 9, чтобы сделать ход"


def check_win(board):
    win_coord = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
    for each in win_coord:
        if board[each[0]] == board[each[1]] == board[each[2]]:
            return board[each[0]]
    return False

def main(board):
    counter = 0
    win = False
    while not win:
        draw_board(board)
        if counter % 2 == 0:
            take_input("X")
        else:
            take_input("O")
        counter += 1
        if counter > 4:
            tmp = check_win(board)
            if tmp:
                print tmp, "Победа!"
                win = True
                break
        if counter == 9:
            print "Ничья!"
            break
    draw_board(board)

