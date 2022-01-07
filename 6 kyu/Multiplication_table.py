"""
6 kyu
Multiplication table

Your task, is to create NxN multiplication table, of size provided in parameter.

for example, when given size is 3:

1 2 3
2 4 6
3 6 9

for given example, the return value should be: [[1,2,3],[2,4,6],[3,6,9]]
Fundamentals
Arithmetic
Mathematics
Algorithms
Numbers
Arrays
"""

"""
def multiplication_table(size):
    columns = []
    for i in range(1,size+1):
        rows = []
        for j in range(1,size+1):
            rows.append(i*j)
        columns.append(rows)
        
    return columns
"""


# How this works
def main():
    print(multiplication_table(3))


def multiplication_table(size):
    columns = []
    for i in range(1, size + 1):
        rows = []
        for j in range(1, size + 1):
            rows.append(i * j)
        columns.append(rows)

    return columns


main()
