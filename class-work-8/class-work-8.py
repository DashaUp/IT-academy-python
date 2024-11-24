
import logging

logging.basicConfig(
    level=logging.DEBUG,
    filename='lesson8.log',
    filemode='w',
    format='%(asctime)s:%(levelname)s - %(message)s'
)

try:
    print(10/0)
except ZeroDivisionError as ex:
    logging.exception(f'exception: {ex}')


if 2 + 2 == 4:
    print('Yes, 2+2+=4')

#assert 2 + 2 == 5, 'wrong result'


"""
>>> 2+2
5
"""
"""if __name__ == '__main__':
    import doctest
    doctest.testmod()"""

def adder(*args, **kwargs):
    result = 0
    for i in args:
        if (isinstance(i, int) or
            isinstance(i, bool) or
            isinstance(i, float)
        ):
            result += i
        else:
            try:
                result+= int (i)
            except (ValueError, TypeError):
                pass

            try:
                result += float(i)
            except (ValueError, TypeError):
                pass

    for k in kwargs.values():
            if (
                isinstance ( k , int ) or
                isinstance ( k , bool ) or
                isinstance ( k , float )
            ):
                result += k
            else:
                try:
                    result += int ( k )
                except (ValueError , TypeError):
                    pass

                try:
                    result += float ( k )
                except (ValueError , TypeError):
                    pass

    return result