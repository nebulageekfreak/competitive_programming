string = input()

lowercases = 0
uppercases = 0

for x in string:
    if x.islower():
        lowercases += 1
    else:
        uppercases += 1

print(string.lower() if lowercases >= uppercases else string.upper())
