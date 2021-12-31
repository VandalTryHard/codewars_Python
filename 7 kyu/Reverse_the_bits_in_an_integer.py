"""
7 kyu
Reverse the bits in an integer
Write a function that reverses the bits in an integer.

For example, the number 417 is 110100001 in binary. Reversing the binary is 100001011 which is 267.

You can assume that the number is not negative.
Fundamentals
Bits
Binary
"""

"""
def reverse_bits(n):
    new_n = str(bin(n))[2:]
    new_n = "0b" + new_n[::-1]
    return int(new_n, 2)
"""


# How this works
def main():
    print(reverse_bits(417))


def reverse_bits(n):
    new_n = str(bin(n))[2:]
    new_n = "0b" + new_n[::-1]
    return int(new_n, 2)


main()
