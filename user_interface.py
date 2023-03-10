# Модуль работы с пользователем
import log_generate as lg


def user_request():
    while True:
        print('Ознакомьтесь с командами для работы со справочником:\n'
              '1 - Сгенерировать случайный справочник;\n'
              '2 - Внести данные в справочник\n'
              '3 - Изменить данные в справочнике\n'
              '4 - Удалить данные из справочника\n'
              '5 - Найти данные в справочнике\n'
              '6 - Импортировать справочник\n'
              '7 - Экспортировать справочник\n'
              '8 - Показать содержимое справочника\n'
              '9 - Выход')
        user_command = input('Введите команду: ')
        if user_command in '123456789':
            lg.write_data('От пользователя получена команда: ' + user_command + ';')
            return int(user_command)
        else:
            lg.write_data('Зафиксирован некорректный ввод;')
            print('Проверьте корректность ввода')


def print_book(book: dict):
    for key in book.keys():
        print(str(key) + ' - ', end='')
        print(*book[key].values())
