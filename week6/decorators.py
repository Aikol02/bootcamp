
# hello_makers()
# хранить функции в переменных

# makers = hello_makers
# # makers()

# #определить функции внутри другой функции
# # def outer_func():
# #     def inner_func():
# #         print('Hello, Makers!')
# #     inner_func()

# # outer_func()

# #Передавать функции в качестве аргумента их из других функций

# # def main_func(func):
# #     print(f'Я получила функцию {func} в качестве аргумента')
# #     func()
# #     return func

# # def hello_makers():
# #     print('Hello, Makers!')

# # main_func(hello_makers)



# # Decorators
# # def func1():
# #     print("I'm called inside other function")

# # def func2(func):
# #     print("I'll do something before func calling")
# #     func()
# # def func3():
# #     print('Hello, Makers!!!!!!')
    
# # func2(func3)


# def decorator(func):
#     print("I'm function-decorator")
#     def wrapper():
#         print("I'm function-wrapper")
#         print("Вызываем обёрнутую функцию")
#         func()
#         print("Выхожу из обёртки")
#         return func
#     return wrapper

# # @decorator
# # def hello_makers():
# #     print("Hello, Makers!")

# @decorator
# def hello_bootcamp():
#     print("This is Bootcamp")

# hello_bootcamp()
    


