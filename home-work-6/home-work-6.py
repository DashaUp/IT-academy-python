import warnings

result = []
def divider(a, b):
    if a < b:
        raise ValueError('a should be greater than b')
    if b > 100:
        raise IndexError
    return a/b

'''
Traceback (most recent call last):
  File "D:\code\python\it-academy-python\home-work-6\home-work-6.py", line 11, in <module>
    data = {10: 2, 2: 5, "123": 4, 18: 0, []: 15, 8 : 4}
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: unhashable type: 'list'
'''
#data = {10: 2, 2: 5, "123": 4, 18: 0, []: 15, 8 : 4}

data = {10: 2, 2: 5, "123": 4, 18: 0, 8: 4}

for key in data:
    try:
        res = divider(key, data[key])
        result.append(res)
    except(ValueError, IndexError, TypeError, ZeroDivisionError) as exception:
        print(f'we have an error {exception.__class__.__name__}: {exception}')

print(result)
