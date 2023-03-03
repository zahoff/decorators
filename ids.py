ids = {'user1': [213, 213, 213, 15, 213],
       'user2': [54, 54, 119, 119, 119],
       'user3': [213, 98, 98, 35]}
b = set()
for x in ids.values():
  for y in x:
    b.add(y)
c = list(b)
c.sort()
print(c)

