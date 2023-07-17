from search import search_person
def choose_mode():
    mode = input('Выберите режим  для работы со справочником: запись или поиск: ')
    if mode == 'запись':
        person = fill_person()
    elif mode == 'поиск':
        person = search_person()
    else:
        print('Такого режима не существует!')
        choose_mode()
    return person, mode

def fill_person():
    surname = input('Введите фамилию: ')
    name = input('Введите имя: ')
    second_name = input('Введите отчество: ')
    phone_number = input('Введите номер телефона: ')
    return surname, name, second_name, phone_number

