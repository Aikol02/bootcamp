# 1

# class Som:
#     currencies = {
#         "USD": 84.5,
#         "EUR": 101.4,
#         "RUB": 1.06,
#         "KZT": 0.2,
#         "SOM": 1
#     }

#     def __init__(self, value, curr):
#         self.value = value
#         self.curr = curr

#     def __add__(self, other):
#         curr1 = Som.currencies.get(self.curr)
#         curr2 = Som.currencies.get(other.curr)
#         print(f'{self.value * curr1} som и {other.value * self.value} som')
#         return self.value * curr1 + other.value * curr2

#     def __sub__(self, other):
#         curr1 = Som.currencies.get(self.curr)
#         curr2 = Som.currencies.get(other.curr)
#         print(f'{self.value * curr1} som и {other.value * self.value} som')
#         return self.value * curr1 - other.value * curr2

# a = Som(100, 'USD')
# b = Som(25, 'EUR')
# print(a + b)
# c = Som(15000, 'RUB')
# d = Som(40000, 'KZT')
# print(c + d)


# 2

# class Distance:
#     units_M = {
#         'SM': 0.01,
#         'DM': 0.1,
#         'M': 1,
#         'KM': 1000,
#         'Miles': 1600
#     }

#     def __init__(self, value, unit):
#         self.value = value
#         self.unit = unit

#     def __gt__(self, other):
#         dist1 = Distance.units_M.get(self.unit)
#         dist2 = Distance.units_M.get(other.unit)
#         print(f'{self.value * dist1} M and {other.value * dist2}')
#         return self.value * dist1 > other.value * dist2

#     def __eq__(self, other):
#         dist1 = Distance.units_M.get(self.unit)
#         dist2 = Distance.units_M.get(other.unit)
#         print(f'{self.value * dist1} M and {other.value * dist2}')
#         return self.value * dist1 == other.value * dist2

#     def __it__(self, other):
#         dist1 = Distance.units_M.get(self.unit)
#         dist2 = Distance.units_M.get(other.unit)
#         print(f'{self.value * dist1} M and {other.value * dist2}')
#         return self.value * dist1 < other.value * dist2

# a = Distance(7, 'KM')
# b = Distance(5.8, 'Miles')
# print(a < b)


# 3

# class PasswordValidationMixin:
#     def validate_password(self, password):
#         if len(password) >= 8 and not password.isdigit() and not password.isalpha() and not password.islower():
#             self.password = password
#             print('password created')
#             return True
#         else:
#             print('Invalid password')
#             return False

# class Facebook(PasswordValidationMixin):
#     def __init__(self, username, password):
#         if self.validate_password(password):
#             self.username = username
#             print(f'Facebook account created for {username}!')
#         else:
#             print('Facebook account NOT created!!!')

#     def __getattr__(self, attr):
#         print('Сработал GETATTRIBUTE!!!  ')
#         return 'You do not have a facebook account yet!'

#     def __getattribute__(self, name:str):
#         print('Сработал GETATTRIBUTE!!!')
#         return  super().__getattribute__(name)


# user1 = Facebook('jannat', 'qwerTyui99')
# print(user1.username)
# print(user1.lastname)
# print(user1.__dict__)
# user1.email = 'jannat@gmail.com'
# print(user1.__dict__)

        
# class Person:

#     def __init__(self, name):
#         self.name = name

#     def __setattr__(self, attr, value):
#         if attr == 'password':
#             print('Cannot create lastname')
#             return None
#         return super().__setattr__(attr, value)

# jannat = Person('Jannat')
# jannat.name = 'Atai'
# jannat.lastname = 'Janatov'
# print(jannat.lastname)
# jannat.password = 'qwerty'
# print(jannat.password)


# Интерактив

# class MyClass:
#     def __init__(self, name):
#         self.name = name

#     def __getattribute__(self, name: str):
#         try:
#             return super().__getattribute__(name)
#         except AttributeError:
#             return super().__setattr__('john')

# a = MyClass('john')

# print(a)





import re
 
text = "The ants go marching one by one"
 
strings = ['the', 'one']
 
for string in strings:
    match = re.search(string, text)
    if match:
        print('Found "{}" in "{}"'.format(string, text))
        text_pos = match.span()
        print(text[match.start():match.end()])
    else:
        print('Did not find "{}"'.format(string))
"""

В этом примере мы импортируем модуль re и создаем простую строку. Когда мы создаем список из двух строк, которые мы будем искать в главной строке. Далее мы делаем цикл над строками, которые хотим найти и запускаем для них поиск. Если есть совпадения, мы выводим их. В противном случае, мы говорим пользователю, что искомая строка не была найдена.

"""