"""8 kyu
Reversed Strings
Complete the solution so that it reverses the string passed into it.

'world'  =>  'dlrow'
'word'   =>  'drow'
"""
def solution(string):
    return ''.join(reversed(string))

### how it work
name = "Hello"
print(''.join(reversed(name)))