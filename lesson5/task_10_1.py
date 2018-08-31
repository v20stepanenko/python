# Получить от пользователя текст, предоставив ему возможность многострочного ввода, окончить ввод по команде "/s";
# Запросить у пользователя путь для сохранения файла;
# Запросить у пользователя название для сохраняемого файла (без расширения);
# Проверить являются ли первые буквы строк большими, если нет, заменить на большие;
# Проверить являются ли первые буквы после символа точка "." в строках большими, если нет, заменить на большие;
# Сохранить обработанный текст в файл по указанному пользователем пути и с указанным названием, добавив в конец файла расширение ".txt".

import re

print('Получить от пользователя текст, предоставив ему возможность многострочного ввода, окончить ввод по команде "/s";')

user_text = []
while True:
    user_input = input()
    if user_input == '/s':
        break
    user_text.append(user_input)

def capitalize(text):
    if not text[0].isupper():
        text = text.capitalize()
    return text

def check_after_dots(text):
    dict_not_stop = {' ': 1, '"': 1, "'": 1, '(': 1}
    indexes_dots = indexes_chars(text, '.')
    list_chars = list(text)
    if indexes_dots:
        for index in indexes_dots:
            for i in range(index+1, len(list_chars)):
                char = list_chars[i]
                if char.isalpha():
                    list_chars[i] = char.upper()
                    break
                elif not dict_not_stop[char]:
                    break
    return ''.join(list_chars)

def indexes_chars(text, char):
    list_indexes = []
    for index in range(0, len(text)):
        if text[index] == char:
            list_indexes.append(index)
    return list_indexes

def task_func(text):
    temp_text = ''
    for item_string in text:
        temp_str = capitalize(item_string)
        temp_str = check_after_dots(temp_str) + '\n'
        temp_text += temp_str
    return temp_text
user_text = task_func(user_text)
print(user_text)

print('Запросить у пользователя путь для сохранения файла;')

file_path = input()

if file_path.isspace() or not file_path:
    file_path = '.'

print('Запросить у пользователя название для сохраняемого файла (без расширения);')

file_name = input()

f = open(file_path + '\\' + file_name + '.txt', 'wb')
f.write(user_text.encode('utf-8'))
f.close()
