a = ['Green', 'Red', 'Blue', 'Purple']
b = ['Cheburashka', 'Chupacabra', 'Panda', 'pokemon']
c = list(zip(b, a))
d = dict(c)
len_a = len(a)
b = range(0, len_a)
sum_b = sum(b)
str_b = '-'.join('%d' %i for i in b)
e = ' | '.join(map(' - '.join, c))
print(e)