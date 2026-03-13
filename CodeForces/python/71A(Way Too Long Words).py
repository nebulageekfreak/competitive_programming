n = int(input())
for i in range(n):
    word = input()
    print(f"{word[0]}{len(word) - 2}{word[-1]}" if len(word) > 10 else word)
