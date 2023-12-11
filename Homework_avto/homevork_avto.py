'''№1
Є список, кожен елемент якого є словником з контактами користувача наступного виду:
    {
    "name": "Allen Raymond",
    "email": "nulla.ante@vestibul.co.uk",
    "phone": "(992) 914-3792",
    "favorite": False,
}
Словник містить ім'я користувача name, його email, телефонний номер phone та властивість favorite - обраний контакт чи ні.
Розробіть дві функції для серіалізації та десеріалізації списку контактів за допомогою пакета pickle та зберігання отриманих даних у бінарному файлі.
Перша функція write_contacts_to_file приймає два параметри: filename - ім'я файлу, contacts - список контактів. Вона зберігає вказаний список у файл, використовуючи метод dump пакету pickle.
Друга функція read_contacts_from_file читає та повертає зазначений список contacts з файлу filename, використовуючи метод load пакету pickle.
'''
# import pickle

# def write_contacts_to_file(filename, contacts):
#     with open(filename, 'wb') as fh:
#         pickle.dump(contacts, fh)
       
# def read_contacts_from_file(filename):
#     with open(filename, 'rb') as fh:
#         unpacked = pickle.load(fh)
#         return unpacked
    
'''№2
Є список, кожен елемент якого є словником з контактами користувача наступного виду:
{
    "name": "Allen Raymond",
    "email": "nulla.ante@vestibul.co.uk",
    "phone": "(992) 914-3792",
    "favorite": False,
}
Словник містить ім'я користувача name, його email, телефонний номер phone та властивість favorite - обраний контакт чи ні.
Розробіть дві функції для серіалізації та десеріалізації списку контактів за допомогою пакету json та зберігання отриманих даних у текстовому файлі.
Перша функція write_contacts_to_file приймає два параметри: filename - ім'я файлу, contacts - список контактів. Вона зберігає вказаний список у файл, використовуючи метод dump пакету json.
Структура json файлу має бути такою:
{
  "contacts": [
    {
      "name": "Allen Raymond",
      "email": "nulla.ante@vestibul.co.uk",
      "phone": "(992) 914-3792",
      "favorite": false
    },
    ...
  ]
}
Тобто список контактів повинен зберігатися за ключем "contacts", а не просто зберегти список у файл.
Друга функція read_contacts_from_file читає та повертає зазначений список contacts з файлу filename, збереженого раніше функцією write_contacts_to_file, використовуючи метод load пакету json.
'''
# import json

# def write_contacts_to_file(filename, contacts):
#     data = {'contacts': contacts}
#     with open(filename, 'w') as fh:
#         json.dump(data, fh, indent = 2)
        
# def read_contacts_from_file(filename):
#     with open(filename, 'r') as fh:
#         unpacked = json.load(fh)
#         return unpacked.get('contacts', [])
    
'''№3
Є список, кожен елемент якого є словником з контактами користувача наступного виду:

    {
    "name": "Allen Raymond",
    "email": "nulla.ante@vestibul.co.uk",
    "phone": "(992) 914-3792",
    "favorite": False,
}
Словник містить ім'я користувача name, його email, телефонний номер phone та властивість favorite - обраний контакт чи ні.
Розробіть дві функції для серіалізації та десеріалізації списку контактів за допомогою пакету csv та зберігання отриманих даних у текстовому файлі.
Перша функція write_contacts_to_file приймає два параметри: filename - ім'я файлу, contacts - список контактів. Вона зберігає вказаний список у файлі формату csv.
Структура csv файлу має бути такою:
name,email,phone,favorite
Allen Raymond,nulla.ante@vestibul.co.uk,(992) 914-3792,False
Chaim Lewis,dui.in@egetlacus.ca,(294) 840-6685,False
Kennedy Lane,mattis.Cras@nonenimMauris.net,(542) 451-7038,True
Wylie Pope,est@utquamvel.net,(692) 802-2949,False
Cyrus Jackson,nibh@semsempererat.com,(501) 472-5218,True
Зверніть увагу, першим рядком у файлі йдуть заголовки – це назви ключів.
Друга функція read_contacts_from_file читає, виконує перетворення даних та повертає вказаний список contacts із файлу filename, збереженого раніше функцією write_contacts_to_file.
Примітка: При читанні файлу csv ми отримуємо властивість словника favorite у вигляді рядка, тобто. наприклад favorite='False' . Необхідно його привести до логічного виразу назад, щоб стало favorite=False.
'''
# import csv


# def write_contacts_to_file(filename, contacts):
#   with open(filename, 'w', newline='\n') as csvfile:
#     fieldnames = ['name', 'email', 'phone', 'favorite']
#     writer = csv.DictWriter(csvfile, delimiter=',', fieldnames=fieldnames)
#     writer.writeheader()
    
#     for row in contacts:
#       writer.writerow(row)
      
# def read_contacts_from_file(filename):      
#   contacts = []
#   with open(filename, 'r') as file:
#     reader = csv.DictReader(file)
    
#     for row in reader:
#       row['favorite'] = row['favorite'].lower() == 'true'
#       contacts.append(row)
#   return contacts

# contacts = [
#     {"name": "Allen Raymond", "email": "nulla.ante@vestibul.co.uk", "phone": "(992) 914-3792", "favorite": False},
#     {"name": "Chaim Lewis", "email": "dui.in@egetlacus.ca", "phone": "(294) 840-6685", "favorite": False},
#     {"name": "Kennedy Lane", "email": "mattis.Cras@nonenimMauris.net", "phone": "(542) 451-7038", "favorite": True},
#     {"name": "Wylie Pope", "email": "est@utquamvel.net", "phone": "(692) 802-2949", "favorite": False},
#     {"name": "Cyrus Jackson", "email": "nibh@semsempererat.com", "phone": "(501) 472-5218", "favorite": True}
# ]

# write_contacts_to_file('user_list.csv', contacts)

# read_contacts = read_contacts_from_file('user_list.csv')

# print(read_contacts)

'''№4
Розробіть клас Person. Він має чотири властивості: ім'я користувача name, його email, телефонний номер phone та властивість favorite - обраний контакт чи ні.
Приклад створення екземпляра класу:
    Person(
    "Allen Raymond",
    "nulla.ante@vestibul.co.uk",
    "(992) 914-3792",
    False,
)
Розробіть клас Contacts. Він повинен ініціалізувати через конструктор дві властивості: filename - ім'я файлу для пакування об'єкта класу Contacts, contacts - список контактів, екземплярів класу Person.
Приклад створення екземпляра класу:
contacts = [
    Person(
        "Allen Raymond",
        "nulla.ante@vestibul.co.uk",
        "(992) 914-3792",
        False,
    ),
    Person(
        "Chaim Lewis",
        "dui.in@egetlacus.ca",
        "(294) 840-6685",
        False,
    ),
]
persons = Contacts("user_class.dat", contacts)
Розробіть два методи для серіалізації та десеріалізації екземпляра класу Contacts за допомогою пакету pickle та зберігання даних у бінарному файлі.
Перший метод save_to_file зберігає екземпляр класу Contacts у файл, використовуючи метод dump пакету pickle. Ім'я файлу зберігається в атрибуті filename.
Другий метод read_from_file читає та повертає екземпляр класу Contacts з файлу filename, використовуючи метод load пакету pickle.
Приклад роботи:
persons = Contacts("user_class.dat", contacts)
persons.save_to_file()
person_from_file = persons.read_from_file()
print(persons == person_from_file)  # False
print(persons.contacts[0] == person_from_file.contacts[0])  # False
print(persons.contacts[0].name == person_from_file.contacts[0].name)  # True
print(persons.contacts[0].email == person_from_file.contacts[0].email)  # True
print(persons.contacts[0].phone == person_from_file.contacts[0].phone)  # True
'''
# import pickle

# class Person:
#     def __init__(self, name: str, email: str, phone: str, favorite: bool):
#         self.name = name
#         self.email = email
#         self.phone = phone
#         self.favorite = favorite

#     def __eq__(self, other):
#         return (
#             self.name == other.name and
#             self.email == other.email and
#             self.phone == other.phone and
#             self.favorite == other.favorite
#         )

# class Contacts:
#     def __init__(self, filename: str, contacts: list[Person] = None):
#         self.filename = filename
#         self.contacts = contacts if contacts else []

#     def save_to_file(self):
#         with open(self.filename, 'wb') as file:
#             pickle.dump(self, file)

#     def read_from_file(self):
#         with open(self.filename, 'rb') as file:
#             return pickle.load(file)
           

# contacts = [
#     Person("Allen Raymond", "nulla.ante@vestibul.co.uk", "(992) 914-3792", False),
#     Person("Chaim Lewis", "dui.in@egetlacus.ca", "(294) 840-6685", False)]

# persons = Contacts("user_class.dat", contacts)
# persons.save_to_file()
# person_from_file = persons.read_from_file()
# print(persons == person_from_file)  # False
# print(persons.contacts[0] == person_from_file.contacts[0])  # False
# print(persons.contacts[0].name == person_from_file.contacts[0].name)  # True
# print(persons.contacts[0].email == person_from_file.contacts[0].email)  # True
# print(persons.contacts[0].phone == person_from_file.contacts[0].phone)  # True

'''№5
Ми продовжимо розширювати приклад попереднього завдання. Додайте до класу Contacts атрибут count_save, за замовчуванням він повинен мати значення 0. Реалізуйте магічний метод __getstate__ для класу Contacts. При упаковуванні екземпляра метод класу повинен збільшувати значення атрибута count_save на одиницю. Таким чином, ця властивість - лічильник повторних операцій пакування екземпляра класу
Приклад роботи коду:

persons = Contacts("user_class.dat", contacts)
persons.save_to_file()
first = persons.read_from_file()
first.save_to_file()
second = first.read_from_file()
second.save_to_file()
third = second.read_from_file()

print(persons.count_save)  # 0
print(first.count_save)  # 1
print(second.count_save)  # 2
print(third.count_save)  # 3
'''
# import pickle


# class Person:
#   def __init__(self, name: str, email: str, phone: str, favorite: bool):
#     self.name = name
#     self.email = email
#     self.phone = phone
#     self.favorite = favorite


# class Contacts:
#   def __init__(self, filename: str, contacts: list[Person] = None):
#     if contacts is None:
#       contacts = []
#     self.filename = filename
#     self.contacts = contacts
#     self.count_save = 0
        

#   def save_to_file(self):
#     with open(self.filename, "wb") as file:
#       pickle.dump(self, file)

#   def read_from_file(self):
#     with open(self.filename, "rb") as file:
#       content = pickle.load(file)
#     return content

#   def __getstate__(self):
#     attributes = self.__dict__.copy()
#     attributes["count_save"] = attributes["count_save"] + 1
#     return attributes

# contacts = [
#     Person("Allen Raymond", "nulla.ante@vestibul.co.uk", "(992) 914-3792", False),
#     Person("Chaim Lewis", "dui.in@egetlacus.ca", "(294) 840-6685", False)]


# persons = Contacts("user_class.dat", contacts)
# persons.save_to_file()
# first = persons.read_from_file()
# first.save_to_file()
# second = first.read_from_file()
# second.save_to_file()
# third = second.read_from_file()

# print(persons.count_save)  # 0
# print(first.count_save)  # 1
# print(second.count_save)  # 2
# print(third.count_save)  # 3

'''№6
Продовжуємо розширювати приклад із попереднього завдання. Додайте до класу Contacts атрибут is_unpacking, за замовчуванням він повинен мати значення False. Реалізуйте магічний метод __setstate__ для класу Contacts. При розпаковуванні екземпляра класу метод повинен змінювати значення атрибута is_unpacking на значення True. Таким чином, ця властивість визначатиме, що екземпляр класу отримано внаслідок розпакування.
Приклад роботи коду:
persons = Contacts("user_class.dat", contacts)
persons.save_to_file()
person_from_file = persons.read_from_file()
print(persons.is_unpacking)  # False
print(person_from_file.is_unpacking)  # True
'''
# import pickle


# class Person:
#     def __init__(self, name: str, email: str, phone: str, favorite: bool):
#         self.name = name
#         self.email = email
#         self.phone = phone
#         self.favorite = favorite


# class Contacts:
#     def __init__(self, filename: str, contacts: list[Person] = None):
#         if contacts is None:
#             contacts = []
#         self.filename = filename
#         self.contacts = contacts
#         self.count_save = 0
#         self.is_unpacking = False
    
#     def save_to_file(self):
#         with open(self.filename, "wb") as file:
#             pickle.dump(self, file)

#     def read_from_file(self):
#         with open(self.filename, "rb") as file:
#             content = pickle.load(file)
#         return content

#     def __getstate__(self):
#         attributes = self.__dict__.copy()
#         attributes["count_save"] = attributes["count_save"] + 1
#         attributes['is_unpacking'] = True
#         return attributes

#     def __setstate__(self, attributes):
#       self.__dict__.update(attributes)   

# contacts = [
#     Person("Allen Raymond", "nulla.ante@vestibul.co.uk", "(992) 914-3792", False),
#     Person("Chaim Lewis", "dui.in@egetlacus.ca", "(294) 840-6685", False)]
     
# persons = Contacts("user_class.dat", contacts)
# persons.save_to_file()
# person_from_file = persons.read_from_file()
# print(persons.is_unpacking)  # False
# print(person_from_file.is_unpacking)  # True

'''№7 
Для копіювання екземпляра класу Person із попереднього прикладу реалізуйте функцію copy_class_person. Як параметр вона приймає екземпляр класу person, та повертає "поверхневу" копію об'єкта за допомогою функції copy із пакета copy.
Приклад коду:
person = Person(
    "Allen Raymond",
    "nulla.ante@vestibul.co.uk",
    "(992) 914-3792",
    False,
)
copy_person = copy_class_person(person)
print(copy_person == person)  # False
print(copy_person.name == person.name)  # True
...
'''
# import copy

# class Person:
#     def __init__(self, name: str, email: str, phone: str, favorite: bool):
#         self.name = name
#         self.email = email
#         self.phone = phone
#         self.favorite = favorite
  
# def copy_class_person(person):
#     person_copy = copy.copy(person)
#     return person_copy
  
    
# person = Person(
#     "Allen Raymond",
#     "nulla.ante@vestibul.co.uk",
#     "(992) 914-3792",
#     False,
# )
# copy_person = copy_class_person(person)
# print(copy_person == person)  # False
# print(copy_person.name == person.name)  # True

'''№8
Як ви вже зрозуміли, для класу Contacts створення поверхневої копії екземпляра класу не увінчається успіхом через те, що ми маємо атрибут contacts, який є списком екземплярів об'єктів класу Person, а отже, всі вони будуть передані за посиланням. Тому необхідно використовувати глибоке копіювання методом deepcopy з пакета copy
Для класу Contacts реалізуйте функцію copy_class_contacts. Як параметр вона приймає екземпляр класу Contacts і повертає глибоку копію об'єкта за допомогою функції deepcopy з пакета copy.
Приклад коду:

persons = Contacts("user_class.dat", contacts)

new_persons = copy_class_contacts(persons)

new_persons.contacts[0].name = "Another name"

print(persons.contacts[0].name)  # Allen Raymond
print(new_persons.contacts[0].name)  # Another name
'''
# import copy
# import pickle


# class Person:
#     def __init__(self, name: str, email: str, phone: str, favorite: bool):
#         self.name = name
#         self.email = email
#         self.phone = phone
#         self.favorite = favorite


# def copy_class_person(person):
#     return copy.copy(person)


# class Contacts:
#     def __init__(self, filename: str, contacts: list[Person] = None):
#         if contacts is None:
#             contacts = []
#         self.filename = filename
#         self.contacts = contacts
#         self.is_unpacking = False
#         self.count_save = 0

#     def save_to_file(self):
#         with open(self.filename, "wb") as file:
#             pickle.dump(self, file)

#     def read_from_file(self):
#         with open(self.filename, "rb") as file:
#             content = pickle.load(file)
#         return content

#     def __getstate__(self):
#         attributes = self.__dict__.copy()
#         attributes["count_save"] = attributes["count_save"] + 1
#         return attributes

#     def __setstate__(self, value):
#         self.__dict__ = value
#         self.is_unpacking = True


# def copy_class_contacts(contacts):
#     contacts_copy = copy.deepcopy(contacts)
#     return contacts_copy
    
    
# contacts = [
#     Person("Allen Raymond", "nulla.ante@vestibul.co.uk", "(992) 914-3792", False),
#     Person("Chaim Lewis", "dui.in@egetlacus.ca", "(294) 840-6685", False)]

# persons = Contacts("user_class.dat", contacts)

# new_persons = copy_class_contacts(persons)

# new_persons.contacts[0].name = "Another name"

# print(persons.contacts[0].name)  # Allen Raymond
# print(new_persons.contacts[0].name)  # Another name

'''№9
Реалізуйте метод __copy__ для класу Person.

Реалізуйте методи __copy__ та __deepcopy__ для класу Contacts.
'''
import copy
import pickle


class Person:
    def __init__(self, name: str, email: str, phone: str, favorite: bool):
        self.name = name
        self.email = email
        self.phone = phone
        self.favorite = favorite

    def __copy__(self):
        new_person = self.__class__(self.name, self.email, self.phone, self.favorite)
        return new_person

class Contacts:
    def __init__(self, filename: str, contacts: list[Person] = None):
        if contacts is None:
            contacts = []
        self.filename = filename
        self.contacts = contacts
        self.is_unpacking = False
        self.count_save = 0

    def save_to_file(self):
        with open(self.filename, "wb") as file:
            pickle.dump(self, file)

    def read_from_file(self):
        with open(self.filename, "rb") as file:
            content = pickle.load(file)
        return content

    def __getstate__(self):
        attributes = self.__dict__.copy()
        attributes["count_save"] = attributes["count_save"] + 1
        return attributes

    def __setstate__(self, value):
        self.__dict__ = value
        self.is_unpacking = True

    def __copy__(self):
        new_contacts = self.__class__(self.filename, copy.copy(self.contacts))
        new_contacts.is_unpacking = self.is_unpacking
        new_contacts.count_save = self.count_save
        return new_contacts
    
    def __deepcopy__(self, memo):
        new_contacts = self.__class__(self.filename, copy.deepcopy(self.contacts, memo))
        new_contacts.is_unpacking = self.is_unpacking
        new_contacts.count_save = self.count_save
        return new_contacts
    

        