
#import main

phone_book = {}
path = "Seminar\8\phone_book.txt"

def open_file():
    with open(path, "r", encoding="UTF-8") as file:
        data = file.readlines()
    for row in data:
        contact = row.strip().split(";")
        contact = {"name": contact[0], 
                   "phone": contact[1], 
                   "comment": contact[3]}
        phone_book.append(contact)
        
        

def get_phone_book():
    return phone_book



#MY!!!!!

def find_contact(phone_book):
    name_contact = input('Введите Имя Фамилию')
    if name_contact in phone_book:
        print(f'{name_contact}: {phone_book[name_contact]}')
        return [name_contact, phone_book[name_contact]]
    else:
        print(f'Не найдено')