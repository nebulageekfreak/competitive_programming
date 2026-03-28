n = int(input())


for i in range(n):
    division = int(input())
    if division <= 1399:
        print("Division 4")

    elif division <= 1599:
        print("Division 3")

    elif division <= 1899:
        print("Division 2")

    else:
        print("Division 1")
