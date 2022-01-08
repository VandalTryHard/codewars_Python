"""
7 kyu
Simple remove duplicates

Remove the duplicates from a list of integers, keeping the last ( rightmost ) occurrence of each element.
Example:

For input: [3, 4, 4, 3, 6, 3]

    remove the 3 at index 0
    remove the 4 at index 1
    remove the 3 at index 3

Expected output: [4, 6, 3]

More examples can be found in the test cases.

Good luck!
Fundamentals
"""

"""
def solve(arr):
    new_arr = []
    for i in arr:
        if i in new_arr:
            new_arr.remove(i)
            new_arr.append(i)
        else:
            new_arr.append(i)
    return new_arr
"""


# How this works
def main():
    print(solve([3, 4, 4, 3, 6, 3]))
    print(solve([1, 2, 1, 2, 1, 2, 3]))


def solve(arr):
    new_arr = []
    for i in arr:
        if i in new_arr:
            new_arr.remove(i)
            new_arr.append(i)
        else:
            new_arr.append(i)
    return new_arr


main()
