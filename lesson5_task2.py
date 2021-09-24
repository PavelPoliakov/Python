# Создать текстовый файл (не программно), сохранить в нём несколько строк, выполнить подсчёт строк и слов в каждой
# строке.
file_obj = open('my_file_task2.txt', 'r')
sum_string = 0
words_in_string = 0
for line in file_obj:
    sum_string += 1
    words_in_string = len(list(line.split()))
    print(f'В строке №{sum_string} находится {words_in_string} слов(а)')
print(f'В файле находится {sum_string} строк')
