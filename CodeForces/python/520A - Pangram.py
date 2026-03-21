_ = int(input())
word = input().lower()

print('YES' if len(set(word)) == 26 else 'NO')
