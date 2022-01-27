"""
8 kyu
Convert number to reversed array of digits
Convert number to reversed array of digits

Given a random non-negative number, you have to return the digits of this number within an array in reverse order.
Example:

348597 => [7,9,5,8,4,3]
0 => [0]

Fundamentals
Numbers
Arrays
"""

"""
def digitize(n):
    return [int(i) for i in str(n)[::-1]]
"""

# How this works
def main():
    print(digitize(35231))


def digitize(n):
    return [int(i) for i in str(n)[::-1]]


main()
