"""8 kyu
Count the Monkeys!
You take your son to the forest to see the monkeys. You know that there are a certain number there (n), but your son is
too young to just appreciate the full number, he has to start counting them from 1.

As a good parent, you will sit and count with him. Given the number (n), populate an array with all numbers up to and
including that number, but excluding zero.

For example:

monkeyCount(10) # --> [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
monkeyCount(1) # --> [1]

Algorithms
Arrays
Fundamentals
Ranges
Basic Language Features
Lists
Data Structures
"""

# def monkey_count(n):
#     list_monkey = []
#     for i in range(1, n+1):
#         list_monkey.append(i)
#     return list_monkey


# How this works
def monkey_count(n):
    list_monkey = []
    for i in range(1, n+1):
        list_monkey.append(i)
    print(list_monkey)


monkey_count(5)
