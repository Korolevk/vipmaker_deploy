# -*- coding:utf-8 -*-
__author__ = 'Kirill Korolev'
from decimal import Decimal


def end(number):
    word = ''
    answer = (Decimal(number) / Decimal(10)) / Decimal(10)
    answer = str(answer).split('.')
    if (number % 10 == 0) or (number % 10 == 5) or (number % 10 == 6)or (number % 10 == 7)or (number % 10 == 8)or (number % 10 == 9):
        word = 'записей'
    elif answer[1] == '11' or answer[1] == '12' or answer[1] == '13' or answer[1] == '14':
        word = 'записей'
    elif number % 10 == 1:
        word = 'запись'
    elif (number % 10 == 2)or (number % 10 == 3)or (number % 10 == 4):
        word = 'записи'
    return word