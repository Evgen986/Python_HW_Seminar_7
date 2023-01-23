# Модуль работы с БД
from random import randint
import log_generate as lg


def get_num(min_num, max_num, even):  # Функция получения рандомных значений для заполнения справочника
    if even:
        num = 1
        while num % 2:
            num = randint(min_num, max_num)
        return num
    else:
        num = 2
        while not num % 2:
            num = randint(min_num, max_num)
        return num


def find_in_book(f_book: dict):  # Функция поиска в справочнике возвращает ключ
    lg.write_data('Запущен поиск по справочнику;')
    while True:
        f_num = input('Выберите вариант поиска:\n'
                      '1 - По коду строки\n'
                      '2 - По фамилии или имени или отчеству или email или номеру телефона\n'
                      'Введите цифру: ')
        if f_num in ['1', '2']:
            lg.write_data('Пользователь ввел команду: ' + f_num)
            break
        else:
            lg.write_data('Введено некорректное значение: ' + f_num)
            print('Проверьте корректность ввода!')
    while True:
        if f_num == '1':
            f_choice = input('Введите код строки: ')
            lg.write_data('Пользователь ввел команду: ' + f_choice)
            if int(f_choice) in f_book.keys():
                lg.write_data('Ключ найден;')
                return int(f_choice)
            else:
                lg.write_data('Введено некорректное значение: ' + f_choice)
                print('Проверьте корректность ввода!')
        else:
            f_choice = input('Введите данные: ').strip().capitalize()
            lg.write_data('Пользователь ввел команду: ' + f_choice)
            choice_list = list()
            for key in f_book:
                if f_choice in f_book[key].values():
                    choice_list.append(key)
            if len(choice_list) == 0:
                lg.write_data('Введено некорректное значение, в справочнике не найдено совпадений;')
                print('Проверьте корректность ввода!')
                continue
            elif len(choice_list) > 1:
                for el in choice_list:
                    print(str(el) + ' - ', end='')
                    print(*f_book[el].values())
                f_choice = input('Введите код строки: ')
                if int(f_choice) in choice_list:
                    lg.write_data('Пользователь выбрал строку: ' + f_choice)
                    return int(f_choice)
                else:
                    lg.write_data('Пользователь выбрал не корректную строку: ' + f_choice)
                    print('Проверьте корректность ввода!')
            else:
                lg.write_data('Возвращается ключ: ' + str(choice_list[0]))
                return choice_list[0]


def work_db(command, book: dict):  # Основная функция работы со справочником
    if command == 1:  # 1. Сгенерировать случайный справочник
        lg.write_data('Начато создание рандомного справочника;')
        surname = ['Щученко', 'Иванько', 'Демченко', 'Пономаренко', 'Харченко', 'Семененко', 'Коваленко', 'Федоренко']
        name = ['Александр', 'Светлана', 'Сергей', 'Екатерина', 'Петр', 'Инга', 'Леонид', 'Ирина']
        patronymic = ['Петрович', 'Семеновна', 'Сергеевич', 'Ивановна', 'Егорович', 'Петровна', 'Иванович', 'Сергеевна']
        email_login = ['user_1', 'user_2', 'user_3', 'user_4', 'user_5', 'user_6', 'user_7', 'user_8']
        email_domain = ['@mail.ru', '@yandex.ru', '@gmail.com', '@mail.com', '@rambler.ru', '@yandex.com']
        for i in range(len(book) + 1, randint(5, 10)):
            book[i] = dict(zip(['surname', 'name', 'patronymic', 'email', 'telephone'],
                               [surname[randint(0, 7)], name[get_num(0, 7, i % 2)], patronymic[get_num(0, 7, i % 2)],
                                ''.join(email_login[randint(0, 7)] + email_domain[randint(0, 5)]),
                                '+7-' + str(randint(900, 999)) + '-' + str(randint(100, 999)) + '-'
                                + str(randint(10, 99)) + '-' + str(randint(10, 99))]))
            lg.write_data('Создана запись: ' + ' '.join(book[i].values()) + ';')
        lg.write_data('Создание справочника завершено;')
        return book

    elif command == 2:  # 2. Ввести данные в справочник
        surname = input('Введите фамилию: ')
        name = input('Введите имя: ')
        patronymic = input('Введите отчество: ')
        email_address = input('Введите email: ')
        telephone = input('Введите телефон в формате +7-000-000-00-00: ')
        lg.write_data('От пользователя получены данные: ' + surname + ' ' + name + ' ' + patronymic  # Запись в лог
                      + ' ' + email_address + ' ' + telephone + ';')
        flag = True  # Флаг для проверки на наличие дублей в справочнике
        for key in book.keys():  # Проверка на наличие совпадений в справочнике
            if surname in book[key].values() and name in book[key].values() and patronymic in book[key].values():
                lg.write_data('Обнаружено совпадение!')
                choice = True
                flag = False
                while choice:
                    choice = input('В справочнике обнаружена запись с совпадающими ФИО\n'
                                   'Хотите обновить запись (''да/нет)?: ')
                    if choice == 'да':
                        lg.write_data('Пользователь обновляет запись;')
                        if email_address not in book[key].values() and len(email_address) > 0:  # Если email в ячейке
                            # словаря не найден
                            count = ' '.join(list(book[key].keys())).count('email')  # Проверяем кол-во ключей с
                            # именем email
                            book[key].update({'email_' + str(count): email_address})  # Создаем новую пару ключ: адрес
                            lg.write_data('В словарь добавлен новый email;')
                        if telephone not in book[key].values() and len(telephone) > 0:
                            count = ' '.join(list(book[key].keys())).count('telephone')  # Проверяем кол-во ключей с
                            # именем telephone
                            book[key].update({'telephone_' + str(count): telephone})  # Создаем новую пару ключ: телефон
                            lg.write_data('В словарь добавлен новый телефон;')
                        choice = False  # Меняем choiсe на True, что-бы выйти из while
                    elif choice == 'нет':
                        choice = False  # Меняем choiсe на True, что-бы выйти из while
                        flag = True  # Меняем флаг на True для создания новой записи
                    else:
                        lg.write_data(f'Введены некорректные данные - "{choice}";')
                        choice = True  # Если введено отличное от да/нет то меняем choice на False, что бы цикл
                        # продолжался
        if flag:  # Если дублей в справочнике не найдено или пользователь решил создать новую запись
            book[len(book) + 1] = dict(zip(['surname', 'name', 'patronymic', 'email', 'telephone'],
                                           [surname, name, patronymic, email_address, telephone]))
        lg.write_data('В справочник внесена новая запись;')
        return book

    elif command == 3:  # 3. Изменить данные в справочнике
        print('Найдите строку в справочнике для замены.')
        change_num = find_in_book(book)
        lg.write_data(f'Пользователь для замены выбрал строку: {str(change_num)};')
        print('Будет изменена строка:', end=' ')
        print(*book[change_num].values())
        surname = input('Введите фамилию: ')
        name = input('Введите имя: ')
        patronymic = input('Введите отчество: ')
        email_address = input('Введите email: ')
        telephone = input('Введите телефон в формате +7-000-000-00-00: ')
        book[change_num] = dict(zip(['surname', 'name', 'patronymic', 'email', 'telephone'],
                                    [surname, name, patronymic, email_address, telephone]))
        lg.write_data(f'В строку {change_num} внесены изменения;')
        return book

    elif command == 4:  # 4. Удалить данные в справочнике
        del_num = find_in_book(book)
        while True:
            print(f'Будет произведено удаление строки: {del_num} с содержимым:', end=' ')
            print(*book[del_num].values())
            resolution = input('Введите да/нет: ')
            if resolution == 'да':
                lg.write_data(f'Удаление ключа {del_num} с содержимым {book.pop(del_num)}')
                return book
            elif resolution == 'нет':
                print('Удаление отменено')
                return book
            else:
                print('Не корректный ввод!')

    elif command == 5:  # 5. Найти данные в справочнике
        print(*book[find_in_book(book)].values())
        return book

    elif command == 6:  # 6. Импортировать в справочник
        with open('for_import.csv', encoding='utf=8') as file:
            base = [str(el).split(';') for el in file.readlines()]
        lg.write_data('Справочник импортируется из внешнего файла;')
        base[0][0] = 1
        for i in range(len(base)):
            base[i][0] = int(base[i][0])
            base[i][-1] = base[i][-1].rstrip('\n')
            book[base[i][0]] = dict(zip(base[i][1::2], base[i][2::2]))
        lg.write_data('Импорт справочника завершен;')
        return book

    elif command == 7:  # 7. Экспортировать справочник
        if len(book) > 0:
            lg.write_data('Начат экспорт справочника во внешний файл;')
            while True:
                print('Выберите вариант экспорта справочника:\n'
                      '1 - Одна ячейка справочника на одной строке;\n'
                      '2 - Значения одной ячейки справочника на отдельных строках')
                choice = input('Введите цифру: ')
                if choice == '1' or choice == '2':
                    if choice == '1':
                        with open('export.csv', 'a', encoding='utf=8') as ex_file:
                            for key in book.keys():
                                ex_file.write(' '.join(list(map(str, book[key].values()))) + '\n')
                        lg.write_data('Экспорт в файл по первому правилу завершен')
                        return book
                    elif choice == '2':
                        with open('export_2.csv', 'a', encoding='utf=8') as ex_2_file:
                            for key in book.keys():
                                ex_2_file.write('\n'.join(list(map(str, book[key].values()))) + '\n\n')
                        lg.write_data('Экспорт в файл по второму правилу завершен')
                        return book
                    else:
                        lg.write_data(f'Пользователь ввел некорректное значение: {choice};')
                        print('Не корректный ввод!')
        else:
            lg.write_data('Попытка экспортировать пустой справочник;')
            print('Убедитесь, что в справочнике есть данные!')
            return book

    elif command == 8:  # 8. Показать справочник
        return book
