from datetime import datetime

LOGFILE = 'log_file.txt'


def file_logger(function):
    def _func(*args, **kwargs):
        print(datetime.now())
        result = function(*args, **kwargs)
        return result

    return _func


def loggertofile(logfile):
    def logger(function):
        def _func(*args, **kwargs):
            nonlocal logfile
            now = datetime.now()
            with open(logfile, 'a', encoding='utf-8') as log:
                log.write(f'вызов функции {function.__name__}, время - {now}\n')
                result = function(*args, **kwargs)
                log.write(f'аргументы {str(*args)}, {str(**kwargs)}, результат - {result}\n')
            return result

        return _func

    return logger



@loggertofile(LOGFILE)
def id(file):
    with open(file, 'r', encoding='utf-8') as f:
        ids = {'user1': [213, 213, 213, 15, 213],
               'user2': [54, 54, 119, 119, 119],
               'user3': [213, 98, 98, 35]}
        b = set()
        for x in ids.values():
            for y in x:
                b.add(y)
        c = list(b)
        c.sort()
        return c



if __name__ == '__main__':
    for c in id('logger2.py'):
        print(c)
