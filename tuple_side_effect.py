import os
os.system('color')

class Style():
    GREEN = lambda x: "\033[92m" + x + "\033[0m"
    RED = lambda x: "\033[31m" + x +"\033[0m"
    BLUE = lambda x: "\033[34m" + x + "\033[0m"

l = [1, 2, 3]  # mutable obj
d = {'a': 1, 'b': 2}
s = 'str'  # immutable obj
i = 777
print(Style.RED(f' int: {i} (id --> {id(i)})\n str: {s} (id --> {id(s)})\n'),
      Style.GREEN(f'list: {l} (id --> {id(l)})\n dict: {d} (id --> {id(d)})'))
t = (s, l, d, i)
print(Style.BLUE(f'new tuple {t} (id --> {id(t)})'))
'''>>> ('str', [1, 2, 3], {'a': 1, 'b': 2}, 777)'''
s += 'ing'
i += 233
print(Style.RED(f'changed(new) int : {i} (id --> {id(i)})\nchanged(new) str: {s} (id --> {id(s)})'))

l.append(4)
d.update(c=3)
print(Style.GREEN(f'changed list: {l} (id --> {id(l)})\nchanged dict: {d} (id --> {id(d)})'))

print(Style.BLUE(f'changed tuple(be careful): {t} (id --> {id(t)})'))
'''>>> ('str', [1, 2, 3, 4], {'a': 1, 'b': 2, 'c': 3}, 777)'''
try:
    t[1] += [5, 6]
except Exception as e:
    print(e.__class__.__name__)
    """Traceback (most recent call last):
      File "<input>", line 1, in <module>
    TypeError: 'tuple' object does not support item assignment"""
print(t)
# >>> ('str', [1, 2, 3, 4, 5])