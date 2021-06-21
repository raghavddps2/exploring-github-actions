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

