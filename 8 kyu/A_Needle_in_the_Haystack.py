"""8 kyu
A Needle in the Haystack
Can you find the needle in the haystack?

Write a function findNeedle() that takes an array full of junk but containing one "needle"

After your function finds the needle it should return a message (as a string) that says:

"found the needle at position " plus the index it found the needle, so:

find_needle(['hay', 'junk', 'hay', 'hay', 'moreJunk', 'needle', 'randomJunk'])

should return "found the needle at position 5"
"""

# def find_needle(haystack):
#     return "found the needle at position " + str(haystack.index("needle"))

### how this works
list_ = ['hay', 'junk', 'hay', 'hay', 'moreJunk', 'needle', 'randomJunk']
print("found the needle at position " + {list_.index('needle')})