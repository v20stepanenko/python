# Программа должна принимать через пользовательский ввод несколько чисел через пробел. Соблюдаем следующие условия:
# Чисел должно быть не менее трех;
# Последнее число должно быть ровно в два раза больше чем первое;
# Если условия не соблюдены, вывести на экран "Error".
# Если условия соблюдены:
# Если чисел парное количество, вывести на экран 2 средних числа, Т.Е. Если числа "10 15 3 20" - вывести на экран "15 3);
# Если непарное, вывести на экран одно среднее число - "12 22 8 32 24" - вывести на экран "8";

print('Введите числа')

str_nums = input().strip()

is_nums = True
nums_list = str_nums.split(' ')
for num in nums_list:
    if(not num.isdigit()):
        is_nums = False
        break
is_2first_last = int(nums_list[-1]) / int(nums_list[0]) == 2

if(not(is_nums and is_2first_last and len(nums_list) >= 3)):
    print('Error')
else:
    if len(nums_list) % 2 == 0:
        middle_num = int(len(nums_list) / 2)    
        print(nums_list[middle_num - 1], nums_list[middle_num])
    else:
        middle_num = int(len(nums_list) / 2)
        print(nums_list[middle_num])