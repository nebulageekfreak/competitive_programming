word = input()
corrected = word
if len(word) == 1 or word[1:].isupper():
    corrected = ''.join(x.upper() if x.islower() else x.lower() for x in word)

print(corrected)

# old solution
# word = input()
#
# if word.isupper():
#     word = word.lower()
# elif len(word) == 1:
#     word = word.upper()
# elif word[0].islower() and word[1:].isupper():
#     word = word.capitalize()
#
# print(word)
#
#
#

