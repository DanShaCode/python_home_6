import os
from functions.a_progression import A_Progression

os.system('cs||clear')
print()
print("Данная программа создает арифметическую прогрессию.")
print()
print("Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.") 
print("Каждое число вводится с новой строки.")
print()
enter_input = input("Нажмите Enter")

os.system('cs||clear')
a1 = int(input("Введите, пожалуйста, первый член прогрессии: "))
print()
d = int(input("Введите, пожалуйста, разность: "))
print()
n = int(input("Введите, пожалуйста, количество элементов: "))
print()
enter_input = input("Нажмите Enter")
os.system('cs||clear')

arithmetic_progressive = []

A_Progression(a1, d, n, arithmetic_progressive)

print()
print("Созданная артифметическая прогрессия: ", arithmetic_progressive)
