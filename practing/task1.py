# Предложить пользовательский ввод, где пользователь через пробел запишет слово и число
# Вывести "Yes", если число совпадет с длиной слова, иначе "No"

print(" Предложить пользовательский ввод, где пользователь через пробел запишет слово и число")
input_text = input()
split_text = input_text.split(' ')
# print(split_text[0])
numb = int(split_text[1])
if(len(split_text[0]) == numb):
    print('Yes')
else: print('No')