greeting = 'Hello Python!'
greeting_length = len(greeting)
print(len(greeting))

# Indexing
print(greeting[1])
print(greeting[6])
print(greeting[-1])
print(greeting[12])
print(greeting[-4])

# Slicing
print(greeting[2:5])
print(greeting[6:10])
print(greeting[2:5])
print(greeting[-5:-2])
print(greeting[2:])
print(greeting[:5])
print(greeting[:])
print(greeting[::2])
print(greeting[::1])
print(greeting[1::3])
print(greeting[1:9:3])
print(greeting[::-1])

#Выведите на печать вторую букву l из строки 'Hello Python!'
#Присвойте строку переменной, затем выведите на печать букву
greeting = 'Hello Python!'
print(greeting[3])
#Выведите на печать вторую букву l из строки 'Hello Python!'
#Сделайте это без присваивания строки переменной, в одной строке кода. Если не знаете, как это сделать, попробуйте погуглить
print('Hello Python!'[3])
#Выведите на печать 'He' из строки 'Hello Python!' минимум двумя способами
greeting = 'Hello Python!'
print(greeting[0:2])
print(greeting[:2])
#Создайте новую строку 'Path' из строки 'Hello Python!' путём конкатенации части строки и отсутствующего
#символа. Выведите новую строку на печать
greeting = 'Hello Python!'
new_string = greeting[6] + 'a' + greeting[8:10]
print(new_string)