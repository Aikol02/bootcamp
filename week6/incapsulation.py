# class Person:
#     def __init__(self, name, hours, per_hour):
#         self.name = name
#         self.hours = hours
#         self._per_hour = per_hour


#     @property
#     def salary(self):
#         try:
#             return self.__salary
#         except:
#             self.__salary = self.hours * self._per_hour
#             return self.__salary
        

    # @salary.setter
    # def salary(self, new_salary):
    #     self.__salary = new_salary


    # def get_salary(self, name):
    #     responce = input(f'{name} хочет узнать вашу зарплату: ').lower()
    #     if responce == 'yes':
    #         return self.__salary
    #     return 'Не скажу'

    # def set_salary(self, new_salary):
    #     self.__salary = new_salary


# person1 = Person('Jannat', 30, 15)
# print(person1.salary)
# person1.salary = 9000
# print(person1.salary)
# print(person1.get_salary('Ulan'))
# person1.set_salary(200000)
# print(person1.get_salary('Atai'))
# person1.__salary = 20000
# print(person1.__salary)


# class User:
#     def __init__(self, username, password, email):
#         self.__username = username
#         self.__password = password
#         self.__email = email

#     @property
#     def info(self):
#         return f'{self.__username} {self.__password} {self.__email}'

# user1 = User('jannat', 'qwerty', 'jannat@gmail.com')
# print(user1.info)


# class Post:
#     posts = [{'id': 123}, {'title': 'hello'}, {'author': 'atai'}]

#     def __init__(self, title, author):
#         self.title = title
#         self.author = author
#         self.comments = []
#         self._add_to_posts()

#     



class RadioMixin:
    def play_music(self, title):
        self.title = title
        print(f'Песня называется butter')
        
class Auto(RadioMixin):
    pass

class Boat(RadioMixin):
    pass

class Amphibian(Auto, Boat, RadioMixin):
    pass

auto = Auto()
boat = Boat()
amphibian = Amphibian()
auto.play_music(title='butter')
boat.play_music(title='ptd')
amphibian.play_music(title='dna')