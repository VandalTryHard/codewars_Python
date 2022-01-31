"""8 kyu
Check same case

Write a function that will check if two given characters are the same case.

    If any of characters is not a letter, return -1
    If both characters are the same case, return 1
    If both characters are letters and not the same case, return 0

Examples

'a' and 'g' returns 1

'A' and 'C' returns 1

'b' and 'G' returns 0

'B' and 'g' returns 0

'0' and '?' returns -1
Fundamentals
"""


# How this works
def main():
    print(same_case('C', 'B'))


def same_case(a, b):
    return a.isupper() == b.isupper() if a.isalpha() and b.isalpha() else -1


main()
