# x = 4
#
# if x > 3:
#     print('x > 3')
#     print('I\'m happy')
# elif x < 3:
#     print('x < 3')
# else:
#     print('x == 3')

# day_time = 'midnight'
#
# if day_time == 'morning':
#     print('Monster wakes up')
# elif day_time == 'afternoon':
#     print('Monster is walking')
# elif day_time == 'evening':
#     print('Monster is eating')
# elif day_time == 'night':
#     print('Monster is sleeping')
# else:
#     print('Monster is doing something')

# x = 41
# if x % 2 == 0:
#     print('x is even')
# else:
#     print('x is odd')
# print('Some text')

# user_input = input('Input something')
# if user_input == 'Hello':
#     print('Hello! Nice to meet you!')


# # False: 0, empty string, None, empty object
#
# if [1, 3]:
#     print('Something')

# 7


# Напишите код, который выводит сообщение: 'Enter any number'. Если было введено число 7, должно выводиться сообщение:
# '7 is a lucky number! Today is your lucky day!', если введено что-то другое - должно выводиться сообщение
# 'Thank you! Have a nice day!'
number = input('Enter any number')
if int(number) == 7:
    print('7 is a lucky number! Today is your lucky day!')
else:
    print('Thank you! Have a nice day!')

# Напишите код, который выводит сообщение: 'Enter an integer number'. Если было введено чётное число, должно
# выводиться сообщение: 'The number is even', если было введено нечётное число, должно выводиться сообщение
# 'The number is odd'
number = input('Enter an integer number')
if int(number)%2 == 0:
    print('The number is even')
else:
    print('The number is odd')
