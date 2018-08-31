# Создадим кота, но дадим возможность пользователю определить некоторые его параметры следующим образом:
# Предлогаем пользователю ввести четырехзначное число;
# Затем разбираем пользовательский ввод следующим образом:
# Первая цифра отвечает за цвет кота. От 0 до 2 - белый. От 3 до 4 - рыжий. От 5 до 7 - серый. От 8 до 9 - черный.
# Вторая цифра отвечает за размер кота. От 0 до 2 - маленький. От 3 до 5 - небольшой. от 6 до 7 - большой. От 8 до 9 - очень большой.
# Третья цифра отвечает за характер кота. От 0 до 1 - ленивый. От 2 до 4 - спокойный. от 5 до 7 - подвижный. от 8 до 9 - гиперактивный.
# Четвертая цифра отвечает за "пушистость". От 0 до 2 - короткошерстный. От 3 до 5 - гладкошерстный. От 6 до 7 - пушистый. От 8 до 9 - очень пушистый.

# После того, как пользователь ввел число, кнему должна вернуться информация примерно следующего вида:
# "Это пушистый белый кот, он крупный и ленивый.".

class Cat:

    __fields_size = { }

    @staticmethod
    def wrong():
        print('Input wrong index')

    def __set_index_fields(self, name_fields):
        while True:
            print('By index from 0 to 10')
            size = input()
            if size.isdigit(): size = int(size)
            else: 
                Cat.wrong()
                continue
            if( 0 < size < 10 ):
                self.__fields_size[name_fields] = size
                break
        print('-'*50)
        

    def set_color(self):
        print('Input color')
        self.__set_index_fields('color')

    def set_size(self):
        print('Input size')
        self.__set_index_fields('size')

    def set_character(self):
        print('Input character')
        self.__set_index_fields('character')

    def set_fluffiness(self):
        print('input fluffiness')
        self.__set_index_fields('fluffiness')

    def run_describe(self):
        self.set_color()
        self.set_size()
        self.set_character()
        self.set_fluffiness()
    
    @staticmethod
    def color_byindex(index):
        return {
                0 <= index <= 2: 'белый',
                3 <= index <= 4: 'рыжий',
                5 <= index < 7:  'серый',
                8 <= index < 9:  'черный'
        }[True]

    def get_color(self):
        return Cat.color_byindex(self.__fields_size['color'])

    @staticmethod
    def size_byindex(index):
        return {
                0 <= index <= 2: 'маленький',
                3 <= index <= 5: 'небольшой',
                6 <= index < 7:  'большой',
                8 <= index < 9:  'очень большой'
        }[True]
    
    def get_size(self):
        return Cat.size_byindex(self.__fields_size['size'])
        
    @staticmethod
    def character_byindex(index):
        return {
                0 <= index <= 1: 'ленивый',
                2 <= index <= 4: 'спокойный',
                5 <= index < 7:  'активный',
                8 <= index < 9:  'гипер активынй'
        }[True]
    
    def get_character(self):
        return Cat.character_byindex(self.__fields_size['character'])

    @staticmethod
    def fluffiness_byindex(index):
        return {
                0 <= index <= 2: 'короткошерстый',
                3 <= index <= 5: 'гладкошерстый',
                6 <= index < 7:  'пушыстый',
                8 <= index < 9:  'очень пушыстый'
        }[True]

    def get_fluffines(self):
        return Cat.fluffiness_byindex(self.__fields_size['fluffiness'])

    def get_description(self):
        print("Это кот, он",
                self.get_color(),
                self.get_size(), 
                self.get_character(), 
                self.get_fluffines()
            )
        

catis = Cat()
catis.run_describe()
catis.get_description()
