"""7 kyu
Disemvowel Trolls

Trolls are attacking your comment section!

A common way to deal with this situation is to remove all of the vowels from the trolls' comments, neutralizing the threat.

Your task is to write a function that takes a string and return a new string with all vowels removed.

For example, the string "This website is for losers LOL!" would become "Ths wbst s fr lsrs LL!".

Note: for this kata y isn't considered a vowel."""

def disemvowel(string_):
    return ''.join(i for i in string_ if i not in 'aeiouAEIOU')


### how this works
# list_ban = ['a', 'e', 'i', 'o', 'u']
string = "This website is for losers LOL!"
string = ''.join(i for i in string if i not in 'aeiouAEIOU')
print(string)
# newString = ""
# for i in string:
#     if i in list_ban:
#         string.remove(i)
#         print(string)