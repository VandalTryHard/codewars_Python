"""8 kyu
Beginner - Lost Without a Map
Given an array of integers, return a new array with each value doubled.

For example:

[1, 2, 3] --> [2, 4, 6]
Fundamentals
Arrays
Numbers"""

# def maps(a):
#     new_a = []
#     for i in a:
#         new_a.append(i*2)
#     return new_a


# How this works

def maps(a):
    new_a = []
    for i in a:
        new_a.append(i*2)
    print(new_a)


n = [1, 2, 3, 4, 5, ]
maps(n)

