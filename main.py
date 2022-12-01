coord = {"00": "-", "01": "-", "02": "-",
         "10": "-", "11": "-", "12": "-",
         "20": "-", "21": "-", "22": "-"}


def print_land():
    print(f"""
      0 1 2
    0 {coord["00"]} {coord["01"]} {coord["02"]}
    1 {coord["10"]} {coord["11"]} {coord["12"]}
    2 {coord["20"]} {coord["21"]} {coord["22"]}
    """)


def game(gamer):
    while True:
        x = input(f'Введите координаты {gamer}: ')
        if len(x) != 2 or x not in coord:
            print("Таких координат нет!")
            continue
        if coord[x] == 'X' or coord[x] == '0':
            print('Эти координаты уже заняты!')
            continue
        coord[x] = gamer
        print_land()
        check_win(gamer)
        break


def check_win(gamer):
    if coord['00'] + coord['01'] + coord['02'] == gamer * 3 \
            or coord['10'] + coord['11'] + coord['12'] == gamer * 3 \
            or coord['20'] + coord['21'] + coord['22'] == gamer * 3 \
        \
            or coord['00'] + coord['10'] + coord['20'] == gamer * 3 \
            or coord['01'] + coord['11'] + coord['21'] == gamer * 3 \
            or coord['02'] + coord['12'] + coord['22'] == gamer * 3 \
        \
            or coord['02'] + coord['11'] + coord['20'] == gamer * 3 \
            or coord['00'] + coord['11'] + coord['22'] == gamer * 3:
        print(f'Победил {gamer}')
        exit(0)

print_land()
print('Игра началась!')

while True:
    game('x')
    if '-' not in coord.values():
        print('Ничья!')
        break
    game('o')