dict_translit = {'а' : 'a',
                'б' : 'b',
                'в' : 'v',
                'г' : 'g',
                'д' : 'd',
                'е' : 'e',
                'ё' :  'e',
                'ж' :  'zh',
                'з' :  'z',
                'к' :  'k',
                'л' :  'l',
                'и' :  'i',
                'й' :  'y',
                'м' :  'm',
                'н' :  'n',
                'о' :  'o',
                'п' :  'p',
                'р' :  'r',
                'с' :  's',
                'т' :  't',
                'у' :  'u',
                'ф' :  'f',
                'х' :  'h',
                'ц' :  'c',
                'ч' :  'ch',
                'ш' :  'sh',
                'щ' :  'sch',
                'ь' :   '',
                'ы' :  'y',
                'ъ' :  '',
                'э' :  'e',
                'ю' :  'ju',
                'я' :  'ya'}

user_text = input()
translit = list(user_text)

for index in range(len(translit)):
    char = translit[index]
    if char.isalpha() and dict_translit.get(char.lower()):
        if char.isupper(): 
            translit[index] = dict_translit[char.lower()].capitalize()
        else: translit[index] = dict_translit[char]

translit = ''.join(translit)

print(translit)