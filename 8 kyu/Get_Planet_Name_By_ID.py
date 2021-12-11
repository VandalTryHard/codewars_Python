"""8 kyu
Get Planet Name By ID
The function is not returning the correct values. Can you figure out why?

Example (Input --> Output ):

3 --> "Earth"

Bugs
Control Flow
Basic Language Features
Fundamentals"""

# def get_planet_name(plan):
#     if plan == 1:
#         return "Mercury"
#     elif plan == 2:
#         return "Venus"
#     elif plan == 3:
#         return "Earth"
#     elif plan == 4:
#         return "Mars"
#     elif plan == 5:
#         return "Jupiter"
#     elif plan == 6:
#         return "Saturn"
#     elif plan == 7:
#         return "Uranus"
#     else:
#         return "Neptune"


# How this works
def get_planet_name(plan):
    if plan == 1:
        return "Mercury"
    elif plan == 2:
        return "Venus"
    elif plan == 3:
        return "Earth"
    elif plan == 4:
        return "Mars"
    elif plan == 5:
        return "Jupiter"
    elif plan == 6:
        return "Saturn"
    elif plan == 7:
        return "Uranus"
    else:
        return "Neptune"


print(get_planet_name(7))
