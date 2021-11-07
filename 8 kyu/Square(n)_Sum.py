"""8 kyu
Square(n) Sum

Complete the square sum function so that it squares each number passed into it and then sums the results together.

For example, for [1, 2, 2] it should return 9 because 1^2 + 2^2 + 2^2 = 9"""

def square_sum(numbers):
    y=[]
    for i in numbers:
        i = i**2
        i = int(i)
        y.append(i)
    return sum(y)

### how this works
x=[1, 2, 2]
y = []
for i in x:
    i = i**2
    i = int(i)
    y.append(i)
print(sum(y))