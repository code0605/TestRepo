import doctest

def sub(a,b):
    """
>>> sub(4,5)
-1
>>> sub(9,0)
9
>>> sub(3,2)
1
>>> sub(0,0)
0
>>> sub('a','b')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 2, in sub
TypeError: unsupported operand type(s) for -: 'str' and 'str'
>>>
    """
    return a-b


doctest.testmod()
