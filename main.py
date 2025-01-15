import random


def move_0_to_the_end(my_list):
    without_0 = [i for i in my_list if i !=0]
    with_0 = [0] * my_list.count(0)
    return without_0 + with_0

my_list = [1, 0, 13, 0, 0, 0, 5]
result = move_0_to_the_end(my_list)
print(result)
