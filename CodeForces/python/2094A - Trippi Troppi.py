t = int(input())

for i in range(t):
    strings = input().split()
    result = ''.join(string[0] for string in strings)
    
    print(result)
