# й[q]ц[w]у[e]к[r]е[t]н[y]г[u]ш[i]щ[o]з[p]х[[]ъ[]]
# ф[a]ы[s]в[d]а[f]п[g]р[h]о[k]л[j]д[l]ж[;]э['] 
# я[z]ч[x]с[c]м[v]и[b]т[n]ь[m]б[,]ю[.]





# calculator task 1


# Ваша программа должна запрашивать
# имя пользователя. Программа должна
# запросить у пользователя хочет ли он
# играть или нет. Если ответ будет ‘нет’, то
# программа должна завершиться.


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
    #     number = random.randint(1, 15)
    #     lives = 0
    #     continue
    # if wish.lower().strip() == 'yes':
    #     try:
    #         guess_number = int(input(f'Загадано число от 1 до 15.У вас есть 6 попыток. Угадайте число. Попытка # {lives}: '))
    #     except ValueError:
    #             print('Введите число, а не строку')
    #             continue
    #     if guess_number == number:
    #             print(f'{name}, Вы выиграли!')
    #             wish = input('Хотите сыграть снова?: ')
    #             lives = 0
    # elif wish.lower().strip() == 'no':
    #     print(f'До свидания, {name}')
    #     break
    # else:
    #     print('Введите "yes" или "no"')
    #     lives == 0
    #     break 





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




# функции

"""
def name_of_function():
    some_code 
    return variable

name_of_function()
"""    


# def function():
#     print('The fanction is called')
#     return 'Makers'

# print(function()) 



# def substract():
#     num1 = 20 
#     num2 = 5 
#     print(num1 + num2)
#     return num1 - num2

# print(substract())

# veriable = substract()
# print(veriable)

# list_ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, substract()]
# print(list_)

# def substract():
#     num1 = 20 
#     num2 = 5 
#     print(num1 + num2)
#     return num1 - num2

# def function():
#     print("I'm calling substract function")
#     variable = substract()
#     return variable

# print(function())


# def multiply(a, b):
#     return a * b

# num1 = 70
# num2 = 10
# print(multiply(num1, num2))

# def welcome(name, last_name):
#     return f'Welcome, {name} {last_name}'

# name = input()
# last_name = input()

# print(welcome(name, last_name))


# def get_word(word):
#     list_letters = list(word)
#     return list_letters



class Song:
    def __init__(self, author, title, year):
        self.author = author
        self.title = title
        self.year = year

    def show_author(self):
        print('Автор этой песни {self.author}')
    def show_title(self):
        print('Название этой песни {self.title}')
    def show_year(self):
        print('Эта песня вышла в {self.year} году')

song = Song('Pharrell Williams', 'Happy', 2013)
song.show_author()
song.show_title()
song.show_year()
