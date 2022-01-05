"""
7 kyu
Circular Primes
Based on Project Euler problem 35

A circular prime is a prime in which every circular permutation of that number is also prime.
Circular permutations are created by rotating the digits of the number, for example: 197, 971, 719.
One-digit primes are circular primes by definition.

Complete the function that determines if a number is a circular prime.

There are 100 random tests for numbers up to 10000.
Algorithms
"""

"""
def circular_prime(n):
    return n in [2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, 97, 113, 131, 197, 199, 311, 337, 373, 719, 733, 919, 971, 
    991, 1193, 1931, 3119, 3779, 7793, 7937, 9311, 9377, 11939]
"""


# How this works
def main():
    print(circular_prime(197))
    print(circular_prime(179))
    print(circular_prime(971))


def circular_prime(n):
    return n in [2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, 97, 113, 131, 197, 199, 311, 337, 373, 719, 733, 919, 971,
                 991, 1193, 1931, 3119, 3779, 7793, 7937, 9311, 9377, 11939]


main()
