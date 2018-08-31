import csv

file = open('doc_csv.csv', encoding='cp1251')
# file.close()

class CSVWorker:

    def __init__(self, file_csv, delimiter=';'):
        self._file = csv.reader(file_csv, delimiter=delimiter)
        self._csv = list(self._file)

    def len_lines(self):
        return len(self._csv)

    def len_column(self):
        return len(self._csv[0])

    def get_headers(self):
        return self._csv[0]

    def num_column_by_name(self, name):
        for col_num in range(len(self._csv[0])):
            if self._csv[0][col_num] == name:
                return  col_num

    def get_column(self, **kwargs):
        result = []
        num = None

        if 'num' in kwargs:
            num = kwargs['num']
        elif 'name' in kwargs:
            num = self.num_column_by_name(kwargs['name'])
        else:
            return

        for point in self._csv:
            result.append(point[num])
        return result

    def get_cells(self, *args):
        result = []
        for coord_cel in args:
            result.append(self._csv[coord_cel[1]][coord_cel[0]])
        return result

    def add_header(self, name, num=None):
        create_num = num if num else len(self._csv[0])

        if not num:
            for item in self._csv:
                item.append(None)
        else:
            for item in self._csv:
                item[create_num] = None

        self._csv[0][create_num] = name

    def set_cell(self, pos, val):
        if len(self._csv) > pos[1] > 0:
            self._csv[pos[1]][self.num_column_by_name(pos[0])] = val

# !!!!!!!!!!!!!!!!!!!!!!!!!!!
    def save(self):
        csv.writer(self._file)

csv_test = CSVWorker(file)
# print(csv_test.get_column(name = "Имя", num = 1))
# print(csv_test.get_cells([2, 0], [2, 4]))
csv_test.add_header('Test')
# csv_test.add_header('Replace', 1)
col = 13
csv_test.set_cell(['Test', 4], 'wtf')
print(csv_test.get_cells([col, 0], [col, 4]))
csv_test.save()
