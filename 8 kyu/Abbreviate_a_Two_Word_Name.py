"""8 kyu
Abbreviate a Two Word Name
Write a function to convert a name into initials. This kata strictly takes two words with one space in between them.

The output should be two capital letters with a dot separating them.

It should look like this:

Sam Harris => S.H

patrick feeney => P.F
Fundamentals
Strings
Arrays"""


# def abbrev_name(name):
#     abb_name = []
#     filename = name.split()
#     for i in filename:
#         abb_name.append(i[0])
#     new = ".".join(abb_name)
#     return new.title()


# How this works
def abbrev_name(name):
    abb_name = []
    filename = name.split()
    for i in filename:
        abb_name.append(i[0])
    new = ".".join(abb_name)
    print(new.title())


abbrev_name("golang hell")
