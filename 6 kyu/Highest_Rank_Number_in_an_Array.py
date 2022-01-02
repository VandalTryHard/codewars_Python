"""
6 kyu
Highest Rank Number in an Array

Complete the method which returns the number which is most frequent in the given input array.
If there is a tie for most frequent number, return the largest number among them.

Note: no empty arrays will be given.
Examples

[12, 10, 8, 12, 7, 6, 4, 10, 12]              -->  12
[12, 10, 8, 12, 7, 6, 4, 10, 12, 10]          -->  12
[12, 10, 8, 8, 3, 3, 3, 3, 2, 4, 10, 12, 10]  -->   3

Fundamentals
Arrays
Objects
"""

"""
def highest_rank(arr):
    return sorted(arr, key=lambda x: (arr.count(x), x))[-1]
"""
# How this works
def main():
    print(highest_rank([12, 10, 8, 12, 7, 6, 4, 10, 12]))
    print(highest_rank([12, 10, 8, 12, 7, 6, 4, 10, 10]))


def highest_rank(arr):
    return sorted(arr, key=lambda x: (arr.count(x), x))[-1]


if __name__ == "__main__":
    main()
