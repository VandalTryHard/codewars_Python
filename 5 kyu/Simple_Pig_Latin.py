"""5 kyu
Simple Pig Latin
Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.
Examples:
pig_it('Pig latin is cool') # igPay atinlay siay oolcay
pig_it('Hello world !')     # elloHay orldway !
"""
# def pig_it(text):
#     text = text.split()
#     new_text = []
#     for word in text:
#         if word == '.' or word == ',' or word == '!' or word == '?' or word == ':' or word == ';' or word == '-':
#             new_word = word
#             new_text.append(new_word)
#         else:
#             new_word = word[1:] + word[0:1] + "ay"
#             new_text.append(new_word)

#     new_text = ' '.join(new_text)
#     return new_text

### How this works
text = input("Your text: ")
text = text.split()
new_text = []
for word in text:
    if word == '.' or word == ',' or word == '!' or word == '?' or word == ':' or word == ';' or word == '-':
        new_word = word
        new_text.append(new_word)
    else:
        new_word = word[1:] + word[0:1] + "ay"
        new_text.append(new_word)

new_text = ' '.join(new_text)

print(f"Pig latin: {new_text}")