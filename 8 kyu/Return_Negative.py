"""8 kyu
Return Negative
In this simple assignment you are given a number and have to make it negative. But maybe the number is already negative?
Examples
MakeNegative(1)    # return -1
MakeNegative(-5)   # return -5
MakeNegative(0)    # return 0
Notes
    The number can be negative already, in which case no change is required.
    Zero (0) is not checked for any specific sign. Negative zeros make no mathematical sense.
Fundamentals
Numbers"""


# def make_negative( number ):
#     if number < 0:
#         return number
#     else:
#         return -1*number

# How this works
def make_negative(number):
    if number < 0:
        print(number)
    else:
        print(-1 * number)


make_negative(-1)
make_negative(1)
make_negative(0)
