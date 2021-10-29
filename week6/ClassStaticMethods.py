# 1
# class Category:
#     def __init__(self, name):
#         self.name = name
    
#     def __str__(self):
#         return f"Category: {self.name}"

# iphone = Category('Iphone')
# samsung = Category('Samsung')
# nokia = Category('Nokia')
# xiaomi = Category('xiaomi')

# class Condition:
#     def __init__(self, condition):
#         self.condition = condition

#     def __str__(self):
#         return f'Condition: {self.condition}'

# new = Condition('Новый')
# used = Condition('Б/У')
# repaired = Condition('отремонтированнный')


# class Phone:
#     def __init__(self, category, model, price, condition):
#         self.category = category
#         self.model = model
#         self.price = price
#         self.conditon = condition

#     @classmethod
#     def create_iphone(cls, model, price, condition):
#         return cls(
#             category=iphone,
#             model=model,
#             price=price,
#             condition=condition
#         )

#     @classmethod
#     def create_samsung(cls, model, price, condition):
#         return cls(
#             category=samsung,
#             model=model,
#             price=price,
#             condition=condition
#         )

#     @classmethod
#     def create_nokia(cls, model, price, condition):
#         return cls(
#             category=nokia,
#             model=model,
#             price=price,
#             condition=condition
#         )

#     @classmethod
#     def create_xiaomi(cls, model, price, condition):
#         return cls(
#             category=xiaomi,
#             model=model,
#             price=price,
#             condition=condition
#         )

#     @property
#     def title(self):
#         return f'{self.category} {self.model} {self.price} {self.conditon}'

#     @staticmethod
#     def sale(percent, price):
#         x = price * percent / 100
#         return x

#     def sale_price(self, percent, code):
#         sale = self.sale(percent, self.price)
#         if code.lower() == 'makers':
#             self.price -= sale


#     def __repr__(self) -> str:
#         return self.title

# p1 = Phone.create_iphone('SE', 78000, new)
# p2 = Phone.create_iphone('X', 56000, new)
# p2.sale_price(30, 'makers')
# print(p2.price)


# # print(p1.title)



# # p3 = Phone.create_xiaomi('8 ligt', 15000, used)
# # p4 = Phone.create_nokia('3310', 25000, repaired)
# # p5 = Phone.create_samsung('A 5', 5000, used)
# # print(p1.category, p1.conditon)
# # print(p2.category, p2.conditon)
# # print(p3.category, p3.conditon)
# # print(p4.category, p4.conditon)
# # print(p5.category, p5.conditon)



# # phone1 = Phone(iphone, 'SE', 45000, 'NEW')
# # phone2 = Phone(samsung, 'Galaxy 9', 23000, 'USED')
# # print(phone2.category)



