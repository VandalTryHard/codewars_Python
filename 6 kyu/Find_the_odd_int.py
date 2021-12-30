"""
6 kyu
Find the odd int
Given an array of integers, find the one that appears an odd number of times.

There will always be only one integer that appears an odd number of times.
Examples

[7] should return 7, because it occurs 1 time (which is odd).
[0] should return 0, because it occurs 1 time (which is odd).
[1,1,2] should return 2, because it occurs 1 time (which is odd).
[0,1,0,1,0] should return 0, because it occurs 3 times (which is odd).
[1,2,2,3,3,3,4,3,3,3,2,2,1] should return 4, because it appears 1 time (which is odd).
Fundamentals
"""

"""
from collections import Counter

def find_it(seq):
    counts = list(Counter(seq).items())
    print(counts)
    for x in counts:
        if x[1] % 2 != 0:
            return x[0]
    return None
"""

# How this works
from collections import Counter


def main():
    print(find_it([20, 1, -1, 2, -2, 3, 3, 5, 5, 1, 2, 4, 20, 4, -1, -2, 5]))


def find_it(seq):
    counts = list(Counter(seq).items())
    print(counts)
    for x in counts:
        if x[1] % 2 != 0:
            return x[0]
    return None


if __name__ == "__main__":
    main()
