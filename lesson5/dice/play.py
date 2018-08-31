from random import randint

money = 100
player1_money, player2_money = money, money

def check_int(numb):
    if numb.isdigit():
        numb_to_int = int(numb)
        if str(numb_to_int) == numb:
            return numb_to_int
    

def get_rate():
    player1_rate, player2_rate = 0, 0
    while True:
        while True:
            player1_rate = input('Введите вашу ставку p1: ')
            player1_rate = check_int(player1_rate)
            if player1_rate and player1_rate <= player1_money and player1_rate <= player2_money and player1_rate >= player2_rate:
                break
            else:
                print('Ставка не принята')
        while True:
            player2_rate = input('Введите вашу ставку p2: ')
            player2_rate = check_int(player2_rate)
            if player2_rate and player2_rate <= player1_money and player2_rate <= player1_money and player2_rate >= player1_rate:            
                break
            else:
                print('Ставка не принята')
        if player1_rate == player2_rate:
            print('Играет ставка ', player1_rate)
            return player1_rate

def throw_dice():
    result = 0
    for i in range(0,3):
        input('для того, чтобы бросить кубики, нажмите Энтер')
        cube1 = randint(1, 6)
        cube2 = randint(1, 6)
        result = result + cube1 + cube2
        print('Кубики покатились и... Выпало {0} и {1}'.format(cube1, cube2))
    return result

def check_step(rate, *, p1, p2):
    global player1_money
    global player2_money
    print('Результат первого игрока: {0}. Результат второго игрока: {1}'.format(p1, p2))
    if p1 > p2:
        player1_money += rate
        player2_money -= rate
    elif p1 < p2:
        player2_money += rate
        player1_money -= rate

    print("Остаток первого игрока: {0}, второго {1}".format(player1_money, player2_money))

def main():
    global player1_money
    global player2_money
    while True:
        
        rate = get_rate()
        print('Бросок 1-го игрока')
        result1 = throw_dice()
        print('Бросок 2-го игрока')
        result2 = throw_dice()
        check_step(rate, p1 = result1, p2 = result2)

        if not player1_money:
            print('Игра окончена, выиграл 2-й игрок ')
            break
        elif not player2_money:
            print('Игра окончена, выиграл 1-й игрок')
            break

main()