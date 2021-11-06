"""8 kyu
Even or Odd
Create a function that takes an integer as an argument and returns "Even" for even numbers or "Odd" for odd numbers."""

def even_or_odd(number):
    if number%2 == 0:
        return "Even"
    elif number%2 != 0:
        return "Odd"

##### how its work
number = 3 
if number%2 == 0:
    print("Even")
elif number%2 != 0:
    print("Odd")
else:
    print("Wtf")