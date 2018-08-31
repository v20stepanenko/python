class Room:
    def __init__(self, length, width, num_windows):
        self._length = length
        self._width = width
        self._num_windows = num_windows

    def get_area(self):
        return self._length * self._width

    def get_num_windows(self):
        return self._num_windows

class Apartment:
    rooms = []

    def _class(self):
        return Apartment

    def add_room(self, room):
        self.rooms.append(room)

    def get_area_rooms(self):
        return sum(room.get_area() for room in self.rooms)

    def get_num_windows_rooms(self):
        return sum(room.get_num_windows() for room in self.rooms)
        

aprtmen1 = Apartment()

aprtmen1.add_room(Room(2,3,3))
aprtmen1.add_room(Room(2,3,3))
aprtmen1.add_room(Room(2,3,3))
aprtmen1.add_room(Room(2,1,3))
print((aprtmen1.get_area_rooms()))
print((aprtmen1.get_num_windows_rooms()))

