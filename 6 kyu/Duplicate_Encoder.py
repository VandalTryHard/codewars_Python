"""
6 kyu
Duplicate Encoder

The goal of this exercise is to convert a string to a new string where each character in the new string is "("
if that character appears only once in the original string, or ")" if that character appears more than once in the
original string. Ignore capitalization when determining if a character is a duplicate.
Examples

"din"      =>  "((("
"recede"   =>  "()()()"
"Success"  =>  ")())())"
"(( @"     =>  "))(("

Notes

Assertion messages may be unclear about what they display in some languages. If you read "...It Should encode XXX", the
"XXX" is the expected result, not the input!
Fundamentals
Strings
Arrays
"""

"""
def duplicate_encode(word):
    iter_word = str(word.lower())
    check_list = []
    formatted_list = []
    position = 0
    for i in iter_word:
        position += 1
        if i not in check_list and i not in (iter_word[position:]):
            check_list.append(i)
            formatted_list.append("(")
        else:
            check_list.append(i)
            formatted_list.append(")")
    return "".join(map(str, formatted_list))
    
    
# or
def duplicate_encode(word):
    return "".join(["(" if word.lower().count(c) == 1 else ")" for c in word.lower()])
"""

# How this works
def main():
    print(duplicate_encode("din"))
    print(duplicate_encode("Success"))
    print(duplicate_encode("recede"))


def duplicate_encode(word):
    iter_word = str(word.lower())
    check_list = []
    formatted_list = []
    position = 0
    for i in iter_word:
        position += 1
        if i not in check_list and i not in (iter_word[position:]):
            check_list.append(i)
            formatted_list.append("(")
        else:
            check_list.append(i)
            formatted_list.append(")")
    return "".join(map(str, formatted_list))


main()
