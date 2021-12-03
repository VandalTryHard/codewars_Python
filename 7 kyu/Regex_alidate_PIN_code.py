"""7 kyu
Regex validate PIN code
ATM machines allow 4 or 6 digit PIN codes and PIN codes cannot contain anything but exactly 4 digits or exactly 6 digits.

If the function is passed a valid PIN string, return true, else return false.
Examples (Input --> Output)

"1234"   -->  true
"12345"  -->  false
"a234"   -->  false

Fundamentals
Regular Expressions
Declarative Programming
Advanced Language Features
Strings"""

# How this works
pin1 = "1234"
pin2 = "12345"
pin3 = "123456"
pin4 = ".234"
pin5 = "-12345"


def validate_pin(pin):
    if len(pin) == 4 or len(pin) == 6:
        try:
            pin = int(pin)
            print(True)
        except ValueError:
            print(False)
    else:
        print(False)


validate_pin(pin1)
validate_pin(pin2)
validate_pin(pin3)
validate_pin(pin4)
validate_pin(pin5)
