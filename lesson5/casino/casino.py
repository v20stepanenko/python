from random import randint

money = 100

def get_result(num, rate):
    global money
    r = randint(1, 9)
    if num == r:
        print('Верно! Вы угадали.')
        money += rate * 3
    else:
        print('К сожалению, на рулетке выпало другое число!')
        money -= rate
    print('У вас {0} денег'.format(money))

def main():
    print('Игра рулетка, у вас {0} денег'.format(money))
    while True:
        if money <= 0:
            break
        num = int(input('Введите число от 1 - 9: '))
        rate = int(input('Введите ставку: '))
        if rate > money:
            continue
        get_result(num, rate)

main()