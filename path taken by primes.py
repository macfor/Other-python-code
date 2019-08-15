"""
This is code that plots the result of if you had a repeated unit line segments that turns left by 60degrees on primes
and turns right 60 degrees on non primes.
finished 15/8/19 by Michael Howlett
"""
import matplotlib.pyplot as py
import time


def if_prime(x, primes):
    """
    checks to see if x is a prime
    :param x: variable being checked
    :param primes: list of primes
    :return: true if prime. false if not prime.
    """
    for p in primes:
        if p**2 > x:
            return True
        if x % p == 0:
            return False
    print(x)
    return "error"


def find_primes(n):
    """
    finds all primes up to n
    only checks numbers that are a multiple of 6 +-1 to improve speed.
    """
    primes = [2, 3]
    for i in range(int(n/6)+1):  # for each multiple of 6
        i += 1
        if if_prime((6*i)-1, primes):
            primes.append((6*i)-1)
        if if_prime((6*i)+1, primes):
            primes.append((6 * i) + 1)
    return primes


def right(direction):
    """
    turns direction right 60 degrees
    uses if statements rather than matrix multiplication to simplify
    :param direction: current direction
    :return: direction after turning
    """
    if direction == [1, 0]:
        return [1/2, -(3**0.5)/2]
    if direction == [1/2, -(3**0.5)/2]:
        return [-1/2, -(3**0.5)/2]
    if direction == [-1/2, -(3**0.5)/2]:
        return [-1, 0]
    if direction == [-1, 0]:
        return [-1/2, (3**0.5)/2]
    if direction == [-1/2, (3**0.5)/2]:
        return [1/2, (3**0.5)/2]
    if direction == [1/2, (3**0.5)/2]:
        return [1, 0]
    print("error")  # the direction is unknown
    return [1, 0]


def left(direction):
    """
    turns direction left 60 degrees
    uses if statements rather than matrix multiplication to simplify
    :param direction: current direction
    :return: direction after turning
    """
    if direction == [1, 0]:
        return [1/2, (3**0.5)/2]
    if direction == [1/2, -(3**0.5)/2]:
        return [1, 0]
    if direction == [-1/2, -(3**0.5)/2]:
        return [1/2, -(3**0.5)/2]
    if direction == [-1, 0]:
        return [-1/2, -(3**0.5)/2]
    if direction == [-1/2, (3**0.5)/2]:
        return [-1, 0]
    if direction == [1/2, (3**0.5)/2]:
        return [-1/2, (3**0.5)/2]
    print("error")
    return [1, 0]


start = time.time()
n = 4  # how many steps to take
primes = find_primes(n+10)
primes.append(0)  # this prevents the code crashing from trying to get the next prime after retrieving the last prime.
print(time.time()-start)  # tells me how much time it took to find the primes
direc = [1, 0]  # current direction
position = [1, 0]  # current end of last line
x_values = [0, 1]  # the x values of each of the points at the end of lines
y_values = [0, 0]  # the y values of each of the points at the end of lines
i = 0
for p in range(2, n+1):
    if p == primes[i]:  # if the number has reached the next prime. i.e. is it prime
        direc = left(direc)  # turn left
        i += 1  # as the ith prime has been reached,
    else:
        direc = right(direc)  # as the number isn't prime, turn right
    position = [position[0]+direc[0], position[1]+direc[1]]  # move to next point
    x_values.append(position[0])  # keep record of points
    y_values.append(position[1])
py.plot(x_values, y_values)
print(time.time()-start)
py.show()
