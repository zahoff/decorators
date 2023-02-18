import os
import datetime

#Определяем декоратор, принимаем функцию как аргумент, определяем время работы
def dir_or_file_decorator(func):
    def newFunc(path):
        start = datetime.datetime.now()
        if os.path.isdir(path):
            filenames = os.listdir(path)
            for filename in filenames:
                filepath = os.path.join(path,filename)
                func(filepath)
        else:
            func(path)
        print(f'время работы {datetime.datetime.now() - start}')
    return newFunc

#Определяем функцию для декорирования
@dir_or_file_decorator
def print_file_name(filepath):
    print(filepath)

#Прогоняем тесты
print('Testing file')
print_file_name(r'c:\testdir\testfile1.txt')
print('Testing dir')
print_file_name(r'c:\testdir')

# Декоратор просто синтаксический сахар. Код ниже показывает, что реально происходит
def print_file_name2(filepath):
    print(filepath)

decorated_func = dir_or_file_decorator(print_file_name2)
print('Testing file')
decorated_func(r'c:\testdir\testfile1.txt')
print('Testing dir')
decorated_func(r'c:\testdir')