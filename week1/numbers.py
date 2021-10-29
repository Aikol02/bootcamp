"""
int, str, bool, dict, list, set, tuple
break, continue, pass
class, def
print input id
"""
"""
функция input всегда возвращает string

"""

# name = input('Enter your name: ')
# last_name = input('Enter your surname: ')
# print('Hello World!', name, last_name)


# first_num = int(input('Enter first number: '))
# second_num = int(input('Enter second number: '))
# print(first_num + second_num)
# print(type(first_num))
# print(type(second_num))

"""
строки
"""

# string1 = "makers45%*"
# string2 = 'bootcamp'
# print(string1, string2)

# string3 = 'makers bootcamp'
# print(string3)
# string = "maker's bootcamp"
# print(string)

# sentence = "I have phone brand 'Samsung"
# print(sentence)

# sentence = 'I love Maker\'s Bootcamp'
# print(sentence)


# string = "Dear friend,\n\nWelcome to Makers Bootcamp!\nEnjoi your time here with us!"
# print(string)

# string = """Dear friend, 
# Welcome to Makers Bootcamp! 
# Enjoy your time here with us!"""
# print(string)

# """
# These are documentation comments
# """

# #this is comment


# string = 'This is a vey long string.\
#     The length of String in Python should not be more then 79 symbols.\
#     Remember this.'
# print(string)

# languages = "Languages:\n\t"
# description = 'Python: backand language\n\t JavaScript: frontend language'
# print(languages, description)


# loop = 'for i in range(5):\n\tprint(i)'
# print(loop)


# sentence = 'Hello\vMakers\vBootcamp\vJohn'
# print(sentence)

"""сырая строка"""
# url = r'https://kaktus\news\topics/\read'
# print(url)


"""конкатенция"""

# string1 = 'Makers'
# string2 = 'Bootcamp'
# # print(string1 + string2)
# print('I study at ' + string1 + ' ' + string2)

# num1 = '6'
# num2 = '7'
# result = num1 + num2
# print(result)

"""дублирование строки"""

# string = 'makers'
# print(string * 10)


"""длина строки"""
#len()
# string = 'Makers Bootcamp'
# print(len(string))

# length = len('john')
# print(length)


"""доступ по индексу"""

# sentence = 'Strings are ordered'
# print(len(sentence))
# print(sentence[0])
# print(sentence[5])
# print(sentence[7])
# print(sentence[-1])
# print(sentence[-2])
# print(sentence[18])

"""среэы 
  подстроки"""


"""
[x:y]
[x:y:z]
"""


# string = 'Makers Bootcamp'
# print(string[::-2])
# print(string[3:5:2])
# print(string[2::3])
# string = string[::-1]
# print(string)
# print(string[:3])
# print(string[2:-2])
# print(string[:6])
# print(string[::])
# part_string = string[:3]
# print(part_string)


# word = 'dream'
# # word[0] = 'c'
# word = 'c' + word[1:]
# print(word)

"""методы строк"""

#find(string), rfind(string)
# string = 'Makers Bootcamp Boot Boot'
# print(string.rfind('Boot'))

#index(string), rindex(string)
# string = 'Makers Bootcamp Boot Boot camp'
# print(string.rindex('camp'))


#replace(pattern, replace_pattern)
# string = 'Makers Bootcamp Makecamp'
# print(string.replace('camp', 'rock'))


#split(symbol) -> list
# string = "Makers Boot*camp"
# print(string.split('*'))
# full_name = input('Enter name and lastname: ').split()
# name = full_name[0]
# last_name = full_name[-1]
# print(name)
# print(last_name)


#isdigit(), isalpha(), isalnum(), islower()
#isupper(), isspace(), istitle()
"""is возвращает нам булевое значение"""

# string = '12345'
# print(string.isdigit())   #True
# string = 'Makers'
# print(string.isalpha()) # True
# string = '12345Makers'
# print(string.isalnum())  # True
# string = 'makers'
# print(string.islower())   # True
# string = 'MAKERS'
# print(string.isupper())    # True
# string = ' \n\t'
# print(string.isspace())    # True
# string = 'Makers Bootcamp'
# print(string.istitle())     # True


# upper(), lower()
# string = 'Makers'
# print(string.upper())
# print(string.lower())

# startswith(), endswith()
# string = 'I love makers'
# print(string.startswith('I'))    #True
# print(string.endswith('makers'))    #True


# join(list)
# list_ = ['m', 'a', 'k', 'e', 'r', 's']
# print('&'.join(list_))

# capitalize(), title()
# string = 'bootcamp makers'
# print(string.capitalize())
# print(string.title())


# count()
# string = 'Makers Bootcamp aaaaa'
# print(string.count('a'))


# lstrip(), rstrip(), strip()
# password = ' qwerty'
# print(password.lstrip())   #удаляет пробел сначала

# password = ' qwerty    '
# print(len(password))
# print(password.rstrip())    #удаляет пробел с конца

# password = ' qwerty    '
# print(len(password))
# print(password.strip()) 


#partition(patter) -> tuple
# string = 'Hello lovely Makers Bootcamp'
# print(string.partition('Makers'))


#swapcase()
# string = 'CamelCase'
# print(string.swapcase())


#zfill(width)
# string = 'makers'
# print(string.zfill(9))


#ljust(width, fillchar), rjust(width, fillchar)
# string = 'makers'
# print(string.ljust(9, '*'))
# print(string.rjust(11, '@'))


# форматирование строк              #format()

# 1. % 

# name = input()
# last_name = input()
# age = int(input())
# some_variable = "Welcome, %s %s, age %d"%(name, last_name, age)
# print(some_variable)


# 2. format()

# name = input()
# last_name = input()
# variable = 'Hello, {} {}'.format(name, last_name)
# print(variable)

# 3. f''

# name = input()
# last_name = input()
# age = input()
# variable = f'Hello {name} {last_name}\nYour age is {age}'
# print(variable)




# string = 'hope'
# print(string[-2:])

# string = 'The quick brown fox jumps over the lazy dog'
# print(string.replace('o', '*'))

# string = 'ferrari'
# print(string.upper())


# hashtags = '#makers#bootcamp#программирование#it#курсы'
# print(hashtags[1::].strip().split('#'))

# name = 'Deni'
# last_name = 'Atlas'
# age = 29
# city = 'Mexica'
# print(f'Вас зовут {name} {last_name}, Ваш возраст: {age}, проживаете в городе {city}')


# name = 'Иван'
# last_name = 'Пупкин'
# age = 35
# city = 'Москва'
# print(f'Вас зовут {name} {last_name}, Ваш возраст: {age}, Вы  проживаете в городе {city}')



# name_of_friends = ['Atai', 'Murat', 'Janat', 'Kani', 'Aikol']
# for name_of_friends in range(4)

# num1 = 8
# num2 = 7
# num3 = 7.6
# print(num1 % num2 * num3)

# string = "makers"
# print(string[::-1])

# list_ = [1, 2, 3, 4, 5]
# for list_ in range('1''6'):
#     print(list_)



# list1_ = [1, 3 ,4, 6, 7]
# list2_ = [5, 8, 9, 2, 4]
# print(list1_ + list2_)


# list1 = [1, 2, 3, 4, 5]
# list2 = [6, 7, 8, 9, 1]
# print(list1 + list2)

