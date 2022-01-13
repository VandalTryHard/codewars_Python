"""
7 kyu
Mumbling

This time no story, no theory. The examples below show you how to write function accum:
Examples:

accum("abcd") -> "A-Bb-Ccc-Dddd"
accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
accum("cwAt") -> "C-Ww-Aaa-Tttt"

The parameter of accum is a string which includes only letters from a..z and A..Z.
Fundamentals
"""

"""
def accum(s):
    output = []
    for count, letter in enumerate(s):
        output.append(letter.upper() + letter.lower() * (count))
    return '-'.join(output)
"""

# How this works
def main():
    print(accum("ZpglnRxqenU"))


def accum(s):
    output = []
    for count, letter in enumerate(s):
        output.append(letter.upper() + letter.lower() * (count))
    return '-'.join(output)


main()
