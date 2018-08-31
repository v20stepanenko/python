# Через пользовательский ввод, получить путь к файлу с текстом;
# Через пользовательский ввод, получить слово или фрагмент строки для поиска в тексте файла;
# Найти все строки, где встречается указанный фрагмент/слово;
# Вывести на экран номера строк и количество повторений слова/фрагмента строки в этих строках.
import codecs
import re

print('Через пользовательский ввод, получить путь к файлу с текстом;')
user_path = input()

print('Через пользовательский ввод, получить слово или фрагмент строки для поиска в тексте файла;')
finder_str = input()

fileObj = codecs.open( user_path, "r", "utf_8" )

counter_line = 1
dict_str = {}
for line in fileObj.readlines():
    if(line.find(finder_str) != -1):
        dict_str[counter_line] = line
    counter_line += 1

fileObj.close()

for index_line in dict_str:
    matches = re.findall(r'' + finder_str, dict_str[index_line])
    print('Номер строки:', index_line, 'повторений:', len(matches))