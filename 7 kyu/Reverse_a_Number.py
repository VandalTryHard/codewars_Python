"""7 kyu
Reverse a Number
Given a number, write a function to output its reverse digits. (e.g. given 123 the answer is 321)
Numbers should preserve their sign; i.e. a negative number should still be negative when reversed.
Examples
 123 ->  321
-456 -> -654
1000 ->    1
"""


# def reverse_number(n):
#     if n < 0:
#         n = n * -1
#         n = str(n)
#         n = n[::-1]
#         n = int(n)
#         n = n * -1
#     else:
#         n = str(n)
#         n = n[::-1]
#         n = int(n)
#     return n

# How this works
def Reverse(num):
    if num < 0:
        num = num * -1
        num = str(num)
        num = num[::-1]
        num = int(num)
        num = num * -1
    else:
        num = str(num)
        num = num[::-1]
        num = int(num)
    print(num)


Reverse(123)
