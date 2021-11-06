"""7 kyu
Vowel Count
Return the number (count) of vowels in the given string.

We will consider a, e, i, o, u as vowels for this Kata (but not y).

The input string will only consist of lower case letters and/or spaces.
"""

def get_count(sentence):
    list_ = ['a', 'e', 'i', 'o', 'u']
    x = 0
    for i in sentence:
        if i in list_:
            x = x + 1
    return x

### how this works
list_ = ['a', 'e', 'i', 'o', 'u']
string = "Hello Python"
x=0
for i in string:
    if i in list_:
        x=x+1
print(x)
