import math


def is_odd(N):
    return N%2 == 1
 

def is_even(N):
   return N%2 == 0


def is_prime(N):
    N_sqrt =int(math.sqrt(N))
    for I in range(2 ,N_sqrt):
        if N % I == 0:
            return False
    return True

