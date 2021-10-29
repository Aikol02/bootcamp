# 1 

# products = {
#     "milk": 2,
#     "bread": 1,
#     'eggs': 20,
#     'potato': 35
# }
# while products:
#     product = input('Enter product: ')
#     try:
#        products.pop(product)
#        print(products)
#     except KeyError:
#         print('There is no such product!!!')
#     finally:
#         print(products)
# else:
#     print('product is empty')

# 2


# gallery = []
# try:
#     memory = int(input('Choose memory size: '))
# except Exception as e:
#     # print('Enter number not a symbol')
#      print(type(e).__name__)
# while memory:
#     photo = input('Make photo: ')
#     gallery.append(photo)
#     memory -= 1
# else:
#     print(gallery)
#     raise MemoryError('your gallery is full!!!!!!')

# 3

# kurs = {
#     'buy':{
#         'dollar': 84.50,
#         'euro': 101.25,
#         'rub': 1.16
#     },
#     'sell': {
#         'dollar': 84.90,
#         'euro': 102.10,
#         'rub': 1.30
#     }
# }

# while True:
#     try:
#        operation = input('Choose operation (sell, buy): ').lower()
#        data = kurs[operation]
#        print(data)
#     except KeyError:
#         print('Enter correct operation')
#         continue
#     else:
#         valuta = input('Choose (dollar, euro, rub): ')
#         try:
#             exchange = data[valuta]
#             summa = int(input('How much money do you want to convert? '))
#             if operation == 'buy':
#                 result = summa * exchange
#                 print(f'Your exchange {result} soms')
#             else:
#                 result = summa / exchange
#                 print(f'Your exchange {round(result, 2)} {valuta}s')
#             if summa <= 0:
#                 raise ValueError
#         except ValueError:
#             print('Enter correct amount')
                
#         except KeyError:
#             print('Enter correct currency')

#         else:
#             end = input('Do you  want to continue? ').lower()
#             if end == 'y' or end == 'yes':
#                 continue
#             else:
#                 break
