"""7 kyu
Shortest Word
Simple, given a string of words, return the length of the shortest word(s).

String will never be empty and you do not need to account for different data types.
Fundamentals"""

# def find_short(s):
#     s = s.split()
#     l = []
#     for i in s:
#         l.append(len(i))
#     l.sort()
#     return l[0] # l: shortest word length

# How this works
s1 = "bitcoin take over the world maybe who knows perhaps"
s2 = "turns out random test cases are easier than writing out basic ones"
s3 = "lets talk about javascript the best language"
s4 = "i want to travel the world writing code one day"
s5 = "Lets all go on holiday somewhere very cold"
s6 = "Let's travel abroad shall we"


def find_short(s):
    s = s.split()
    listLen = []
    for i in s:
        listLen.append(len(i))
    listLen.sort()
    print(listLen[0])


find_short(s1)
find_short(s2)
find_short(s3)
find_short(s4)
find_short(s5)
find_short(s6)
