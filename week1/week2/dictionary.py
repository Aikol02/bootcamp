# 1
# test = {
#     'Atai': 15,
#     'Bektur': 13,
#     'Jannat': 2,
#     'Kamila': 11,
#     'Ulan': 10
# }

# scores = test.values()
# print(sum(scores))

# 2

# users = {
#      'kani': 'kani@gmail.com',
#      'atai': 'elchacha@gmail.ru',
#      'jannat': 'jannat@gmail.com',
#      'bektur': 'beka@yandex.ru',
#      'nurba': 'nurba@gmail.com',
#      'ulan': 'ulik@gmail.ru',
#      'sezim': 'sezim@gmail.com'
# }
# user_emails = users.values()
# total = len(users)
# gmail_count = 0
# for email in user_emails:
#     if email.endswith('@gmail.com'):
#         gmail_count += 1

# # total - 100% 
# # gmail_count - x%
# print(f' Prosent polzovateley c gmail sostovlyaet {round(gmail_count * 100 / total, 2)}%')   


# 3
# person = {
#      "name": "Nurbolot",
#      "age": 35,
#      "Languages": ['Python', 'JavaScript'],
#      "children":[
#          {
#              "name": "Jannat",
#              'age': 10
#          },
#          {
#              "name": "Aselya",
#              "age": 5 
#          }
#      ]

# }
# person["Languages"].append('C++')
# # person.setdefault('salary', 4000)
# # person.update({'salary': 4000})
# person['wife'] = {
#     "name": 'Karen',
#     "age": 29
# }
# print(len(person['children']))

# print(person)



# 4
# TIME = "10:00:00"


# students = {
#     'Kanat': "09:20:34",
#     'Aliya': "09:50:50",
#     'Uluk': "14:00:00",
#     'Kair': "09:59:59",
#     'Emil': "10:00:01"
# }
# print(students.items())


# late_students = []
# for key,val in students.items():
#     if val > TIME:
#         late_students.append(key)
#     print(late_students)


# list1 = [1, 2, 3, 4, 5]
# list2 = [6, 8, 4, 5, 2]
# new_list = list1 + list2

# print(sum(new_list))


# list_ = [7, 4, 7]
# if list_[0]==list_[1] or list_[1]==list_[2] or list_[0] == list_[2]:
#     print('yes')
# else:
#     print('ERROR')