import logging
import timeit

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s:%(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

def SayHelpMe():
    print('god helpMe :( / with this home work')



def TimeExecution(func):
    def wrapper(*args, **kwargs):
        start = timeit.timeit ()
        try:
            result = func(*args, **kwargs)
            return result
        finally:
            end = timeit.timeit ()
            logging.info("Execution time:" + ((end - start) * 1000).__str__() + " ms; function:" + func.__name__ )

    return wrapper
@TimeExecution
def calculate(expression):
    return eval(expression)

#calculate = checker(calculate)
calculate("2+2")
print("Sdsfdf")
SayHelpMe()
