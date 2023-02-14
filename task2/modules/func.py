
def Find_Index(my_list, min, max):
    range_list = []
    for i in range(len(my_list)):
        if my_list[i] > min and my_list[i] < max:
            range_list.append(i)
            print()
            print("Индекс элемента в заданном диапозоне: ", '[', i, ']',my_list[i])
    range_list.sort()
    return range_list