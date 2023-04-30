import random

def greeting():
    print(' Игра \n Камень, ножницы, бумага')
    print(' ---------------- ')
    print(' Форма ввода: \n 1 - камень \n 2 - ножницы \n 3 - бумага')


def check():

    score1 = 0
    score2 = 0
    board = f'{score1} : {score2}'

    Player = 1 or 2 or 3

    print(' ')
    print(board)
    print(' ')
    Player = int(input('Ваш ход:'))

    print (' Ходит ИИ! ')

    PC = random.randint(1, 3)

    if Player == 1 and PC == 1:
        print('Ты поставил камень! ИИ поставил камень! Ничья! ')
    elif Player == 1 and PC == 2:
        print(' Ты поставил камень! ИИ поставил ножницы! Ты победил! ')
        board = f'{score1 + 1} : {score2}'
    elif Player == 1 and PC == 3:
        print('Ты поставил камень! ИИ поставил бумагу! Ты проиграл! ')
        board = f'{score1} : {score2 + 1}'
    elif Player == 2 and PC == 1:
        print('Ты поставил ножницы! ИИ поставил камень! Ты проиграл! ')
        board = f'{score1} : {score2 + 1}'
    elif Player == 2 and PC == 2:
        print('Ты поставил ножницы! ИИ поставил ножницы! Ничья! ')
    elif Player == 2 and PC == 3:
        print(' Ты поставил ножницы! ИИ поставил бумагу! Ты победил! ')
        board = f'{score1 + 1} : {score2}'
    elif Player == 3 and PC == 1:
        print(' Ты поставил бумагу! ИИ поставил камень! Ты победил! ')
        board = f'{score1 + 1} : {score2}'
    elif Player == 3 and PC == 2:
        print('Ты поставил бумагу! ИИ поставил ножницы! Ты проиграл! ')
        board = f'{score1} : {score2 + 1}'
    elif Player == 3 and PC == 3:
        print(' Ты поставил бумагу! ИИ поставил бумагу! Ничья! ')
    else:
        print(' Введена не верная команда!')
        check()

    print(board)

    again()

def again():
    print(" ")
    print('Сыграть еще раз?')
    print('1: Да, 2: Нет')
    choice = int(input(' Выбор: '))
    if choice == 1:
        return check()
    elif choice == 2:
        print(' Хорошего дня! ')
        exit()
    else:
        print('Команда не распознана')
        again()

def start():
    greeting()
    check()
    again()

start()
