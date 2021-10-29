# # 1
# # def slugify(func):
# #     def wrapper(title):
# #         return title.replace(' ', '-').lower()
# #     return wrapper

# # @slugify
# # def get_title(word):
# #     return word

# # print(get_title('Nike Airforce 2021'))
# # print(get_title('BMW X-5 samurai'))



# def on_sale(func):
#     def wrapper(sale, old_price):
#         print('START!!!')
#         func(sale, old_price)
#         new_price = old_price - (sale * old_price / 100)
#         print((f'New price is {new_price}'))
#         return new_price
#     return wrapper

# @on_sale
# def buy_product(sale, price):
#     print(f'I have a coupon {sale}%. old price is {price}$')


#     buy_product()

# print(buy_product(input('Enter sale: ')), int(input('Enter price: ')))


# def say_hello():
#     print('HELLO WORLD!!!!')

# # print(globals())

# if __name__ == '__main__':
#     say_hello()


# login
# users = {
#     'jannat': 'qwerty',
#     'atai': 'elchacha',
#     'ulan': 'ulik'
# }
# def login_required(func):
#     def wrapper(**kwarqs):
#         username = kwarqs.get('username')
#         password = kwarqs.get('password')
#         if username in users and password==users.get(username):
#             print('POST CREATED!!!')
#             func(kwarqs.get('title'),
#                  kwarqs.get('image'))
#         elif not username or not password:
#             print('You should login')
#         else:
#             print('Not valid')
#     return wrapper

# @login_required
# def create_post(title, image):
#     print(f'{title} - {image}')

# create_post(title='Post 1', 
#             image='post1.jpeg', 
#             username='atai', 
#             password='elchacha')