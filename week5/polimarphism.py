# # 1
# from abc import ABC, abstractmethod


# class Pizza(ABC):
#     def __init__(self, pizza, cost):
#         self.pizza = pizza
#         self.cost = cost

#     @abstractmethod
#     def add_exstra(self, ingredient):
#         self.ingredient = ingredient
#         print(f'{self.pizza} with extra {self.ingredient} costs {self.cost}')

# class DodoPizza(Pizza):
#     def add_exstra(self, *ingredient):
#         self.cost += 50 * len(ingredient)
#         return super().add_exstra(ingredient)

#     def late(self, time):
#         if time >= 5:
#             print(f'You get free pizza card!!!')

# class PapaJohns(Pizza):
#     def add_exstra(self, *ingredient):
#         self.cost += 70 * len(ingredient)
#         return super().add_exstra(ingredient)

#     def late(self, time):
#         if time >= 100:
#             print(f'This pizza is free')
#             self.cost = 0 
#         else:
#             self.cost = self.cost = (self.
#             cost * time / 100)

# pizza1 = DodoPizza('Pepperoni', 500)
# pizza1.add_exstra('cheese', 'sauce', 'pepperoni')
# pizza1.late(5)
# pizza2 = PapaJohns('Margarita', 400)
# pizza2.add_exstra('tomato', 'bazil')
# pizza2.late(30)
# print(pizza2.cost)


# for pizza in [pizza1, pizza2]:
#     pizza.late(10)


# 2 

# instance_method
# class_method
# static_method

# class King:
#     @staticmethod
#     def some_static_method():
#         print('I am a static method')

#     # def some_method(cls): pass

#     def move(self):
#         print('Я хожу на 1 клетку в любую сторону')

# class Queen:
#     def move(self):
#         print('Я хожу как королева')

# class Horse:
#     def move(self):
#         print('я хожу буквой Г')

# figure1 = King()
# figure1.some_static_method()
# figure2 = Queen()
# figure3 = Horse()
# for figure in [figure1, figure2, figure3]:
#     figure.move()