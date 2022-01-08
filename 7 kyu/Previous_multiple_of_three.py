"""
7 kyu
Previous multiple of three

Given a positive integer n: 0 < n < 1e6, remove the last digit until you're left with a number that is a
multiple of three.

Return n if the input is already a multiple of three, and return null/nil/None/-1 if no such number exists.
Examples

1      => null
25     => null
36     => 36
1244   => 12
952406 => 9

Fundamentals
"""

"""
def prev_mult_of_three(n):
    while n % 3:
        n //= 10
    return n or None
"""

# How this works
def main():
    print(prev_mult_of_three(25))
    print(prev_mult_of_three(36))
    print(prev_mult_of_three(1244))
    print(prev_mult_of_three(62814))


def prev_mult_of_three(n):
    while n % 3:
        n //= 10
    return n or None


main()
