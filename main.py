import random
# first_list = [[1, 2, 3], [4, 5, 6]]
# tmp = first_list.copy()
# print(id(first_list) == id(tmp))


# first_list = [[1, 2, 3], [4, 5, 6]]
# tmp = first_list.copy()
# print(id(first_list[0]) == id(tmp[0]))
#
# print(all([2 > 2, True, 5 == 5]))
#
# print(any([2 > 2, True, 5 < 5]))


# first_list = [2, 4, 7, 11 , '0', -2, 8]
# max(first_list)
# number = 0
# while number <= 10:
#     number = number + 2
#     if number == 5:
#         break
#     print(number, end=',')

# number = 0
#
# while number < 10:
#     number = number + 1 # До continue !!!!
#     if number == 5:
#         continue
#     print(number)

# number = int(input("input positive number "))
# i = 2
# while i < number:
#     if number % i == 0:
# 				# Якщо число ділиться без залишку на інше число, то це число не є простим
#         print("It is not a prime number")
#         break
#     i = i + 1
# else: # виконається тільки якщо break в циклі не буде викликаний.
#     print("It is a prime number")

first_list = [1, 2, 3, 4, 5, 6]
# i = 1
# while i < len(first_list):
#     j = 0
#     lst = first_list[i]
#     while j < len(lst):
#         print(lst[j])
#         j += 1
#     i += 1

# for a, et in enumerate(first_list):
#     print(a, "->", et)

# qwe = range(1, 20, 3)
# for i in qwe:
#     print(i)

# list(range(3, 10))
# print(list)

# import random
# my_list = []
# # Не найоптимальніший варіант рішення
# for i in range(random.randint(6, 15)):
#     my_list.append(random.randint(1, 1000))
# print(my_list)
#
# summa = 0
# for element in my_list:
#     summa += element
# print(summa)

# my_lists = [random.randint(1, 100) for i in range(random.randint(6, 15))]
# print(my_lists)

def move_0_to_the_end(my_list):
    without_0 = [i for i in my_list if i !=0]
    with_0 = [0] * my_list.count(0)
    return without_0 + with_0

my_list = [1, 0, 13, 0, 0, 0, 5]
result = move_0_to_the_end(my_list)
print(result)
