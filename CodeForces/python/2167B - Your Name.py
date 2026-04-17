t = int(input())

for i in range(t):
    lengthOfName = int(input())
    name1, name2 = input().split()
    
    lstName2 = list(name2)
    counter = 0
    
    for i, v in enumerate(name1):
        if v in lstName2:
            counter += 1
            lstName2.remove(v)
    print('YES' if counter == lengthOfName else "NO")
