# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Напишите программу, открывающую файл на чтение и считывающую построчно данные. При этом английские числительные должны
# заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.
file_obj = open('my_file_task4.txt', 'r')
file_obj_write = open('my_file_task4_copy.txt', 'w')
numeral_dict = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
for line in file_obj.readlines():
    numeral_name, num = line.rstrip('\n').split(' — ')
    file_obj_write.write(f'{numeral_dict[numeral_name]} - {num}\n')
file_obj.close()
file_obj_write.close()