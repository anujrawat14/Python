# Object Types / Data Types

- Number : 1234, 3.1415, 3+4j, 0b111, Decimal(), Fraction()
- String : 'spam', "Bob's", b'a\x01c', u'sp\xc4m'
- List : [1, [2, 'three'], 4.5], list(range(10))
- Tuple : (1, 'spam', 4, 'U'), tuple('spam'), namedtuple()
- Dictionary : {'food': 'spam', 'taste': 'yum'}, dict(hours=10)

- Set : set('abc'), {'a', 'b', 'c'}

- File : open('eggs.txt'), open(r'C:\ham.bin', 'wb')

- Boolean : True, False
- None : None
- Functions, modules, classes

- Advance: Decorators, Generators, Iterators, MetaProgramming

```python
>>> 12+12
24
>>> 2.5+6
8.5
>>> import math
>>> math.pow(2,4)
16.0
>>> import random
>>> random.choice([1,2,3])
1
>>> random.choice([1,2,3])
2
>>> random.choice([1,2,3])
2
>>> username="anuj"
>>> len(username)
4
>>> username[1]
'n'
>>> username[1:4]
'nuj'
>>> dir(username) 
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> mylist=[123,"an",1.2]
>>> mylist
[123, 'an', 1.2]
>>> len(mylist)
3
>>> myD=('one':"supermna","two":"hanuman"}
  File "<stdin>", line 1
    myD=('one':"supermna","two":"hanuman"}
              ^
SyntaxError: invalid syntax
>>> myD={'one':"supermna","two":"hanuman"}
>>> myD
{'one': 'supermna', 'two': 'hanuman'}
>>> myD['two']
'hanuman'
>>> mytup=(1,2,4)
>>> mytup[0]
1
>>> len(mytup)\
... len(mytup) 
  File "<stdin>", line 2
    len(mytup)
    ^^^
SyntaxError: invalid syntax
>>> len(mytup)
3
>>> 
```