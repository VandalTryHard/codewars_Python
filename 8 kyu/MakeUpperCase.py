"""
8 kyu
MakeUpperCase

Write a function which converts the input string to uppercase.
Fundamentals
"""

"""
def make_upper_case(s):
    new_s = ""
    for i in s:
        new_s = new_s + i.title()
    return new_s
        
or

def make_upper_case(s):
    return s.upper()
"""

# How this works
def main():
    print(make_upper_case("hello"))


def make_upper_case(s):
    return s.upper()


main()