"""
6 kyu
Format a string of names like 'Bart, Lisa & Maggie'.

Given: an array containing hashes of names

Return: a string formatted as a list of names separated by commas except for the last two names, which should be
separated by an ampersand.

Example:

namelist([ {'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'} ])
# returns 'Bart, Lisa & Maggie'

namelist([ {'name': 'Bart'}, {'name': 'Lisa'} ])
# returns 'Bart & Lisa'

namelist([ {'name': 'Bart'} ])
# returns 'Bart'

namelist([])
# returns ''

Note: all the hashes are pre-validated and will only contain A-Z, a-z, '-' and '.'.
Fundamentals
Strings
Formatting
Algorithms
"""

"""
def namelist(names):
    toReturn = ''
    if len(names) == 1:
        return names[0]['name']
    elif len(names) == 2:
        toReturn = toReturn + names[0]['name'] + " & " + names[1]['name']
    elif len(names) > 2:
        for i in range(0, len(names) - 1):
            toReturn = toReturn + names[i]['name'] + ", "
        toReturn = toReturn[:-2] + " & " + names[len(names) - 1]['name']
    return toReturn
"""

# How this works
def main():
    print(namelist([{'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'}]))
    print(namelist([{'name': 'Bart'}]))
    print(namelist([]))


def namelist(names):
    toReturn = ''
    if len(names) == 1:
        return names[0]['name']
    elif len(names) == 2:
        toReturn = toReturn + names[0]['name'] + " & " + names[1]['name']
    elif len(names) > 2:
        for i in range(0, len(names) - 1):
            toReturn = toReturn + names[i]['name'] + ", "
        toReturn = toReturn[:-2] + " & " + names[len(names) - 1]['name']
    return toReturn


main()
