"""
7 kyu
Reverse words

Complete the function that accepts a string parameter, and reverses each word in the string.
All spaces in the string should be retained.
Examples

"This is an example!" ==> "sihT si na !elpmaxe"
"double  spaces"      ==> "elbuod  secaps"

Fundamentals
Strings
"""

"""
def reverse_words(str):
    strList = []
    for word in str.split(' '):
        strList.append(word[::-1])
    return ' '.join(strList)
"""


# How this works
def main():
    print(reverse_words('The quick brown fox jumps over the lazy dog.'))
    print(reverse_words('double spaced words'))


def reverse_words(str):
    strList = []
    for word in str.split(' '):
        strList.append(word[::-1])
    return ' '.join(strList)


main()
