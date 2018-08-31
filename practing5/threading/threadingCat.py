from threading import Thread, Lock
from helper import *
import time

class Cat(Thread):

    def __init__(self, name, location):
        super().__init__()
        self.name = name
        self.is_live = True
        self.is_here = False
        self.location = location
        location.append(self)
        self.lock = Lock()

    def run(self):
        print('Кот {0} запущен'.format(self.name))
        time.sleep(speed_interval)
        while self.is_live:
            if random_bool(2):
                self.is_here = False
                self.attention_to_self()
            elif not self.is_here:
                print('Кот %s вышел поискать кого то' % self.name)
                self.is_here = True
                self.find_cat()
            time.sleep(speed_interval)

    def find_cat(self):
        for inhabitant in self.location:
            if inhabitant != self and inhabitant.is_here and random_bool():
                self.reaction_to_cat(inhabitant)
                return
        print('Кот %s никого не нашел' % self.name)

    def reaction_to_cat(self, cat):
        if cat.lock.acquire(False):
            print('Друг на друга хихикают кот {0} и {1}'.format(self.name, cat.name))
            cat.lock.release()

    def attention_to_self(self):
        if self.is_live:
            print('Выглянул из за тучки кот {0}'.format(self.name))


class Dog(Thread):

    def __init__(self, name, location):
        super().__init__()
        self.name = name
        self.location = location

    def run(self):

        while location:
            time.sleep(1)
            if randrange(4):
                self.see_location()
            else:
                self.show_lonely()
            time.sleep(speed_interval)

    def voice(self):
        print('Гав-гав(громко) собакен с именем {}'.format(self.name))

    def see_location(self):
        for habitait in self.location:
            if habitait.is_here:
                self.reaction_to_cat(habitait)
                break

    def reaction_to_cat(self, cat):
        cat.lock.acquire()
        survive = not bool(randrange(3))
        if not survive:
            print('Собака {0} задушила кота {1}'.format(self.name, cat.name))
            for pos in range(len(self.location)):
                if self.location[pos] == cat:
                    cat.is_live = False
                    self.location.pop(pos)
                    break
        else:
            print('Собака {0} не задушила кота {1}, он убежал'.format(self.name, cat.name))
        cat.lock.release()

    def show_lonely(self):
        print("Скучно хоть волком вой", ' собакен с именем {}'.format(self.name))


location = []
test_cat = Cat('pepsi', location)
test_cat3 = Cat('pepsi3', location)
test_cat2 = Cat('pepsi2', location)
dog = Dog('bobik', location)

test_cat.start()
time.sleep(speed_interval)
test_cat2.start()
time.sleep(speed_interval)
test_cat3.start()
time.sleep(speed_interval)
dog.start()
