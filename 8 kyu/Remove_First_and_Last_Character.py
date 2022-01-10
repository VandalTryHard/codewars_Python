"""
8 kyu
Remove First and Last Character

It's pretty straightforward. Your goal is to create a function that removes the first and last characters of a string.
You're given one parameter, the original string. You don't have to worry with strings with less than two characters.
Fundamentals
Basic Language Features
Strings
"""

"""
def remove_char(s):
    return s[1:-1]
"""


# How this works
def main():
    print(remove_char('eloquent'))


def remove_char(s):
    return s[1:-1]


main()
