from pprint import pprint

# '__iter__' in dir(collection)

'''There are four collection data types in the Python programming language:

List is a collection which is ordered and changeable. Allows duplicate members.
Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
Set is a collection which is unordered and unindexed. No duplicate members.
Dictionary is a collection which is ordered* and changeable. No duplicate members.
Strings in Python are arrays of bytes representing unicode characters, 
however, Python does not have a character data type, a single character is simply a string with a length of 1'''

_int = 9999
_str = "132456789AB"
_tuple = (1, 'string', (2, 3.5))

_list = ['abc', 123, {'lol': 101}]  # collection of objects diff types
_dict = {'str': {15: 'str'}, 51: 'rts'}  # container for objects `key: value`, key __hash__ble type
_set = {1, 's', ('t', 2)}  # container for unique immutable(__hash__ed) objects
_set_ = set(_dict)  # can create only from iterable

print("_____________________iter_object____________________________")
itr = iter(_dict)  # create iter object from iterable(has __iter__ method)
# print(f"{type(_set)} have __iter__ method: {'__iter__' in dir(itr)}")
# print('__next__' in dir(itr))
print("_____________________list_comprehension_____________________")

list_compr = [tuple(x) for x in zip(_str, _set)]
print(list_compr)
print(sorted(list_compr))  # sorted(Iterable object) -> New sorted object
print(list_compr)
print("_____________________python_generator______________________")

def generator(num, pow):
    for i in range(num):
        if i > 2:
            return None
        else:
            yield i**pow

for n in generator(4, 2):
    print(n)
print("_____________________mutable_tuple__________________________")

test_list = [0, 1, 2, 3, 4, 5]
test_dict = {'a': 101, 'b': 102, }
# print(len(test_dict))
mutable_tuple = ('str', test_list)  # wtf!
# print(id(mutable_tuple))
test_list += [7, 8, 9, 10, ]
# print(id(mutable_tuple))
# print(mutable_tuple)
print("_____________________*args_vs_**kwargs_unpacking____________")
# *args - tuple of positions arguments
# **kwargs - dict of key-value arguments
test_list = [1, 2, 3, ]
test_dict = {'a': 101, 'b': 102, }
# print('Pos arg1: {}, Pos arg2: {}\nKey-Val arg1: {a}, Key-Val arg2: {b}'.format(*test_list, **test_dict))
print("_____________________python_Classes_________________________")


class Person:
    count = 0
    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name
        type(self).count += 1

person1 = Person('Guido', 'Rossum')
person2 = Person('Linus', 'Torvalds')
# print('Person count: {}\nperson1 name:{}\nperson2 name:{}'.format(person1.count, person1.first_name, person2.first_name,))
print("_______________________________________________")

# print(test_dict['a'])
# print(test_list[2])
# print('s' in _set)
print("_______________________________________________")
# pprint(dir(_dict))
print("_______________________________________________")
val = _dict.keys()
# pprint(type(val))
# ''.join()  # can only join an iterable of str type
