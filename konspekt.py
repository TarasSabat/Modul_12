''' Серіалізація об'єктів Python '''
''' Завжди, коли ви хочете зберегти інформацію для подальшого використання в зрозумілої машині (комп'ютеру) формі, ви робите серіалізацію. Найочевидніший приклад — це збереження даних у текстовий файл. Ви можете зберегти, наприклад, перелік витрат у текстовий файл:'''

# expenses = {
#     "hotel": 150,
#     "breakfast": 30,
#     "taxi": 15,
#     "lunch": 20
# }


# file_name = "expenses.txt"
# with open(file_name, "w") as fh:
#     for key, value in expenses.items():
        # fh.write(f"{key}|{value}\n")

'''Цей файл буде повністю читабельним і, якщо вам знадобиться потім завантажити цей перелік назад у Python, ви завжди зможете це зробити:'''

# file_name = "expenses.txt"
# expenses = {}
# with open(file_name, "r") as fh:
#     raw_expenses = fh.readlines()
#     for line in raw_expenses:
#         key, value = line.split("|")
#         expenses[key] = int(value)

'''У цьому примітивному прикладі ми серіалізували та десеріалізували словник expenses.'''

###############################

''' Серіалізація об'єктів Python за допомогою pickle '''
'''У пакета pickle є дві пари парних методів:
dumps запаковує в byte-рядок об'єкт, loads розпаковує з byte-рядок в об'єкт. Ці методи потрібні, коли ми хочемо контролювати, що робити з byte представленням, наприклад, відправити його мережею або прийняти з мережі.'''

# import pickle


# some_data = {
#     (1, 3.5): 'tuple',
#     2: [1, 2, 3],
#     'a': {'key': 'value'}
# }

# byte_string = pickle.dumps(some_data)
# unpacked = pickle.loads(byte_string)

# print(unpacked == some_data)    # True
# print(unpacked is some_data)    # False

'''У цьому прикладі упакований у byte_string словник some_data розпакований в unpacked та unpacked суворо дорівнює some_data, але це все ж таки не той самий об'єкт.
dump, load упаковує у відкритий для byte-запису файл та розпаковує із відкритого для byte-читання файлу.'''

# import pickle


# some_data = {
#     (1, 3.5): 'tuple',
#     2: [1, 2, 3],
#     'a': {'key': 'value'}
# }

# file_name = 'data.bin'

# with open(file_name, "wb") as fh:
#     pickle.dump(some_data, fh)


# with open(file_name, "rb") as fh:
#     unpacked = pickle.load(fh)


# print(unpacked == some_data)    # True
# print(unpacked is some_data)    # False

'''Результат аналогічний попередньому прикладу. Головна відмінність у тому, що під час виконання цього коду в робочій папці з'явився файл data.bin.
Ви можете зберігати об'єкти для подальшого використання, але з умовою. Самі класи та функції pickle зберігати не вміє і, якщо вам потрібно розпакувати упакований об'єкт класу, то сам клас повинен бути оголошений раніше у коді.'''

# import pickle


# class Human:
#     def __init__(self, name):
#         self.name = name


# bob = Human("Bob")
# encoded_bob = pickle.dumps(bob)

# decoded_bob = pickle.loads(encoded_bob)

# bob.name == decoded_bob.name    # True

'''Але, якби ви захотіли передати об'єкт bob мережею іншому комп'ютеру, який нічого не знає про клас Human, то ви отримаєте помилку. Якщо ж на обох кінцях каналу зв'язку оголошено клас Human, то такий обмін працюватиме.'''

#######################

''' Серіалізація об'єктів Python за допомогою json '''
'''Python підтримує JSON і в стандартному постачанні є пакет json, в якому є все необхідне для роботи з JSON.
dumps запаковує в byte-рядок об'єкт, loads розпаковує з byte-рядка в об'єкт. Ці методи потрібні, коли ми хочемо контролювати, що робити з byte представленням, наприклад, відправити його мережею або прийняти з мережі.'''

# import json


# some_data = {'key': 'value', 2: [1, 2, 3], 'tuple': (5, 6), 'a': {'key': 'value'}}

# byte_string = json.dumps(some_data)
# unpacked = json.loads(byte_string)

# unpacked is some_data    # False
# unpacked == some_data    # False

# unpacked['key'] == some_data['key']     # True
# unpacked['a'] == some_data['a']         # True
# unpacked['2'] == some_data[2]           # True
# unpacked['tuple'] == [5, 6]             # True

'''В цьому прикладі запакований в byte_string словник some_data розпакований в unpacked та unpacked не дорівнює some_data, але це все ж таки не той самий об'єкт.

Окрім того:
ключ 2 був неявно перетворений на '2';
кортеж (5, 6) — у список [5, 6]
dump, load упаковує у відкритий для byte-запису файл та розпаковує із відкритого для byte-читання файлу.'''

# import json


# some_data = {'key': 'value', 2: [1, 2, 3], 'tuple': (5, 6), 'a': {'key': 'value'}}
# file_name = 'data.json'

# with open(file_name, "w") as fh:
#     json.dump(some_data, fh)


# with open(file_name, "r") as fh:
#     unpacked = json.load(fh)


# unpacked is some_data    # False
# unpacked == some_data    # False

# unpacked['key'] == some_data['key']     # True
# unpacked['a'] == some_data['a']         # True
# unpacked['2'] == some_data[2]           # True
# unpacked['tuple'] == [5, 6]             # True

'''Результат аналогічний попередньому прикладу. Головна відмінність у тому, що під час виконання цього коду в робочій папці з'явився файл data.json.'''

############################

''' Робота з таблицями CSV у Python '''
'''Python підтримує роботу з табличними даними у форматі csv. Для цього у стандартному постачанні йде пакет csv.'''

# import csv


# with open('eggs.csv', 'w', newline='') as fh:
#     spam_writer = csv.writer(fh)
#     spam_writer.writerow(['Spam'] * 5 + ['Baked Beans'])
#     spam_writer.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])


# with open('eggs.csv', newline='') as fh:
#     spam_reader = csv.reader(fh)
#     for row in spam_reader:
#         print(', '.join(row))

'''В результаті виконання цього коду в робочій папці з'явився файл eggs.csv. Якщо відкриєте його табличним редактором, він відкриється як таблиця.
Є два допоміжні класи в пакеті csv, які виконують роботу з табличними даними трохи зручніше:'''
# import csv


# with open('names.csv', 'w', newline='') as fh:
#     field_names = ['first_name', 'last_name']
#     writer = csv.DictWriter(fh, fieldnames=field_names)
#     writer.writeheader()
#     writer.writerow({'first_name': 'Baked', 'last_name': 'Beans'})
#     writer.writerow({'first_name': 'Lovely', 'last_name': 'Spam'})
#     writer.writerow({'first_name': 'Wonderful', 'last_name': 'Spam'})


# with open('names.csv', newline='') as fh:
#     reader = csv.DictReader(fh)
#     for row in reader:
#         print(row['first_name'], row['last_name'])

'''Класи DictWriter та DictReader дозволяють працювати з рядками таблиці як зі словниками, де як ключі використовуються назви колонок (перший рядок).
Таким чином за допомогою Python можна генерувати табличні дані та імпортувати дані з таблиць.'''

##########################

''' Управління порядком серіалізації '''
'''Не всі об'єкти Python можна серіалізувати. Наприклад, не можна серіалізувати файловий дескриптор або системний ресурс. Але що робити, коли у вас є клас, об'єкт якого ви хочете запакувати, використовуючи pickle, але у нього є атрибути, що не серіалізуються? У такій ситуації ви можете скористатися магічними методами, які управляють серіалізацією та десеріалізацією за допомогою pickle.
Магічний метод __getstate__ викликається, коли pickle намагається отримати представлення об'єкта у вигляді byte-рядка. У звичайній реалізації __getstate__ повертає __dict__ словник, де зберігаються всі атрибути класу.
Але можyf змінити цей метод.'''

# import pickle


# class Reader:
#     def __init__(self, file):
#         self.file = file
#         self.fh = open(self.file)
#         self.position = 0

#     def close(self):
#         self.fh.close()

#     def read(self, size=1):
#         data = self.fh.read(size)
#         self.position = self.fh.tell()
#         return data

#     def __getstate__(self):
#         attributes = self.__dict__.copy()
#         attributes['fh'] = None
#         return attributes

'''У цьому прикладі клас Reader можна серіалізувати, помилки через неможливість упакувати файловий дескриптор не виникне.

Цей магічний метод отримує на вхід словник, розпакований з файлу або byte-рядка. Поведінка за замовчуванням — це записати отримане значення в self.__dict__. Доопрацюймо клас Reader так, щоб він міг після розпакування продовжити читання з того самого місця.'''

# import pickle


# class Reader:
#     def __init__(self, file):
#         self.file = file
#         self.fh = open(self.file)
#         self.position = 0

#     def close(self):
#         self.fh.close()

#     def read(self, size=1):
#         data = self.fh.read(size)
#         self.position = self.fh.tell()
#         return data

#     def __getstate__(self):
#         attributes = {**self.__dict__}
#         attributes['fh'] = None
#         return attributes

#     def __setstate__(self, value):
#         self.__dict__ = value
#         self.fh = open(value['file'])
#         self.fh.seek(value['position'])

######################

''' Створення копій об'єктів Python '''
'''Python намагається заощаджувати пам'ять і не копіювати дані з однієї області пам'яті в іншу. Натомість інтерпретатор створює нове посилання (ще один псевдонім) на існуючий об'єкт, замість копіювання вмісту. Така поведінка може бути небажаною, наприклад:'''

# my_list = [1, 2, 3]
# copy_list = my_list
# copy_list.append(4)
# print(my_list)  # [1, 2, 3, 4]

'''Виходить, що copy_list — це просто ще одне ім'я для того самого списку my_list і, змінюючи copy_list, ми змінюємо й my_list. Це неочевидно і може збивати з пантелику.'''

'''Така поведінка може призводити до помилок, коли справа стосується типів, словників, списків, класів користувача, що змінюються. Для списків та словників можна скористатися явним копіюванням:'''

# my_list = [1, 2, 3]
# copy_list = my_list[:]
# copy_list.append(4)
# print(my_list)  # [1, 2, 3]

# d = {1: 'a'}
# d_copy = {**d}
# d_copy[2] = 'b'
# print(d)        # {1: 'a'}

'''Але з типами користувача так не зробиш. Щоб вирішити цю проблему, у Python є механізм копіювання — це функції із пакету copy.'''

'''Щоб створити "поверхневу" копію об'єкта, у пакеті copy є функція copy. Ця функція створює новий об'єкт такого самого типу і потім створює посилання на увесь вміст старого об'єкта в новий. Такий механізм досить хороший для роботи з об'єктами, де вже на першому рівні вкладеності немає змінних об'єктів, і він працює досить швидко.'''

'''Але для об'єктів із глибокою вкладеністю така функція все ж таки не дасть потрібного ефекту:'''

# import copy


# my_list = [1, 2, {1: 'a'}]
# copy_list = copy.copy(my_list)
# copy_list.append(4)
# print(my_list)      # [1, 2, {1: 'a'}]
# print(copy_list)    # [1, 2, {1: 'a'}, 4]

# copy_list[2][2] = 'b'
# print(my_list)    # [1, 2, {1: 'a', 2: 'b'}]

'''З цього прикладу видно, що хоча copy_list вже є новим об'єктом (не посилання на my_list), але вкладений у нього словник з індексом 2 — це один і той самий словник і в copy_list, і в my_list.

Для ситуацій, коли нам потрібно, щоб на будь-якому рівні вкладеності створювалися нові об'єкти, а не посилання на існуючі, у пакеті copy є функція deepcopy. Ця функція рекурсивно створює нові об'єкти.'''

# import copy


# my_list = [1, 2, {1: 'a'}]
# copy_list = copy.deepcopy(my_list)
# copy_list.append(4)
# print(my_list)      # [1, 2, {1: 'a'}]
# print(copy_list)    # [1, 2, {1: 'a'}, 4]

# copy_list[2][2] = 'b'
# print(my_list)    # [1, 2, {1: 'a'}]

'''Ще одна проблема вирішується за допомогою пакету copy — це копіювання об'єктів користувача. Щоб створити об'єкт, який буде коректно оброблятися функціями copy та deepcopy, ваш клас повинен реалізувати два магічних методи: __copy__ та __deepcopy__ для поверхневого та глибокого копіювання відповідно.'''

# from copy import deepcopy, copy


# class Expenses:
#     def __init__(self):
#         self.data = {}
#         self.places = []

#     def spent(self, place, value):
#         self.data[str(place)] = value
#         self.places.append(place)

#     def __copy__(self):
#         copy_obj = Expenses()
#         copy_obj.data = self.data
#         copy_obj.places = self.places
#         return copy_obj

#     def __deepcopy__(self, memo):
#         copy_obj = Expenses()
#         memo[id(self)] = copy_obj
#         copy_obj.data = deepcopy(self.data, memo)
#         copy_obj.places = deepcopy(self.places, memo)
#         return copy_obj


# e = Expenses()
# e.spent('hotel', 100)
# e.spent('taxi', 10)
# print(e.places)             # ['hotel', 'taxi']

# e_copy = copy(e)
# print(e_copy is e)          # False
# e_copy.spent('bar', 30)
# print(e.places)             # ['hotel', 'taxi', 'bar']

# e_deep_copy = deepcopy(e)
# print(e_deep_copy is e)     # False
# e_deep_copy.spent(
#     'airport',
#     300
# )
# print(e.places)             # ['hotel', 'taxi', 'bar']
# print(e_deep_copy.places)   # ['hotel', 'taxi', 'bar', 'airport']

'''Використовуючи методи __copy__ та __deepcopy__, ви можете керувати як саме буде створюватися копія вашого об'єкта. Метод __deepcopy__ обов'язково повинен приймати один аргумент — словник, в який записуються усі об'єкти, які піддаються копіюванню. 
Це потрібно, щоб уникнути нескінченної рекурсії, якщо якийсь об'єкт є спільним для кількох копійованих. У такому випадку алгоритм глибокого копіювання може зайти в нескінченний цикл, копіюючи поперемінно об'єкти із посиланнями один на одного. 
Словник memo зберігає як ключі id об'єктів і самі об'єкти як значення. Коли перевизначаємо як повинно відбуватися копіювання, ми можемо і не використовувати memo, якщо точно знаємо, що рекурсії не виникне.'''


