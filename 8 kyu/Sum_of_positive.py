"""8 kyu
Sum of positive

You get an array of numbers, return the sum of all of the positives ones.

Example [1,-4,7,12] => 1 + 7 + 12 = 20

Note: if there is nothing to sum, the sum is default to 0.
"""
def positive_sum(arr):
    x = 0
    for i in arr:
        if i >= 0:
            x = i + x
    return x

# how this works
sumList = [1, -4, 7, 12]
x = 0
for i in sumList:
    if i >= 0:
        x = i + x
        print(x)
print(x)