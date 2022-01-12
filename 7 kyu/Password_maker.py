"""
7 kyu
Password maker

One suggestion to build a satisfactory password is to start with a memorable phrase or sentence and make a password by
extracting the first letter of each word.

Even better is to replace some of those letters with numbers (e.g., the letter O can be replaced with the number 0):

    instead of including i or I put the number 1 in the password;
    instead of including o or O put the number 0 in the password;
    instead of including s or S put the number 5 in the password.

Examples:

"Give me liberty or give me death"  --> "Gml0gmd"
"Keep Calm and Carry On"            --> "KCaC0"

Fundamentals
Strings
Regular Expressions
Declarative Programming
Advanced Language Features
"""

"""
def make_password(phrase):
    phraseList = phrase.split()
    password = ""
    for i in range(len(phraseList)):
        if phraseList[i][0] == "i" or phraseList[i][0] == "I":
            password = password + "1"
        elif phraseList[i][0] == "o" or phraseList[i][0] == "O":
            password = password + "0"
        elif phraseList[i][0] == "s" or phraseList[i][0] == "S":
            password = password + "5"
        else:
            password = password + phraseList[i][0]
    return password
"""

# How this works
def main():
    print(make_password("Give me liberty or give me death"))


def make_password(phrase):
    phraseList = phrase.split()
    password = ""
    for i in range(len(phraseList)):
        if phraseList[i][0] == "i" or phraseList[i][0] == "I":
            password = password + "1"
        elif phraseList[i][0] == "o" or phraseList[i][0] == "O":
            password = password + "0"
        elif phraseList[i][0] == "s" or phraseList[i][0] == "S":
            password = password + "5"
        else:
            password = password + phraseList[i][0]
    return password


main()
