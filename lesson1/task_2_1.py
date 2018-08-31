a = "First Red Second Green"
list_a = a.split(' ')

def print_first_letter(word):
    print(word[0])

def First_letter_words(text):
    list_by_text = text.split(' ')
    list_first_letters = []
    for word in list_by_text:
        list_first_letters.append(word[0])
    return list_first_letters

# print_first_letter(list_a[0])
# print_first_letter(list_a[1])
# print_first_letter(list_a[2])
# print_first_letter(list_a[3])

print(First_letter_words(a));

print(list_a[0][-1])
print(list_a[1][-1])
print(list_a[2][-1])
print(list_a[3][-1])

print(a[6:9])
print(a[:5])
print(a[17:])
slice_a = a.find("Second")
print(slice_a)
print(a[slice_a:])
b = a[::2]
print(b)
c = a[1::2]
print(c)
revers_a = a[::-1]
print(revers_a)