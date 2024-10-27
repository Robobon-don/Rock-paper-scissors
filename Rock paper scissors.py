import random

gg = ["камень", "ножницы", "бумага"] #0,1,2
player = input('Вы выбрали: ')
if player in gg:
    robot = random.sample(gg, 1)
    if player == robot[0]:
        print(f'Компьютер выбрал: {robot[0]}')
        print('Ничья!')
    elif player in 'камень': #0,1
        if robot[0] in "ножницы":
            print(f'Компьютер выбрал: {robot[0]}')
            print('Ты выйграл!')
        elif robot[0] in "бумага":
            print(f'Компьютер выбрал: {robot[0]}')
            print('Компьютер выиграл!')
    elif player in "ножницы": #1,0
        if robot[0] in 'камень':
            print(f'Компьютер выбрал: {robot[0]}')
            print('Компьютер выиграл!')
        elif robot[0] in "бумага":
            print(f'Компьютер выбрал:{robot[0]}')
            print('Ты выйграл!')
    elif player in "бумага": #2,0
        if robot[0] in "ножницы":
            print(f'Компьютер выбрал: {robot[0]}')
            print('Компьютер выиграл!')
        elif robot[0] in "камень":
            print(f'Компьютер выбрал: {robot[0]}')
            print('Ты выйграл!')
else:
    print('Играй по правилам!')
