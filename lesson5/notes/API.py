import DAO

DAO.download_by_file()

def create_note(login):
    print('Создание заметки')
    title = input('Введите title: ')
    text = input('Введите текст: ')
    if DAO.new_note(login = login, title = title, body = text):
        print('Заметка созана')
    else:
        print('Заметка не создана')

def del_note(login):
    num = input('Введите номер удаляемой заметки: ')
    if num.isdigit() and DAO.delete_notes(login = login, num = int(num)):
        print('Заметка удалена')
    else:
        print('Не удалось удалить заметку')

def show_note(login):
    num = input('Введите номер заметки для просмотра: ')
    if num.isdigit(): 
        note = DAO.get_note(login = login, num = int(num))
        if note:
            print('=' * 40)
            print('Название заметки: ', note['title'])
            print('Время создание заметки: ', note['datetime'])
            print('-' * 40)
            print(note['body'])
            print('*' * 80)
            return
    print('Что то пошло не так')

def notes_info_by_user(login):
    notes_list = DAO.get_notes(login)
    for item in range(0, len(notes_list)):
        note_stack = notes_list[item]
        id = note_stack[0]
        note = note_stack[1]
        print(id, '|', note['title'], '|', note['datetime'])

def work_notes_by_user(login):
    while True:
        print('=' * 30)
        print('=' * 30)
        notes_info_by_user(login)
        print('=' * 30)
        print('=' * 30)
        command = input('Работа с заметкой \n' +
                        'cr - создать, del - удалить, rd - просмотреть, ex - выход: ')
        if command == 'cr':
            create_note(login)
        elif command == 'del':
            del_note(login)
        elif command == 'rd':
            show_note(login)
        elif command == 'ex':
            break

def registration():
    print('придумать и ввести login, email и password')
    login = input('Введите логин: ')
    password = input('Введите пароль: ')
    email = input('Введите email: ')
    if not DAO.create_user(login = login, password = password, email = email):
        print('Регистрация не успешна')

def authorization():
    print('Авторизация')
    login = input('Введите логин: ')
    password = input('Введите пароль: ')
    if DAO.check_authorization(login = login, password = password):
        work_notes_by_user(login)
    else:
        print('Неверный логин или пароль')

def acc_worker():
    while True:
        comand = input('Введите - "auth" для авторизации, "reg" для регистрации, "ex" для выхода ')
        if comand == 'auth':
            authorization()
        elif comand == 'reg':
            registration()
        elif comand == 'ex':
            break