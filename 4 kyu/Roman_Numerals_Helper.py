"""
4 kyu
Roman Numerals Helper

Create a RomanNumerals class that can convert a roman numeral to and from an integer value. It should follow the API
demonstrated in the examples below. Multiple roman numeral values will be tested for each helper method.

Modern Roman numerals are written by expressing each digit separately starting with the left most digit and skipping
any digit with a value of zero. In Roman numerals 1990 is rendered: 1000=M, 900=CM, 90=XC; resulting in MCMXC.
2008 is written as 2000=MM, 8=VIII; or MMVIII. 1666 uses each Roman symbol in descending order: MDCLXVI.

Input range : 1 <= n < 4000

In this kata 4 should be represented as IV, NOT as IIII (the "watchmaker's four").
Examples

RomanNumerals.to_roman(1000) # should return 'M'
RomanNumerals.from_roman('M') # should return 1000

Help
Symbol 	Value
I 	1
IV 	4
V 	5
X 	10
L 	50
C 	100
D 	500
M 	1000
Algorithms
Parsing
Strings
Type Conversion
"""

from itertools import groupby

"""A RomanNumerals helper object"""


class RomanNumerals(object):
  letters = [('M', 1000), ('CM', 900), ('D', 500), ('CD', 400), ('C', 100), ('XC', 90),
             ('L', 50), ('XL', 40), ('X', 10), ('IX', 9), ('V', 5), ('IV', 4), ('I', 1)]

  @classmethod
  def to_roman(cls, val):
    rom = []
    for l, v in cls.letters:
      m = val // v
      rom += m * [l]
      val -= m * v
    return ''.join(rom)

  @classmethod
  def from_roman(cls, rom):
    cumu = 0
    for l, v in cls.letters:
      while rom[:len(l)] == l:
        rom = rom[len(l):]
        cumu += v
      if not rom: break
    return cumu
