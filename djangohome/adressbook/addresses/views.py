from django.http import HttpResponse
from .models import Address


def get_address(request, field, value):
    my_dict = {field: value}
    find = Address.objects.get(**my_dict)
    data = '<h2>Смотрите, что мы нашли</h2>' \
           '<p>' \
           'Страна: значение {0} найденного объекта<br>' \
           'город: значение {1} найденного объекта<br>' \
           'Район: значение {2}  найденногго объекта<br>' \
           'Улица: значение {3}  найденногго объекта<br>' \
           'Номер дома: значение {4}  найденногго объекта<br>' \
           'Подьезд: значение {5}  найденногго объекта<br>' \
           '</p>'.format(find.country,
                         find.city,
                         find.district,
                         find.street,
                         find.house_number,
                         find.flat)
    return HttpResponse(data)
