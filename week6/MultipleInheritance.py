# 1
# class IceCream:
#     def __init__(self, flavor):
#         self.flavor = flavor

#     @staticmethod
#     def melt():
#         print('I am melting...')

#     def change_flavor(self, new_flavor):
#         self.flavor = new_flavor

# class Cake:
#     def __init__(self, level:int):
#         self.level = level

#     def add_extra_level(self, k=1):
#         self.level += k

# class IceCreamCake(Cake, IceCream):
#     def __init__(self, flavor:str, level:int):
#         IceCream.__init__(self, flavor)
#         Cake.__init__(self, level)
#         self.layer = self.level = 1

#     def add_extra_level(self, k):
#         super().add_extra_level(k=k)
#         self.layer += k 

#     def melt(self):
#         super().melt()
#         self.layer -= 1

# obj1 = IceCreamCake('vanilla', 4)
# obj1.add_extra_level(3)
# print(obj1.level)
# print(obj1.layer)
# obj1.melt()
# obj1.melt()
# print(obj1.layer)
# obj1.change_flavor('chocolate')
# print(obj1.flavor)

# # cake1 = Cake(5)
# # print(cake1.level)
# # cake1.add_extra_level()
# # cake1.add_extra_level(4)
# # cake1.add_extra_level()
# # print(cake1.level)
        


# # ic1 = IceCream('chocolate')
# # print(ic1.flavor)
# # ic1.melt()
# # ic1.change_flavor('strawberry')
# # print(ic1.flavor)

        
# class Teacher:
#     def __init__(self, subject):
#         self.subject = subject
#         self.groups = []
#     @property
#     def groups_count(self):
#         return len(self.groups)

#     def add_group(self, group:str):
#         self.groups.append(group)
#         print(f'New {group} added')

# class DeveLoper:
#     def __init__(self, language):
#         self.language = language
#         self.projects = []

#     def add_project(self, new_project:str):
#         self.projects.append(new_project)
#         print(f'Got a new project {new_project}')

#     @property
#     def projects_count(self):
#         return len(self.projects)

# class Mentor(DeveLoper, Teacher):
#     def __init__(self, language):
#         super().__init__(language)
#         self.groups = []

# jannat = Mentor('Python')
# print(jannat.projects)
# print(jannat.groups)
# jannat.add_group('Python 14')
# jannat.add_group('Python Ev. 15')
# jannat.add_project('Makers Courses')
# jannat.add_project('Individual project')
# print(jannat.projects)
# print(jannat.groups)
# print(jannat.groups_count)
# print(jannat.projects_count)

# john = DeveLoper('Python')
# john.add_project('Online Shop')
# john.add_project('Tesla')
# john.add_project('Makers Courses')
# print(john.projects)
# print(john.projects_count)
        

# john = Teacher('Math')
# print(john.groups)
# john.add_group('Kuiruk Mai')
# john.add_group('11-A')
# print(john.groups_count)



# 3

# class GmailMixin:
#     def gmail_validate(self, email:str):
#         if email.endswith('@gmail.com'):
#             self.email = email
#             print(f'Account for {email} created!!!')
#         else:
#             print("it's not a gmail account!!!")

# class FaceBook(GmailMixin):
#     def __init__(self, email):
#         super().gmail_validate(email)

# class HackerRank(GmailMixin):
#     def __init__(self, email, username):
#         super().gmail_validate(email)
#         try:
#             self.email = email
#             self.username = username
#         except AttributeError:
#             print('Account not created!!!')

# user1 = FaceBook('kani@gmail.com')
# user2 = HackerRank('jannat@mail.ru', 'jannat')