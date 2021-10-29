# Employee

# class Employee:

#     stuff = []

#     def __init__(self, name, last_name):
#         self.name = name
#         self.last_name = last_name
#         self.id = self.generate_id()
#         Employee.stuff.append({
#             'id': self.id,
#             'name': self.name,
#             'last_name': self.last_name
#         })

#     def __str__(self) -> str:
#         return f'{self.name} {self.last_name}'

#     def generate_id(self):
#         import random
#         id_ = random.randint(500, 505)
#         for worker in Employee.stuff:
#             if worker.get('id') == id_: 
#                 return self.generate_id()
#         return id_

# class BonuxMixin:
#     def bonus(self, hours):
#         if hours > 200:
#             self.salary = self.salary + (self.salary * 5 / 100)
#         else:
#             self.salary = self.salary


# class SalaryEmployee(Employee):

#     def __init__(self, name, last_name, salary):
#         super().__init__(name, last_name)
#         self.salary = salary

# class HourlyEmployee(Employee):

#     def __init__(self, name, last_name, hours, per_hour):
#         super().__init__(name, last_name)
#         info = {
#             "id": self.id,
#             "name": self.name,
#             "last_name": self.last_name}
#         self.salary = hours * per_hour
#         self.bonus(hours)
#         for worker in Employee.stuff:
#             if info == worker:
#                 worker.update({"salary": self.salary})

# # john = Employee('John', 'Snow')
# # emily = Employee('Emily', 'Snow')
# jannat = SalaryEmployee('Jannat', 'Jannatov', 15000)
# aykol = HourlyEmployee('Aykol', 'Aykolev', 100, 150)
# print(jannat)
# print(Employee.stuff)








# class SmartPhones:
    
#     battery = 0
    
#     def __init__(self, name, color, memory, battery):
#                 self.name = name
#                 self.color = color
#                 self.memory = memory
#                 self.battery = battery
        
#     def __str__(self, charge):
#         self.battery > charge
        
# class Iphone(SmartPhones):
#     def __init__(self, name, color, memory, battery):
#         super().__init__(name, color, memory, battery)
