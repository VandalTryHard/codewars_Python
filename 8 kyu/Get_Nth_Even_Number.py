"""
8 kyu
Get Nth Even Number
Return the Nth Even Number

Example(Input --> Output)

1 --> 0 (the first even number is 0)
3 --> 4 (the 3rd even number is 4 (0, 2, 4))
100 --> 198
1298734 --> 2597466

The input will not be 0.
Puzzles
Mathematics
Algorithms
Numbers
Games
"""

"""
def nth_even(n):
    return (n*2)-2
"""


def main():
    print(nth_even(1))
    print(nth_even(100))
    print(nth_even(1298734))


def nth_even(n):
    return (n*2)-2


main()
