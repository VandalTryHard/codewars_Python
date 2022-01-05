"""
6 kyu
Find the unique number

There is an array with some numbers. All numbers are equal except for one. Try to find it!

find_uniq([ 1, 1, 1, 2, 1, 1 ]) == 2
find_uniq([ 0, 0, 0.55, 0, 0 ]) == 0.55

It’s guaranteed that array contains at least 3 numbers.

The tests contain some very huge arrays, so think about performance.

This is the first kata in series:

    Find the unique number (this kata)
    Find the unique string
    Find The Unique

Fundamentals
Algorithms
Numbers
Arrays
"""

"""
def find_uniq(arr):
    a, b = set(arr)
    return a if arr.count(a) == 1 else b
    
or

def find_uniq(arr):
    arr.sort()
    if arr[0] < arr[len(arr) - 1] and arr[0] < arr[len(arr) - 2]:
        n = arr[0]
    else:
        n = arr[len(arr) - 1]
    return n
"""

# How this works
def main():
    print(find_uniq([1, 1, 1, 2, 1, 1]))
    print(find_uniq([0, 0, 0.55, 0, 0]))
    print(find_uniq([3, 10, 3, 3, 3]))


def find_uniq(arr):
    a, b = set(arr)
    return a if arr.count(a) == 1 else b


main()
