
# with open('platform.txt', 'w+') as f:
#     while True:
#         email = input('Enter your email: ')
#         if not email:
#             print('STUDENT ADDED')
#             break
#         f.write(email + '\n')




# with open('platform.txt') as f:
#     student = input('Enter your email: ')
#     students = f.read()
#     if student in students:
#         print('You have an acces')
#     else:
#         print('--')    



# with open('kpi.txt') as f:
#     # print(f.readlines())
#     data = list(map(lambda x : x.replace('\n', ''), f.readlines()))
#     # print(data)
#     data = [name.split() for name in data]
#     # print(data)
#     max_point = 0
#     max_voice = 0
#     for list in data:
#         if int(list[1]) > max_point:
#             max_point = int(list[1])
#             best_student = list[0]
#         if int(list[-1]) > max_voice:
#             max_voice = int(list[-1])
#             fire_student = list[0]
# print(best_student, max_point)
# print(fire_student, max_voice)

# with open('contacts.txt') as f:
#     contacts = f.readlines()
#     # print(contacts)
#     contacts = [contact.split() for contact in contacts]
#     # print(contacts)
#     contacts = {contact[0]: contact[1] for contact in contacts}
#     name = input('Enter name: ').lower().title()
#     # print(name)
#     print(contacts.get(name, 'No such name in contact book'))



# from datetime import datetime
# with open('qrcode.txt', 'a') as f:
#     name = input('Enter name: ')
#     f.write(f'{name} {datetime.now().strftime("%H:%M:%S %d-%B-%Y")}\n')



seconds_in_minutes = 60
minutes_in_hours = 60
seconds_in_hour = seconds_in_minutes * minutes_in_hours 
hours_in_day = 24 
seconds_in_day = hours_in_day * seconds_in_hour 
days_in_year = 365 
seconds_in_year = seconds_in_day * days_in_year
print(seconds_in_year)
