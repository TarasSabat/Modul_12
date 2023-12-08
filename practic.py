''' Серіалізація об'єктів Python за допомогою pickle '''
# import pickle

# d = {"data": 12345}
# with open('lesson.bin', 'wb') as file:
#     pickle.dump(d, file)                  # запис серіалізованого обєкту у файл. Файл буде бінарним

# d_bytes = pickle.dumps(d)                 # повертає серіалізований обєкт. Його можна використовувати
# print(d_bytes)

# with open('lesson.bin', 'rb') as file:
#     d_load = pickle.load(file)            # зчитуємо і десералізуємо обєкт
# print(d_load)

# d_loads = pickle.loads(d_bytes)           # повертає серіалізований обєкт. Його можна використовувати
# print(d_loads)


# dump i load - використовуємо при роботі з файлами
# dumps i loads - використовуємо при передачі по мережі

###

# import pickle
# FILENAME = "users.dat"
# users = [
#     ["Tom", 28, True],
#     ["Alice", 23, False],
#     ["Bob", 34, False]
# ]
# with open(FILENAME, "wb") as file:
#     pickle.dump(users, file)

# with open(FILENAME, "rb") as file_1:
#     users_from_file = pickle.load(file_1)
#     for user in users_from_file:
#         print('Name: ', user[0], "\tAge: ", user[1])

###

''' Серіалізація класів '''
# from pickle import loads, dumps

# class A:
#     x = 'text'

#     def __init__(self):
#         print('class A')
#         self.y = 'нова змінна'

# a = A()
# s_instance = dumps(a)    # серіалізація екземпляру класу
# s_class = dumps(A)       # серіалізація класу

# restored_a = loads(s_instance)  # десеріалізація екземпляру класу
# restored_A = loads(s_class)     # десеріалізація класу

# print(a.x, a.y)
# print(restored_a.x, restored_a.y)
# print(a == restored_a)  # False
# print(A == restored_A)  # True

# print(id(a))
# print(id(restored_a))

# print(id(A))
# print(id(restored_A))

#########################

''' Серіалізація об'єктів Python за допомогою json '''

# import json

# d = {'a': 1}
# l = [1, 3.3]
# t = (3, 4)
# s = 'Hello world!'
# b = False
# st = {1, 2, "Test"}
# n = None
# int = 5
# obj = {"tuple": t, "list": l, 'bool': b, 'str': s, 'none': n, 'int': int}
# print(json.dumps(obj))
# print(json.dumps(d))
# print(json.dumps(l))
# print(json.dumps(t))
# print(json.dumps(s))
# print(json.dumps(b))
# print(json.dumps(st))

# with open('storage.json', 'w') as f:
#     json.dump(obj, f)

### зчитування десеріалізація

# import json

# with open('storage.json', 'r') as f:
#     store = json.load(f)
# print(store)

''' Работа с кирилицею '''
# import json

# data = {
#     'dev': {
#         'name': 'Володимир',
#         'test': 'програміст'
#     }
# }

# with open('test.json', 'w', encoding='utf-8') as f:  # серіалізація
#     json.dump(data, f, ensure_ascii=False)           # без кодування (бачимо кирилицю)
#     # json.dump(data, f)

# with open('test.json', 'r', encoding='utf-8') as f:   # десеріалізація
#     restore_data = json.load(f)
#     print(restore_data)

''' Робота з таблицями CSV у Python '''
# import csv

# with open('names.csv', 'w', newline='\n') as csvfile:  # newline = '\n', краще при роботі з csv файлами
#     fieldnames = ['first_name', 'last_name', 'test', 'bool', 'adrress', 'age']  # навза стовпчиків
#     # записуємо заголовок
#     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#     writer.writeheader()
#     # записуємо рядки
#     writer.writerow({'first_name': '\tTony', 'last_name': 'Stark', 'age': 35})
#     writer.writerow({'first_name': 'Bob', 'last_name': 'Smith', 'age': 15})
#     writer.writerow({'first_name': 'Alexsa', 'last_name': 'Smith', 'age': 45, 'bool': True})

######

# import csv

# FILENAME = 'users.csv'
# users = [
#     {'name': 'Микола', 'age': 22, 'sex': 'male'},
#     {'name': 'Марія', 'age': 25, 'sex': 'female'},
#     {'name': 'Ігор', 'age': 45, 'sex': 'male'},
# ]

# with open(FILENAME, 'w', newline='', encoding='utf-8') as file:
#     columns = ['name', 'age', 'sex']
#     writer = csv.DictWriter(file, delimiter=',', fieldnames=columns)
#     writer.writeheader()

#     for row in users:
#         writer.writerow(row)

# with open(FILENAME, 'r', newline='', encoding='utf-8') as file:
#     reader = csv.DictReader(file)
#     for row in reader:
#         print(row['name'], row.get('age'))

#####

# c_codes = {}
# # {код країни: назва країни}
# import csv
# name = 'countries.csv'
# with open(name, 'r') as file:
#     reader = csv.reader(file)
#     for line in reader:
#         c_codes[line[0]] = line[1]
#     c_codes.pop('Code')
# print(c_codes.get('UA'))
# print(c_codes)

###

# Зберегти у файлі таблицю квадратів та кубів цілих чисел від 1 до 20
# name = 'table.csv'
# import csv

# with open(name, 'w') as file:
#     writer = csv.writer(file)
#     for item in range(1, 100):
#         writer.writerow([item, item ** 2, item ** 3])

# with open(name, 'r') as file:
#     reader = csv.reader(file)
#     res = []
#     for line in reader:
#         res.append(line)
# print(res)

''' YAML '''
'''YAML — зручний для читання людиною формат серіалізації даних, концептуально близький до мов розмітки, але орієнтований на зручність введення-виведення типових структур даних багатьох мов програмування.'''

# import yaml
# # pip install PyYAML

# users = [
#     {'name': 'Микола', 'age': 32, 'gender': 'male'},
#     {'name': 'Марія', 'age': 44, 'gender': 'female'},
#     {'name': 'Ігор', 'age': 55, 'gender': 'male'},
# ]
# serialize = yaml.dump(users)
# result = yaml.load(serialize, Loader=yaml.FullLoader)
# print(result)

# with open('test.yaml', 'w', encoding='utf-8') as f:
#     yaml.dump({"users": users}, f, allow_unicode=True)

''' __getstate__ та __setstate__ '''
''' Магічні методи в яких ми зазначаємо що потрібно серіалізувати а що ні '''
# import pickle
# from time import sleep


# class A:
#     def __init__(self, value):
#         self.value = value
#         self.data = lambda: 5  # cannot be pickled
#         self.is_valid = False  # don't want to pickled
#         self.text = 'hfdgfhdghdgfhgdhfgdhfd'

#     def __getstate__(self):
#         return [self.value, self.text]

#     def __setstate__(self, state):
#         self.value = state[0]
#         self.data = lambda: 5
#         self.is_valid = False
#         self.text = state[1]


# a = A('Hello world!')

# s = pickle.dumps(a)

# a_deserialize = pickle.loads(s)
# print(a_deserialize)
# print(a_deserialize.value)
# print(a_deserialize.data())
# print(a_deserialize.is_valid)
# print(a_deserialize.text)

#####

# import pickle
# from time import sleep
# from datetime import datetime


# class Test:
#     def __init__(self, *args):
#         self.data = list(args)
#         self.saved = None
#         self.restored = None

#     def __getstate__(self):
#         state = self.__dict__.copy()  # self.__dict__ - тут зберігаються всі властивості класу (поля...)
#         state['saved'] = datetime.now()
#         return state

#     def __setstate__(self, state):
#         self.__dict__.update(state)  # все що було в self.__dict__ замінити на якийсь state
#         self.restored = datetime.now()


# if __name__ == "__main__":
#     # ==============================
#     test = Test(1, 2, 3, 4, 5)
#     print(test.data)

#     # ==============================
#     test_dump = pickle.dumps(test)
#     sleep(3)
#     test_load = pickle.loads(test_dump)
#     print(test.saved, test.restored)
#     print(test_load.saved, test_load.restored)

#####

# Друк та нумерація рядків у текстовому файлі.

# import pickle

# class TextReader:
#     def __init__(self, filename):
#         self.filename = filename
#         self.file = open(self.filename, encoding='utf-8')
#         self.line_count = 0

#     def readline(self):
#         self.line_count += 1
#         line = self.file.readline()
#         if not line:
#             return None
#         if line.endswith('\n'):
#             line = line[:-1]  # позбуваємось \n
#         return f"{self.line_count}: {line}"

#     def __getstate__(self):
#         state = self.__dict__.copy()  # self.__dict__ - тут зберігаються всі властивості класу (поля...)
#         del state['file']  # Fix for: TypeError: cannot serialize '_io.TextIOWrapper' object
#         return state

#     def __setstate__(self, state):
#         self.__dict__.update(state)
#         file = open(self.filename, encoding='utf-8')
#         for _ in range(self.line_count):  # пропускаємо раніше прочитані строки з файлу
#             file.readline()
#         self.file = file  # зберігаємо файл


# if __name__ == "__main__":
#     reader = TextReader('text.txt')
#     print(reader.readline())  # 1
#     print(reader.readline())  # 2
#     print(reader.readline())  # 3
#     new_reader = pickle.loads(pickle.dumps(reader))  # повинен запамятати коли він був серіалізований
#     # і продовжити друкувати текст з того самого місця
#     while True:
#         line = new_reader.readline()
#         if line is None:
#             break
#         else:
#             print(line)

#     print('-' * 5)
#     print(reader.readline())

''' Створення копій об'єктів Python '''
'''Інтерпретатор Python лінивий і якщо його явно не попросити створити копію об'єкта,
він створить новий показник на той же об'єкт. Не завжди така поведінка вітається.
Для створення копії об'єкта у пакеті copy є функції:
- copy - поверхнева копія
- Deepcopy - глибока копія.'''

# from copy import copy, deepcopy

# l = [1, 2, 3, ['a', 'b', 'c']]
# test_l = l[:]
# l_copy = copy(l)
# l_deep = deepcopy(l)
# print(l == test_l)
# print(l == l_copy, l == l_deep)

# l[0] = 9
# print(l, test_l, l_copy, l_deep)
# l[3][0] = 'Hello'
# print(l, test_l, l_copy, l_deep)

#####

'''Під капотом функції copy, deepcopy роблять нічого більше,
ніж викликають методи __copy__, __deepcopy__.'''
# from collections import UserList
# from copy import copy, deepcopy

# class CopyList(UserList):
#     def __init__(self, *args):
#         super().__init__()
#         self.data = list(args)

#     def __copy__(self):
#         n = CopyList()
#         n.data = self.data
#         return n

#     def __deepcopy__(self, memodict={}):
#         n = CopyList()
#         memodict[id(self)] = n  # {"140640986278160": [1, 2, 3, 4]}
#         print(memodict)
#         for element in self.data:
#             n.append(deepcopy(element, memodict))
#         return n


# data = CopyList([1, 2, 3, 4])
# data_copy = copy(data)
# data_deep = deepcopy(data)

# print(id(data), data)
# print(id(data_copy), data_copy)
# print(id(data_deep), data_deep)

# print(id(data[0]), data[0])
# print(id(data_copy[0]), data_copy[0])
# print(id(data_deep[0]), data_deep[0])

#####

# import shelve  # сховище файлів, https://ru.wikipedia.org/wiki/DBM
# shelve - дає можливість створювати базу даних у файлі.

#####

# from typing import List
# import json

# class Student:
#     def __init__(self, first_name, last_name):
#         self.first_name = first_name
#         self.last_name = last_name

# class Team:
#     def __init__(self, students: List[Student]):
#         self.students = students

#     # def serialize(self):
#     #     json_str = json.dumps(self, default=lambda o: o.__dict__)
#     #     return json.loads(json_str)
#     #
#     # @classmethod
#     # def deserialize(cls, data):
#     #     return cls(**data)


# student1 = Student('Tony', 'Stark')
# student2 = Student('John', 'Smith')
# team = Team([student1, student2])
# print(team.__dict__)

# json_data = json.dumps(team, default=lambda o: o.__dict__)

# print(json_data)

# decode = Team(**json.loads(json_data))
# print(decode.students)

''' Використання пакету Faker (рандомні вмена, телефони, емейли ...) '''
# from faker import Faker

# fake = Faker()
# users = []


# def create_usere(fake, users: list, n=10):
#     for _ in range(n):
#         user = {}
#         user['name'] = fake.name()
#         user['phone_numder'] = fake.phone_number()
#         user['email'] = fake.email()
#         user['address'] = fake.address()
#         user['birthday'] = fake.date()
#         users.append(user)
#         print(user)


# if __name__ == '__main__':
#     create_usere(fake, users, n=12)

##### (українські дані - кирилиця не спрацювала)
# from faker import Faker, Factory
# import json

# fake = Factory.create('uk_UA')
# users = []


# def create_usere(fake, users: list, n=10):
#     for _ in range(n):
#         user = {}
#         user['name'] = fake.name()
#         user['phone_numder'] = fake.phone_number()
#         user['email'] = fake.email()
#         user['address'] = fake.address()
#         user['birthday'] = fake.date()
#         users.append(user)
#     to_json(users)
        
# def to_json(users):
#     with open('users.json', 'w', encoding='utf-8') as file:
#         json.dump(users, file, indent = 4, ensure_ascii = False)
#         print('Users were saved.')


# if __name__ == '__main__':
#     create_usere(fake, users, n=12)  

### (запис даних у таблицю)

# from csv import DictWriter 
# import json

# file_json = 'users.json' 
# file_csv = 'users.csv'

# def get_users():	
#     with open(file_json) as reader: 
#         users = json.load(reader) 
#         return users

# def write_table():
#     users = get_users()
#     with open(file_csv, 'w', newline='') as file:
#         fieldsnames = users[0].keys()
#         writer = DictWriter(file, delimiter = ';', fieldnames=fieldsnames)
#         writer.writeheader() 
#         for row in users:
#             writer.writerow(rowdict=row) 
#             print('CSV table was created.')

# if __name__ == '__main__':	
#     write_table()