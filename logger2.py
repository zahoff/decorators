import logger

@logger.loggertofile('log_file2.txt')
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