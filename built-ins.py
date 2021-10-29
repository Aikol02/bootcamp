# a = {'a': 1, 'b': 2, 'c': 1}
# a.pop('c')
# print(a)


# a = {'a': 1, 'b': 2, 'c': 1}
# a.update({'f': 55})
# print(a)


# a = {'a': 1, 'b': 2, 'c': 1}
# a.clear()
# print(a)


# a = {'a': 1, 'b': 2, 'c': 1}
# b = list(a.keys())
# print(b)


# a = {'a': 1, 'b': 2, 'c': 1}
# a.items()
# print(a)

# some_dict = {0: False, 1: 'это', 2: 'строка', 3: True}
# for k, v in list(some_dict.items()):     
#      if type(v) != str:         
#          del some_dict[k]  
# print(some_dict)


# dict_ = {'key1': 'value1', 'key2': 'value2'}
# try:
#     new_dict = {v : k for k, v in dict_.items()}
#     print(dict_['val'])
# except Exception as e:
#     print(e)
    
# dict_ = {'key1': 'value1', 'key2': 'value2'}
# try:
#     print(dict_['key1'])
# except KeyError:
#     print('Нет такого ключа!')




# import random 

# name = input('Как тебя зовут: ')
# number = random.randint(1, 15)
# wish = input('Хотите сыграть: ')
# print(number)

# lives = 0
# while True:
#     lives += 1
#     if lives > 6:
#         print('GAME OVER = (')
#         wish = input('Хотите сыграть снова?: ')
#         number = random.randint(1, 15)
#         lives = 0
#         continue
#     if wish.lower().strip() == 'yes':
#         try:
#             guess_number = int(input(f'Загадано число от 1 до 15.У вас есть 6 попыток. Угадайте число. Попытка # {lives}: '))
#         except ValueError:
#                 print('Введите число, а не строку')
#                 continue
#         if guess_number == number:
#                 print(f'{name}, Вы выиграли!')
#                 wish = input('Хотите сыграть снова?: ')
#                 lives = 0
#     elif wish.lower().strip() == 'no':
#         print(f'До свидания, {name}')
#         break
#     else:
#         print('Введите "yes" или "no"')
#         lives == 0
#         break 




# var = 'переменная bar'

# def foo():

#     var = 'переменная foo'

#     def bar():

#         var = 'переменная bar'
#     bar()

#     print("переменная в foo: ", var)
# foo()

# print("переменная в foo: ", var)


# from functools import reduce
# list_ = [5, 6, 7, 8]
# result = reduce(lambda x, y: x * y, list_)
# print(result)


# list_ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ] 
# result = len(list(filter(lambda x: x % 2 == 0, list_)))
# result1 = len(list(filter(lambda x: x % 2 != -0, list_)))
# print(f'even: {result}, odd: {result1}')



# list_ = []
# for i in range(1, 101):
#     list_.append(i)
# print(list_)

# list_ = [x for x in range(1, 101)]
# print(list_)

# list_ = [x for x in range(1, 50)]
# print(list_)


# dict_ = {'a': 1, 'b': 2, 'c': 3}
# dict1_ = {key: val * 2 for key, val in dict_.items()}
# print(dict1_)





# def registration(name, *arqs, **kwarqs):
#     name = name
#     email = arqs[0]
    
#     password = kwarqs.get('password')
#     password_confirm = kwarqs['password_confirm']
    
#     def is_valid(*arqs, **kwarqs):
#         password = kwarqs.get('password')
#         password_confirm = kwarqs.get('password_confirm')
#         if password != password_confirm:
#             raise ValueError('paroli ne sovpadayut!')
#         else:    
#             return 'vy zaregistrirovany'
#     return is_valid(password=password, password_confirm=password_confirm)

# print(registration('python14', 'python14@gmail.com', password = '123', password_confirm= '123' ))



# def registration(name, *arqs, **kwarqs):
#     name = name
#     email = arqs[0]

#     def is_email(*arqs, **kwarqs):
#         email = kwarqs.get('email')
#         if email.endswith('@gmail.com'):
#             return 'Email прошел!'
#         else:
#             raise ValueError('Email не прошел!')
#     is_email(email=email)            

#     password = kwarqs.get('password')
#     password_confirm = kwarqs['password_confirm']
    
#     def is_valid(*arqs, **kwarqs):
#         password = kwarqs.get('password')
#         password_confirm = kwarqs.get('password_confirm')
#         if password != password_confirm:
#             raise ValueError('paroli ne sovpadayut!')
#         else:    
#             return 'vy zaregistrirovany'
#     return is_valid(password=password, password_confirm=password_confirm)

# print(registration('python14', 'python14@gmail.com', password = '123', password_confirm= '123' ))