def is_an_number(number):
    if type(number) == int or type(number) == float :
        return round(number)
    else :
        return False
        

def is_even(number) :
    if (number % 2) == 0:
        return True
    else :
        return False

def is_odd(number) :
    if (number % 2) == 0:
        return False
    else :
        return True      


def hello_world():
    return "Hello world!"  