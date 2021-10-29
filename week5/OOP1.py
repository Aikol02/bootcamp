# # user registration

# class User:
#     platform = 'Makers'

#     def __init__(self, age, username, password):
#         self.username = username 
#         self.age = age
#         self.password = password 
#         self.followers = []

#     def follow(self, user):
#         user.followers.append(self.username)
    
#     def unfollow(self, user):
#         user.followers.remove(self.username)

#     def followers_count(self):
#         print(len(self.followers))
#         return len(self.followers)

#     def __str__(self):
#         return f'{self.username} {self.age}'
        
# user1 = User(username='jannat', 
#              age=22,
#              password='qwerty')
# user2 = User(username='atai',
#              age=18,
#              password='helloworld')
# user3 = User(username='ulan',
#              age=25,
#              password='python')

# user1.follow(user2)
# # print(user1)
# # print(user1.age, user1.username, user1.platform)
# # print(user2.age, user2.username, user2.platform)
# print('Atai`s followers: ',user2.followers)
# user2.follow(user1)
# user3.follow(user1)
# print('Jannat`s followers: ',user1.followers)

# user2.unfollow(user1)
# print('Jannat`s followers: ', user1.followers)

# user1.followers_count()
# user2.followers_count()
# user3.followers_count()



# football player


# class FootballPlayer:
#     status = 'sportsmen'

#     def __init__(self, name, last_name, team, salary):
#         self.name = name
#         self.last_name = last_name
#         self.team = team
#         self.salary = salary
#         self.goals = 0

#     def goal(self):
#         self.goals += 1
#         print('GOOOAAAAALL!!!!')

# player1 = FootballPlayer('Cristiano', 'Ronaldo', 'MU', 90000)
# player2 = FootballPlayer('lionel', 'Messi', 'PSG', 60000)

# import random
# players = [player1, player2]
# for _ in range(10):
#     random.choice(players).goal()

#     print(player1.status)
#     player1.status = 'proger'
#     print(player1.status)

# # print(player1.goals)
# print(player2.goals)
# print(player1.team)
# player1.team = 'Dordoi'
# print(player1.team)
# player1.salary = 100000
# print(player1.salary)
# print(player1.status)
# player1.goal()
# player2.goal()
# player1.goal()
# player2.goal()

# print(player1.goals)
# print(player2.goals)


