import random

def Find_Index(my_list, minimum, maximum):
    range_list = []
    for i in range(len(my_list)):
        if my_list[i] >= minimum and my_list[i] <= maximum:
            range_list.append(i)
            print()
            print("Индекс элемента в заданном диапозоне: ", '[', i, ']', my_list[i])
    range_list.sort()
    return range_list

def FillRnd():
    my_list = []
    for i in range(1,10):
        my_list.append(random.randint(1,10))
    print()
    return my_list