"""8 kyu
If you can't sleep, just count sheep!!
If you can't sleep, just count sheep!!
Task:

Given a non-negative integer, 3 for example, return a string with a murmur: "1 sheep...2 sheep...3 sheep...". Input
will always be valid, i.e. no negative integers.
Fundamentals Loops Control Flow Basic Language Features """


# def count_sheep(n):
#     list_ = []
#     for i in range(n):
#         ke = f"{i + 1} sheep..."
#         list_.append(ke)
#     return "".join(list_)

# How this works
def count_sheep(n):
    list_ = []
    for i in range(n):
        ke = f"{i + 1} sheep..."
        list_.append(ke)
    return "".join(list_)


print(count_sheep(5))
