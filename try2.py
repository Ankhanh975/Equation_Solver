l = range(100)
total = 0
for x in l:
    total += x
print(total)

l = range(100)
total = 0
list(map(lambda x: (globals().__setitem__('total', x + total)), l))
print(total)

