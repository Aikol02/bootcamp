# class Human:
#     golova = 'Голова'

#     def __init__(self, name, age = 0):
#         self.name = name
#         self.age = age

#     def custom_method(self, *arqs, **kwarqs):
#         pass

#     def __str__(self):
#         return str(self.age)

#     # def __add__(self):
# #     #     return f'(len{self.name}, {huma.name}'


# # class Planet:

# #     people = []

# #     def __init__(self, name, life):
# #         self.name = name
# #         self.life = life # есть ли жизнь?

# #     def add_human(self, human):
# #         self.people.append(human)
# #         print(f'Welcome {self.name}, {human.name}')


# # earth = Planet('Earth', True)
# # Naiza = Human('Naiza', age = 20)
# # earth.add_human(Naiza)
# # print(earth.people)


# # a = str("Naiza")
# # print(a)


# from abc import ABC, abstractclassmethod
# class Animal(ABC):
#     instinct = ('eat', 'razmnozhenie')

#     def __init__(self, name, age, poroda):
#         self.name = name
#         self.age = age
#         self.poroda = poroda

#     @abstractclassmethod
#     def hunting(self):
#         print('it can hunt')

#     @abstractclassmethod
#     def eat(self):
#         print('i can eat')

# class Hobby:
#     game = {
#         'cat': 'зарапать',
#         'dog': 'играть с мячиком'
#     }


#     def play(self, classs):
#         try:
#             return Hobby.game[classs]
#         except KeyError:
#             return 'такого вообще нет!!!'

# class Dog(Animal, Hobby):
#     def __init__(self, name, age, poroda):
#         super().__init__(name, age, poroda)
        

#     def eat(self):
#         return super().eat()

#     def hunting(self):
#         return super().hunting()

#     def __str__(self):
#         return self.name


# rex = Dog('Rex', 3, 'ovcharka')
# print(rex.instinct)
# print(rex.hunting())


# class Cat(Animal, Hobby):
#     def __init__(self, name, age, poroda, owner):
# #         super().__init__(name, age, poroda)
# #         self.owner = owner

# #     @property
# #     def hunting(self):
# #         print('It can not hunt it is domastic')
    
# #     def eat(self):
# #         print('It can eat')
# #     @property
# #     def info(self):
# #         return f'{self.name} {self.age} {self.poroda} {self.owner}'

# # cat = Cat('Gosha', 4, 'Siamtwin', 'Bekbol')
# # print(cat.info)

# # bobik = Dog('bobik', 5, 'tuzic')
# # print(bobik.play('dog'))
# # print(cat.play('cat'))
# # inst = [i for i in cat.instinct if i == 'eat']
# # print(inst)

# from abc import ABC, abstractmethod

# class Initil(ABC):
#     @abstractmethod
#     def __init__(self, name, email, password):
#         self.name = name
#         self.email = email
#         self.password = password 



# class DataBase(Initil):
#     dict_ = {}

#     def __init__(self, name, email, password):
#         # super().__init__(name, email, password)
#         self.name = name
#         self.email = email
#         self.password = password 
        

#     @property
#     def db(self, email, password):
#         DataBase.dict_.setdefault({email,password})


# class Registration(DataBase, Initil):
#     def __init__(self, name, email, password, password_confirm):
#         super().__init__(name, email, password)
#         self.password_confirm = password_confirm

#     def registration(self):
#         if not self.email.endswith() in ['@gmail.com', '@mail.ru', '@yandex.ru']:
#             raise ValueError('email должен заканчивать на @gmail.com, @mail.ru, @yandex.ru')
#         if len(str(self.password)) < 5:
#             raise ValueError ('Пароль не должен быть меньше 5')
#         else:
#             self.password = self.password
#         if self.password != self.password_confirm:
#             raise ValueError('Пароли не совпадают ты БОТ')
      

#         DataBase.db(email=self.email, password=self.password)



# class Authorization():
#     def __init__(self, name, email, password):
#         super().__init__(name, email, password)

#     def authorization(self):
#         if self.email in DataBase.dict_.keys():
#             if self.password == DataBase.dict_.get(self.email):
#                 return f'для user {self.email} Доступ разрешен'
#             else: 
#                 return f'У вас не верный пароль'
#         else:
#             return f''



# user = Registration('Sezim', 'sezim@mail.ru', 12345, 12345)
# user.registration

# user2 = Registration('Esen', 'Esen@mail.ru', 12345, 12345)
# user2.registration

# user3 = Registration('Kayr', 'Kayr@mail.ru', 12345, 12345)
# user3.registration

# print(DataBase.dict_)

