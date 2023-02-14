# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)

import os
from modules.func import *

os.system('cs||clear')

my_list = FillRnd()

print("Сенерированный массив: ", my_list)

print()
min = int(input("Введите, пожалуйста, значение минимальной границы: "))
print()
max = int(input("Введите, пожалуйста, значение максимальной границы: "))
print()
enter_func = input("Нажмите Enter, чтобы запустить функцию ... ")
range_list = Find_Index(my_list, min, max)

print()
print("Индексы значений: ", range_list)

print()
exit_programm = input("Нажмите Enter, чтобы завершить программу ... ")
os.system('cs||clear')