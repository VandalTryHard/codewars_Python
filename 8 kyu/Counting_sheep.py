"""8 kyu
Counting sheep...
Consider an array/list of sheep where some sheep may be missing from their place. We need a function that counts the
number of sheep present in the array (true means present).
For example,
[True,  True,  True,  False,
  True,  True,  True,  True ,
  True,  False, True,  False,
  True,  False, False, True ,
  True,  True,  True,  True ,
  False, False, True,  True]
The correct answer would be 17.
Hint: Don't forget to check for bad values like null/undefined
Fundamentals
Arrays"""

# def count_sheeps(sheep):
#     result = 0
#     for ewe in sheep:
#         if ewe:
#             result = result + 1
#         elif not ewe:
#             result = result
#
#     return result


# How this works

def count_sheeps(array):
    result = 0
    for sheep in array:
        if sheep:
            result = result + 1
        elif not sheep:
            result = result

    return result


array1 = [True, True, True, False,
          True, True, True, True,
          True, False, True, False,
          True, False, False, True,
          True, True, True, True,
          False, False, True, True]

print(count_sheeps(array1))
