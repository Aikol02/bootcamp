# 1 
# def get_poduct_cost(item, qty, price_per_one):
#     # item, qty, price_per_one
#     result = qty * price_per_one
#     print(f'{item} - {result} dollars')
    # return None

# get_poduct_cost(price_per_one=3, item='Banana', qty=5)
# get_poduct_cost('Banana', qty=5, price_per_one=3)
# print('hello', 'world', sep='\n')

# def print(*arqs, **kwarqs):

# arqs, kwarqs

# best_friends = []

# def add_to_best_friends(*arqs, **kwarqs):
#     print(arqs)
#     print(kwarqs.values())
#     print(kwarqs['name'])
#     for name in arqs:
#      best_friends.append(name)
#      print(f'New friend {name} added to best friends')

# add_to_best_friends('Aidai', 'Bektur', 'Jannat', bff='Atai', bff2='Otoi', bff3='kair', bff4='Timur', name='Aliya') 
# # add_to_best_friends('Atai', 'Ulan')
# # add_to_best_friends('Janna')
# # add_to_best_friends()
# print(best_friends)

# a, b, *c = 1, 2, 3, 4, 5
# print(a, b, c)






# def get_sum(a, b):
#     # print(a + b)
#     return f'Result is: {a + b}'


# result1 = get_sum(3, 7)  
# result2 = get_sum(10, 9)
# print(result1)
# print(result2)




# def shpargalka(par1, par2, *arqs, **kwarqs):
#     if-else, for, while, def, print(), input()
#     try-except
#     return 'hello'
#     print()

# shpargalka(arq1, arq2, arq3, kwarqs)






# def get_type(x, z):
#     a = x / 2
#     b = z +10
#     print(x + z)
    
# num1 = 100
# num2 = 12
# print(get_type)





# def is_palindrome(string):
#   if string.lower().strip() == string[: : - 1].lower().strip():
#     return True
#   else:
#     return False
# print(is_palindrome('довод'))




# def max_num(a, b):
#     return max(a,b)
# print(max_num(10, 12))


# list_ = [1, 2, 3, 4, 5, 6]
# def multiply_list(list_):
#     result = 1
#     for i in list_:
#         result *= i
#     return result
# print(multiply_list([1, 2, 3, 4, 5, 6]))



# def sum_digits(num):
#     result = 0
#     list_ = str(105).split(",")

#     for i in str(num):
#         result += int(i)
#     return result
# print(sum_digits(105))







# global
# nonlocal



# a = 9

# def func():
#     # global a 
#     a = 0
#     a += 1
#     return a

# print(func())
# print(a)


# def func1():
#     a = 9
#     def func2():
#     #     # a = 10
#     #     nonlocal a 
#     #     a += 1
#     #     print('hello') 
#     #     return a 
#     # return func2()

# print(func1())



# def func1():
#     a = 9
#     def func2():
#         # a = 10
#         nonlocal a
#         def func3():
#             # a = 0
#             nonlocal a 
#             a += 1
#             return a
#         return func3()
#     return func2()
# print(func1())        


# def func1():
#     a = 9
#     def func2():
#         # a = 10
#         nonlocal a
#         def func3():
#             # a = 0
#             nonlocal a 
#             a += 1
#             return a
#         return 'hello'
#     return func2()
# print(func1())  


# def func1():
#     a = 9
#     def func2():
#         # a = 10
#         nonlocal a
#         def func3():
#             # a = 0
#             nonlocal a 
#             a += 1
#             return a + 1
#         return 'hello'
#         # result = func2()
#     return func2()
# print(func1()) 


# CRUD 
# Creatr
# Read/Retriev
# Update
# Delete


# instagram = {}

# def generate_id():
#     import random
#     id_ = random.randint(1, 100)
#     return id_

# def create_post(title, author):
#     post_id = generate_id()
#     print(post_id)
#     post = {
#         post_id: {
#         'title': title,
#         'author': author
#         }
#     }
#     instagram.update(post)
#     return post_id

# post1 = create_post('Hello World', 'Kani')
# post2 = create_post('Python 14', 'Aikol')
# post3 = create_post('JavaScript', 'Jannat')
# print(instagram)



# instagram = {}

# def generate_id():
#     import random
#     id_ = random.randint(1, 3)
#     if id_ in instagram.keys():
#         return generate_id()
#     else:    
#         return id_

# def create_post(title, author):
#     post_id = generate_id()
#     print(post_id)
#     post = {
#         post_id: {
#         'title': title,
#         'author': author
#         }
#     }
#     instagram.update(post)
#     return post_id

# def delete_post(post_id):
#     confirm = input('Do you really want to delete this post? (y/n): ').lower()
#     if confirm == 'y':
#         instagram.pop(post_id)
#         print("SUCCESSFULLY DELETED")
#     else:
#         pass    

# post1 = create_post('Hello World', 'Kani')
# post2 = create_post('Python 14', 'Aikol')
# post3 = create_post('JavaScript', 'Jannat')
# print(instagram)
# delete_post(post1)
# print(instagram)


