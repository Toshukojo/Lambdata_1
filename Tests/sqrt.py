# a function that writes the square root of a number
from math import sqrt

def squared(n):
    answer = sqrt(n)
    return answer
    
squared(4)

def lazy_sqrt(n):
    return n**0.5

lazy_sqrt(15)

def newton_sqrt(n):
    """Return the square root of x using Newton's Method."""
    val = n
    while True: 
        last = val
        val = (val + n / val) * 0.5
        if abs(val - last) < 1e-9:
            break
    return val
    
    
newton_sqrt(34)


def newton_sqrt2(n, guess=2):
    from numpy.testing import assert_almost_equal as eq
    if eq(newton_sqrt2(n, guess)**2, n):
        return guess
    else:
        guess = 0.5*(guess+n)
        return newton_sqrt(n, guess)
    








