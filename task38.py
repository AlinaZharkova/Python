# Создать телефонный справочник с возможностью импорта и
# экспорта данных в формате .txt. Фамилия, имя, отчество,
# номер телефона - данные, которые должны находиться в файле.

# Программа должна выводить данные
# Программа должна сохранять данные в текстовом файле
# Пользователь может ввести одну из характеристик для поиска
# определенной записи(Например имя или фамилию человека)
# Использование функций. Ваша программа не должна быть линейной

# Дополнить телефонный справочник возможностью изменения и
# удаления данных. Пользователь также может ввести имя или фамилию,
# и Вы должны реализовать функционал для изменения и удаления данных


# r - только чтение файла
# a - дозапись в файл
# w - перезапись файла

def show_data():
    # Ф-ция для отображения содержимого справочника
    with open('phon.txt', 'r', encoding='utf-8') as file:
        book = file.read()  # .split('\n')
    return book


def new_data():
    # Ф-ция для добавления строки в справочник
    with open('phon.txt', 'a', encoding='utf-8') as file:
        file.write(input('Введите новую строку: ' + '\n'))


def find_data():
    # Ф-ция для поиска данных в справочнике
    with open('phon.txt', 'r', encoding='utf-8') as file:
        book = file.read().split('\n')
        temp = input('Что будем искать в справочнике?: ')
        for i in book:
            if temp in i:
                print(i)


def delete_person(name):
    # Ф-ция для удаления данных
    persons = read_data()
    with open("phon.txt", "w", encoding="utf8") as file:
        for person in persons:
            if name != person:
                file.write(person)


def change_person(new_name, old_name):
    # Ф-ция для изменения данных
    persons = read_data()
    with open("phon.txt", "w", encoding="utf8") as file:
        for person in persons:
            if old_name != person:
                file.write(person)
            else:
                file.write(new_name + "\n")


while True:
    mode = input('Выберите опцию для работы со справочником: ' + '\n'
                 + '(0- поиск, 1 - чтение файла, 2 - добавление в файл, 3 - удаление, 4 - замена, 5 - выход) ')
    if mode == '0':
        find_data()
    elif mode == '1':
        print(show_data())
    elif mode == '2':
        new_data()
    elif mode == '3':
        name = input('Выберите объект, который необходимо удалить: ')
        delete_person(name)
    elif mode == '4':
        old_name = input('Выберите объект, который необходимо переименовать: ')
        new_name = input('Новое название объекта: ')
        change_person(new_name, old_name)
    elif mode == '5':
        break
    else:
        print('ОШИБКА. Введите существующий номер команды для работы со справочником!')
