

def show_menu() -> None:
    print("""Главное меню:
    1. Открыть файл
    2. Сохранить файл
    3. Создать контакт
    4. Показать все контакты""")


def choice_menu() -> int:
    while True:
        number = input("Выберите пункт меню: ")
        if number.isdigit() and 0 < int(number) < 5:
            return int(number)
        print("Введите число 1-4")


def show_contacts(phone_book: list[dict]):
    if not phone_book:
        print("Телефонная книга пуста")
        return False
    for index, contact in enumerate(phone_book, 1):
        print(f"{index}. {contact.get('name'):.<20}"
              f"{contact.get('phone'):.<20}"
              f"{contact.get('comment'):<20}")