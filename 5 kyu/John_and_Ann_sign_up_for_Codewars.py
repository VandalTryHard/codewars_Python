"""
5 kyu
John and Ann sign up for Codewars

John and his wife Ann have decided to go to Codewars. On the first day Ann will do one kata and John - he wants to know
how it is working - 0 kata.

Let us call a(n) - and j(n) - the number of katas done by Ann - and John - at day n. We have a(0) = 1 and in the same
manner j(0) = 0.

They have chosen the following rules:

    On day n the number of katas done by Ann should be n minus the number of katas done by John at day t, t being equal
    to the number of katas done by Ann herself at day n - 1

    On day n the number of katas done by John should be n minus the number of katas done by Ann at day t,
    t being equal to the number of katas done by John himself at day n - 1

Whoops! I think they need to lay out a little clearer exactly what there're getting themselves into!
Could you write:

    functions ann(n) and john(n) that return the list of the number of katas Ann/John does on the first n days;
    functions sum_ann(n) and sum_john(n) that return the total number of katas done by Ann/John on the first n days

Examples:

john(11)  -->  [0, 0, 1, 2, 2, 3, 4, 4, 5, 6, 6]
ann(6)    -->  [1, 1, 2, 2, 3, 3]

sum_john(75)  -->  1720
sum_ann(150)  -->  6930

Note:

Keep an eye on performance.
Algorithms
Rules
Mathematics
Numbers
"""

"""
def j_n(n):
    j = [0]
    a = [1]
    for i in range(1, n):
        j.append((i - a[j[i - 1]]))
        a.append((i - j[a[i - 1]]))
    return j, a


def john(n):
    return j_n(n)[0]


def ann(n):
    return j_n(n)[1]


def sum_john(n):
    return sum(john(n))


def sum_ann(n):
    return sum(ann(n))
"""

# How this works
def main():
    print(john(11))
    print(ann(6))
    print(sum_john(75))
    print(sum_ann(115))


def j_n(n):
    j = [0]
    a = [1]
    for i in range(1, n):
        j.append((i - a[j[i - 1]]))
        a.append((i - j[a[i - 1]]))
    return j, a


def john(n):
    return j_n(n)[0]


def ann(n):
    return j_n(n)[1]


def sum_john(n):
    return sum(john(n))


def sum_ann(n):
    return sum(ann(n))
