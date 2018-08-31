print('start')
user_math = input('Введите мат. выражение используя plus minus divide minus\n')

def math_command(command):
    list_words = command.split(' ')
    
    def extract_nums(index):
        return (float(list_words[index - 1]), float(list_words[index + 1]))
        
    def del_nums(index):
        del list_words[index + 1]
        del list_words[index - 1]

    if list_words.count('divide') or list_words.count('multiply'):
        index = 0        
        while True:
            if index == len(list_words):
                break
            word = list_words[index]
            if word == 'divide':
                nums = extract_nums(index)
                list_words[index] = nums[0] / nums[1]
                del_nums(index)
                continue
            elif word == 'multiply':
                nums = extract_nums(index)
                list_words[index] = nums[0] * nums[1]
                del_nums(index)
                continue
            index += 1
    if list_words.count('plus') or list_words.count('minus'):
        index = 0
        while True:
            if len(list_words) == 1:
                break
            word = list_words[index]
            if word == 'plus':
                nums = extract_nums(index)
                list_words[index] = nums[0] + nums[1]
                del_nums(index)
                continue
            elif word == 'minus':
                nums = extract_nums(index)
                list_words[index] = nums[0] - nums[1]
                del_nums(index)
                continue
            index += 1

    print(list_words)
math_command(user_math)
