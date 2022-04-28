import time


class TimeUpError(Exception):
    """Raises an exception if execution time is more than 1 second"""
    def __init__(self, exec_time, message="Execution time must be less than 1 sec"):
        self.exec_time = exec_time
        self.message = message

    def __str__(self):
        return f"{self.message}, instead: {self.exec_time} sec"


def measure_time(function):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = function(*args, **kwargs)
        end = time.time()
        final_time = end - start
        if final_time > 1:
            raise TimeUpError(final_time)
        else:
            return result
    return wrapper


@measure_time
def factorial(number):
    num = 1
    for i in range(2, number+1):
        num *= i
    return num
