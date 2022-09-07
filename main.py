# Создать информационную систему позволяющую работать с сотрудниками некой компании
# \ студентами вуза \ учениками школы

import json
import os
from getch import pause


def DrawLine():
    print("________________________________")


def ClearScreen():
    os.system('clear')


def Pause():
    pause('Нажмите любую клавишу, чтобы продолжить.')


def Hello():
    print('Вас приветствует программа по работе с учениками школы!')


def UnderConstruction():
    print('Извините, программа находится в стадии разработки. Выберите другой пункт.')
    Pause()


def ShowChoose(choose_menu):
    print(f'Вы выбрали пункт {choose_menu}.')


def GoodBuy():
    print('До новых встреч!')


def AddNewStudent():
    with open('students.json', 'r') as f:
        data = json.load(f)
    fio_of_student = input('Введите ФИО ученика: ')
    class_of_student = input('Введите в каком классе учится: ')
    perfomance_of_student = input(
        'Успеваемость ученика (отличник / хорошист / троечник): ')
    new_student = {
        'fio_of_student': fio_of_student,
        'class_of_student': class_of_student,
        'perfomance_of_student': perfomance_of_student
    }
    data["students"].append(new_student)
    with open('students.json', 'w') as fp:
        data = json.dump(data, fp, indent=2, ensure_ascii=False)
    print('Данные внесены успешно.')
    Pause()


def PrintAllData():
    with open('students.json', 'r') as f:
        data = json.load(f)
        print('ФИО. Класс. Успеваемость')
        for item in data['students']:
            print(item.get('fio_of_student', '') + '.', item.get('class_of_student', '') + '.', item.get('perfomance_of_student', ''))
    Pause()


def FindStudent():
    find = input('Введите ФИО ученика: ')
    with open('students.json', 'r') as f:
        data = json.load(f)
        wasfind = False
        for item in data['students']:
            if item['fio_of_student'] == find:
                print('ФИО, класс')
                print(item['fio_of_student'], item['class_of_student'])
                wasfind = True
                break
        if not wasfind:
            print('Ученик с таким ФИО не найден.')
    Pause()


def DeleteStudent():
    find = input('Введите ФИО ученика: ')
    with open('students.json', 'r') as f:
        data = json.load(f)
        wasfind = False
        for i in range(len(data['students'])):
            if find.lower() == data['students'][i]['fio_of_student'].lower():
                del data['students'][i]
                wasfind = True
                break
        if not wasfind:
            print('Ученик с таким ФИО не найден. Должно быть строгое соответствие.')
        else:
            with open('students.json', 'w') as fp:
                data = json.dump(data, fp, indent=2, ensure_ascii=False)
                print('Данные об ученике успешно удалены.')
    Pause()


def AreYouShure():
    are_u_sure = input(
        'Вы уверены, что хотите стереть все данные? Если да, введите "Да" \n(если нет - любую другое слово или просто Enter): ')
    if are_u_sure.lower() == "да":
        InitializeJSON()
    else:
        print('Отмена инициализации.')
    Pause()


def InitializeJSON():
    with open('students.json', 'w') as fp:
        data_to_json = '''{"students": []}'''
        b = json.loads(data_to_json)
        data = json.dump(b, fp)
        print('Данные успешно инициализированы.')


def MainMenu():
    print('------ ГЛАВНОЕ МЕНЮ ------')
    print('1. Отобразить информацию обо всех учениках')
    print('2. Отобразить информацию о необходимом ученике')
    print('3. Внести данные нового ученика')
    print('4. Внести изменения у необходимого ученика')
    print('5. Удалить данные об ученике')
    print('6. Инициализировать (стереть) базу данных')
    print('7. Выход')
    button = input("Выберите пункт меню: ").replace(' ', '')
    if button == '1':
        ClearScreen()
        print(f'Выбран пункт меню 1. Отобразить информацию обо всех учениках.')
    elif button == '2':
        ClearScreen()
        print(f'Выбран пункт меню 2. Отобразить информацию о необходимом ученике.')
    elif button == '3':
        ClearScreen()
        print(f'Выбран пункт меню 3. Внести данные нового ученика.')
    elif button == '4':
        ClearScreen()
        print(f'Выбран пункт меню 4. Внести изменения у необходимого ученика.')
    elif button == '5':
        ClearScreen()
        print(f'Выбран пункт меню 5. Удалить данные об ученике.')
    elif button == '6':
        ClearScreen()
        print(f'Выбран пункт меню 6. Инициализировать (стереть) базу данных.')
    elif button == '7':
        ClearScreen()
        print(f'Выбран пункт меню 7. Выход из программы.')
    else:
        ClearScreen()
        print(f'Введен пункт {button}.')
    try:
        button = int(button)
    except:
        ClearScreen()
        print("НЕПРАВИЛЬНЫЙ ВВОД! Необходимо ввести целое число от 1 до 7. Попробуйте ещё раз.")
        Pause()
    return button


def MainProgram():
    ClearScreen()
    Hello()
    print('Если Вы запустили программу в первый раз, обязательно запустите инициализацию! \nЕсли нет - откажитесь, чтобы не потерять данные.')
    AreYouShure()
    
    while True:
        ClearScreen()
        start_program = MainMenu()
        if start_program == 1:
            PrintAllData()
        elif start_program == 2:
            FindStudent()
        elif start_program == 3:
            AddNewStudent()
        elif start_program == 4:
            UnderConstruction()
        elif start_program == 5:
            DeleteStudent()
        elif start_program == 6:
            AreYouShure()
        elif start_program == 7:
            DrawLine()
            print('До новых встреч!')
            quit()
        else:
            DrawLine()
            print('НЕПРАВИЛЬНЫЙ ВВОД! Попробуйте ещё раз.')
            Pause()


MainProgram()