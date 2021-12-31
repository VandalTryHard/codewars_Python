"""8 kyu
Switch it Up!
When provided with a number between 0-9, return it in words.

Input :: 1

Output :: "One".

If your language supports it, try using a switch statement.
Fundamentals"""

"""
def switch_it_up(number):
    dict_ = {0: "Zero",
             1: "One",
             2: "Two",
             3: "Three",
             4: "Four",
             5: "Five",
             6: "Six",
             7: "Seven",
             8: "Eight",
             9: "Nine"}
    return dict_[number]
"""

# How this works
def main():
    print(switch_it_up(9))


def switch_it_up(number):
    dict_ = {0: "Zero",
             1: "One",
             2: "Two",
             3: "Three",
             4: "Four",
             5: "Five",
             6: "Six",
             7: "Seven",
             8: "Eight",
             9: "Nine"}
    return dict_[number]


main()
