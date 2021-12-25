"""7 kyu
Longest vowel chain
The vowel substrings in the word codewarriors are o,e,a,io. The longest of these has a length of 2.
Given a lowercase string that has alphabetic characters only (both vowels and consonants) and no spaces,
return the length of the longest vowel substring. Vowels are any of aeiou.

Good luck!

If you like substring Katas, please try:

Non-even substrings

Vowel-consonant lexicon
Fundamentals
Strings"""

# def solve(s):
#     check = "aeiou"
#     vowel_string = ""
#     vowel_list = []
#     for i in s:
#         if i in check:
#             vowel_string += i
#         else:
#             vowel_list.append(vowel_string)
#             vowel_string = ""
#     return len(max(vowel_list, key=len))


# How this works
def main():
    print(solve("iiihoovaeaaaoougjyaw"))


def solve(s):
    check = "aeiou"
    vowel_string = ""
    vowel_list = []
    for i in s:
        if i in check:
            vowel_string += i
        else:
            vowel_list.append(vowel_string)
            vowel_string = ""
    return len(max(vowel_list, key=len))


if __name__ == "__main__":
    main()
