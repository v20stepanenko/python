class Person:
    def __init__(self, first_name, second_name, age, tel, email):
        self._first_name = first_name
        self._second_name = second_name
        self._age = age
        self._tel = tel
        self._email = email
        
    def get_first_name(self):
        return self._first_name

    def set_first_name(self, first_name):
        self._first_name = first_name

    def get_second_name(self):
        return self._second_name

    def set_second_name(self, second_name):
        self._second_name = second_name

    def get_age(self):
        return self._age

    def set_age(self, age):
        self._age = age

    def get_tel(self):
        return self._tel

    def set_tel(self, tel):
        self._tel = tel

    def get_email(self):
        return self._email

    def set_email(self, email):
        self._email = email

    def summary_dict(self):
        return {
            'first_name': self._first_name,
            'second_name': self._second_name,
            'age': self._age,
            'tel': self._tel,
            'email': self._email
        }

    def summary_list(self):
        return [self._first_name, self._second_name, self._age, self._tel, self._email]


some_person = Person('vova', 'stepanneko', 24 , 32055651, 'asdj@asdasd.com')
print(some_person.summary_list())