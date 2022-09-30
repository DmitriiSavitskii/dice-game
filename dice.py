import random
import time



def play_kosty():
    new_game = True
    while new_game:
        player1 = input('Введите имя первого игрока - ')
        player2 = input('Введите имя второго игрока - ')
        pl1 = random.randint(1, 6)
        pl2 = random.randint(1, 6)
        print(f'Игрок {player1} бросает кости')
        time.sleep(1)
        print(player1, 'получает', pl1)
        time.sleep(1)
        print(f'Игрок {player2} бросает кости')
        time.sleep(1)
        print(player2, 'получает', pl2)
        time.sleep(1)
        if pl1 == pl2:
            print('Ничья')
        elif pl1 > pl2:
            print(f'Побеждает {player1}')
        elif pl1 < pl2:
            print(f'Побеждает {player2}')
        while True:
            res_game = input('Еще разок?  Введите да/нет ')
            if res_game.lower() != 'нет' and res_game.lower() != 'да':
                print("Не верно, попробуйте снова.")
            elif res_game.lower() == 'нет':
                print('До скорой встречи!')
                new_game = False
                break
            else:
                break
    
play_kosty()