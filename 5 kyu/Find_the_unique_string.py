"""
5 kyu
Find the unique string

There is an array of strings. All strings contains similar letters except one. Try to find it!

find_uniq([ 'Aa', 'aaa', 'aaaaa', 'BbBb', 'Aaaa', 'AaAaAa', 'a' ]) # => 'BbBb'
find_uniq([ 'abc', 'acb', 'bac', 'foo', 'bca', 'cab', 'cba' ]) # => 'foo'

Strings may contain spaces. Spaces are not significant, only non-spaces symbols matters. E.g. string that contains only
spaces is like empty string.

It’s guaranteed that array contains more than 3 strings.

This is the second kata in series:

    Find the unique number
    Find the unique string (this kata)
    Find The Unique

Algorithms
Fundamentals
Arrays
Strings
"""

"""
def find_uniq(arr):
    A = sorted([["".join(sorted(set(i.replace(" ", "").upper()))), i] for i in arr])
    if A[0][0] == A[1][0]:
        return A[-1][1]
    else:
        return A[0][1]
"""


# How this works
def main():
    print(find_uniq(['Aa', 'aaa', 'aaaaa', 'BbBb', 'Aaaa', 'AaAaAa', 'a']))


def find_uniq(arr):
    A = sorted([["".join(sorted(set(i.replace(" ", "").upper()))), i] for i in arr])
    if A[0][0] == A[1][0]:
        return A[-1][1]
    else:
        return A[0][1]


main()
