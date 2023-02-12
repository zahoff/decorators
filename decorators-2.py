import os
import polog
from polog import config, log, file_writer

config.add_handlers(file_writer('main.log'))

def test_2():
    paths = ('log_1.log', 'log_2.log', 'log_3.log')
    if os.path.exists(path):
        os.remove(path)

    @log
    def hello_world():
        return 'Hello World'

    @log
    def summator(a, b=0):
        return a + b

    @log
    def div(a, b):
        return a / b

    assert 'Hello World' == hello_world(), "Функция возвращает 'Hello World'"
    result = summator(2, 2)
    assert isinstance(result, int), 'Должно вернуться целое число'
    assert result == 4, '2 + 2 = 4'
    result = div(6, 2)
    assert result == 3, '6 / 2 = 3'

    assert os.path.exists(path), 'файл main.log должен существовать'

    summator(4.3, b=2.2)
    summator(a=0, b=0)

    with open(path) as log_file:
        log_file_content = log_file.read()

if __name__ == '__main__':
    test_1()