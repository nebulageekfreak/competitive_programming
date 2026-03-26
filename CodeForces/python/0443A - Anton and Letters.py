n = input()[1:-1]

if n:
    letters = set(n.split(', '))
    print(len(letters))
else:
    print(0)
