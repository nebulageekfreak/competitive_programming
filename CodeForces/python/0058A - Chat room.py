word = input()
ref = ''
for x in word:
    if x == 'h' and ref == '':
        ref += x
    elif x == 'e' and ref == 'h':
        ref += x
    elif x == 'l' and ref == 'he':
        ref += x
    elif x == 'l' and ref == 'hel':
        ref += x
    elif x == 'o' and ref == 'hell':
        ref += x
print('YES' if ref == 'hello' else 'NO')
