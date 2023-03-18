
def main_menu() -> int:

    print('''Главное меню: 
    1. Открыть файл
    2. Сохранить файл 
    3. Показать контакты 
    4. Добавить контакт 
    5. Изменить контакт''')
    
    while True:
        choice = input("Выберите пункт меню:")
        if choice.isdigit() and 0 < int(choice) <6:
            return int(choice)


def show_contacts(book: list[dict], error_message: str):
    if not book:
        print(error_message)
        return False
    else:
        for i, contact in enumerate(book, 1):
            print(f"{i}.{contact.get('name'):<20}"
                 f"{contact.get('phone'):<20}"
                 f"{contact.get('comment'):<20}")
        return True
            


def add_contact() -> dict:
    name = input("Введите имя: ")
    phone = input("Введите номер: ")
    comment = input("Введите комментарий: ")
    return {"name": name, "phone": phone, "comment": comment}
    

def input_index(message: str):
     return int(input(message))


def input_search(message):
     return input(message)

def show_message(message: str):
     print('-'*len(message))
     print(message)
     print('-'*len(message))


def change_contact(book: list[dict], index: int):
     print('Введите новые данные или оставьте пустое поле, если изменения не требуются')
     contact = add_contact()
     return {'name': contact.get('name') if contact.get('name') else book[index - 1].get('name'),
             'phone': contact.get('phone') if contact.get('phone') else book[index - 1].get('phone'),
             'comment': contact.get('comment') if contact.get('comment') else book[index - 1].get('comment')}