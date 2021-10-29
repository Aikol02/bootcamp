# import random
# words = ['книга', 'дом','ручка', 'конкатенация', 'очки']
# secret = random.choice(words)
# hidden_word = list('*' * len(secret))
# attempts = 5 

# while attempts > 0:
#     letter = input(f'Угадайте слово {hidden_word}\nКоличество попыток {attempts}\nВведите букву: ')
#     if letter in secret:
#         for index, value in enumerate(secret):
#             if letter == value:
#                 hidden_word[index] = letter
#             if '*' not in hidden_word:
#                 print(f'Вы угадали слово {secret}! Поздравляем!')
#                 break
#     else:
#         attempts -= 1
#         if attempts < 5: print('  |  ')
#         if attempts < 4: print('  0  ')
#         if attempts < 3: print(' / \ ')
#         if attempts < 2: print('  |  ')
#         if attempts < 1: print(' / \ ')
#     if attempts == 0:
#         print('Вы проиграли. Загаданное слово {secret}')
#         break

