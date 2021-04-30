from math import sqrt
import time
import numpy as np # importing numpy

def solution_1 (n): # in this case n = 1000

    start = time.time()

    sum = 0

    multiples_of_3 = np.arange(3, n, 3)
    multiples_of_5 = np.arange(5, n, 5)
    multiples_of_15 = np.arange(15, n, 15)

    sum = np.sum(multiples_of_3) + np.sum(multiples_of_5)  
    - np.sum(multiples_of_15)

    elapsed = time.time() - start

    print (sum, "Elapsed time: ", elapsed, "s")

    return

def solution_2(n):
    start = time.time()

    series = [1, 2]
    a3 = series[-1] + series[-2]

    while (a3 < n):
        a3 = series[-1] + series[-2]
        series.append(a3)

    evens = [series[x] for x in range(1,len(series), 3)]
    elapsed = time.time() - start
    print(np.sum(evens), elapsed)

    return

def trial_division_primes(n):
    factors = []
    for i in range (2,int(sqrt(n))):
        if n % i == 0:
            factors.append(i)
            factors.append(int(n/i))

    # We need to sort it, otherwise the algorithm won't work
    factors.sort()
    prime_factors = factors
    to_remove = []

    for i in range (len(factors)-1,0,-1):
        a = i-1
        for ii in range (a,-1,-1):
            if prime_factors[i] % prime_factors[ii] == 0:
                to_remove.append(prime_factors[i])
            a = a - 1

    prime_factors = list(set(set(prime_factors) - set(to_remove)))

    return prime_factors
def solution_3(n):
    start = time.time()

    prime_factors = trial_division_primes(n)
    prime_factors.sort()
    print (prime_factors)
    
    elapsed = time.time() - start
if __name__ == '__main__':
    solution_1(1000)
    solution_2(4000000)
    solution_3(600851475143) 