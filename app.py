from collections import Counter
from typing import Coroutine
def addition(*numbers):
    sum = 0
    for i in numbers:
        sum += i

    return sum

def multiplication(*numbers):
    if len(numbers) == 0:
        return 0
    product = 1
    for i in numbers:
        product *= i

    return product

def uniqueInArray(numbers):

    count = Counter(numbers)
    for i,j in count.items():
        if j == 1:
            return i
    
    return -1
    

