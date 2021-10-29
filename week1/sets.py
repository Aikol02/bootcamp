#  1
# monday = {'Math', 'Literature', 'Physics'}
# tuesday = {'Russian', 'Biology', 'Chemistry'}
# wednesday = {'PE', 'Biology', 'History'}
# thursday = {'Russian', 'Music', 'Math'}
# friday = {'Economics', 'Chemistry', 'CS', 'Math'}

# study_week = (monday, tuesday, wednesday, thursday, friday)

# a
# for day in study_week:
#     # print(day)
#     for subject in day:
#         if subject == 'Chemistry':
#             day.remove('Chemistry')
#             day.add('Politics')
# print(study_week)
# for day in study_week:
#     day.discard('Chemistry')
#     day.add('Politics')
# print(study_week)


#  b
                    # 4
# for i in range(len(study_week) - 1):

#     # print(study_week[i])
#     # print(study_week[i + 1])
    
#     if study_week[i] & study_week[i + 1]:
#         # print(*(study_week[i] & study_week[i + 1]))
#         study_week[i + 1].remove(*(study_week[i] & study_week[i + 1]))
#         study_week[i + 1].add('Politics')

# print(study_week)

    #     print(subject)
    # print('----------')





# set1 = {20, 78, 33}
# set2 = {90, 20, 40}
# set3 = {33, 90, 100}

# print(set1 - set2 - set3)

# import random

# # print(dir(random))

# print(random.choice(['Atai', 'Nurbek', 'Eldiyar','Jannet']))

# print(random.randrange(50, 10000))

# print(random.choices(['Atai', 'Nurbek', 'Eldiyar','Jannet'], k=2))

# # print(random.sample(['Atai', 'Nurbek', 'Eldiyar','Jannet'], k=2))


 