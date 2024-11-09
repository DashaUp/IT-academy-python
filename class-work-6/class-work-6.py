try:
    print('start code')
    print(10 / 0)
    print('No errors')
except (NameError, ZeroDivisionError) as ex :
    print(f'we heve an error: {ex}')
print('code after')

try:
    print('start code')
    #print(10 / 0)
    print('No errors')
except (NameError, ZeroDivisionError) as ex :
    print(f'we heve an error: {ex}')
else:
    print('I am ELSE')
finally:
    print("fanally code")


def checker(value):
    if not isinstance(value, str):
        raise TypeError(f"Sorry we cannot work with {type(value)}."
                        f"We need only str"
        )
    else:
        return 'NiiiiiiiCeeeeeee' + value

#checker(100)

class BuildingError(Exception):
    def __init__(self, msg, amount, limit):
        self.msg = msg
        self.amount = amount
        self.limit = limit
    def __str__(self):
        return (f'Not enought materials to build.'
                f'we nedd at leastc{self.limit}, but got {self.amount}!')

def check_materials(amount, limit):
    if amount >= limit:
        print('yes! we can build the house')
    else:
        raise BuildingError(amount, limit)

#check_materials(100, 250)



import warnings

warnings.simplefilter('always', ImportWarning)
warnings.simplefilter('always', SyntaxWarning)
warnings.simplefilter('ignore', ImportWarning)

warnings.warn('warning, no code here', SyntaxWarning)
warnings.warn('warning, wrong import', SyntaxWarning)

print("Hello world!")
warnings.simplefilter('error', ImportWarning)
try:
    warnings.warn('warning, wrong import', SyntaxWarning)
except:
    print('warning processed')
