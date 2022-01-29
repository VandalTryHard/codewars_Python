"""
8 kyu
Vowel remover

Create a function called shortcut to remove the lowercase vowels (a, e, i, o, u ) in a given string.
Examples

"hello"     -->  "hll"
"codewars"  -->  "cdwrs"
"goodbye"   -->  "gdby"
"HELLO"     -->  "HELLO"

    don't worry about uppercase vowels
    y is not considered a vowel for this kata

Fundamentals
Strings
Parsing
Algorithms
"""


# How this works
def main():
    print(shortcut('hello'))


def shortcut(s):
    new_s = ""
    test_ = ['a', 'e', 'i', 'o', 'u']
    for i in s:
        if i in test_:
            new_s = new_s + ""
        else:
            new_s = new_s + i
    return new_s


main()
