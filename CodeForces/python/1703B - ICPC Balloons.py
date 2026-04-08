t = int(input())


for i in range(t):
    _ = int(input())

    solved = input()
    firstSolved = set()
    counter = 0

    for s in solved:
        if s not in firstSolved:
            counter += 2;
            firstSolved.add(s)
        else:
            counter += 1;

    print(counter)
