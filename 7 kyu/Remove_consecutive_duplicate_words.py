"""
7 kyu
Remove consecutive duplicate words

Your task is to remove all consecutive duplicate words from a string, leaving only first words entries. For example:

"alpha beta beta gamma gamma gamma delta alpha beta beta gamma gamma gamma delta"

--> "alpha beta gamma delta alpha beta gamma delta"

Algorithms
Strings
Regular Expressions
Declarative Programming
Advanced Language Features
Fundamentals
"""


# How this works
def main():
    print(remove_consecutive_duplicates('alpha beta beta gamma gamma gamma delta alpha beta beta gamma gamma gamma '
                                        'delta'))


def remove_consecutive_duplicates(s):
    s = s.split(' ')
    output = [0]
    for word in s:
        if word != output[-1]:
            output.append(word)
    return ' '.join(output[1:])


main()
