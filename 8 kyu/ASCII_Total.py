"""8 kyu
ASCII Total
You'll be given a string, and have to return the sum of all characters as an int. The function should be able to handle
all ASCII characters.

examples:

uniTotal("a") == 97 uniTotal("aaa") == 291
Fundamentals"""

"""
def uni_total(s):
    result = 0
    new_ = list(s)
    for i in new_:
        result = result + ord(i)
    return result
"""


# How this works
def main():
    print(uni_total("a"))
    print(uni_total(""))
    print(uni_total("Mary Had A Little Lamb"))


def uni_total(s):
    result = 0
    new_ = list(s)
    for i in new_:
        result = result + ord(i)
    return result


main()
