# map
# 1
# numbers = [-2, -1, 0, 1, 2]
# # abs()
# abs_values = list(map(abs, numbers))
# print(abs_values)


# 2
# words = ['Welcome', 'to', 'Python','14']
# len_words = list(map(len, words))
# print(len_words)


# 3 
# first_it = [1, 2, 3]
# second_it = [4, 5, 6]
# third_it = [1, 3, 1]
# # pow(a, b, c) -> a ** b % c
# new_list = list(map(pow,first_it, second_it, third_it))
# print(new_list)

# 4
# def starts_with_A(word):
#     return word[0] == 'A'

# fruits = ['Apple', 'Banana', 'Pear', 'Apricot', 'Orange']
# A_fruits = list(map(fruits))     
# print(A_fruits.count(True))

# fruits = ['Apple', 'Banana', 'Pear', 'Apricot', 'Orange']
# A_fruits = list(filter(starts_with_A, fruits))     
# # print(A_fruits.count(True))
# print(A_fruits)

# 4,2
# fruits = ['Apple', 'Banana', 'Pear', 'Apricot', 'Orange']
# new_fruits = list(filter(lambda x: not x.startswith('A'),fruits))
# print(new_fruits)

# def not_starts_with_A(x):
#     return not x.startswith('A')


# strings = ['john', 'emily', 'atai', 'ulan', 'jannat']
# strings = [(lambda x: f'${x}!')(name) for name in strings]
# print(strings)


# filter
# 5
# students = [
#     ('Adilet', 89),
#     ('Gulya', 78),
#     ('Beks', 50),
#     ('Nurs', 49),
#     ('Aibek', 69)
# ] 

# # pass_students = list(filter(lambda x: x[-1] >= 61, students))
# pass_students = [name[0] for name in students if name[-1] >=61]
# print(pass_students)


# reduce()
# from functools import reduce

# def add(x, y):
#     return x + y

# numbers = [6, 7, 1, 90, 33, 45]
# print(reduce(add, numbers))   


# students = ['Atai', 'Jannat','Ulan']
# groups = ['Python14','JS13', 'Python Ev. 13']
# room = [9, 11, 5
# ]
# result = list(zip(students, groups, room))
# print(result)



# code = 'print("Hello World")'
# eval(code)

# code = 'for i in range(100):\n\tprint(i)'
# exec(code)