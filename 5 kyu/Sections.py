"""5 kyu
Sections

Consider the following equation of a surface S: z*z*z = x*x * y*y.
Take a cross section of S by a plane P: z = k where k is a positive integer (k > 0).
Call this cross section C(k).
Task

Find the number of points of C(k) whose coordinates are positive integers.
Examples

If we call c(k) the function which returns this number we have

c(1) -> 1
c(4) -> 4
c(4096576) -> 160
c(2019) -> 0 which means that no point of C(2019) has integer coordinates.

Notes

    k can go up to about 10,000,000,000
    Prolog: the function cis called section.
    COBOL: the function cis called sections.
    Please could you ask before translating : some translations are already written.

Fundamentals
"""

"""
def c(k):
    from math import sqrt
    root = int(sqrt(k))
    if (root * root != k):
        return 0
    i = 2; num = k * root; result = 1
    while (num > 1):
        div_num_nb = 0
        while (num % i == 0):
            num //= i
            div_num_nb += 1
        result *= div_num_nb + 1
        i += 1
    return result
"""


# How this works
def main():
    print(c(423128))


def c(k):
    from math import sqrt
    root = int(sqrt(k))
    if (root * root != k):
        return 0
    i = 2;
    num = k * root;
    result = 1
    while (num > 1):
        div_num_nb = 0
        while (num % i == 0):
            num //= i
            div_num_nb += 1
        result *= div_num_nb + 1
        i += 1
    return result


main()
