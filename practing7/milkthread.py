from threading import Thread, Lock, Event
from random import randrange
import time


class Bowl:
    def __init__(self):
        self.sip = 0
        self.lock = Lock()
        self.event = Event()
        self.event.set()
        self.max_sip = 15

    def add_sip(self, sip):
        quantity = self.sip + sip
        if quantity <= self.max_sip:
            self.sip = quantity
        else:
            self.sip = self.max_sip

    def get_drink(self):
        self.event.wait()
        if self.sip != 0:
            self.sip -= 1
            return True
        else:
            return False


class Cat(Thread):

    def __init__(self, name, bowl):
        super().__init__()
        self.bowl = bowl
        self.name = name

    def run(self):
        for i in range(5):
            self.drink()

    def drink(self):
        try:
            print('Кот %s прибигает к минсочке и становиться в очередь' % self.name)
            self.bowl.lock.acquire()
            print('Кот %s начинает пить молоко' % self.name)
            for i in range(randrange(2, 5)):
                time.sleep(2)
                if not self.bowl.get_drink():
                    print('Миска пуста')
                    return
                else:
                    print('Кот %s делает глоток' % self.name)
        finally:
            print('Кот %s напился и убегает' % self.name)
            self.bowl.lock.release()
            time.sleep(3)


class Kate(Thread):

    def __init__(self, blow):
        super().__init__()
        self.blow = blow

    def add_milk(self, quantity=4):
        print('Катя доливает молоко')
        self.blow.event.clear()
        self.blow.add_sip(quantity)
        time.sleep(5)
        self.blow.event.set()

    def run(self):
        time.sleep(3)
        kate.add_milk(15)

bowl = Bowl()
bowl.add_sip(15)
kate = Kate(bowl)
cat1 = Cat('pisikot', bowl)
cat2 = Cat('pepsi', bowl)
cat3 = Cat('zdrisni', bowl)

kate.start()
cat1.start()
cat2.start()
cat3.start()
