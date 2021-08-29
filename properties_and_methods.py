# Immutable
first_name = 'Jake'
print(first_name[2])
# first_name[2] = 'n'
# print(first_name)

first_two_letters = first_name[:2]
print(first_two_letters)
last_letter = first_name[-1:]
print(last_letter)

# Concatenable
new_first_name = first_two_letters + 'n' + last_letter
print(new_first_name)

greeting = 'Hello'
greeting = greeting + ' Python!'
print(greeting)

# Multiplication
yummy = 'Yum '
print(yummy * 3)

print(yummy.upper())
print(yummy.lower())
print(yummy)

long_string = 'This is the long string'
print(long_string.split('s'))

#Создайте новую строку 'Path' из строки 'Hello Python!' путём конкатенации частей строки и
#отсутствующего символа. Выведите новую строку на печать
greeting = 'Hello Python!'
part1 = greeting[6]
part2 = greeting[-5:-3]
path = part1 + 'a' + part2
print(path)
#Создайте строку 'zzzzzzz' при помощи умножения и выведите её на экран
letter = 'z'
many_letter = letter * 7
print(many_letter)
#Сделайте все буквы строки из предыдущего вопроса заглавными и выведите её на экран
letter = 'z'
many_letter = letter * 7
print(many_letter.upper())