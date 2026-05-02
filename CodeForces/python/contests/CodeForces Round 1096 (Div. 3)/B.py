t = int(input())

for _ in range(t):
    length = int(input())
    string = input()
    
    counter1 = 0
    counter2 = 0

    for symbol in string:
        if symbol == '(':
            counter1 += 1
        else:
            counter2 += 1

    print('YES' if counter1 == counter2 else 'NO')
