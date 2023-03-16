
#import main

phone_book = {}
path = "phonebook.txt"

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