n = int(input())
val = 0
for x in range(n):
    operation = input()
    if operation =='++X' or operation == 'X++':
        val += 1
    elif operation == '--X' or operation == 'X--':
        val -= 1

print(val)