def add(n1, n2):
    '''returns the addition of two numbers'''
    return n1 + n2


def subtract(n1, n2):
    '''returns the subtraction of two numbers'''
    return n1 - n2


def multiply(n1, n2):
    '''returns the multiplication of two numbers'''
    return n1 * n2


def divide(n1, n2):
    '''returns the division of two numbers'''
    if n2 == 0:
        print("Zero Error. Operation Cannot be Performed.")
        return 0
    return n1 / n2
