# for 
# list_ = []
# for num in range(1, 21):
#     list_.append(num * 2)
#     print(list_)

# list comprehenshion
# list_ = [num * 2 for num in range(1, 21)]
# print(list_)


# list_users = ['Alice', 'Sam', 'Sandy', 'Ben', 'John']
# invitations = ['You are invited' + name for name in list_users]
# print(invitations)


# list1 = [10, 5, -6, -8, -12, 20, 3, 14, 4]
# list2 = [num for num in list1 if num % 2 == 0 or num % 3 == 0]
# print(list2)
# strings = ['1998']




"""
try:
    some code 1
except:
    some code 2
else:
    some code 3
finally:
    some code 4
# """

# try:
#     num1 = int(input('Введите число: '))
# except:
#     print('Вы ввели не число')


# try:
#     num1 = int(input('Введите первое число: '))
#     num2 = int(input('Введите первое число: '))
#     result =  num1 / num2
# except ZeroDivisionError:                #голое исключение 
#     print('На ноль делить нельзя')
# except ValueError:
#     print('Вы ввели не число')
# else:
#     print(result)
# finally:
#     print('Программа завершена')



# dict_ = dict.fromkeys(('makers', 'bootcamp', 'hello', 'dictionary'), 0)
# dict_ = {key: len(key) for key, val in dict_.items()}
# dict_.update({'except': 'Exception'})
# print(dict_)

# while True:
#     try:
#         key = input('Введите слово: ')
#         if key == 'exit':
#             break
#         dict_[key] += 2
#     except (KeyError, TypeError):
#         print('Данного ключа нет либо произвести конкатенацию с числами нельзя')
#     else:
#         print(dict_[key])
#     finally:
#         print(dict_)


# list_ = [i for i in range(1, 31)]

# try:
#     index = int(input())
#     list_[index] = 'Makers'
# except IndexError:
#     print('You are out of list range')
# except ValueError:
#     print('Please enter the number, not a string')
# else:
#     print('There is no exception')
# finally:
#     print(list_)


# try:
#     print(makers)
# except NameError:
#     print('Вы не создавали переменную makers')


# raise

# number = int(input('Введите число от 1 до 70: '))
# if not number in range(1, 71):
#     raise Exception('Вы ввели число, которое не находиться в данном промежутке')
# print('ok')
