# class SomeClass:
#     pass 

# class A:
#     pass

# a = A()          #экземпляр класса
# print(isinstance(a, A))

class Dog:
    owner = 'Deni'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'{self.name}, {self.age}'

    def bark(self):
        print('Gav-gav')

    def dog_info(self):
        return f'This is {self.name}, he is {self.age} years old'

    def birthday(self, cake):
        self.age +=1
        self.cake = cake
        return f'{self.name} is {self.age} now'

    def friends(self, friend):
        self.friend = friend
        friend.friend = self

dog1 = Dog(name='Djangu', age=0)
dog2 = Dog(name='Bobik', age=1)
dog3 = Dog(name='Tuzik', age=2)

dog1.friends('dog2')
print(dog1.friend)
# print(dog1.birthday('Vanila'))
# print(dog2.birthday('Strawberry'))
# print(dog3.birthday('Chocolate'))
# print(dog1.cake)
# print(dog2.cake)
# print(dog3.cake)

# print(dog1.age)
# dog1.bark()
# dog2.bark()
# dog3.bark()
# print(dog1.dog_info())
# dog3.owner = 'Lula'
# print(dog1.name)
# dog1.name = 'Djangu'
# dog1.food = 'meat'
# print(dog1.food)
# print(dog2.name)
# print(dog1.owner)
# print(dog2.owner)
# print(dog3.owner)