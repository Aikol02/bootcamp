

# 1



# string = 'Azamat in an amazing actor.'
# list_ = [
#     f'Eto bukva (letter)' + '$' if not letter.lower() == 'a' else '*$' 
#     for letter in string 
#     ]

# print(list_)

# print(''.join(list_))



# list_ = []
# for letter in string:
#     if letter.lower() == 'a':
#         list_.append('*')
#     else:
#         list_.append(letter)
# print(''.join(list_))


# 2

# users = {
#     'post1': ['Emil', 'Jannat', 'Sezim', 'Atai', 'Jannet', 'Bektur'],
#     'post2': ['Atai', 'Nurbek','Bektur', 'Emil'],
#     'post3': ['Jannat', 'Atai', 'Aikol', 'Aliya', 'Emil', 'Bektur']
# }
# # print(list(users.values()))
# list_users = [set(list_) for list_ in users.values()]
# # print(list_users)
# candidates = list_users[0]
# for set in list_users:
#     candidates &= set
#     # print(set)
# print(candidates.pop())

# print(list_users[0] & list_users[1] & list_users[-1])

# candidates = [
#     name.upper() + '!!!' for name in users['post3'] 
#     if name in users['post1'] and 
#     name in users['post2']
# ]

# import random
# winner = random.choice(list(candidates))
# print(winner)



# likes = {key: len(val) for key,val in users.items()}
# most_liked_post = None 
# most_likes = 0
# for post,like in likes.items():
#     if like >= most_likes:
#         most_likes = like
#         most_liked_post = post 
# print(likes)
# print(most_liked_post)

# a = set()
# a.add('Hello World!')
# print(a)

# a = set()
# b = set()
# a.update()
# print(a)

a = {1, 2}
a.pop()
print(a)
