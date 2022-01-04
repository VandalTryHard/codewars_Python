"""
6 kyu
Create Phone Number
Write a function that accepts an array of 10 integers (between 0 and 9), that returns a string of those numbers in
the form of a phone number.
Example

create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) # => returns "(123) 456-7890"

The returned format must be correct in order to complete this challenge.
Don't forget the space after the closing parentheses!
Algorithms
Arrays
Strings
Loops
Control Flow
Basic Language Features
Fundamentals
Formatting
Regular Expressions
Declarative Programming
Advanced Language Features
"""

"""
def create_phone_number(n):
    listToString = "".join(str(e) for e in n)
    result = f"({listToString[0:3]}) {listToString[3:6]}-{listToString[6:]}"
    return result
"""


# How this works
def main():
    print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))


def create_phone_number(n):
    listToString = "".join(str(e) for e in n)
    result = f"({listToString[0:3]}) {listToString[3:6]}-{listToString[6:]}"
    return result


if __name__ == "__main__":
    main()
