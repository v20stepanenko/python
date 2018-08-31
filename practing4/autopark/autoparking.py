class Avto:

    def __init__(self, width, height, length, weight):
        self._id = None
        self._width = width
        self._height = height
        self._length = length
        self._weight = weight

    def set_width(self, val):
        self._width = val

    def get_width(self):
        return self._width

    def set_height(self, val):
        self._height = val

    def get_height(self):
        return self._height

    def set_length(self, val):
        self._length = val

    def get_length(self):
        return self._length

    def set_id(self, id):
        self._id = id

    def get_id(self):
        return self._id

    def set_weight(self, weight):
        self._weight = weight

    def get_weight(self):
        return self._weight

    def get_dimension(self):
        return {'width': self.get_width(), 'length': self.get_length(), 'height': self.get_height()}

class Boxes:

    def __init__(self, width, length, height, weight):
        self._place = None
        self._width = width
        self._length = length
        self._height = height
        self._weight = weight
        self.in_angar = False

    def set_width(self, val):
        self._width = val

    def get_width(self):
        return self._width

    def set_length(self, val):
        self._length = val

    def get_length(self):
        return self._length

    def set_height(self, val):
        self._height = val

    def get_height(self):
        return self._height

    def set_weight(self, val):
        self._weight = val
    
    def get_weight(self):
        return self._weight

    def set_car_to_place(self, car):
        if (not self._place and
            self.get_width() >= car.get_width() and
            self.get_length() >= car.get_length() and
            self.get_height() >= car.get_height() and
            self.get_weight() >= car.get_weight()):
            self._place = car
            return True
        else:
            return False

    def get_car(self, id):
        if self._place and self._place.get_id() == id:
            tempPlace = self._place
            self._place = None
            return tempPlace

class Angar:
    
    def __init__(self):
        self._boxes = []
        self._in_autoparking = False

    def add_boxes(self, *boxes):
        for box in boxes:
            if not box.in_angar:
                box.in_angar = True
                self._boxes.append(box)

    def find_boxes(self, car):
        for box in self._boxes:
            if box.set_car_to_place(car):
                return True
    
    def find_car(self, id):
        for box in self._boxes:
            car = box.get_car(id)        
            if car:
                return car

class AutoParking:

    id_cars = 0

    def __init__(self):
        self._angars = []

    def add_angars(self, angar):
        if not angar._in_autoparking:
            angar._in_autoparking = True
            self._angars.append(angar)

    def find_car(self, id):
        for angar in self._angars:
            car = angar.find_car(id)
            if car:
                return car

    def get_id(self):
        self.id_cars += 1
        return self.id_cars

    def find_place_car(self, car):
        for angar in self._angars:
            if angar.find_boxes(car):
                id_generate = self.get_id()
                car.set_id(id_generate)
                return id_generate

        
autoparking = AutoParking()
box1 = Boxes(20, 40, 60, 2)
box2 = Boxes(14, 23, 32, 2)
box3 = Boxes(15, 24, 22, 2)
box4 = Boxes(12, 23, 32, 1)
box5 = Boxes(13, 23, 32, 2.5)
box6 = Boxes(19, 23, 32, 3)

angar1 = Angar()
angar1.add_boxes(box1, box2, box3)
angar2 = Angar()
angar2.add_boxes(box4, box5, box6)

autoparking.add_angars(angar1)
autoparking.add_angars(angar2)

car1 = Avto(18, 22, 23, 1)
car2 = Avto(23, 12, 9, 1)
car3 = Avto(18, 22, 23, 1)
car4 = Avto(18, 22, 23, 1)

id_car = autoparking.find_place_car(car1)
id_car2 = autoparking.find_place_car(car2)
id_car3 = autoparking.find_place_car(car3)
id_car4 = autoparking.find_place_car(car4)

print(id_car)
print(id_car2)
print(id_car3)
print(id_car4)

find_car_1 = autoparking.find_car(id_car)
print('Найденый первый кар',find_car_1)
