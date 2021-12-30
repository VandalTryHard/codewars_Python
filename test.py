limit = 8
a, b = 1, 1
total = 0
while a <= limit:
    if a % 2 == 0:
        total += a
    a, b = b, a+b  # the real formula for Fibonacci sequence
print(total)
