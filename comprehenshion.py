# numbers1 = []
# numbers2 = list()
# print(type(numbers1))
# print(type(numbers2))


# numbers4 = [1, 2, 3, 4]
# numbers5 = list(['makes', 'bootcamp', True, 56])
# print(numbers5)


# numbers = [7, 7, 7, 7, 7, 7, 7]
# numbers2 = [7] * 6
# print(numbers)
# print(numbers2)


"""range()"""

#1. range(end)
# numbers = list(range(10))
# print(numbers)

#2. range(start, end)
# numbers = list(range(1, 10))
# print(numbers)

#3. range(start, end, step)
# numbers = list(range(1, 10, 2))
# print(numbers)


# numbers = list(range(10, 0, -2))
# print(numbers)

# for i in range(1, 21):
#     print(i ** 2)


"""сравнение списков"""

# numbers1 = [1, 2, 3, 4, 5, 11]
# numbers2 = [1, 2, 3, 4, 5, 9, 100]

# print(numbers1 > numbers2)


# numbers = [1, True, 'Makers', 'hello', 8.9, (1, 2), ['hello']]
# print(numbers)

"""индексация"""

# numbers = [1, True, 'Makers', 'hello', 8.9, (1, 2), ['hello']]

# print(numbers[0])
# print(numbers[2])
# print(numbers[4])
# print(numbers[-1])
# print(numbers[-2])


# numbers = [1, True, 'Makers', 'hello', 8.9, (1, 2), ['hello']]

# numbers[3] = 'Bootcamp'
# numbers[-1] = {1: 'a'}
# print(numbers)

"""неизменяемый"""
# string = 'Makers'
# string[-1] = 'S'
# print(string)

"""перебор элементов списка"""
# users = ['Alice', 'Sam', 'Carly']
# for user in users:
#     print(f'Hello {user}')

# for letter in 'Makers':
#     print(letter.upper())

"""List Methods"""
#append(element)
# users = ['Alice', 'Cat', 'Billy']
# user = 'Tom'
# users.append(user)
# print(users)

# guests = []
# list_lenght = int(input('Enter  number of guests: '))

# for i in range(list_lenght):
#     guest = input('Enter guest name: ')
#     print(guests)
#     guests.append(guest)

# print(guests)


# extend(list)
users1 = ['Alice', 'Sam']
users2 = ['Bob', 'Tom']
# users1.extend(users2)
# print(users1)
# users2.extend(['John', 'Aibek'])
# print(users2)

# print(users1 + users2)

#insert(index, element)

# users = ['John', 'Lenny', 'Andy', 'Ann']
# users.insert(2, 'Raychel')
# print(users)

#remove(element)

# 



#clear()
# users = ['Sam', 'Cat', 'Carly']
# print(id(users))
# users.clear()
# print(id(users))


#index(element)

# my_list = ['hello', 'makers', True, 6]
# print(my_list.index('makers'))

#pop(index), default - pop(-1)
# numbers = [1, 2, 3, 4, 5]
# number = numbers.pop(1)
# numbers.pop()

# print(numbers)
# print(number)


#count(element)
# numbers = [2, 4, 2, 2, 6, 8, 0, 2, 2, 2]
# print(numbers.count(2))

# users = ['Ann', 'Ann', 'Alice', 'Sam', 'Ann']
# print(users.count('Ann'))

#sort(key)
# users = ['Alice', 'Thomas', 'Cat', 'Ann', 'Raychell']
# users.sort(key=len)
# print(users)

#reverse()

# users = ['Alice', 'Thomas', 'Cat', 'Ann', 'Raychell']
# users.reverse()
# print(users)

#copy()


