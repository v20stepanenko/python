def print_line():
    print('-' * 30)

a,b = 3,8
c = (a%2) == 0
d = (b%2) == 0
e = c + d
print(c)
print(d)
print(e)
a = str(a)
b = str(b)
print_line()
print(a)
print(b)
print_line()
c = a + b
print(c)
a = int(c)
print (a * 2)