# Модуль объединения рабочих модулей
import user_interface as ui
import time
import log_generate as lg
import working_with_datebase as wd

book = {}


def start():
    lg.write_data('Начало работы программы: ' + time.strftime('%d.%m.%y %H:%M:%S') + ';')
    print('Начало работы программы: ' + str(time.strftime('%d.%m.%y %H:%M:%S')) + ';')
    while True:
        num = ui.user_request()
        global book
        if num == 9:
            lg.write_data('Конец работы программы: ' + time.strftime('%d.%m.%y %H:%M:%S') + ';')
            exit()
        book = wd.work_db(num, book)
        print()
        ui.print_book(book)
        print()
