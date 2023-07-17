def search_person():
    search_surname = input('Введите фамилию для поиска контакта: ')

    with open('example.txt', 'r', encoding = 'utf-8') as file:
        text_list = [line.strip() for line in file.readlines()]

    for i, el in enumerate(text_list):
        if search_surname in el:
            print(*text_list[i:i+4], sep = '\n')
