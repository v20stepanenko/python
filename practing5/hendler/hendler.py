class Handler:
    
    def __init__(self):
        self._dict_hendlers = dict()

    def register_handler(self, alias, callback):
        if not alias in self._dict_hendlers:
            self._dict_hendlers[alias] = callback

    def unregister_handler(self, alias):
        if alias in self._dict_hendlers:
            del self._dict_hendlers[alias]

    def get_handler_aliases(self):
        return self._dict_hendlers.keys()

    def get_aliases_from_command(self, command):
        aliases = list(self._dict_hendlers.keys())
        lenght_command = len(command)
        for index in range(len(aliases)):
            if aliases[index].find(command, 0, lenght_command) != -1:
                return aliases[index]

    def get_handler(self, alias):
        if alias in self._dict_hendlers:
            return self._dict_hendlers[alias]
        
    def run(self, command, **kwargs):
        alias = self.get_aliases_from_command(command)
        if alias:
            self.get_handler(alias)(kwargs)


def some_func(kwargs_dict):
    print('ulalala')

def some_func2(kwargs_dict):    
    print(kwargs_dict['text'])

my_handler = Handler()

my_handler.register_handler('test_alias', some_func)
my_handler.register_handler('2test_alias', some_func2)

my_handler.run('test')
my_handler.run('2t', text = 'Текст через параметры')
